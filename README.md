# WDIC_Projekt_Bargehr
 Im Rahmen des WDIC Unterrichts ist ein Projekt zu machen

Es soll ein GUI Programm auf dem RaspberryPi programmiert werden,
welches zwischen Bildern wechseln kann, welche sich in einem Ordner befinden.
Zum Umschalten zwischen den Bildern gibt es eine UART Kommunikation zwischen 
einer Megacard und dem RaspberryPi. Sobald auf der Megacard eine Taste gedrückt wird,
wird eine Info per UART zum RaspberryPi gesendet und das Bild wechselt.



MainWindow.mainloop() / Schleifenproblem + Lösung:
Statt dem mainloop()-Befehl muss wahlweise eine andere Lösung gefunden werden!
Das Problem ist, dass ich wegen der GUI-Schleife nicht nebenbei in einer anderen Schleife die UART Schnittstelle abfragen kann.
Eine Lösung im Internet ist in einer While-Schleife, wo sich ja auch die UART-Empfangsroutine befinden wird,
'tk.update_idletasks()' und 'tk.update()' zu verwende, wobei dies nicht ganz funktioniert.
Das Problem mit der Schleife wurde mit Threading gelöst.


Bevor man die UART in Betrieb nehmen kann, muss man noch in den Einstellungen des RPi's die serielle Schnittstelle aktivieren:
https://www.electronicwings.com/raspberry-pi/raspberry-pi-uart-communication-using-python-and-c
in diesem Tutorial ist alles beschrieben.


Tkinter kann leider keine jpg Bilder anzeigen, sondern nur png und andere, was derzeit noch zu Problemen mit dem Anzeigen der
Bilder mit sich bringt. Lösung ist einfach: nur png Bilder verwenden.


In der Konsole muss man ein paar Befehle zuvor eingeben, damit Programmtechnische Funktionen installiert werden
'sudo apt-get install python python-tk idle python-pmw python-pil --yes'        # Tkinter/GUI
'sudo apt-get install minicom python-serial'                                    # UART
'sudo apt-get install xrdp                                                      # RemoteDesktop
