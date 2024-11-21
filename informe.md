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

**Noviembre, 2024**

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

La asignación de horarios es un problema típico de optimización que puede ser abordado mediante técnicas de programación con restricciones (Constraint Programming, CSP), ya que estas permiten modelar de manera explícita todas las restricciones del problema y buscar una solución que las satisfaga de manera óptima.

**Razones para utilizar CSP:**

1. **Automatización:** 
  - Utilizar CSP para la asignación de horarios permite automatizar un proceso que de otra manera sería tedioso y propenso a errores. Con la definición adecuada de las restricciones, el sistema puede generar un horario completo y consistente en cuestión de segundos.
2. **Optimización:** 
  - El uso de CSP permite no solo cumplir con todas las restricciones, sino también optimizar el uso de recursos, como asegurar que no haya aulas vacías en horarios pico o balancear la carga horaria entre los profesores.
3. **Flexibilidad:** 
  - Un modelo CSP bien diseñado permite realizar cambios en las restricciones de manera sencilla. Por ejemplo, si un profesor cambia su disponibilidad o se añade un nuevo curso, el sistema puede reajustar el horario completo sin necesidad de rehacerlo desde cero.
4. **Reducción de Conflictos:** 
  - Al modelar explícitamente todas las restricciones, el sistema asegura que no haya conflictos de horarios entre profesores, estudiantes y aulas. Esto reduce significativamente los problemas operativos que suelen surgir al inicio de cada ciclo lectivo.
5. **Mejora Educativa:** 
  - Al evitar problemas de sobrecarga de profesores y aulas, y al asegurar que los estudiantes puedan asistir a todas sus clases sin conflictos, se mejora la calidad del entorno educativo, permitiendo una mejor experiencia tanto para estudiantes como para profesores.

---

## 2. Objetivos

### 2.1. Objetivo General

Desarrollar un modelo de programación con restricciones (CSP) para la asignación óptima de horarios en una escuela, asegurando que todas las restricciones de disponibilidad de profesores, capacidad de aulas y conflictos de horarios entre cursos sean respetadas, y que se minimicen los conflictos y la subutilización de recursos.

### 2.2. Objetivos Específicos

1. Modelar las restricciones del problema en un modelo CSP:
  - Definir las variables, dominios y restricciones necesarias para representar el problema de asignación de horarios, asegurando que se contemplen la disponibilidad de profesores, capacidad de aulas y evitar conflictos de horarios.
2. Implementar el modelo CSP en Python utilizando la biblioteca python-constraint:
  - Desarrollar el modelo en código, integrando todas las restricciones identificadas y generando soluciones válidas para la asignación de horarios que respeten todas las condiciones del problema.
3. Validar y optimizar las soluciones generadas:
  - Probar el modelo CSP con datos de prueba, verificar que no existan conflictos en las soluciones obtenidas y optimizar el uso de recursos (aulas y profesores), buscando el balance óptimo entre las restricciones y la eficacia del horario generado.

---

## 3. Diseño de Solución

El diseño de solución se centra en la implementación de un modelo de **Programación con Restricciones (CSP)** para la asignación óptima de horarios en una institución educativa. El objetivo principal es asegurar que todas las restricciones de disponibilidad de profesores, capacidad de aulas y conflictos de horarios entre cursos sean respetadas. A continuación, se detallan los pasos y componentes clave del diseño de solución:

### 3.1. Modelado del Problema con CSP

- **Definición de Variables:**  
  Se definen variables para cada curso, las cuales representan la asignación de un aula, un horario y un día específico.

- **Dominios:**  
  Cada variable tiene un dominio que incluye todas las combinaciones posibles de aulas, horarios y días en los que se puede asignar el curso.

- **Restricciones:**  
  Se modelan varias restricciones para garantizar que las soluciones generadas sean válidas y óptimas:
  - **Capacidad de Aulas:** Asegura que la cantidad de estudiantes no exceda la capacidad máxima del aula asignada.
  - **Conflictos de Horarios:** Evita que más de un curso se asigne al mismo aula, horario y día.
  - **Distribución Equitativa:** Garantiza que se utilicen todas las aulas disponibles y que no se concentren todos los cursos en un solo día o aula.
  - **Disponibilidad de Profesores:** Asegura que los profesores no se asignen a más de un curso al mismo tiempo.

