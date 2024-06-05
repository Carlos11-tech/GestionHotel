# SISTEMA DE GESTION DE HOTEL

Bienvenidos compañeros a este proyecto que conciste en un sistema de gestión de hotel diseñado para manejar reservas, clientes, habitaciones y facturación. El sistema proporciona una interfaz intuitiva para el personal del hotel, facilitando la administración de las operaciones diarias.
Para ello vamos a realizar el respectivo diagrama UML con sus clases identificadas y sus respectivas relaciones

## DIAGRAMA UML
![Imagen de WhatsApp 2024-06-03 a las 16 33 17_9629c967](https://github.com/Carlos11-tech/GestionHotel/assets/166561281/04b75f51-4b66-4d30-a30a-51f03a6fd771)

#### EXPLICACION DIAGRAMA UML

Partimos de una clase para la reservacion donde se encuentra el poder agregar clientes y emplear una interfza a traves del personal para hacer reservaciones, de igual manera se lleva el control de fecha de ingreso y fecha de salida del cliente
El segundo paquete se refire a la manera para generar una factura , utilizando varias enumeraciones y mandandolas a la super clase de factura donde se establecen los atributos y metodos que se emplearan para generar dicha factura.
El último paquete nos ayuda a gestionar los empleados y poder a su vez contratar, asignar cargo y un turno

#### REALIZACION DE TRABAJO CON ESTRUCTURA GIT FLOW
![image](https://github.com/Carlos11-tech/GestionHotel/assets/166561281/1d591c4a-5d8c-46c9-aedc-e40888c65c18)

# **PASOS DE INTALACION**
##### 1. Activa el Entorno Virtual (si estás usando uno)
Si estás trabajando en un entorno virtual, actívalo utilizando el comando adecuado para tu sistema operativo:

###### En Windows:   
- venv\Scripts\activate

###### En macOS/Linux: 
- source venv/bin/activate

##### 2. Navega al Directorio del Proyecto
Abre una terminal o línea de comandos y navega hasta el directorio raíz de tu proyecto. Por ejemplo:

`cd /ruta/a/tu/proyecto`

##### 3. Instala los Requerimientos
Utiliza el comando pip para instalar los requerimientos desde el archivo requirements.txt:

`pip install -r requirements.txt`

Este comando instalará todas las dependencias listadas en el archivo requirements.txt.

##### 4. Verifica la Instalación (Opcional)
Una vez completada la instalación, puedes verificar que todas las dependencias se instalaron correctamente ejecutando el comando pip list:

`pip list`

Esto mostrará todas las bibliotecas instaladas en tu entorno virtual, lo que te permitirá confirmar que todas las dependencias se han instalado correctamente.

##### 5. Desactiva el Entorno Virtual (Opcional)
Si has terminado de trabajar en tu proyecto, puedes desactivar el entorno virtual:

`deactivate`

Este comando es necesario solo si has activado un entorno virtual al principio.

Siguiendo estos pasos, deberías ser capaz de instalar los requerimientos de tu proyecto Python sin problemas. Este enfoque es útil para asegurarte de que todas las dependencias estén instaladas correctamente y que tu proyecto esté listo para ejecutarse, 

------------


## Características

- Gestión de reservas de Habitaciones 
- Registro y administracion de clientes
- Control de disponibilidad de habitaciones
- Generación de facturas y recibos
- Interfaz gráfica de usuario fácil de usar

 Requisitos

- [VisualParadigm] Para el diagrma UML
- [Pycharm] Ide de Python
- [Django] Creacion del modelo del Sistema

  ## Resultado
  ![ce98f8fa-cd34-437d-bab2-feefc9573416](https://github.com/Carlos11-tech/GestionHotel/assets/166523461/51da7e32-b625-4211-9438-1935fcc97626)
  ![dab0d876-f261-4b73-a904-56cb56e8f774](https://github.com/Carlos11-tech/GestionHotel/assets/166523461/6351ff02-b478-40c5-a7c7-74eb9ff2bbfe)
  ![5b7681bc-2505-4418-9e45-3673d84a9e05](https://github.com/Carlos11-tech/GestionHotel/assets/166523461/33eb568e-cf20-4f37-a992-8cbc37fd36ab)
  ![f785ba3e-2f5c-407b-b3cc-f1ba0a304dd4](https://github.com/Carlos11-tech/GestionHotel/assets/166523461/53c04d3c-07d6-4e7a-b589-64735d299c02)
  ![79d0c117-da0c-498e-822c-bc3acfc2a3e8](https://github.com/Carlos11-tech/GestionHotel/assets/166523461/d589cdd6-492c-4e89-8f71-33fef4a40067)

 ## Como ejecutar nuestro programa en base a esta imagen deben ingresar esos comandos
 ![image](https://github.com/Carlos11-tech/GestionHotel/assets/166523461/67f8c97d-9a11-4a87-931a-bf752b370527)
 ![image](https://github.com/Carlos11-tech/GestionHotel/assets/166523461/de3436b6-36dc-4f40-8b3c-70562a99c544)


  

  


  


