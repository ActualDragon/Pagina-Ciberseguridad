Glosario
--------

**Credenciales**: *cuenta de usuario* y contraseña.

**Cuenta de usuario**: identificador alfanumérico único que representa un usuario del sistema, también *nombre de usuario*.

**Prospecto**: una persona que aún no es usuario pero podría serlo.

Especificación Funcional
------------------------

1.  Un *Prospecto* puede registrar una cuenta.

    1.  El *Prospecto* proporciona sus credenciales.

    1.  Se genera un *cuenta de usuario* en el sistema si aún no existe.

    1.  Si la *cuenta de usuario* existe, se solicita que elija otra.

1.  Un *Usuario* puede iniciar sesión en el sistema para identificarse (autenticación).

    1.  Si las credenciales son correctas el usuario puede publicar mensajes.

    1.  Si las credenciales son incorrectas se informa al usuario.

1.  Un *Usuario* autenticado puede publicar mensajes de hasta 512 caracteres.

1.  La página principal muestra los 10 mensajes más recientes.

    1.  Si se llega al final de la página, muestra los siguientes 10 mensajes (scroll infinito).