---

### 3.2. Implementación en Python usando `python-constraint`

- **Configuración del Modelo:**  
  Se utiliza la biblioteca `python-constraint` para modelar el problema con todas las restricciones identificadas.

- **Definición del Problema:**  
  Se crea un objeto `Problem()` y se añaden variables, dominios y restricciones mediante funciones `addVariable()` y `addConstraint()`.

- **Validación de Soluciones:**  
  Se utiliza el método `getSolutions()` para obtener todas las soluciones posibles que cumplan con las restricciones definidas.

---

### 3.3. Optimización de la Solución

- **Evaluación de Soluciones:**  
  Se aplica un criterio de evaluación para seleccionar la mejor solución en función de la distribución equilibrada de aulas y horarios.

- **Penalización y Selección:**  
  Se utiliza una función de puntaje para penalizar las soluciones que no cumplen con la distribución ideal de horarios y aulas. La solución con el puntaje más bajo es seleccionada como la mejor.

---

### 3.4. Validación y Pruebas

- **Pruebas de Consistencia:**  
  Se prueban diferentes combinaciones de cursos, aulas y horarios para asegurar que el modelo puede manejar casos complejos y garantizar la validez de las soluciones generadas.

- **Evaluación de Escenarios de Cambio:**  
  Se simulan cambios en la disponibilidad de profesores o la adición de nuevos cursos para evaluar la adaptabilidad del modelo CSP.

- **Pruebas de Consistencia de Agentes:**  
  Explica que se realizan pruebas unitarias para asegurar que cada agente (Aula, Horario, Optimización) cumpla con su función específica.

- **Pruebas de Integración de Agentes:**  
  Describe cómo los agentes interactúan y se integran para asegurar que el sistema multiagente funcione de manera coordinada, resolviendo las asignaciones sin conflictos.

- **Pruebas de Rendimiento:**  
  Menciona que pruebas de carga y rendimiento se realizarán para verificar que el sistema multiagente puede manejar aumentos en el número de cursos y restricciones.

---

### 3.5. Resultados Esperados

- **Optimización del Uso de Recursos:**  
  Se espera una utilización óptima de las aulas y una distribución balanceada de la carga horaria de los profesores.

- **Reducción de Conflictos:**  
  Al modelar explícitamente todas las restricciones, se minimizan los conflictos de horario y se evita la sobrecarga o subutilización de recursos.

- **Adaptabilidad a Cambios:**  
  El modelo puede ajustarse fácilmente a cambios en las restricciones o a la adición de nuevas variables sin necesidad de reestructurar completamente el horario.

---

## 4. Desarrollo de Solución

Se definieron tres aulas con capacidades variables, y se generaron aleatoriamente la cantidad de estudiantes para cada curso, asegurando que el total de estudiantes se imprimiera en consola.  

Luego, se establecieron restricciones para garantizar que ningún curso excediera la capacidad de su aula asignada y que no se usara un aula por más de un curso a la vez en el mismo horario y día.  

Después de buscar todas las soluciones posibles, se calculó el uso de aulas en cada asignación y se identificó la mejor solución, que minimiza la cantidad de aulas utilizadas, presentando finalmente la asignación óptima de cursos junto con sus respectivas aulas, horarios y días.

