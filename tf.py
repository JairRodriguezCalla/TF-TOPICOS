import tkinter as tk
from tkinter import ttk, messagebox
import pandas as pd
from constraint import Problem
import random


# Cargar datos desde Excel
archivo = "datos.xlsx"
cursos_regulares = pd.read_excel(archivo, sheet_name="CursosRegulares")
cursos_electivos = pd.read_excel(archivo, sheet_name="CursosElectivos")
aulas = pd.read_excel(archivo, sheet_name="Aulas")

# Parámetros del horario
dias = ["Lunes", "Martes", "Miércoles", "Jueves", "Viernes", "Sábado"]  # No aleatorizamos los días
horarios_visualizados = [f"{h}:00" for h in range(7, 21)]  # Horas visualizadas de 7:00 a 23:00
horarios_asignados = [f"{h}:00 - {h+1}:00" for h in range(10, 20)]  # Horas para asignación de cursos entre 10:00 y 16:00

# Crear ventana principal
root = tk.Tk()
root.title("Gestión de Horarios")
root.geometry("1000x1000")

# Establecer color de fondo para la ventana
root.configure(bg="#fff8ca")  # Fondo de toda la ventana

# Entrada para la cantidad de cursos
cantidad_label = tk.Label(root, text="Cantidad de Cursos:", bg="#fff8ca", font=('Helvetica', 14, 'bold'))
cantidad_label.pack(pady=5)

cantidad_entry = tk.Entry(root)
cantidad_entry.pack(pady=5)

# Contenedor para los selectores dinámicos
selector_frame = tk.Frame(root, bg="#fff8ca")  # Fondo en selector_frame
selector_frame.pack(pady=10, fill="both", expand=True)

# Frame para mostrar el horario generado
horarios_frame = tk.Frame(root, bg="#fff8ca")  # Fondo en horarios_frame
horarios_frame.pack(pady=10, fill="both", expand=True)

# Botón para generar los selectores
def generar_selectores():
    for widget in selector_frame.winfo_children():
        widget.destroy()

    cantidad = int(cantidad_entry.get())
    for i in range(cantidad):
        tk.Label(selector_frame, text=f"Curso {i + 1}:", bg="#fff8ca").grid(row=i, column=0, padx=5, pady=5)

        ciclo_combo = ttk.Combobox(selector_frame, values=["Electivo"] + list(cursos_regulares["Ciclo"].unique()))
        ciclo_combo.grid(row=i, column=1, padx=5, pady=5)
        ciclo_combo.set("Electivo")

        curso_combo = ttk.Combobox(selector_frame, values=[])
        curso_combo.grid(row=i, column=2, padx=5, pady=5)

        def actualizar_cursos(event, combo=ciclo_combo, curso_combo=curso_combo):
            ciclo = combo.get()
            if ciclo == "Electivo":
                cursos = cursos_electivos["Curso"].tolist()
            else:
                cursos = cursos_regulares[cursos_regulares["Ciclo"] == int(ciclo)]["Curso"].tolist()
            curso_combo["values"] = cursos

        ciclo_combo.bind("<<ComboboxSelected>>", actualizar_cursos)

generar_button = tk.Button(root, text="Generar Selectores", command=generar_selectores, 
                           bg="#ce0000", fg="white", font=("Helvetica", 12))
generar_button.pack(pady=5)

