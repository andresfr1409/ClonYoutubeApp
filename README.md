<h1 align="center">
  <b>PlayDev</b>
</h1>

<p align="center">
  <img src="" alt="PlayDev">
</p>

## Nombre y descripcion 

PlayDev es una aplicación web desarrollada con Django, HTML, CSS, Bootstrap y MySQL. Este proyecto recrea la experiencia de YouTube, ofreciendo una sección de inicio, sistema de autenticación de usuarios, sección de perfil personalizado y un sistema de seguimiento de usuarios.

## Capturas de Pantalla

pendiente

## Funcionalidades Principales

1. ### Sección de Inicio

#### Feed de Videos

- Muestra un feed dinámico de videos subidos por diversos usuarios, proporcionando una experiencia similar a la de YouTube.

- Los videos se ordenan según la fecha de publicación, brindando a los usuarios una visión completa de la diversidad de contenido.

#### Buscador

- Incluye un buscador integrado en el navbar para facilitar a los usuarios la búsqueda de videos por nombre o usuarios específicos para ver sus perfiles.
- La búsqueda es rápida y precisa, mejorando la accesibilidad a los contenidos deseados.

2. ### Sistema de Autenticación:

#### Registro de Usuarios

- Permite a los usuarios registrarse proporcionando su nombre de usuario, correo electrónico y contraseña.
- La información del usuario se almacena de manera segura en la base de datos, garantizando la integridad de los datos.

#### Inicio de Sesión

- Ofrece un sistema de inicio de sesión que autentica a los usuarios mediante el ingreso de su correo electrónico y contraseña registrada.
- La autenticación se realiza de manera segura, protegiendo las cuentas de los usuarios.

#### Recuperación de Contraseña

- Permite a los usuarios cambiar su contraseña en caso de olvido a través de un proceso seguro y verificable.
- El sistema garantiza la privacidad y seguridad durante el proceso de recuperación.

3. ### Sección de Mi Perfil

#### Información del Perfil

- Muestra la información del usuario autenticado, incluyendo nombre, correo electrónico, foto de perfil y banner.
- Proporciona una experiencia similar a YouTube, donde los usuarios pueden personalizar su perfil de manera intuitiva.

#### Edición del Perfil

- Permite al usuario editar su información, cambiar su nombre de usuario, correo electrónico, agregar o cambiar fotos de perfil y banner.
- La interfaz es amigable, facilitando a los usuarios la personalización de su presencia en la plataforma.

#### Subida de Videos

- Permite a los usuarios subir videos proporcionando nombre y descripción.
- Los videos se almacenan en la base de datos MySQL, asegurando una gestión eficiente de los contenidos multimedia.

#### Gestión de Videos

- Permite a los usuarios ver, editar o eliminar los videos que han subido.
- La gestión de videos es fácil e intuitiva, brindando control total sobre el contenido compartido.

4. ### Sistema de Seguimiento de Usuarios

#### Relaciones de Seguimiento

- Permite a los usuarios seguir a otros usuarios, estableciendo relaciones en la base de datos.
- La funcionalidad de seguimiento mejora la interacción y la conexión entre los usuarios de la plataforma.

## Tenologias Utilizadas

### Django

- Django se utiliza para construir la estructura de la aplicación, manejar el sistema de autenticación, gestionar relaciones en la base de datos y más.
- Proporciona una arquitectura MVT sólida para el desarrollo rápido y eficiente.

### HTML, CSS y Bootstrap

- HTML y CSS se combinan con Bootstrap para crear una interfaz visualmente atractiva y receptiva.
- Bootstrap acelera el desarrollo al proporcionar componentes y estilos predefinidos.

### MySQL

- MySQL se utiliza para almacenar y gestionar información, incluyendo perfiles de usuario, videos y relaciones de seguimiento.
- Ofrece una solución eficiente y escalable para la persistencia de datos.

## Instalacion

1. Clonar el repositorio
2. Configurar el entorno virtual y instalar las dependencias con el comando "pip install -r requirements.txt".
3. Configurar la Base de Datos

Cree una base de datos MySQL y configure las credenciales en el archivo settings.py en el directorio myproject/settings.py.

![image](https://github.com/andresfr1409/BibliotecaDeCine/assets/138944864/d64f4f26-d464-4fe6-a33d-a51efb91e8a9)

4. Ejecuta las migraciones con "python manage.py makemigrations" y despues ejecutar "python manage.py migrate".
5. Inicia el servidor de desarrollo local con el comando "python manage.py runserver".









