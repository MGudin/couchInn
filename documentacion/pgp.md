# Plan de Gestion De Proyecto


Proyecto: *CouchInn*


Revision: 1


---

| fecha      | revision | autor    | verificado |
| ---        | ---      | ---      | ---        |
| 04/06/2016 | 1        | Grupo 24 |            |


Documento validado por las partes en la fecha:

| Por el cliente | Por la empresa suministradora |
| --- | --- |
|     |     |
|aclaracion: | aclaracion: |

---


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
+ El desarrollo se realizara en Python2.7 sobre el framework Django1.9
+ Se utilizara para la persistencia de los datos el motor de base de
datos MySQL.
+ Sera necesario la contratacion de un servidor externo(web hosting)
+ Por ser una aplicacion web, correra sobre un navegador web en un
dispositivo con conexion a internet.
+ El tiempo de desarrollo de la aplicacion sera de 2 meses (16/5/2016 - 16/7/2016)
+ Se debera utilizar el logo de la empresa.

### 1.I.c Entregables del proyecto.

+ Demo 1: Sabado 04/06/16

+ Demo 2: Sabado 25/06/16

+ Demo 3: Sabado 16/07/16

### 1.I.d Calendario y resumen del presupuesto.
El sistema finalizado se entregará el sábado 16 de Julio de 2016.  El presupuesto del
proyecto es de $63200

## 2 Documentos referenciados

| referencia | titulo | fecha | autor |
| ---        | ---    | ---   | ---   |
| 1          | [entrevista 1]  (https://github.com/chudix/couchInn/blob/master/documentacion/entrevista1.md) | 17/03/2016 | grupo 24 |
| 2          | [entrevista 2] (https://github.com/chudix/couchInn/blob/master/documentacion/entrevista2.md) | 1/04/2016 | grupo 24 |
| 3          | [SRS] (https://github.com/chudix/couchInn/blob/master/documentacion/srs.md) | 10/04/2016  | grupo 24 |
| 4          | [DER] (https://github.com/chudix/couchInn/blob/master/documentacion/CouchInnDB.pdf)| 20/04/2016 | grupo 24 |


## 3 Definiciones y acronimos

Framework: Es un conjunto estandarizado de conceptos, prácticas y criterios para enfocar un tipo de problemática particular que sirve como referencia, para enfrentar y resolver nuevos problemas de índole similar.
Testers: Personas que se encargan de probar las funcionalidades del sistema.
Backup:copia y archivo de datos de la computadora de modo que se puede utilizar para restaurar la información original después de una eventual pérdida de datos.

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

| recurso                     | cantidad | tiempo   | precio x unidad | precio total |
| ---                         | ---      | ---      | ---             | ---          |
| servidor                    | 1        | 12 meses | $3000           | $3000        |
| dominio                     | 1        | 12 meses | us$60           | us$60        |
| servicio de pivotal tracker | 1        | 3 meses  | $400/mes        | $1200        |
| servidor mysql              | 1        | -        | $0              | $0           |


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

| Actividad                        | cantidad | tiempo unitario (hs) | tiempo: sub-total (hs por semana) |
| ---	                           | ---      | ---                  | ---		                 |
| Elicitacion de requisitos        | 3        | 2 horas semanales    | 6 horas                           |                
| Creacion de la pila del producto | 3        | 2 hs semanales       | 6 horas                           |
| Diseno de base de datos          | 3        | 3 hs semanales       | 9 horas                           |
| Planificacion del proyecto       | 3        | 3 hs semanales       | 9 horas                           |
| Analisis de riesgos              | 3        | 3 hs semanales       | 9 horas                           |
| Diseno de interfaz               | 3        | 3 hs semanales       | 9 horas                           |
| Implementacion                   | 3        | 18 hs semanales      | 54 horas                          |
|                                  |          | total                | 102 horas


### 5.II.c Asignacion de presupuesto
El presupuesto queda establecido por la cantidad total de horas de trabajo mas los gastos en recursos establecidos
previamente. Por lo tanto:

Horas de trabajo: 102hs semanales * 8 semanas de desarrollo = 816hs
Monto por hora: $75
Gastos en recursos: $5100

PRESUPUESTO: $66300

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

### 7.IV Plan de aseguramiento de calidad.
NA

### 7.V Plan de revisiones y auditorias
NA

### 7.VI Plan de resolucion de problemas.
NA

### 7.VII Plan de administracion de terceros.
NA

### 7.VIII Plan de mejoras en el proceso.
NA

## 8 Planes adicionales
**Plan de backup:** Se seguirá un plan de backup semanal, en el que se corroborará que el sistema funcione correctamente, sobre todo en sus partes críticas, y se generará una copia de respaldo de la base de datos y cualquier información que se considere relevante en el momento.
**Plan de instalación:** Una vez finalizado el desarrollo del sistema, se instalará y pondrá en producción el sistema, como también se prepararan todos los componentes necesarios para el correcto funcionamiento del sistema, sean: motor de base de datos MySQL, servidor web, etc.
**Plan de mantenimiento:** Durante los primeros 3 meses G24 se hara responsable del mantenimiento del sistema en forma gratuita, pasado ese periodo el cliente podra contratar un abono de mantenimiento mensial o llamar al soporte tecnico cuando lo considere necesario.
