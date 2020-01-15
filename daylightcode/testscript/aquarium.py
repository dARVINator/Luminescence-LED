"""
**************************************************************************
V24
Aquariensteuerung Lampen/CO2/Tagesdünger/Nachfuellen/Temperatur
Abends und Morgens
==> Aus-an-Zeiten selber einstellbar
Zeit Variablen muessen im Format hh:mm angeben werden !!!!
Nachfuell-Zeiten muessen min. 5 Minuten auseinander liegen!


*************************** Variablen ******************************

Lampe1       = Boolean, Schaltzustand Lampe1
Lampe2       = Boolean, Schaltzustand Lampe2
Lampe3       = Boolean, Schaltzustand Lampe3
CO2          = Boolean, Schaltzustand CO2
Duengerpumpe = Boolean, Schaltzustand Tagesduengerpumpe
Fuellpumpe   = Boolean, Schaltzustand Nachfuellpumpe
Bodenheizer  = Boolean, Schaltzustand Bodenheizer
Stabheizer   = Boolean, Schaltzustand Stabheizer
alive        = Boolean, Anzeige, dass Programm läuft

m1           = Einschaltzeit morgens Lampe 1
m2           = Ausschaltzeit morgens Lampe 1
m3           = Einschaltzeit morgens Lampe 2
m4           = Ausschaltzeit morgens Lampe 2
m5           = Einschaltzeit morgens Lampe 3
m6           = Ausschaltzeit morgen"""
**************************************************************************
V24
Aquariensteuerung Lampen/CO2/Tagesdünger/Nachfuellen/Temperatur
Abends und Morgens
==> Aus-an-Zeiten selber einstellbar
Zeit Variablen muessen im Format hh:mm angeben werden !!!!
Nachfuell-Zeiten muessen min. 5 Minuten auseinander liegen!


*************************** Variablen ******************************

Lampe1       = Boolean, Schaltzustand Lampe1
Lampe2       = Boolean, Schaltzustand Lampe2
Lampe3       = Boolean, Schaltzustand Lampe3
CO2          = Boolean, Schaltzustand CO2
Duengerpumpe = Boolean, Schaltzustand Tagesduengerpumpe
Fuellpumpe   = Boolean, Schaltzustand Nachfuellpumpe
Bodenheizer  = Boolean, Schaltzustand Bodenheizer
Stabheizer   = Boolean, Schaltzustand Stabheizer
alive        = Boolean, Anzeige, dass Programm läuft

m1           = Einschaltzeit morgens Lampe 1
m2           = Ausschaltzeit morgens Lampe 1
m3           = Einschaltzeit morgens Lampe 2
m4           = Ausschaltzeit morgens Lampe 2
m5           = Einschaltzeit morgens Lampe 3
m6           = Ausschaltzeit morgens Lampe 3
m7           = Einschaltzeit morgens CO2
m8           = Ausschaltzeit morgens Co2

a1           = Einschaltzeit abends Lampe 1
a2           = Ausschaltzeit abends Lampe 1
a3           = Einschaltzeit abends Lampe 2
a4           = Ausschaltzeit abends Lampe 2
a5           = Einschaltzeit abends Lampe 3
a6           = Ausschaltzeit abends Lampe 3
a7           = Einschaltzeit abends CO2
a8           = Ausschaltzeit abends Co2


Duengen      = Zeitpunkt für Tagesduenger
Nachfuellen  = Zeitpunkt für Nachfuellen

s1           = Dauer Doesierung Tagesduenger in sec
s2           = Dauer Nachfuellen ins sec

temp         = Temperaur in °C

BHL          = Bodenheizer Low (ein)
BHH          = Bodenheizer High (aus)

SHL          = Stabheizer Low (ein)
SHH          = Stabheizer High (aus)

TWH          = Temperatur-Warnlevel High
TWL          = Temperatur-Warnlever Low

************************ Ende Variablen ******************************