# Función para generar el horario
def generar_horario():
    sesiones_cursos = {}

    # Recopilar datos seleccionados
    for i in range(int(cantidad_entry.get())):
        curso_combo = selector_frame.grid_slaves(row=i, column=2)[0]
        curso = curso_combo.get()
        if curso:
            # Verificar si es electivo o regular
            if curso in cursos_electivos["Curso"].values:
                curso_data = cursos_electivos[cursos_electivos["Curso"] == curso]
            else:
                curso_data = cursos_regulares[cursos_regulares["Curso"] == curso]
            
            if not curso_data.empty:
                horas = curso_data["Horas"].values[0]
                veces = curso_data["Veces"].values[0]
                horas_por_sesion = horas // veces
                for sesion in range(veces):
                    sesiones_cursos[f"{curso}_Sesion{sesion + 1}"] = horas_por_sesion

    if not sesiones_cursos:
        messagebox.showerror("Error", "Debe seleccionar al menos un curso.")
        return

    # Configurar CSP
    problem = Problem()
    # Aleatorizar solo los horarios, pero los días no se modifican
    random.shuffle(horarios_asignados)
    dominio = [(aula, horario, dia) for aula in aulas["Aula"].tolist()
               for horario in horarios_asignados
               for dia in dias]

    for sesion in sesiones_cursos:
        curso = sesion.split("_")[0]
        # Verificar si el curso es electivo o regular
        if curso in cursos_electivos["Curso"].values:
            curso_data = cursos_electivos[cursos_electivos["Curso"] == curso]
        else:
            curso_data = cursos_regulares[cursos_regulares["Curso"] == curso]

        if not curso_data.empty:
            capacidad_minima = curso_data["Vacantes"].values[0]
            dominio_reducido = [
                (aula, horario, dia)
                for aula, horario, dia in dominio
                if not aulas[aulas["Aula"] == aula].empty and
                max(aulas[aulas["Aula"] == aula]["Capacidad"].values) >= capacidad_minima
            ]

            if dominio_reducido:
                random.shuffle(dominio_reducido)  # Mezclar las opciones dentro del dominio reducido
                problem.addVariable(sesion, dominio_reducido)
            else:
                messagebox.showerror("Error", f"No hay aulas disponibles para la sesión: {sesion}")
                return

    # Agregar restricciones
    def no_conflictos(asignacion1, asignacion2):
        aula1, horario1, dia1 = asignacion1
        aula2, horario2, dia2 = asignacion2
        if dia1 == dia2 and aula1 == aula2 and horario1 == horario2:
            return False
        return True

    for sesion1 in sesiones_cursos:
        for sesion2 in sesiones_cursos:
            if sesion1 != sesion2:
                problem.addConstraint(no_conflictos, (sesion1, sesion2))

    # Obtener una solución
    solucion = problem.getSolution()
    if solucion:
        mostrar_horario(solucion)
    else:
        messagebox.showinfo("Sin Solución", "No se encontró una solución válida.")

# Mostrar el horario generado en formato de tabla
def mostrar_horario(solucion):
    for widget in horarios_frame.winfo_children():
        widget.destroy()

    # Crear la tabla de horario
    tk.Label(horarios_frame, text="Horario Generado", font=('Helvetica', 14, 'bold'), bg="#fff8ca").grid(row=0, column=0, columnspan=len(dias) + 1, pady=10)

    # Encabezado de la tabla con los días de la semana
    for i, dia in enumerate(dias):
        tk.Label(horarios_frame, text=dia, font=('Helvetica', 10, 'bold'), relief="solid", width=15, bg="#ce0000", fg="white").grid(row=1, column=i + 1)

    # Mostrar las horas en la primera columna (visualizadas de 7:00 a 23:00)
    for i, hora in enumerate(horarios_visualizados):
        tk.Label(horarios_frame, text=hora, font=('Helvetica', 10), relief="solid", width=15, bg="#fff8ca", fg="black").grid(row=i + 2, column=0)

    # Rellenar la tabla con las sesiones asignadas
    for sesion, (aula, horario, dia) in solucion.items():
        hora_idx = horarios_asignados.index(horario) + 2  # Obtener la fila correspondiente a la hora real de asignación
        dia_idx = dias.index(dia) + 1  # Obtener la columna correspondiente al día
        session_text = f"{sesion}\n{aula}"  # Combinar el nombre del curso y el aula
        tk.Label(horarios_frame, text=session_text, font=('Helvetica', 10), bg="lightblue", relief="solid", width=15).grid(row=hora_idx, column=dia_idx)

# Botón para generar el horario
horario_button = tk.Button(root, text="Generar Horario", command=generar_horario, 
                           bg="#ce0000", fg="white", font=("Helvetica", 12))
horario_button.pack(pady=5)

root.mainloop()
