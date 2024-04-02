<h1 align="center">
  <b>PlayDev</b>
</h1>

<p align="center">
  <img src="videos_app/static/img/Logo app videos.png" alt="PlayDev">
</p>

## Nombre y descripcion 

PlayDev es una aplicación web desarrollada con Django, HTML, CSS, Bootstrap y MySQL. Este proyecto recrea la experiencia de YouTube, ofreciendo una sección de inicio, sistema de autenticación de usuarios, sección de perfil personalizado y un sistema de seguimiento de usuarios.

## Capturas de Pantalla

1. ### Feed de Videos

![image](https://github.com/andresfr1409/ClonYoutubeApp/assets/138944864/4a2f435e-20c1-4e67-88ed-795ffb20d6cd)

2. ### Buscador

![image](https://github.com/andresfr1409/ClonYoutubeApp/assets/138944864/8946dad7-b5e6-41f1-82e8-6f44b2c155f3)

3. ### Perfil 

![image](https://github.com/andresfr1409/ClonYoutubeApp/assets/138944864/e313c56d-714a-405e-a429-612755e72ce7)

4. ### Seccion de Registro

![image](https://github.com/andresfr1409/ClonYoutubeApp/assets/138944864/6aa9b4f0-25f3-4a00-9bd0-fd2ee9c9743e)

5. ### Seccion de Inicio de sesion 

![image](https://github.com/andresfr1409/ClonYoutubeApp/assets/138944864/04897960-70c8-4f55-a99a-2e91008be6d1)

6. ### Seccion de Recuperacion de contraseña

![image](https://github.com/andresfr1409/ClonYoutubeApp/assets/138944864/03a58057-f437-494d-ae08-429f3e152fa3)

7. ### Seccion de Mi perfil

![image](https://github.com/andresfr1409/ClonYoutubeApp/assets/138944864/d97c1199-8724-4a82-8bb6-c90e0b7fc35e)

8. ### Editar de perfil

![image](https://github.com/andresfr1409/ClonYoutubeApp/assets/138944864/5c4ba1c8-6243-4d39-8acb-23d5c21fcfbb)

9. ### Subida de videos

![image](https://github.com/andresfr1409/ClonYoutubeApp/assets/138944864/af1622db-fea7-497e-9bd8-ef74d684e7ff)

10. ### Gestion de videos

![image](https://github.com/andresfr1409/ClonYoutubeApp/assets/138944864/ae9f687f-4c49-48fe-9456-d478b1d11e3f)

11. ### Seguimiento de usuarios

![image](https://github.com/andresfr1409/ClonYoutubeApp/assets/138944864/50d94db0-2833-4d2a-a284-63f4c30393f6)

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

## Uso 

1. ### Registro y Autenticación
  
- Inicia la aplicación y crea una cuenta utilizando la opción de registro.
- Ingresa tu nombre de usuario, correo electrónico y contraseña.
- Después de registrarte, puedes iniciar sesión con tu correo electrónico y contraseña.

2. ### Explora el Feed de Videos

- Accede a la sección de inicio para explorar el feed de videos
- Disfruta de una variedad de contenidos subidos por otros usuarios.

3. ### Busca Videos y Usuarios

- Utiliza el buscador en el navbar para encontrar videos por nombre o buscar usuarios específicos.
- La búsqueda es rápida y proporciona resultados relevantes.

4. ### Gestiona Tu Perfil

- Accede a la sección de tu perfil para ver y editar tu información.
- Personaliza tu perfil agregando o cambiando fotos de perfil y banner.
- Edita tu nombre, correo electrónico y realiza otras modificaciones según tus preferencias.

5. ### Sube y Gestiona Tus Videos

- En la sección de tu perfil, encuentra la opción para subir nuevos videos.
- Proporciona el nombre y la descripción del video.
- Gestiona tus videos existentes, editando o eliminando según sea necesario.

6. ### Sistema de Seguimiento

- Explora la funcionalidad de seguimiento en la sección de perfil.
- Sigue a otros usuarios para mantenerse al tanto de sus actividades y videos.

7. ### Explora Otras Funcionalidades

- Explora todas las funcionalidades ofrecidas, como la recuperación de contraseña y la navegación intuitiva.