"""

# ******************** Importierte Module *****************************


import  RPi.GPIO as GPIO
from time import *
# from time import localtime
import sys
import os

#import time

# ******************* Definieren der GPIOs ***************************


GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
GPIO.setup(13, GPIO.OUT) # Lampe1
GPIO.setup(16, GPIO.OUT) # Lampe2
GPIO.setup(19, GPIO.OUT) # Lampe3
GPIO.setup(20, GPIO.OUT) # CO2
GPIO.setup(21, GPIO.OUT) # Tagesduenger
GPIO.setup(26, GPIO.OUT) # Nachfuellen
GPIO.setup(12, GPIO.OUT) # Bodenheizer
GPIO.setup(6, GPIO.OUT)  # Stabheizer
GPIO.setup(5, GPIO.OUT)  # Alive
GPIO.setup(7, GPIO.OUT)  # Temperatur out of range


#  ****************** Beginn Einstellparameter **************************

# Ein- und Ausschaltzeiten der Lampen

#Lampe 1
m1 = "10:0"
m2 = "14:00"

#Lampe 2
m3 = "10:30"
m4 = "13:30"

#Lampe 3
m5 = "11:00"
m6 = "13:00"

#CO2
m7 = "08:00"
m8 = "21:00"

#Lampe 1
a1 = "18:00"
a2 = "22:00"

#Lampe 2
a3 = "18:30"
a4 = "21:30"

#Lampe 3
a5 = "19:00"
a6 = "21:00"

#CO2
a7 = "08:00"
a8 = "21:00"

# Tagesduenger
s1 = 10
Duengen = "08:00"

# Nachfuellen
s2 = 59
Nachfuellen = "09:00"

# Temperatur-Schaltpunkte

BHL = 24.0  # Bodenheizer Low (ein)
BHH = 24.3  # Bodenheizer High (aus)

SHL = 23.8  # Stabheizer Low (ein)
SHH = 24.1  # Stabheizer High (aus)

TWH = 24.4  # Warnlevel Temperatur High
TWL = 23.7  # Warnlevel Temperatur Low


# ************************ Ende Einstellparameter *******************************


# ************************ Beginn Programm **************************************

# Initialisieren aller Ausgaenge auf AUS

GPIO.output(12, True)
GPIO.output(13, True)
GPIO.output(16, True)
GPIO.output(19, True)
GPIO.output(20, True)
GPIO.output(21, True)
GPIO.output(26, True)
GPIO.output(6, True)
GPIO.output(5, True)

# Initialisieren der Variablen

Lampe1       = False
Lampe2       = False
Lampe3       = False
CO2          = False
Duengerpumpe = False
Fuellpumpe   = False
Bodenheizer  = False
Stabheizer   = False
temp         = 25
zeit         = strftime("%H:%M", localtime())
alive        = False

# Endlosschleife

while True:

# Auslesen des Tempratursensors
   
    # 1-Wire Slave-Liste lesen
    file = open('/sys/devices/w1_bus_master1/w1_master_slaves')
    w1_slaves = file.readlines()
    file.close()

  # Fuer jeden 1-Wire Slave aktuelle Temperatur ausgeben
    for line in w1_slaves:
  # 1-wire Slave extrahieren
     w1_slave = line.split("\n")[0]
  # 1-wire Slave Datei lesen
     file = open('/sys/bus/w1/devices/' + str(w1_slave) + '/w1_slave')
     filecontent = file.read()
     file.close()

  # Temperaturwerte auslesen und konvertieren
     stringvalue = filecontent.split("\n")[1].split(" ")[9]
     temp = float(stringvalue[2:]) / 1000


    
# Auswerten der Zeit und Schalten der Ausgaenge

# Lampen

    if (zeit >= m1 and zeit<= m2) or (zeit >= a1 and zeit<= a2) :
        GPIO.output(13, False)
        Lampe1= True
    
    else :
        GPIO.output(13, True)
        Lampe1 = False
      
    #sleep(2)
    
    if (zeit >= m3 and zeit<= m4) or (zeit >= a3 and zeit<= a4) :
        GPIO.output(16, False)
        Lampe2 = True
    
    else :
        GPIO.output(16, True)
        Lampe2 = False
      
    #sleep(2)

    if (zeit >= m5 and zeit<= m6) or (zeit >= a5 and zeit<= a6) :
        GPIO.output(19, False)
        Lampe3= True
    
    else :
        GPIO.output(19, True)
        Lampe3 = False


    if (zeit >= m7 and zeit<= m8) or (zeit >= a7 and zeit<= a8) :
        GPIO.output(20, False)
        CO2= True
    
    else :
        GPIO.output(20, True)
        CO2 = False

 # Tagesduenger                   

    if zeit == Duengen:
        GPIO.output(21, False)
        sleep(s1)
        GPIO.output(21, True)
        print ("Duengen an")
        sleep(60)
              
 # Nachfuellen                   


    if zeit == Nachfuellen:
        GPIO.output(26, False)
        print ("Nachfuellen an")
        sleep(s2)
        GPIO.output(26,True)

        sleep(60)

# Temperatur  

    if (temp < BHL) :
        GPIO.output(12, False)
        Bodenheizer = True

    if (temp > BHH) :
        GPIO.output(12, True)
        Bodenheizer = False

    if (temp < SHL) :
        GPIO.output(6, False)
        Stabheizer = True

    if (temp > SHH) :
        GPIO.output(6, True)
        Stabheizer = False

    if (temp >= TWL) and (temp <= TWH) :
        GPIO.output(7, True)
    else:
        GPIO.output(7, False)

        
# Output von x Zeilen zum Klaeren des Bildschirms


    zaehler= 10
    while zaehler>0:
        print("*")
        zaehler-=1

# Ausgabe der Zeit

    zeit =strftime("%H:%M", localtime())
    print (zeit)


# Ausgabe aller Schaltzustaende
      
    if Lampe1== True:
        print("Lampe 1 an")
    else:
        print("Lampe 1 aus")

    if Lampe2== True:
        print("Lampe 2 an")
    else:
        print("Lampe 2 aus")

    if Lampe3== True:
        print("Lampe 3 an")
    else:
        print("Lampe 3 aus")

    if CO2   == True:
        print("CO2 an")
    else:
        print("CO2 aus")


      # Temperatur ausgeben
    print(str("Temperatur =") + ' %6.2f °C' % temp)

    if Bodenheizer   == True:
        print("Bodenheizer an")
    else:
        print("Bodenheizer aus")

    if Stabheizer   == True:
        print("Stabheizer an")
    else:
        print("Stabheizer aus")


    if alive == True:
        GPIO.output (5, True)
        alive = False
        print ("x")
    else:
        GPIO.output (5, False)
        alive = True
        print ("+")

        
    sleep (0.1)        
        
s Lampe 3
m7           = Einschaltzeit morgens CO2
m8           = Ausschaltzeit morgens Co2

a1           = Einschaltzeit abends Lampe 1
a2           = Ausschaltzeit abends Lampe 1
a3           = Einschaltzeit abends Lampe 2
a4           = Ausschaltzeit abends Lampe 2
a5           = Einschaltzeit abends Lampe 3
a6           = Ausschaltzeit abends Lampe 3
a7           = Einschaltzeit abends CO2
a8           = Ausschaltzeit abends Co2


Duengen      = Zeitpunkt für Tagesduenger
Nachfuellen  = Zeitpunkt für Nachfuellen

s1           = Dauer Doesierung Tagesduenger in sec
s2           = Dauer Nachfuellen ins sec

temp         = Temperaur in °C

BHL          = Bodenheizer Low (ein)
BHH          = Bodenheizer High (aus)

SHL          = Stabheizer Low (ein)
SHH          = Stabheizer High (aus)

TWH          = Temperatur-Warnlevel High
TWL          = Temperatur-Warnlever Low

************************ Ende Variablen ******************************

"""

