from tkinter import *    # for GUI
import serial    # für UART
from time import sleep # for delay
import os, sys   # für Verzeichnisse auslesen
#from PIL import *
from threading import Thread


#Listes
images = []
imagenumber = 0


#Funktionen:
def callbackbkw():
	global images
	global imagenumber
	imagenumber=imagenumber-1
	if imagenumber < 0:
		imagenumber = len(images) - 1
	picture = 'images_png/' + images[imagenumber]
	print(picture)
	img = PhotoImage(file = picture)
	Label(pictureFrame, image=img).grid(row=0, column=0, padx=10, pady=3)
	MainWindow.mainloop()
	

def callbackfwd():
	global images
	global imagenumber
	imagenumber=imagenumber+1
	if imagenumber >= len(images):
		imagenumber = 0
	picture = 'images_png/' + images[imagenumber]
	print(picture)
	img = PhotoImage(file = picture)
	Label(pictureFrame, image=img).grid(row=0, column=0, padx=10, pady=3)
	MainWindow.mainloop()
	

#vorhandene Ordner/Files anzeigen:
def list_folder():
    for file in os.listdir('images_png'):
        print(file)
        images.append(file)



#Uart Routine
def uart(main_window):
    print("Hello")
    print("World")
    while True:
        print("Hello")
        xneu = ser.readline()
        print(xneu)
	    # der Empfangene Befehl (ein Bild weiter oder zurück) steht jetzt in xneu
        if(xneu == 'fwd'):	#Hier kommt quasi der selbe Befehlsblock wie wenn man im GUI auf den forward Button drücken würde
            main_window.after(0, callbackfwd)
            #imagenumber=imagenumber + 1 
            #picture = 'images_png/' + images[imagenumber]
            #print(picture)
            #img = PhotoImage(file = picture)
            #Label(pictureFrame, image=img).grid(row=0, column=0, padx=10, pady=3)
        elif(xneu == 'bkw'):
            main_window.agter(0, callbackbkw)
            #imagenumber=imagenumber - 1 
            #picture = 'images_png/' + images[imagenumber]
            #print(picture)
            #img = PhotoImage(file = picture)
            #Label(pictureFrame, image=img).grid(row=0, column=0, padx=10, pady=3)
        print("World")
        #main_window.after(0, callbackfwd)
        #sleep(1)

list_folder()
print(images)

#GUI
MainWindow = Tk() #Fenster erstellen
MainWindow.title("Image-Viewer") # Fenster Titel
MainWindow.config(background = '#FFFFFF') # Hintergrundfarbe des Fensters (weiß)
#MainWindow.geometry('1920x1080') # Größe des Fensters

buttonFrame = Frame(MainWindow, width=1080, height = 50) # Frame initialisieren
buttonFrame.grid(row=1, column=0, padx=0, pady=0) # Relative Position und Seitenabstand

pictureFrame = Frame(MainWindow, width=1500, height = 400) 
pictureFrame.grid(row=0, column=0, padx=0, pady=0)

picture = 'images_png/DS1Z_QuickPrint1.png'
img = PhotoImage(file = picture)
Label(pictureFrame, image=img).grid(row=0, column=0, padx=10, pady=3)

buttonClose = Button(buttonFrame, bg='#FF0000', text='X', command=MainWindow.destroy, width=50)
buttonClose.grid(row=0, column=1, padx=0, pady=0)

buttonfwd = Button(buttonFrame, bg='#0000FF', text='Eins Weiter', command=callbackfwd, width=50)
buttonfwd.grid(row=0, column=2, padx=0, pady=0)
                
buttonbkw = Button(buttonFrame, bg='#0000FF', text='Eins Zurück', command=callbackbkw, width=50)
buttonbkw.grid(row=0, column=0, padx=0, pady=0)

#MainWindow.mainloop()
#Statt dem mainloop()-Befehl muss wahlweise eine andere Lösung gefunden werden!
#Das Problem ist, dass ich wegen der GUI-Schleife nicht nebenbei in einer anderen Schleife die UART Schnittstelle abfragen kann.
#Eine Lösung im Internet ist in einer While-Schleife, wo sich ja auch die UART-Empfangsroutine befinden wird,
#'tk.update_idletasks()' und 'tk.update()' zu verwende, wobei dies nicht ganz funktioniert.



#Serielle Schnittstelle initialisieren:
ser = serial.Serial(
        port='/dev/ttyS0', 		#Replace ttyS0 with ttyAM0 for Pi1,Pi2,Pi0
        baudrate = 9600,
        parity=serial.PARITY_NONE,
        stopbits=serial.STOPBITS_ONE,
        bytesize=serial.EIGHTBITS
        #timeout=1				#weiß leider nicht ganz was timeout genau macht
)
# Davor muss noch in den Einstellungen des RPi's die serielle Schnittstelle aktiviert werden:
# https://www.electronicwings.com/raspberry-pi/raspberry-pi-uart-communication-using-python-and-c
# in diesem Tutorial ist alles beschrieben.


thread = Thread(target=uart, args=(MainWindow,), daemon=True)
thread.start()

MainWindow.mainloop()



#Tkinter kann leider keine jpg Bilder anzeigen, sondern nur png und andere, was derzeit noch zu Problemen mit dem Anzeigen der
#Bilder mit sich bringt


#In der Konsole zuvor eingeben, damit Programmtechnische Funktionen installiert werden
#'sudo apt-get install python python-tk idle python-pmw python-pil --yes'
#'sudo apt-get install minicom python-serial'
#'sudo apt-get install xrdp