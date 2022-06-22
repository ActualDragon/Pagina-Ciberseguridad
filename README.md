Para estudiantes de licenciatura que quieren aprender ciberseguridad

# Proyecto de Ciberseguridad (Verano 2022)

Es una práctica de desarrollo que permite practicar habilidades de desarrollo seguro y a diferencia de otros proyectos pre-diseñados nuestro producto permite explorar desarrollo y remediación.

Las [especificaciones funcionales](./spec.md) describen la funcionalidad esperada del proyecto.

Cada caso tiene una funcionalidad díficil de implementar en forma segura y el tiempo para desarrollar el código funcional es limitado.

- En la primera etapa, no intentes que el código sea seguro o inseguro, únicamente concéntrate en que funcione.

- En la segunda etapa, buscaremos los errores de seguridad que se generaron durante la programación y los usaremos para hacer funcionar al programa de forma inesperada.

- En la tercera etapa, remediaremos los errores que encontramos.

## Requerimientos del sistema

Para poder utilizar el código de forma local se necesitan hacer las siguientes intstalaciones:

### General

- [Docker](https://www.docker.com/products/docker-desktop/)
- [Python v3^](https://www.python.org/downloads/)
- [Firebase](https://console.firebase.google.com/)

### MacOS

```zsh
brew install git-crypt
brew install virtualenv
brew install pre-commit
```

## Esctructura del código

El repositorio esta estructurado de la siguiente manera:
- **app**: carpeta que contiene el fullstack de nuestra página web, se utilizó una arquitectura MVC.
    - **classes**: carpeta que contiene clases de nuestro programa.
    - **models**: carpeta que contiene modelos de las collecciones de la base de datos.
    - **static**: contenido estático utilizado en el front end.
        - **images**: imágenes de nuestra página web.
        - **js**: código para dar lógica a nuestro frontend.
    - **templates**: archivos HTML de la página.
    - **tests**: pruebas utilizadas por el código.
    - **views**: vistas de la aplicación (archivos a renderear).
    - **controller.py**: archivo orquestrador, ruteo de las requests.
    - **__init.py__**: archivo que inicializa el firebase-manager, controlador y sessión del usuario cifrada.
- **cmd**: scripts utilizados durante el desarrollo.
- **containers**: contenedores de Docker que se utilizaron.
    - **code-tests**: YAML de pre-commit, YAML de compose y Dockerfile que genera el ambiente de pruebas.
    - **dev**: YAML de compose para development, este archivo monta los archivos de código locales dentro del contenedor para permitir cambios a través de comando `touch uwsgi.ini` en el directorio local.
    - **prod**: YAML de compose que construye el ambiente y Dockerfile que genera la imagen que queremos utilizar.
    - **.flake8**: archivo de linter con sus reglas.
    - **.gitattributes**: decimos a git-crypt que encriptar.
    - **.gitignore**: archivos que no queremos agregar a GitLab.
    - **credentials.json**: archivo que contiene credenciales de acceso a Firebase.
    - **main.py**: inicializa todo el programa.
    - **makefile**: commandos de make para el repositorio.
    - **pyproject.toml**: reglas de black (auto-formatter) y pytest.
    - **requirements.txt**: paquetes de python que debemos instalar.
    - **uwsgi.ini**: middleware de aplicación y servidor, ejecuta la aplicación.
