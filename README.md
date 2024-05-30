# Sistema de Gestión de Hotel

Este proyecto es un sistema de gestión de hotel diseñado para manejar reservas, clientes, habitaciones y facturación. El sistema proporciona una interfaz intuitiva para el personal del hotel, facilitando la administración de las operaciones diarias.

## Tabla de Contenidos

- [Características](#características)
- [Requisitos](#requisitos)
- [Instalación](#instalación)
- [Uso](#uso)
- [Estructura del Proyecto](#estructura-del-proyecto)
- [Contribución](#contribución)
- [Licencia](#licencia)
- [Contacto](#contacto)

## Características

- Gestión de reservas de Habitaciones 
- Registro y administracion de clientes
- Control de disponibilidad de habitaciones
- Generación de facturas y recibos
- Interfaz gráfica de usuario fácil de usar

## Requisitos

- [VisualParadigm] Para el diagrma UML
- [Pycharm] Ide de Python
- [Django] Creacion del modelo del Sistema

## Uso

1. Abre tu navegador web y visita `http://localhost:3000`
2. Inicia sesión con las credenciales proporcionadas por el administrador
3. Navega por las diferentes secciones del sistema para gestionar el hotel

## Estructura del Proyecto

```plaintext
sistema-gestion-hotel/
├── src/
│   ├── controllers/
│   ├── models/
│   ├── routes/
│   ├── services/
│   └── utils/
├── public/
│   ├── css/
│   ├── Html/
├── views/
│   ├── layouts/
│   ├── partials/
│   └── pages/
├── .env
├── .gitignore
├── package.json
├── README.md
└── server.js
