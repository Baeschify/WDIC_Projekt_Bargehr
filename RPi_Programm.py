from tkinter import *    # for GUI
#import serial    # für UART
#from time import sleep # for delay
#import RPi.GPIO as GPIO  # Import Raspberry Pi GPIO library
import os, sys   # für Verzeichnisse auslesen
#from PIL import *

imagenumber = 1
#Liste
images = []

def callbackclose():
    MainWindow.quit()
    
def callbackbkw():
	global images
	global imagenumber
	imagenumber=imagenumber-1
	picture = 'pictures/' + images[imagenumber]
	img = PhotoImage(file = picture)
	Label(pictureFrame, image=img).grid(row=0, column=0, padx=10, pady=3)
	MainWindow.mainloop()

def callbackfwd():
	global images
	global imagenumber
	imagenumber=imagenumber+1
	picture = 'pictures/' + images[imagenumber]
	img = PhotoImage(file = picture)
	Label(pictureFrame, image=img).grid(row=0, column=0, padx=10, pady=3)
	MainWindow.mainloop()

#vorhandene Ordner anzeigen:
def list_folder():
    for file in os.listdir('images'):
        print(file)
        images.append(file)

list_folder()
print(images)

#GUI:
MainWindow = Tk() # Fenster erstellen
MainWindow.title("Raspberry Pi GUI") # Fenster Titel
MainWindow.config(background = '#FFFFFF') # Hintergrundfarbe des Fensters (weiß)
#MainWindow.iconbitmap('/home/pi/WDIC_Projekt')
MainWindow.geometry('1920x1080') # Größe des Fensters

buttonFrame = Frame(MainWindow, width=1080, height = 50) # Frame initialisieren
buttonFrame.grid(row=1, column=0, padx=0, pady=0) # Relative Position und Seitenabstand

pictureFrame = Frame(MainWindow, width=1500, height = 800) 
pictureFrame.grid(row=0, column=0, padx=0, pady=0)

picture = 'images/Kekssortenliste_Seite_1.png'
img = PhotoImage(file = picture)
Label(pictureFrame, image=img).grid(row=0, column=0, padx=10, pady=3)

buttonClose = Button(buttonFrame, bg='#FF0000', text='X', command=MainWindow.quit, width=50)
buttonClose.grid(row=0, column=1, padx=0, pady=0)

buttonfwd = Button(buttonFrame, bg='#0000FF', text='Eins Weiter', command=callbackfwd, width=50)
buttonfwd.grid(row=0, column=2, padx=0, pady=0)
                
buttonbkw = Button(buttonFrame, bg='#0000FF', text='Eins Zurück', command=callbackbkw, width=50)
buttonbkw.grid(row=0, column=0, padx=0, pady=0)

MainWindow.mainloop()
#Als nächstes müssen alle Namen der Bilder in eine Liste gespeichert werden, um danach schön
#nacheinander zwischen den Bildern zu wechseln ohne dass die Bilder nur 1.png 2.png heißen