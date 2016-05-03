
## INTRODUCCION


### 1.I Resumen del Proyecto

El presente documento tiene como propósito definir las
especificaciones funcionales y no funcionales del sistema
para la implementación de una aplicación web que permitirá la gestión
de un sistema de alojamiento para viajeros.

### 1.I.a Proposito y alcance de objetivos

El sistema se basa en el blog ya en funcionamiento llamado CouchIn. El
propósito del proyecto es sistematizar dicho blog para facilitar la
administración y mantenimiento del mismo. Éste, es el medio de
comunicación entre visitantes y dueños de hospedajes del territorio
Argentino. El presente documento esta dirigido a desarrolladores,
aunque será validado y aprobado por ambas partes. 


### 1.I.b Supuestos y restricciones

+ Se utilizara como metodologia de desarrollo scrum
+ El desarrollo se realizara en Python2.7 sobre el framwork Django1.9
+ Se utilizara para la persistencia de los datos el motor de base de
datos MySQL.
+ Sera necesario la contratacion de un servidor externo(web hosting)
+ Por ser una aplicacion web, correra sobre un navegador web en un
dispositivo con conexion a internet.
+ ??? que poner en tiempo de desarrollo -> cronograma
+ ??? presupuesto? -> calcular con las cosas FN
+ Se debera utilizar el logo de la empresa.

### 1.I.c Entregables del proyecto.

+ Demo 1: Sabado 04/06/16

+ Demo 2: Sabado 25/06/16

+ Demo 3: Sabado 16/07/16

### 1.I.d Calendario y resumen del presupuesto.  El sistema finalizado
se entregará el sábado 16 de Julio de 2016.  El presupuesto del
proyecto es de $  ???

## 2 Documentos referenciados

