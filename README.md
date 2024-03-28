# used-cars-django
Proyecto Django como una web dinámica sobre Linux, Ubuntu 16.04. Esto se debe a que el sitio es interactivo y personalizado según las acciones del usuario.

## Descripción técnica de los elementos que tiene esta página
Logo: Es una imagen que identifica visualmente la marca o el sitio web.

### Botones:

- Inicio de sesión: Permite al usuario iniciar sesión ingresando su nombre de usuario y contraseña. Si el usuario no está autenticado, solo puede ver los primeros 4 autos de la página de inicio.
- Bienvenido: Aparece después de iniciar sesión, mostrando un saludo personalizado al usuario.
- Inicio: Muestra una imagen y una descripción de 4 autos diferentes, separados por un espacio.
- Acerca: Contiene información sobre la empresa, como su historia, misión, visión, etc. pero yo la llené con 2 "Lorem ipsum".
- Contacto: Presenta un formulario con campos para el nombre, correo y mensaje del usuario. Al enviar el formulario, se redirige a otra página que muestra un mensaje de confirmación.
- Conoce más: Presente solo en la página de inicio, redirige a la página Acerca.
- Mensaje de bienvenida: Se muestra en la página de inicio de sesión después de iniciar sesión correctamente, dando la bienvenida al usuario por su nombre.
- Superusuario admin: Es un usuario con privilegios especiales que permite modificar las imágenes de los autos y sus descripciones tanto en la página de inicio como en la página de bienvenida.
- Footer: Sección al final de la página que muestra información adicional, como "Creado por" seguido del nombre de la empresa.

### Username: admin
### Password: admin

## Descripción técnica paso a paso de cómo crear un proyecto Django llamado "Used Cars":

### Pasos previos:

1ro Se crea un ambiente virtual (hay muchas maneras de hacerlo).
2do Se intala el archivo requiriments.txt así: pip install -r requirements.txt
Esto nos permitirá un sistema orquesatdo entre las bibliotecas y dependencias usadas en el proyecto.

1. Instalar Django: Si no tienes Django instalado, puedes hacerlo usando pip, el gestor de paquetes de Python. Abre una terminal y ejecuta el siguiente comando:
   pip install django
   
2. Crear un nuevo proyecto Django: Abre una terminal en la ubicación donde desees crear el proyecto y ejecuta el siguiente comando:
   django-admin startproject usedcars
   
3. Navegar al directorio del proyecto: Ingresa al directorio recién creado ejecutando el siguiente comando:
   cd usedcars
   
4. Crear una aplicación: En Django, una aplicación es un conjunto de funcionalidades relacionadas. Puedes crear una nueva aplicación ejecutando el siguiente comando:
   python manage.py startapp web
   
5. Definir modelos de datos: Abre el archivo models.py dentro de la carpeta web y define los modelos de datos para tu aplicación. Por ejemplo, podrías tener un modelo para representar un vehículo.
    
6. Migraciones de la base de datos: Después de definir los modelos, crea las migraciones ejecutando los siguientes comandos:
   python manage.py makemigrations
   python manage.py migrate
7. Crear vistas: Abre el archivo views.py dentro de la carpeta web y define las vistas para tu aplicación. Las vistas son funciones que procesan las solicitudes HTTP y devuelven respuestas.

8. Configurar URLs: Abre el archivo urls.py dentro de la carpeta web y define las URL para tu aplicación. Mapea las URL a las vistas correspondientes.

9. Crear plantillas HTML: Crea las plantillas HTML para tu aplicación dentro de la carpeta templates. Estas plantillas definirán la apariencia de tus páginas web.

10. Definir archivos estáticos: Si tienes archivos estáticos como CSS, JavaScript o imágenes, colócalos en la carpeta static.

11. Ejecutar el servidor de desarrollo: Ejecuta el siguiente comando para iniciar el servidor de desarrollo de Django:
    python manage.py runserver

12. Acceder a la aplicación: Abre un navegador web y navega a http://localhost:8000/ para acceder a tu aplicación.
    El enlace "http://127.0.0.1:8000/" generalmente se refiere a la dirección local de un servidor en ejecución en tu computadora.
    Cuando ejecutas un servidor web localmente, a menudo se asigna al puerto 8000 por defecto.

13. Acceder a la aplicación como superusuario: Abre un navegador web y navega a http://localhost:8000/admin para acceder a tu aplicación y modificar elementos.


