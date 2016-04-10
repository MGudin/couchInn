# Especificacion de requisitos de software


Proyecto: *CouchInn*


Revision: 1


---

| fecha | revision | autor | verificado |
| --- | --- | --- | --- |
| 10/4/2016 | 1 | Grupo 24 |


Documento validado por las partes en la fecha:

| Por el cliente | Por la empresa suministradora |
| --- | --- |
|     |     |
|aclaracion: | aclaracion: |

---

## Contenido

### Ficha del documento
### Contenido

1. INTRODUCCION.[INTRODUCCION][]
   1. Proposito.
   2. Alcance.
   3. Definiciones, acronimos y abreviaturas.
   4. Referencias.
   5. Resumen.

2. DESCRIPCION GENERAL.
   1. Perspectiva del Producto.
   2. Funcionalidades del producto.
   3. Caracteristicas de los usuarios.
   4. Restricciones.
   5. Suposiciones y dependencias.
   6. Evolucion previsible del sistema.

3. REQUISITOS ESPECIFICOS
   1. Requisitos comunes de los interfaces
      1. Interfaces de Usuaios.
      2. Interfaces de Hardware.
      3. Interfaces de Software.
      4. Interfaces de comunicacion.
   2. Requisitos funcionales.
   3. Requisitos no funcionales
      1. Requisitos de rendimiento.
      2. Seguridad.
      3. Fiabilidad.
      4. Disponibilidad.
      5. Mantenibilidad.
      6. Portabilidad.
   4. Otros requisitos.

   

## INTRODUCCION


### 1.I PROPOSITO

El presente documento tiene como propósito definir las
especificaciones funcionales y no funcionales del sistema
para la implementación de una aplicación web que permitirá la gestión
de un sistema de alojamiento para viajeros.

### 1.II ALCANCE

Diseño, desarrollo y sistematización del sistema CouchInn. Dicho sistema
permitirá a los usuarios solicitar y/u ofrecer hospedaje.

### 1.III DEFINICIONES, ACRONIMOS Y ABREVIATURAS

- **Publicar:** Proceso en el que un usuario registrado publica un hospedaje
para su solicitud.
- **Hospedaje:** Alojamiento que se da a una persona en un inmueble.
- **Solicitar:** Pedir una cosa, generalmente de un modo formal y siguiendo
un procedimiento establecido.
- **Calificacion:** Puntuación o palabra con la que se expresa esta
valoración.
- **Rango:** conjunto de niveles en que se divide una actividad o
profesión

### 1.IV REFERENCIAS

