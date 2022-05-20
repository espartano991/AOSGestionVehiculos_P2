
# Arquitectura Orientada a Servicios 2022
_EQUIPO 4:_
- Sergio Arroyo Ramos _ sergio.arroyoram@alumnos.upm.es
- Alberto Seijo Simó _ a.seijo@alumnos.upm.es
- Víctor Martín Díaz _ victor.martin.diaz@alumnos.upm.es
- Manuel Antonio García Frino _ manuel.gfrino@alumnos.upm.es
- Francisco Andrés Ferreyra _ franciscoandres.ferreyra@alumnos.upm.es
## Subsistema 2: gestión de vehículos de un taller
### _**Consideraciones de diseño tomadas**_
- Se han añadido 4 métodos `GET` | `POST` | `DELETE` | `OPTION`. Se consideró que para la gestión de los vehículos de un taller eran necesarias.

- Se han añadido dos métodos `GET` uno para recuperar el listado de todos los vehículos, ya sea ordenados por: VIN, anno, reparacionUltima, clienteID. Además, también se puede ordenar por orden ascendente o descendente. Y otro método para buscar por VIN de vehículo, que es el único atributo que no se repite.

- Se ha considerado que el método `POST` necesita como mínimo los siguientes valores: Matrícula, la marca, el modelo, el anno de fabricación, el motor, el id del cliente propietario del vehículo.

- Tras la implementación de los métodos `PUT` y `DELETE` (completan las operaciones CRUD), la especificación alcanza el Nivel 2 de madurez de Richardson. Para alcanzar _**the glory of REST**_, se implementa HATEOAS. Se introducen los _links_ para completar la información del vehículo. En este caso, hacen referencia al listado de todos los vehículos y a las posibles acciones que se pueden realizar con el vehículo

- Se adjuntan pruebas de todos los métodos y _responses_ posibles en el mismo archivo openapi.yaml.
  
### **_Instrucciones para desplegar el servicio desde 0🐳_**
###
Para llevar a cabo el despliegue del servicio son necesarios tres componentes fundamentales:
- Backend. Con un servidor Mock que hace las veces de server de prueba para realizar las peticiones. 
- Frontend. Con una utilidad que levanta un servidor HTTP y habilita una interfaz gráfica.
- Proxy. Con un servidor Proxy que resuelva los problemas de rutas entre Backend y Frontend.

_Docker_ nos permite agrupar los tres componentes sin necesidad de usar una máquina virtual o servidor remoto.
Para cada parte respectivamente se hará uso de:
- SpotLight/Prism
- Swagger-UI
- Caddy

Los pasos para el despliegue, mediante el uso de `docker-compose`, son los siguientes:


#### **1. Situarse en la carpeta de la especificación**

- `cd /ruta/a/la/carpetaBase`

#### **2. Iniciar Docker**

Abrir el _Daemon_ de Docker en la máquina(imprescindible haber instalado Docker Desktop previamente)

#### **3. Ejecutar Docker Compose**

Una vez situado en la carpeta de la especificación, ejecutar el siguiente comando:

- `docker-compose up` (imprescindible estar en la carpeta del proyecto; ya que en esa ruta se encuentra el `.yaml`
del Docker Compose).

En caso de que no se pueda llevar a cabo, añadir la siguiente sentencia después de `up`:

- `--force-recreate`
  
La línea de comando a ejecutar quedaría de la siguiente manera:
`docker-compose up --force-recreate`

#### **4. Acceder al navegador**

En la ruta del navegador, acceder a la URL: `localhost:8000`

#### **5. Juega**

Realizar las peticiones deseadas desde la UI de Swagger. Podrás probar cualquiera de las funcionalidades disponibles.

# AOSgestionvehiculos

> Atributos finales:
- vin (string)
- matricula (string)
- marca (string)
- modelo (string)
- motor (cilindrada, CV, tipo de motor) (Text)
- anno (int)
- reparación (fecha ultima reparación) (Text) 
- clienteID (string)

> Respuestas_HTTP:
- 200 OK
- 201 Created
- 400 Bad Request
- 403 Forbidden
- 401 unauthorized
- 404 Not Found
- 408 Request Timeout
- 412 Precondition failed (el ETag no es el mismo)
- 422 Unprocessable Entity: validación de parámetros fallida
- 500 Internal Server Error
