# Documento de diseño de interfaces


Proyecto: *CouchInn*


Revision: 1


---

| fecha | revision | autor | verificado |
| --- | --- | --- | --- |
| 18/5/2016 | 1 | Grupo 24 |


Documento validado por las partes en la fecha:

| Por el cliente | Por la empresa suministradora |
| --- | --- |
|     |     |
|aclaracion: | aclaracion: |

---

## Contenido

1. [Diseño de interfaces](#1-diseño-de-interfaces)
   1. [Tipos de interfaz a utilizar.](#11-tipos-de-interfaz-a-utilizar)
   2. [Tratamiento de errores.](#12-tratamiento-de-errores)
   3. [Manejo de prevencion de errores.](#13-manejo-de-prevencion-de-errores)
   4. [Generacion de ayudas.](#14-generacion-de-ayudas)
   5. [Definicion de atajos.](#15-definicion-de-atajos)
   6. [Manejo de salidas.](#16-manejo-de-salidas)


## 1. Diseño de interfaces.

### 1.1 Tipos de interfaz a utilizar.

#### index

![index][index]


#### Log In
![alt text][login]


#### Sign In
![alt text][signin]

#### Alta de Hospedaje
![alt text][altahospedaje]

#### Pantalla de Publicacion
![alt text][publicacion]

#### Resultado de Busqueda
![alt text][busqueda]

#### Pantalla de perfil
![alt text][perfil]

### 1.2 Tratamiento de errores.

El sistema mostrara un mensaje reportando el problema que haya ocurrido. 

A continuacion se veran varios ejemplos:

#### Error de Log In
![alt text][login_error]

#### URL no encontrada
![alt text][404error]

#### Campo invalido
![alt text][campo_invalido]


### 1.3 Manejo de prevencion de errores.

Siempre que exista un campo a rellenar, se permitirá únicamente el uso de los caracteres
validos para evitar errores.

Dentro de los campos se mostrará una referencia de qué información debe ser ingresada.
En caso de eventos en los cuales sean definitivos (Dar de baja hospedaje, eliminar cuenta,
etc.), se mostrara un mensaje esperando la confirmación del usuario.


### 1.4 Generacion de ayudas.

El sistema contará con una sección de “Preguntas frecuentes” donde se repondrán dudas
básicas sobre el sistema, destinado especialmente a los usuarios finales. Además se
entregará un manual donde se expliquen las funcionalidad del usuario administrador.


### 1.5 Definicion de atajos.

Los atajos serán los brindados por el navegador que este utilizando el usuario durante el
uso del sistema.


### 1.6 Manejo de salidas

Dado que el sistema es utilizado a través de un navegador web, las opciones de retorno y
cierre se podrán realizar desde el mismo navegador. Sin embargo, se añaden los siguientes
accesos dentro del sistema para facilitar la navegación dentro del mismo.


Para acceder a la pagina inicial (index), solo basta con presionar sobre el texto ubicado en
el margen superior derecho. (CouchInn) Este se encontrará en todas las secciones del
sistema permitiendo volver al inicio del sistema en cualquier momento.


Para los usuarios logueados, encontraremos en el margen superior izquierdo el cierre de
sesión en cualquier momento. (Log Out) Este estará disponible siempre y cuando haya una
sesión iniciada.


En ciertos casos, se brindará un link con acceso a la pagina anterior. (Por ejemplo: Volver al
listado de búsquedas)


[campo_invalido]: https://github.com/chudix/couchInn/blob/master/documentacion/MockUp/signin_error.png "Campo invalido"
[404error]: https://github.com/chudix/couchInn/blob/master/documentacion/MockUp/404_error.png "URL no encontrada"
[login_error]: https://github.com/chudix/couchInn/blob/master/documentacion/MockUp/login_error.png "Error de Log In "
[perfil]: https://github.com/chudix/couchInn/blob/master/documentacion/MockUp/perfil.png "Pantalla de perfil "
[busqueda]: https://github.com/chudix/couchInn/blob/master/documentacion/MockUp/busqueda.png "busqueda"
[publicacion]: https://github.com/chudix/couchInn/blob/master/documentacion/MockUp/publicacion.png "Pantalla de publicacion"
[altahospedaje]: https://github.com/chudix/couchInn/blob/master/documentacion/MockUp/alta_hospedaje.jpg "Alta de Hospadaje"
[signin]: https://github.com/chudix/couchInn/blob/master/documentacion/MockUp/signin.png "Sign in"
[login]: https://github.com/chudix/couchInn/blob/master/documentacion/MockUp/login.png "Log In"
[index]: https://github.com/chudix/couchInn/blob/master/documentacion/MockUp/index.png "Index"
