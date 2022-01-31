# GestorHendrix
****************************************************************************************************************************************************************

																		README.txt

****************************************************************************************************************************************************************

Instalacion (acciones opcionales pero recomendadas):

- Se recomienda crear un enlace simbolico mediante el comando "sudo ln -s (ruta donde tienes el ejecutable de la aplicacion) /usr/local/bin" 
  Ejemplo: sudo ln -s /home/$USER/hendrix/hendrix /usr/local/bin"

- Realizar un ssh-keygen y ssh-copy-id para el intercambio de claves con hendrix y poder loguearnos sin necesidad de introducir password

- Se recomienda guardar el contenido de la aplicacion en el directorio "/home/$USER" para el correcto funcionamiento de la opcion relacionada con la desintalacion del programa. 



Listo con este proceso ya has completado la instalacion, a continuacion se muestran las instrucciones de uso

Instrucciones de uso:

-  Para ejecutar el programa necesitas abrir la terminal y escribir desde el directorio que quieras "hendrix".
-  Se abrira un menu con 4 opciones las cuales se describen a continuacion:

   -> 1. Conectarse a Hendrix: Opcion para conectaros a hendrix. Si es la primera vez que usamos el programa nos pedira introducir nuestros datos (nip y password de hendrix), estos datos
        solo se necesitaran introducir la primera vez posteriormente se conectara automaticamente al presionar el boton.

   -> 2. Copiar un archivo a hendrix: Copiar algun archivo del directorio actual en el que nos encontramos a hendrix. Si es la primera vez que usamos el programa y no estan nuestros datos
        registrados se procedera como en el caso anteriormente nombrado.

   -> 3. Salir del programa: Opcion para terminacion del programa.

   -> 4. Desinstalar programa: Opcion para desinstalar el programa. Esta accion no puede ser revertida por lo que ten cuidado de utilizar si estas completamente seguro.


Detalles adicionales:

- Los datos de nuestra cuenta de hendrix se almacenaran en un fichero de configuracion llamado "hendrix.conf" el cual se encontrara situado en nuestro directorio home dentro de un directorio llamado
  "gestorHendrix". Por lo que esto significa que la ruta del fichero sera: "/$HOME/gestorHendrix/hendrix.conf"

Gracias por la utilizacion del programa GESTOR HENDRIX. Cualquier sugerencia o problema hagalo llegar al desarrollador.