# ******************** Importierte Module *****************************


import  RPi.GPIO as GPIO
from time import *
# from time import localtime
import sys
import os

#import time

# ******************* Definieren der GPIOs ***************************


GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
GPIO.setup(13, GPIO.OUT) # Lampe1
GPIO.setup(16, GPIO.OUT) # Lampe2
GPIO.setup(19, GPIO.OUT) # Lampe3
GPIO.setup(20, GPIO.OUT) # CO2
GPIO.setup(21, GPIO.OUT) # Tagesduenger
GPIO.setup(26, GPIO.OUT) # Nachfuellen
GPIO.setup(12, GPIO.OUT) # Bodenheizer
GPIO.setup(6, GPIO.OUT)  # Stabheizer
GPIO.setup(5, GPIO.OUT)  # Alive
GPIO.setup(7, GPIO.OUT)  # Temperatur out of range


#  ****************** Beginn Einstellparameter **************************

# Ein- und Ausschaltzeiten der Lampen

#Lampe 1
m1 = "10:0"
m2 = "14:00"

#Lampe 2
m3 = "10:30"
m4 = "13:30"

#Lampe 3
m5 = "11:00"
m6 = "13:00"

#CO2
m7 = "08:00"
m8 = "21:00"

#Lampe 1
a1 = "18:00"
a2 = "22:00"

#Lampe 2
a3 = "18:30"
a4 = "21:30"

#Lampe 3
a5 = "19:00"
a6 = "21:00"

#CO2
a7 = "08:00"
a8 = "21:00"

# Tagesduenger
s1 = 10
Duengen = "08:00"

# Nachfuellen
s2 = 59
Nachfuellen = "09:00"

# Temperatur-Schaltpunkte

BHL = 24.0  # Bodenheizer Low (ein)
BHH = 24.3  # Bodenheizer High (aus)

SHL = 23.8  # Stabheizer Low (ein)
SHH = 24.1  # Stabheizer High (aus)

TWH = 24.4  # Warnlevel Temperatur High
TWL = 23.7  # Warnlevel Temperatur Low


# ************************ Ende Einstellparameter *******************************


# ************************ Beginn Programm **************************************

