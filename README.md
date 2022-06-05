
# Arquitectura Orientada a Servicios 2022
_EQUIPO 4:_
- Sergio Arroyo Ramos _ sergio.arroyoram@alumnos.upm.es
- Alberto Seijo Simó _ a.seijo@alumnos.upm.es
- Víctor Martín Díaz _ victor.martin.diaz@alumnos.upm.es
- Manuel Antonio García Frino _ manuel.gfrino@alumnos.upm.es
- Francisco Andrés Ferreyra _ franciscoandres.ferreyra@alumnos.upm.es
## Consideraciones de diseño y despliegue
Es necesario tener instalados los siguientes progarmas:
- Minikube
- docker
- kubernetes
### **_Creación de la imagen para el servicio_**
En este caso se ha decidido compilar la imagen con una base de `Ubuntu 18.04`, a la que se le instala `OpenJdK`(la API está implementada en Spring mediante la generación de código de Swagger Codegen). Además, para la implementación se hace uso de persistencia con `MongoDB`. Por tanto, se instala también una versión de mongo mediante el Dockefile.



Para la utilización de la imagen simplemente es necesario descargarla y crear un contenedor con ella:
Para descargar: `docker pull albertoseijo/aos_grupo4_global:serviciovehiculos`
`docker run --name <nombre> -p 8080:8080 albertoseijo/aos_grupo4_global:serviciovehiculos`  



modificar de aqui paraa abajo
### **_Docker compose_**
Tras el análisis del resto de servicios se concluyen las siguientes decisiones de diseño de cara al despliegue con `docker-compose`. Debido a que ningun grupo ha especificado el lugar donde se ha subido la imagen en docker hub, hemos subido todas las imagenes de cada grupo a nuestro repositorio de docker hub, cambiando las imagenes por el tag, para que todas estén en el mismo repositorio de docker-hub.
Todas las imagenes pueden verse en el siguiente link:
`https://hub.docker.com/r/albertoseijo/aos_grupo4/tags`

Para igualar los puertos endpoints de cada imagen, lo que hemos hecho es modificar los mismos en las imagenes subidas al dockerhub a 808X, y luego en el docker-compose lo redireccionamos todo al puerto 8080.
Por otra parte, debido a que no tenemos implementada nuestra imagen (vehñiculos) hemos añadido la pseudoimplementacion con swagger. por lo que hemos añadido el backend y frontend de lo mismo direccionándolo al puerto 8000.

- **Servicio 1** (clientes): API para los clientes. No observamos que la API esté implementada ni que tenga una BBDD, por lo que no vemos necesario levantar un contenedor. 
- **Servicio 2** (vehículos): API para los vehiculos. Levantamos un servicio en la imagen para la BBDD de mongo.Imagen realizada por nosotros. Debido a la pseudoimplementacion de la openapi por swagger, hemos añadido el swagger en el docker compose para poder levantarla correctamente.
- **Servicio 3** (trabajos): API para los trabajos. No observamos que la API esté implementada ni que tenga una BBDD, por lo que no vemos necesario levantar un contenedor. 
- **Servicio 4** (notificaciones): API para las notificaciones. No observamos que la API esté implementada ni que tenga una BBDD, por lo que no vemos necesario levantar un contenedor.
- **Servicio 5** (facturas): API para las facturas.  No observamos que la API esté implementada ni que tenga una BBDD, por lo que no vemos necesario levantar un contenedor. 
- **Servicio 6** (recambios): API para los recambios. Esta API también tiene una implementación incompleta, sin persistencia por detrás. Se crea un solo contenedor.
- **Servicio 6** (logs): API para los logs. Esta API también tiene una implementación incompleta, sin persistencia por detrás. Se crea un solo contenedor.

Para el despliegue:
Asegurarse que se está en la misma carpeta que el archivo de docker-compose.  
`docker-compose up` sobre la capeta donde se encuentra el archivo.

### **_Kubernetes_**

Esta implementación es parecida a la de docker compose.  
Para Kubernetes se realiza un despliegue por cada servicio. Es decir, 7 despliegues con objetos de tipo `deployment`. Además, se añaden las plantillas para la especificación de los `service` que permiten la conexión a los `pods` desde el exterior. Los puertos que se exponen siguen el mismo esquema que docker-compose.

Para desplegar correctamente los servicios es necesario seguir los siguientes pasos:
1. Para desplegar el clúster en kubernetes hay que ejecutar el comando  `kubectl apply -f despliegue.yaml` 
2. Posteriormente para deplegar algún servicio, hay que ejecutar el comando `minikube service nombreServicio --url`. Esto generará la url del servicio a desplegar.
3. Abrir el navegador e introducir `localhost:puertoObtenido/ruta`.
  
### **_Despliegue en la nube de Azure_** 

Mediante Kubernetes hemos desplegado los servicios en un entorno _cloud_. Las capturas se adjuntan en la carpetas _images_.