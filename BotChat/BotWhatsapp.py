import pywhatkit as kit
import time

""" Con la libreria time,manejas eventos con respento al tiempo,
en caso que quieras cronometrar eventos o, en este caso, mandas
mensajes a un cierto horario"""


# num = "+5493544438465"
num = "+5493533684061"

path_img = "/home/fer/Desktop/Python_New/BotChat/Img/Fabri.png"

# pywhatkit.sendwhatmsg_to_group(id_grup,"Mensaje de Prueba",8,28)

# pywhatkit.sendwhats_image(id_grup, path_img,"Mensaje medio raro")


# Send an Image to a Group with the Caption as Hello
# pywhatkit.sendwhats_image(num, path_img, "Hello")
# Send an Image to a Contact with the no Caption
kit.sendwhats_image(phone_no = num, img_path = path_img,caption = "Recordatorio de Tarea,prueba de pywhatkit...")

"""

# Send a WhatsApp Message to a Contact at 1:30 PM
pywhatkit.sendwhatmsg("+910123456789", "Hi", 13, 30)

# Same as above but Closes the Tab in 2 Seconds after Sending the Message
pywhatkit.sendwhatmsg("+910123456789", "Hi", 13, 30, 15, True, 2)

# Send an Image to a Group with the Caption as Hello
pywhatkit.sendwhats_image("AB123CDEFGHijklmn", "Images/Hello.png", "Hello")

# Send an Image to a Contact with the no Caption
pywhatkit.sendwhats_image("+910123456789", "Images/Hello.png")

# Send a WhatsApp Message to a Group at 12:00 AM
pywhatkit.sendwhatmsg_to_group("AB123CDEFGHijklmn", "Hey All!", 0, 0)

# Send a WhatsApp Message to a Group instantly
pywhatkit.sendwhatmsg_to_group_instantly("AB123CDEFGHijklmn", "Hey All!")

# Play a Video on YouTube
pywhatkit.playonyt("PyWhatKit")

"""