# Initialisieren aller Ausgaenge auf AUS

GPIO.output(12, True)
GPIO.output(13, True)
GPIO.output(16, True)
GPIO.output(19, True)
GPIO.output(20, True)
GPIO.output(21, True)
GPIO.output(26, True)
GPIO.output(6, True)
GPIO.output(5, True)

# Initialisieren der Variablen

Lampe1       = False
Lampe2       = False
Lampe3       = False
CO2          = False
Duengerpumpe = False
Fuellpumpe   = False
Bodenheizer  = False
Stabheizer   = False
temp         = 25
zeit         = strftime("%H:%M", localtime())
alive        = False

# Endlosschleife

while True:

# Auslesen des Tempratursensors
   
    # 1-Wire Slave-Liste lesen
    file = open('/sys/devices/w1_bus_master1/w1_master_slaves')
    w1_slaves = file.readlines()
    file.close()

  # Fuer jeden 1-Wire Slave aktuelle Temperatur ausgeben
    for line in w1_slaves:
  # 1-wire Slave extrahieren
     w1_slave = line.split("\n")[0]
  # 1-wire Slave Datei lesen
     file = open('/sys/bus/w1/devices/' + str(w1_slave) + '/w1_slave')
     filecontent = file.read()
     file.close()

  # Temperaturwerte auslesen und konvertieren
     stringvalue = filecontent.split("\n")[1].split(" ")[9]
     temp = float(stringvalue[2:]) / 1000


    
# Auswerten der Zeit und Schalten der Ausgaenge

# Lampen

    if (zeit >= m1 and zeit<= m2) or (zeit >= a1 and zeit<= a2) :
        GPIO.output(13, False)
        Lampe1= True
    
    else :
        GPIO.output(13, True)
        Lampe1 = False
      
    #sleep(2)
    
    if (zeit >= m3 and zeit<= m4) or (zeit >= a3 and zeit<= a4) :
        GPIO.output(16, False)
        Lampe2 = True
    
    else :
        GPIO.output(16, True)
        Lampe2 = False
      
    #sleep(2)

    if (zeit >= m5 and zeit<= m6) or (zeit >= a5 and zeit<= a6) :
        GPIO.output(19, False)
        Lampe3= True
    
    else :
        GPIO.output(19, True)
        Lampe3 = False


    if (zeit >= m7 and zeit<= m8) or (zeit >= a7 and zeit<= a8) :
        GPIO.output(20, False)
        CO2= True
    
    else :
        GPIO.output(20, True)
        CO2 = False

 # Tagesduenger                   

    if zeit == Duengen:
        GPIO.output(21, False)
        sleep(s1)
        GPIO.output(21, True)
        print ("Duengen an")
        sleep(60)
              
 # Nachfuellen                   


    if zeit == Nachfuellen:
        GPIO.output(26, False)
        print ("Nachfuellen an")
        sleep(s2)
        GPIO.output(26,True)

        sleep(60)

# Temperatur  

    if (temp < BHL) :
        GPIO.output(12, False)
        Bodenheizer = True

    if (temp > BHH) :
        GPIO.output(12, True)
        Bodenheizer = False

    if (temp < SHL) :
        GPIO.output(6, False)
        Stabheizer = True

    if (temp > SHH) :
        GPIO.output(6, True)
        Stabheizer = False

    if (temp >= TWL) and (temp <= TWH) :
        GPIO.output(7, True)
    else:
        GPIO.output(7, False)

        
# Output von x Zeilen zum Klaeren des Bildschirms


    zaehler= 10
    while zaehler>0:
        print("*")
        zaehler-=1

# Ausgabe der Zeit

    zeit =strftime("%H:%M", localtime())
    print (zeit)


# Ausgabe aller Schaltzustaende
      
    if Lampe1== True:
        print("Lampe 1 an")
    else:
        print("Lampe 1 aus")

    if Lampe2== True:
        print("Lampe 2 an")
    else:
        print("Lampe 2 aus")

    if Lampe3== True:
        print("Lampe 3 an")
    else:
        print("Lampe 3 aus")

    if CO2   == True:
        print("CO2 an")
    else:
        print("CO2 aus")


      # Temperatur ausgeben
    print(str("Temperatur =") + ' %6.2f °C' % temp)

    if Bodenheizer   == True:
        print("Bodenheizer an")
    else:
        print("Bodenheizer aus")

    if Stabheizer   == True:
        print("Stabheizer an")
    else:
        print("Stabheizer aus")


    if alive == True:
        GPIO.output (5, True)
        alive = False
        print ("x")
    else:
        GPIO.output (5, False)
        alive = True
        print ("+")

        
    sleep (0.1)        
        
