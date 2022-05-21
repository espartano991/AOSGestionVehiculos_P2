
# Arquitectura Orientada a Servicios 2022
_EQUIPO 4:_
- Sergio Arroyo Ramos _ sergio.arroyoram@alumnos.upm.es
- Alberto Seijo Simó _ a.seijo@alumnos.upm.es
- Víctor Martín Díaz _ victor.martin.diaz@alumnos.upm.es
- Manuel Antonio García Frino _ manuel.gfrino@alumnos.upm.es
- Francisco Andrés Ferreyra _ franciscoandres.ferreyra@alumnos.upm.es
## Consideraciones de diseño y despliegue

### **_Creación de la imagen para el servicio_**
En este caso se ha decidido compilar la imagen con una base de `Ubuntu 18.04`, a la que se le instala `OpenJdK`(la API está implementada en Spring mediante la generación de código de Swagger Codegen). Además, para la implementación se hace uso de persistencia con `MongoDB`. Por tanto, se instala también una versión de mongo mediante el Dockefile.



Para la utilización de la imagen simplemente es necesario descargarla y crear un contenedor con ella:

`docker run --name <nombre> -p 8080:8080 migue9b/trabajos:latest`  
`http://localhost:8080/api/v1` tras arrancar el contenedor.  


modificar de aqui paraa abajo
### **_Docker compose_**
Tras el análisis del resto de servicios se concluyen las siguientes decisiones de diseño de cara al despliegue con `docker-compose`.  

- **Servicio 1** (clientes): API para los clientes. En su especificación se aprecia una implementación del servicio. Sin embargo, la conexión con la BD no es correcta. Sin embargo, se decide crear un contenedor para el servicio con la imagen del subsistema, y otro contenedor para la BD en Mongodb. `http://localhost:8080/clientes`
- **Servicio 2** (vehículos): API para los vehiculos. Se aprecia una conexión correcta con la BD y una implementación funcional. Por tanto, se especifican contenedores para el servicio y para MySQL. `http://localhost:8081/api/v1/ui`
- **Servicio 3** (trabajos): usamos nuestra propia imagen(que no necesita persistencia adicional con contenedor porque ya la lleva incorporada la imagen). `http://localhost:8082/api/v1/`
- **Servicio 4** (notificaciones): API para las notificaciones. Esta API está implementada. Sin embargo, la conexión con la BD no es correcta. Aún así se decide crear un contenedor para el servicio y otro para su persistencia con MySQL. `http://localhost:8083/AOS4`
- **Servicio 5** (facturas): API para las facturas. Se aprecia una pseudoimplementación, en donde las peticiones están "falseadas" con respuestas precreadas. Por tanto, se crea un único contendor. `http://localhost:8084/api/v1/factura`
- **Servicio 6** (recambios): API para los recambios. Esta API también tiene una implementación incompleta, sin persistencia por detrás. Se crea un solo contenedor. `http://localhost:8085/api/v1/recambios` 

Para el despliegue:  
`docker-compose up` sobre la capeta donde se encuentra el archivo.

### **_Kubernetes_**

Esta implementación es parecida a la de docker compose.  
Para Kubernetes se realiza un despliegue por cada servicio. Es decir, 6 despliegues con objetos de tipo `deployment`. Además, se añaden las plantillas para la especificación de los `service` que permiten la conexión a los `pods` desde el exterior. Los puertos que se exponen siguen el mismo esquema que docker-compose.

Para desplegar correctamente los servicios es necesario seguir los siguientes pasos:
1. Para desplegar el clúster en kubernetes hay que ejecutar el comando  `kubectl apply -f kubernetes-deployment.yaml` 
2. Posteriormente para deplegar algún servicio, hay que ejecutar el comando `minikube service nombreServicio --url`. Esto generará la url del servicio a desplegar.
3. Abrir el navegador e introducir `localhost:puertoObtenido/ruta`.
  
### **_Despliegue en la nube de Azure_** 

Mediante Kubernetes hemos desplegado los servicios en un entorno _cloud_. Las capturas se adjuntan en la carpetas _images_.