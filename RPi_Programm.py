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
    print("UART Thread gestartet!")
    while True:
        data = ser.readline()
        print(data)
	    # der Empfangene Befehl (ein Bild weiter oder zurück) steht jetzt in xneu
        if data == b'fwd':
            main_window.after(0, callbackfwd)
        elif data == b'bkw':
            main_window.after(0, callbackbkw)


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


#Serielle Schnittstelle initialisieren:
ser = serial.Serial(
        port='/dev/ttyS0', 		#Replace ttyS0 with ttyAM0 for Pi1,Pi2,Pi0
        baudrate = 9600,
        parity=serial.PARITY_NONE,
        stopbits=serial.STOPBITS_ONE,
        bytesize=serial.EIGHTBITS,
        timeout=1				#weiß leider nicht ganz was timeout genau macht
)


thread = Thread(target=uart, args=(MainWindow,), daemon=True)
thread.start()

MainWindow.mainloop()