| referencia | titulo | fecha | autor |
| ---        | ---    | ---   | ---   |
| 1          | [entrevista 1]  (https://github.com/chudix/couchInn/blob/master/documentacion/entrevista1.md) | 17/03/2016 | grupo 24 |
| 2          | [entrevista 2] (https://github.com/chudix/couchInn/blob/master/documentacion/entrevista2.md) | 1/04/2016 | grupo 24 |
| 3          | [SRS]
| (https://github.com/chudix/couchInn/blob/master/documentacion/srs.md)
| | 10/04/2016  | grupo 24 |
| 4 | [DER]
| (https://github.com/chudix/couchInn/blob/master/documentacion/CouchInnDB.pdf)
| | 20/04/2016 | grupo 24 |


## 3 Definiciones y acronimos

# TODO: !

## 4 Organizacion del proyecto

### 4.I Interfaces externas

El equipo de desarrolladores se organizara utilizando la metodologia
scrumm.
El equipo esta conformado por:
   Santiago Mayahara
   Fernan Nestier
   Matias Garcia

### 4.II Estructura interna

La estructura interna se conformara acorde a la metodologia de scrum,
esto significa que sera descentralizada controlada. Los
desarrolladores del equipo seran coordinados por el scrum master que
sera quien tenga relacion directa con el cliente.


IMAGEN


### 4.III Roles y responsabilidades.

**Product Owner**

El Dueño de Producto es la única persona autorizada para decidir sobre
cuáles funcionalidades y características funcionales tendrá el
producto. Es quien representa al cliente, usuarios del software y
todas aquellas partes interesadas en el producto.

**El Scrum Master**

El Scrum Master es el alma mater de Scrum. Un error frecuente es
llamarlo "líder", puesto que el Scrum Master no es un líder típico,
sino que es un un auténtico Servidor neutral, que será el encargado de
fomentar e instruir sobre los principios ágiles de Scrum.

**El Scrum Team**

El Scrum Team (o simplemente "equipo"), es el equipo de
desarrolladores multidisciplinario, integrado por programadores,
diseñadores, arquitectos, testers y demás, que en forma
auto­organizada, será los encargados de desarrollar el producto.

## 5 Planes de administracion del proceso.

### 5.I Plan inicial.

### 5.I.a Plan del personal.

**Desarrolladores:** El personal a cargo del desarrollo sera:
+   Santiago Mayahara
+   Fernan Nestier
+   Matias Garcia
Con tiempo estimado de trabajo de 5 dias por semana, 6 horas por dia.

**Testers:** El personal a cargo de realizacion de pruebas sera:
+   Santiago Mayahara
+   Fernan Nestier
+   Matias Garcia
Con tiempo estimado de trabajo de 3 dias por semana, 2 horas por dia.

**Entrevistadores:**El personal a cargo de la realizacion de las
entrevistas sera:
+   Santiago Mayahara
+   Fernan Nestier
+   Matias Garcia
Con tiempo estimado de trabajo de 1 dias por semana, 1/2 horas por dia.

### 5.I.b Plan de adquisicion de recursos.

| recurso | cantidad | tiempo | precio x unidad | precio total |
| ---     | ---      | ---    | ---             | ---          |
| servidor | 1 | 12 meses | $3000 | $3000 |
| dominio | 1  | 12 meses | us$60 | us$60 |
| servicio de pivotal tracker | 1 | 3 meses | $400/mes | $1200 |
| servidor mysql | 1 | - | $0 | $0 |


### 5.I.c Plan de entrenamiento del personal del protecto.

El personal disponible o contratado cuenta con la capacitación
necesaria para llevar adelante el proyecto.

## 5.II Plan de trabajo.

### 5.II.a Principales actividades del proyecto.

+ Elicitación de requisitos: Incluye realizar entrevistas con el
cliente, cuestionarios para los usuarios finales y el desarrollo del
SRS.
+ Creación de la pila del producto: Se anota la funcionalidad a
implementar.
+ Diseño de la base de datos
+ Planificación del proyecto: Se refiere al desarrollo de este
documento.
+ Análisis de riesgos
+ Diseño de la interfaz
+ Implementación: Se codifica el sistema.

### 5.II.b Asignacion de esfuerzo

#TODO:

### 5.III Plan de control.

N/A

### 5.IV Plan de administracion de riesgos
Aplica a futura entrega.

### 5.V Plan de liberacion de proyecto.

Una vez finalizado, el sistema se entregará en una demo, para
corroborar el correcto funcionamiento del mismo. Existirá un plazo de
tres meses para realizar cualquier tipo de mantenimiento en el
sistema, sin costo y de acuerdo a los documentos generados durante el
desarrollo.

## 6 Planes de procesos tecnicos.

### 6.I Modelo del proceso.

### 6.II Metodos, herramientas y tecnicas.

La aplicacion se desarrollara con el lenguaje python2.7 en el
framework Django1.9. Sera alojado en un servidor nginx y utilizara un
motor de base de datos MySQL.
Para el control de versiones se utilizara GitHub y pivotal tracker
para la administracion de las historias de usuario.

### 6.III Plan de infraestructura.

Para el desarrollo de la aplicacion sera necesario:
+ Una estacion de trabajo con una maquina portatil por miembro del
equipo.
+ Servicio de conexion a internet.
+ Una cuenta en pivotaltracker con la informacion de las
funcionalidades del sistema.
+ Un repositorio github incluyendo la documentacion generada, y
mantenido por los mismos desarrolladores.

### 6.IV Plan de aceptacion del producto.

El producto será aceptado si y sólo si cumple con las especificaciones
de las historias de usuario mínimas, que pueden encontrarse en la web
del proyecto en Pivotal Tracker.


### 7 Plan de procesos de apoyo

### 7.I Plan de administracion de configuracion
NA
### 7.II Plan de pruebas.
NA
### 7.III Plan de documentacion

+ Entrevistas
+ SRS
+ DER
+ Plan de gestion de producto.
+ Diseño de interfaz
+ Analisis de riesgo.