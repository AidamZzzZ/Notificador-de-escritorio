#se importan las librerias
import time
#se importan los modulos
from winotify import Notification,audio

#se crea una variable llamada toast la cual creara el script(cartelito) de notificacion con todos sus argumentos como Titulo,subtitulo,nombre del mensaje,duracion,etc...
toast = Notification(app_id="Notification Script",
                     title="Notificacion de Gmail",
                     msg="Tienes una notificiacion!.",
                     duration="short",
                     icon=r"C:\Users\Aidam\Desktop\iconsito.png")
#se le agrega el audio a la notificacion
toast.set_audio(audio.SMS,loop=False)
#se le agrega un link,el cual el usuario puede cliclear
toast.add_actions(label="Haz click aqui!", launch="https://mail.google.com/mail/u/0/#inbox")

#muestra todo por pantalla al usuario
toast.show()