| referencia | titulo | fecha | autor |
| ---        | ---    | ---   | ---   |
| 1          | [entrevista 1]  (https://github.com/chudix/couchInn/blob/master/documentacion/entrevista1.md) | 17/03/2016 | grupo 24 |
| 2          | [entrevista 2] (https://github.com/chudix/couchInn/blob/master/documentacion/entrevista2.md) | 1/4/2016 | grupo 24 |

### 1.V RESUMEN

El documento consta de dos secciones. En la sección 2 se busca establecer
una descripción clara del producto, indicando características, funcionalidades,
restricciones, etc. En la sección 3 se describirán los requisitos específicos.

## 2 DESCRIPCION GENERAL

### 2.I PERSPECTIVA DEL PRODUCTO

Es un producto independiente, que se forma a partir de uno ya
creado que intenta sistematizarse debido a la gran demanda que obtuvo
el trabajo inicial.

### 2.II FUNCIONALIDAD DEL PRODUCTO

El sistema debe proporcionar las siguientes funcionalidades:

- Registro de usuarios.
- Publicación de hospedajes y solicitud del mismo.
- Medio de comunicación mediante preguntas y respuestas.
- Sistema de donaciones.
- Especificación de rangos.
- Sistema de calificación.


### 2.III CARACTERISTICAS DE LOS USUARIOS

**Tipo de usuario:** Administrador

**Formacion:** Uso de PC.

**Actividades:** Moderacion de comentarios.

---

**Tipo de usuario:** Usuario Registrado

**Formacion:** Uso de PC.

**Actividades:** Realizacion de preguntas, respuestas. Creacion de hospedajes y pedido de alojamientos.

---

**Tipo de usuario:** Usuario Anonimo.

**Formacion:** Uso de PC.

**Actividades:** Navegacion limitada del sitio, pudiendo unicamente ver las ofertas de alojamiento


### 2.IV RESTRICCIONES

- Los pagos deben realizarse con tarjeta de credito.
- Es necesario para el funcionamiento del sistema tener conxion a internet y un navegador web.
- Es necesario el uso de un servidor.
- El marco geografico es la Republica Argentina.
- Se debe respetar el logo de la empresa y su respectiva gama de colores
  que lo representan.
- El proyecto tiene como tiempo limite de entrega hasta 11-07


### 2.V SUPOSICIONES Y DEPENDENCIAS.

Algunos de los factores que pueden afectar a los requerimientos del
sistema son:
- Contratacion de un servidor externo
- El marco geografico es la Republica Argentina
- Contratacion del servicio Mercado pago
- Agregar nuevas funcionalidades a las ya definidas anteriormente
- Restriccion del presupuesto disponible para desarrollar el sistema

### 2.VI EVOLUCION PREVISIBLE DEL SISTEMA.

Existe la posibilidad de la futura incorporación de las siguientes funcionalidades:
- Sistema de autoadministración de publicaciones y comentarios no permitidos.
- Creación de estadísticas a través de reportes mensuales.
- Sistema de loguin y signup mediante cuentas externas en redes sociales. Ejemplo: facebook, twitter...
- Extension del marco geografico.
- Creacion de newsletter para los usuarios

## 3 REQUISITOS ESPECIFICOS.

### 3.I REQUISITOS COMUNES DE LAS INTERFACES.

#### 3.I.a INTERFACES DE USUARIOS.

El sistema proveerá diferentes interfaces dependiendo del tipo de usuario, entre ellos: Administrador,
Usuario registrado, Usuario anónimo.
La interfaz de la aplicacion se basara en torno al diseño del sitio web AirBnb (Poner link),
con una gama de colores propios reprentativos de la marca CouchInn

#### 3.I.b INTERFACES DE HARDWARE

(N/A)


#### 3.I.c INTERFACES DE SOFTWARE

Las donaciones a través de tarjeta de crédito se realizarán mediante el sistema de Software de MercadoPago.

### 3.II REQUISITOS FUNCIONALES

Serán descriptos como Historias de Usuario. (N/A)


### 3.III REQUISITOS NO FUNCIONALES.

#### 3.III.a REQUISITOS DE RENDIMIENTO

El rendimiento del sistema depende de tres factores, servidor externo contratado, velocidad de la conexión
a internet y hardware del dispositivo en el cual se conecte el usuario.
Segun los estandares actuales de estos tres items pueden garantizarse respuestas casi inmediatas al sistema.

#### 3.III.b SEGURIDAD.

Se utilizara un sistema de login(nombre de usuario y cotraseña), de
esta forma solo los usuarios permitidos tienen acceso a las
funcionalidades del sistema.
Las contraseñas seran cifradas en el servidor, otorgando mayor
seguridad al sistema.


Los formularios tendran un token csrf, para evitar que comandos no
autorizados sean transmitidos por un usuario en el cual el sitio web
confía.

#### 3.III.c FIABILIDAD

El sistema estaria preparado para recuperar toda la informacion
guardada frente a un caso extremo, perdiendose solo los datos de las
operaciones no completadas durante ese fallo.
El sistema garantiza menos de 10 errores por cada 1000 operaciones
realizadas.


#### 3.III.d DISPONIBILIDAD

El sistema estara disponible las 24 horas los 365 dias del año,
siempre y cuando no se produzcan fallas mecanicas o externas al
sistema.


#### 3.III.e MANTENIBILIDAD

Durante los primeros 3 meses G24 se hara responsable del mantenimiento
del sistema en forma gratuita, pasado ese periodo el cliente podra
contratar un abono de mantenimiento mensial o llamar al soporte
tecnico cuando lo considere necesario.


#### 3.III.f PORTABILIDAD

La aplicación estará desarrollada para tablet, smartphone y pc.


### 3.IV OTROS REQUISITOS

(N/A)