**Código del desarrollo:**  
[Repositorio en GitHub](https://github.com/JairRodriguezCalla/TF-TOPICOS.git)

---

### 4.1. Definición del Problema y Variables

Se tomaron en cuenta las siguientes variables para el problema:  

- **Cursos:** Representan los cursos que necesitan ser asignados.  
- **Aulas:** Representan los espacios disponibles con capacidad limitada.  
- **Horarios:** Representan los periodos de tiempo en los que se asignan los cursos.  
- **Días:** Representan los días disponibles para la asignación de horarios.  

---

### 4.2. Definición de Restricciones

Se definieron las siguientes restricciones para garantizar la validez de las soluciones:

- **Restricción de capacidad de aulas:**  
  Un curso no puede ser asignado a un aula que tenga menos capacidad que el número de estudiantes inscritos en el curso.

- **Restricción de uso único de aula:**  
  Un aula no puede ser utilizada por más de un curso al mismo tiempo en el mismo día.

- **Optimización de uso de aulas:**  
  Se busca que los cursos se asignen de manera que se utilicen el máximo número posible de aulas diferentes para evitar concentración.

---

### 4.3. Búsqueda de Soluciones y Selección de la Mejor Opción

#### **Búsqueda de soluciones:**

- Se exploran todas las posibles combinaciones de asignaciones de aulas, horarios y días para cada curso, considerando las restricciones impuestas.  
- Cada combinación generada es evaluada para verificar que cumpla con todas las restricciones definidas.

#### **Selección de la mejor opción:**

- **Criterio de optimización:**  
  Se selecciona la solución que maximiza el uso de diferentes aulas para mejorar la distribución de los cursos y evitar la concentración en un mismo espacio.  

- **Solución ideal:**  
  La solución que utiliza el mayor número de aulas distintas se considera la mejor opción para evitar sobrecargas en aulas específicas.

---

## 5. Diseño de Solución Actualizada

Con el objetivo de mejorar la eficacia y flexibilidad del sistema de asignación de horarios, se ha implementado un **sistema multiagente** que permite dividir el problema en tareas específicas manejadas por agentes independientes.  

Un sistema multiagente es una arquitectura compuesta por múltiples agentes, cada uno responsable de cumplir con una función específica, colaborando para lograr una solución óptima de forma conjunta. En esta solución, cada agente gestiona una parte del proceso de asignación de horarios, mejorando la adaptabilidad y permitiendo una resolución eficiente de restricciones.

---

### Descripción de los Agentes

#### **Agente de Aula**

- Responsable de asignar aulas a los cursos, asegurando que cada aula tenga la capacidad suficiente para los estudiantes inscritos en el curso correspondiente.  
- Al gestionar la capacidad de las aulas, este agente ayuda a evitar problemas de sobrecarga y garantiza que los recursos físicos sean usados de manera eficiente.

---

#### **Agente de Horario**

- Se encarga de coordinar los horarios de los cursos.  
- Su función es asegurar que no existan conflictos de horarios para los cursos asignados a la misma aula o profesor, evitando así situaciones en las que un recurso (aula o profesor) esté doblemente asignado en el mismo horario.

---

#### **Agente de Optimización**

- Evalúa las soluciones generadas por los otros agentes y selecciona la mejor alternativa según criterios de optimización.  
- Los criterios incluyen:
  - Uso eficiente de las aulas.
  - Distribución equilibrada de la carga horaria.
  - Cumplimiento de todas las restricciones de capacidad y disponibilidad.
- Este agente mejora el desempeño general del sistema, logrando una asignación de horarios sin conflictos y adaptada a los recursos disponibles.

---

### Interacción entre Agentes

Los agentes en este sistema multiagente colaboran entre sí para asegurar que la solución final sea válida y eficiente.  

La interacción entre los agentes se realiza de la siguiente manera:

1. **Agente de Aula**  
   - Proporciona información sobre las aulas disponibles y sus capacidades al **Agente de Horario** para que este pueda coordinar las asignaciones de horarios sin exceder la capacidad de las aulas.

2. **Agente de Horario**  
   - Coordina con el **Agente de Optimización**, informándole de las soluciones de asignación de horarios que cumplen con las restricciones de aula y capacidad.

3. **Agente de Optimización**  
   - Evalúa todas las soluciones viables proporcionadas por los otros agentes y selecciona la que mejor optimice el uso de recursos, distribuyendo equitativamente las asignaciones de aulas y horarios.

---

### Beneficios del Sistema Multiagente

Esta colaboración permite que el sistema multiagente realice asignaciones de horarios de manera más rápida, adaptable y precisa, optimizando los recursos y reduciendo la posibilidad de conflictos.

**Ventajas principales:**

- **Rapidez:** Procesa soluciones en menos tiempo al dividir el problema en tareas específicas.
- **Adaptabilidad:** Facilita la incorporación de cambios en las restricciones.
- **Precisión:** Minimiza los errores y garantiza la validez de las soluciones.
- **Optimización:** Mejora la utilización de recursos y la distribución de horarios.


---

## 6. Plan de Validación

Para asegurar que el sistema multiagente cumpla con sus objetivos y funcione correctamente, se han diseñado varias pruebas que permitirán validar cada agente de manera individual y en conjunto, así como evaluar el rendimiento del sistema bajo diferentes condiciones. A continuación, se describen las pruebas y los criterios de éxito.

---

### Definición de Pruebas

#### **Pruebas Unitarias para Agentes**

Estas pruebas tienen como objetivo verificar que cada agente cumpla su función de manera independiente:

- **Agente de Aula:**  
  - Validar que todos los cursos asignados a un aula cumplen con las restricciones de capacidad.

- **Agente de Horario:**  
  - Verificar que no se produzcan conflictos de horario en las aulas y que cada curso esté asignado en un horario único, sin superposiciones.

- **Agente de Optimización:**  
  - Asegurar que las soluciones seleccionadas maximizan el uso de diferentes aulas y optimizan la distribución de horarios.

---

#### **Pruebas de Integración de Agentes**

Estas pruebas evaluarán la interacción entre los agentes, verificando que colaboren correctamente para producir una solución válida:

- **Interacción entre Agente de Aula y Agente de Horario:**  
  - Comprobar que las asignaciones de aulas y horarios no generen conflictos y que la información se intercambie de manera efectiva.

- **Interacción con el Agente de Optimización:**  
  - Validar que las soluciones generadas por los agentes de Aula y Horario sean correctamente evaluadas por el Agente de Optimización, garantizando que la solución final sea eficiente y sin conflictos.

---

#### **Pruebas de Rendimiento**

Estas pruebas evaluarán la capacidad del sistema multiagente para manejar un mayor volumen de datos y restricciones:

- **Incremento del volumen de datos:**  
  - Incrementar el número de cursos, aulas y horarios disponibles para observar el rendimiento del sistema y garantizar que pueda procesar las asignaciones sin pérdida significativa de eficiencia o precisión.

- **Pruebas de carga:**  
  - Verificar que el sistema pueda adaptarse a cambios en las restricciones o en el número de cursos, manteniendo un rendimiento aceptable.

---

### Criterios de Éxito

Para considerar que el sistema multiagente ha pasado las pruebas de validación, debe cumplir con los siguientes criterios:

- **Soluciones sin conflictos:**  
  - Todas las asignaciones de horarios y aulas deben cumplir con las restricciones definidas, evitando conflictos de horario, capacidad o uso de aulas.

- **Distribución eficiente de recursos:**  
  - La solución final debe maximizar el uso de diferentes aulas y distribuir de manera equitativa la carga horaria entre las asignaciones.

- **Adaptabilidad a cambios:**  
  - El sistema debe ajustarse rápidamente a modificaciones en las restricciones o a la adición de nuevos cursos, sin requerir reestructuraciones significativas.

- **Rendimiento óptimo:**  
  - El sistema debe procesar las asignaciones y generar soluciones en tiempos razonables, incluso al manejar un número elevado de restricciones y datos.


---

## 7. Conclusión

El diseño de solución propuesto garantiza la asignación eficiente de horarios mediante la utilización de técnicas de programación con restricciones. La implementación en Python facilita la validación y optimización de las soluciones, asegurando un modelo flexible y robusto capaz de manejar las complejidades típicas del entorno educativo. Este enfoque no solo resuelve la problemática inicial, sino que también proporciona una herramienta adaptable para futuras necesidades y cambios.
La programación con restricciones (CSP) es una herramienta eficaz para resolver problemas complejos de asignación, como la distribución de cursos en aulas. Utilizando variables y restricciones precisas, se logran soluciones óptimas que maximizan el uso de los recursos disponibles y optimizan la planificación académica. CSP permite explorar múltiples combinaciones y seleccionar la mejor opción, demostrando su aplicabilidad en contextos educativos y logísticos.

