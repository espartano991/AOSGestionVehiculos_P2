# AOS-Grupo 6
      Juan José Meneses Fernández
	  Víctor Díaz de Diego
	  Raúl Núñez Alonso
	  Víctor Sánchez Corrales
	 
# Descripción

Creación de un subsistema para gestión de clientes de un taller

# Instalación y Uso
Para llevar a cabo el despliegue del servicio son necesarios tres componentes fundamentales:

    Backend. Con un servidor Mock que hace las veces de server de prueba para realizar las peticiones.
    Frontend. Con una utilidad que levanta un servidor HTTP y habilita una interfaz gráfica.
    Proxy. Con un servidor Proxy que resuelva los problemas de rutas entre Backend y Frontend.

Docker nos permite agrupar los tres componentes sin necesidad de usar una máquina virtual o servidor remoto. Para cada parte respectivamente se hará uso de:

    SpotLight/Prism
    Swagger-UI
    Caddy

Los pasos para el despliegue, mediante el uso de docker-compose, son los siguientes:

	1. Descomprimir el fichero .zip

		Descomprimir el archivo en una carpeta de fácil acceso.
	2. Abrir la consola

		Para Windows:

		    Windows + r
		    Escribe cmd y pulsa Intro

		Para máquinas basadas en Linux:

		    CTRL + T

		Para MacOS:

		    OPTION + espacio
		    Escribe terminal y pulsa Intro

	3. Situarse en la carpeta de la especificación

		cd /ruta/a/la/carpeta

	4. Ejecutar Docker

		Abrir el Daemon de Docker en la máquina(imprescindible haber instalado Docker Desktop previamente)

	5. Ejecutar Docker Compose

		Una vez situado en la carpeta de la especificación, ejecutar el siguiente comando:

		    docker-compose up (imprescindible estar en la carpeta del proyecto; ya que en esa ruta se encuentra el .yaml del Docker Compose).

		En caso de que no se pueda llevar a cabo, añadir la siguiente sentencia después de up:

		    --force-recreate

	6. Acceder al navegador

		En la ruta del navegador, acceder a la URL: localhost:8000

	7. Probar la API

		Realizar las peticiones deseadas desde la UI de Swagger.


# Guía de Uso

#### Para registrar un nuevo cliente

		POST http://x.x.x.x:8080/clientes
		Body:
		{
				"nif/nie": "90596299-X",
				"idCliente": 452,
				"nombre": "Juanjo",
				"apellidos": "Meneses",
				"domicilio": "Calle Indalecio 32",
				"telefono": "638765432",
				"email": "jjmeneses@outlook.es"
			}

#### Para obtener los clientes del taller 

	  GET http://x.x.x.x:8080/clientes

#### Para modificar datos de un cliente del taller (identificado por idCliente)

		PUT http://x.x.x.x:8080/clientes/2022
		headers:
			  if-match = 24f21ae791234aeb
		Body:
		{
				"nif/nie": "67834236-N",
				"idCliente": 42,
				"nombre": "Victor",
				"apellidos": "Diaz",
				"domicilio": "Calle Europa 4",
				"telefono": "665492318",
				"email": "vidiaz@gmail.com"
			}

#### Para obtener datos de un cliente del taller (identificado por idCliente)

		GET http://x.x.x.x:8080/clientes/2022
		
#### Para obtener datos de un cliente del taller (identificado por su NIF o NIE)

		GET http://x.x.x.x:8080/clientes/nifnie/52013776-T
		
#### Para obtener una lista de clientes por nombre 

		GET http://x.x.x.x:8080/clientes/nombre/Francisco
		
