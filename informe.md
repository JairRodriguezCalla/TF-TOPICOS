# UNIVERSIDAD PERUANA DE CIENCIAS APLICADAS

## TÓPICOS EN CIENCIAS DE LA COMPUTACIÓN

### Sección CC82

**PROFESOR**  
Canaval Sanchez, Luis Martín

**INFORME DE TRABAJO FINAL**

**Integrantes del equipo:**

| Código       | Nombres y apellidos                     |
|--------------|-----------------------------------------|
| U202116247   | Rodriguez Calla, Jair Stephano         |
| U202111299   | Zuñiga Lovera, Angel Ruben             |
| U202111197   | Adauto Angulo, Mauro Imanol Obermeyer  |
| U202112116   | Niño Suárez, David Joaquín             |

**Agosto, 2024**

---

## Contenido

1. Problemática y Motivación  
   1.1. Problemática  
   1.2. Motivación  
2. Objetivos  
   2.1. Objetivo General  
   2.2. Objetivos Específicos  
3. Diseño de Solución  
   3.1. Modelado del Problema con CSP  
   3.2. Implementación en Python usando python-constraint  
   3.3. Optimización de la Solución  
   3.4. Validación y Pruebas  
   3.5. Resultados Esperados  
4. Desarrollo de Solución  
   4.1. Definición del Problema y Variables  
   4.2. Definición de Restricciones  
   4.3. Búsqueda de Soluciones y Selección de la Mejor Opción  
5. Diseño de Solución Actualizada  
6. Plan de Validación  
7. Conclusión  

---

## 1. Problemática y Motivación

### 1.1. Problemática

En el entorno educativo, una de las tareas más complejas y críticas es la planificación y asignación de horarios para los diferentes cursos que se imparten. Esta planificación implica coordinar a profesores, estudiantes y aulas disponibles, asegurando que no existan conflictos de horario y que se cumplan con todas las restricciones operativas de la institución. La complejidad de esta tarea aumenta proporcionalmente con el número de cursos, profesores y aulas disponibles, y cualquier error en la asignación puede tener consecuencias significativas, como:

#### Principales Problemas:

- **Conflictos de Horarios:**
  - Un profesor asignado a dos cursos en el mismo horario.
  - Un aula asignada a más de un curso al mismo tiempo.
  - Estudiantes que deben asistir a dos clases diferentes en el mismo horario.

- **Subutilización de Recursos:**
  - Aulas vacías durante gran parte del horario lectivo.
  - Profesores con cargas horarias desbalanceadas, con algunos sobrecargados y otros subutilizados.

- **Sobrecapacidad en Aulas:**
  - Asignación de un aula pequeña a un curso con muchos estudiantes, superando la capacidad física y logística del espacio.

- **Dificultad para Ajustar Cambios:**
  - Cualquier cambio, como la adición de un nuevo curso o la modificación de la disponibilidad de un profesor, puede requerir una reestructuración significativa de todo el horario.

Estas dificultades, además de afectar la operatividad diaria de la institución, impactan negativamente en la experiencia educativa de estudiantes y docentes. La tarea de asignación de horarios se suele realizar manualmente o utilizando herramientas básicas como hojas de cálculo, lo cual es ineficiente y propenso a errores, especialmente en instituciones con un gran número de cursos y restricciones.

### 1.2. Motivación

La asignación de horarios puede ser abordada mediante técnicas de **Programación con Restricciones (CSP)**, que modelan todas las restricciones del problema y buscan soluciones óptimas.

**Razones para utilizar CSP:**

1. **Automatización:** Generación rápida y consistente de horarios.
2. **Optimización:** Uso eficiente de recursos.
3. **Flexibilidad:** Adaptación sencilla a cambios.
4. **Reducción de Conflictos:** Eliminación de errores comunes.
5. **Mejora Educativa:** Asegurar la mejor experiencia para estudiantes y profesores.

---

## 2. Objetivos

### 2.1. Objetivo General

Desarrollar un modelo de **CSP** para asignación óptima de horarios, respetando restricciones de disponibilidad de profesores, capacidad de aulas y evitando conflictos.

### 2.2. Objetivos Específicos

1. Modelar las restricciones del problema en un modelo CSP.
2. Implementar el modelo en Python usando `python-constraint`.
3. Validar y optimizar las soluciones generadas.

---

## 3. Diseño de Solución

### 3.1. Modelado del Problema con CSP

- **Definición de Variables:** Representan la asignación de un aula, horario y día para cada curso.
- **Dominios:** Combinaciones posibles de aulas, horarios y días.
- **Restricciones:** 
  - Capacidad de Aulas.
  - Conflictos de Horarios.
  - Disponibilidad de Profesores.

---

### 3.2. Implementación en Python usando `python-constraint`

- **Configuración del Modelo:** Uso de `Problem()` para modelar restricciones.
- **Validación:** `getSolutions()` para obtener soluciones válidas.

---

### 3.3. Optimización de la Solución

- Evaluación y selección de la mejor solución mediante funciones de puntaje.

---

### 3.4. Validación y Pruebas

- Pruebas unitarias, integración de agentes y rendimiento.

---

### 3.5. Resultados Esperados

- Optimización de recursos.
- Reducción de conflictos.
- Adaptabilidad a cambios.

---

## 4. Desarrollo de Solución

### 4.1. Definición del Problema y Variables

Definición de aulas, cursos, horarios y estudiantes. Verificación de límites de capacidad y generación aleatoria de datos.

---

### 4.2. Definición de Restricciones

- **Capacidad:** Cursos asignados a aulas adecuadas.
- **Conflictos de Horarios:** Restricciones para evitar superposiciones.

---

### 4.3. Búsqueda de Soluciones y Selección de la Mejor Opción

Exploración y optimización mediante agentes.

**Repositorio de código:**  
[GitHub - TopicosCC-TP-TF](https://github.com/JairRodriguezCalla/TF-TOPICOS.git)

---

## 5. Diseño de Solución Actualizada

Implementación de un sistema **multiagente**, compuesto por:

1. **Agente de Aula:** Asignación basada en capacidades.
2. **Agente de Horario:** Coordinación de horarios sin conflictos.
3. **Agente de Optimización:** Selección de soluciones óptimas.

---

## 6. Plan de Validación

- **Pruebas Unitarias:** Verificación de cada agente.
- **Pruebas de Integración:** Colaboración efectiva entre agentes.
- **Pruebas de Rendimiento:** Escalabilidad y adaptabilidad.

**Criterios de Éxito:**  
1. Soluciones sin conflictos.  
2. Uso eficiente de recursos.  
3. Adaptabilidad.  
4. Rendimiento óptimo.

---

## 7. Conclusión

El diseño propuesto implementa técnicas de **CSP** y un sistema **multiagente**, logrando una solución modular, escalable y eficiente. Esto asegura horarios óptimos y adaptables a restricciones futuras, mejorando la calidad de la planificación académica.
