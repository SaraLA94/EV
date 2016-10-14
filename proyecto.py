# -*- coding: utf-8 -*-
from Tkinter import*
from PIL import ImageTk
from PIL import Image
from drawnow import *
import matplotlib.pyplot as plt
import gmplot
import serial
import numpy as np
import webbrowser

win=Tk()

# Permite crear la ventana principal con un fondo de color negro
win.title("Electric Vehicle Interface")
win.geometry('950x480')
win.configure(background='black')

labelfont = ('Helvetica',10,'bold')
labelfont1 = ('Helvetica',40,'bold')
labelfont2 = ('Helvetica',16,'bold')
labelfont3 = ('Helvetica',12,'bold')


# Crear mapa desplegable en Chromium

#gmap = gmplot.GoogleMapPlotter.from_geocode("Universidad Del Valle De Guatemala")
#gmap.draw("mapa.html")

#gmap1 = gmplot.GoogleMapPlotter(14.605841,-90.473829,16)
gmap1 = gmplot.GoogleMapPlotter(14.608023,-90.644652,16)
gmap1.draw("mapa1.html")
url = "mapa1.html"

webbrowser.get('chromium-browser').open_new_tab(url)



# BatteryLevel Section

BatteryLevel=50

# Modificar las dimensiones de la imagen para Low Battery Level
low = Image.open("low.png")
low = low.resize((200,100), Image.ANTIALIAS)
newLow ='newlow.png'
low.save(newLow)
# Modificar las dimensiones de la imagen para Battery Level above 50 percent
middle = Image.open("stable.png")
middle = middle.resize((200,100), Image.ANTIALIAS)
newMiddle ='newmiddle.png'
middle.save(newMiddle)
# Modificar las dimensiones de la imagen para Battery Level above 50 percent
full = Image.open("charged.png")
full = full.resize((200,100), Image.ANTIALIAS)
newFull ='newfull.png'
full.save(newFull)
# Importar las imagenes con sus nuevas dimensiones
lowLevel = PhotoImage(file="/home/pi/Desktop/Library/newlow.png")            
stable = PhotoImage(file="/home/pi/Desktop/Library/newmiddle.png")
charged = PhotoImage(file="/home/pi/Desktop/Library/newfull.png")

# Condiciones para mostrar las imagenes
if (BatteryLevel<= 50):
    labelBattery = Label(win,image=lowLevel)
    labelBattery.configure(background='black')
    labelBattery.place(x=10,y=30)
elif (BatteryLevel>50 and BatteryLevel<90):
    labelBattery = Label(win,image=stable)
    labelBattery.configure(background='black')
    labelBattery.place(x=10,y=30)
elif (BatteryLevel>=90 and BatteryLevel<=100):
    labelBattery = Label(win,image=charged)
    labelBattery.configure(background='black')
    labelBattery.place(x=10,y=30)
 
    labelPer=Label(win,text="100%")
    labelPer.config(bg='black', fg='white')
    labelPer.config(font=labelfont)
    labelPer.place(x=100,y=10)

# Environment Section

tempAmbiente=22
humedad=63


# Modificar las dimensiones de la imagen para humedad
hum = Image.open("humi.png")
hum = hum.resize((50,50))
newHum ='newhumi.png'
hum.save(newHum)

# Importar las imagenes con su nueva dimension
newh= PhotoImage(file="/home/pi/Desktop/Library/newhumi.png")
# Mostrar la imagen 
labelHumi = Label(win,image=newh)
labelHumi.configure(background='black')
labelHumi.place(x=25,y=210)

# Modificar las dimensiones de la imagen para la temperatura ambiente
tempi = Image.open("temp.png")
tempi = tempi.resize((40,40))
newTempi ='newtemp.png'
tempi.save(newTempi)

# Importar las imagenes con su nueva dimension
newt= PhotoImage(file="/home/pi/Desktop/Library/newtemp.png")
# Mostrar la imagen 
labelTempi = Label(win,image=newt)
labelTempi.configure(background='black')
labelTempi.place(x=30,y=150)



# Labels con texto para las variables del ambiente
labelAmbD=Label(win,text=tempAmbiente)
labelAmbD.config(bg='black', fg='white')
labelAmbD.config(font=labelfont2)
labelAmbD.place(x=110,y=160)


labelAmb=Label(win,text="°C")
labelAmb.config(bg='black', fg='white')
labelAmb.config(font=labelfont2)
labelAmb.place(x=135,y=160)


labelHumD=Label(win,text=humedad)
labelHumD.config(bg='black', fg='white')
labelHumD.config(font=labelfont2)
labelHumD.place(x=110,y=220)

labelHum=Label(win,text="%")
labelHum.config(bg='black', fg='white')
labelHum.config(font=labelfont2)
labelHum.place(x=135,y=220)



# Temperature Section
temperature=20


# Modificar las dimensiones de la imagen para Temperature
motor = Image.open("engine.png")
motor = motor.resize((80,80))
newTemperature ='newtemp.png'
motor.save(newTemperature)

# Importar las imagenes con su nueva dimension
motorTemp = PhotoImage(file="/home/pi/Desktop/Library/newtemp.png")
# Mostrar la imagen 
labelMotor = Label(win,image=motorTemp)
labelMotor.configure(background='black')
labelMotor.place(x=10,y=400)


labeldim=Label(win,text=temperature)
labeldim.config(bg='black', fg='white')
labeldim.config(font=labelfont2)
labeldim.place(x=100,y=425)

labeldim=Label(win,text="°C")
labeldim.config(bg='black', fg='white')
labeldim.config(font=labelfont2)
labeldim.place(x=130,y=425)

# Modificar las dimensiones de la imagen para Temperature
car = Image.open("carro.png")
car = car.resize((200,250))
newCar ='newcar.png'
car.save(newCar)

# Importar las imagenes con su nueva dimension
pCar= PhotoImage(file="/home/pi/Desktop/Library/newcar.png")
# Mostrar la imagen 
labelCar = Label(win,image=pCar)
labelCar.configure(background='black')
labelCar.place(x=400,y=135)

# Proximity Sensors Section
labelLF=Label(win,text="LEFT FRONT")
labelLF.config(bg='black', fg='red')
labelLF.config(font=labelfont)
labelLF.place(x=400,y=120)

labelL=Label(win,text="LEFT")
labelL.config(bg='black', fg='gray')
labelL.config(font=labelfont)
labelL.place(x=350,y=270)

labelLR=Label(win,text="REAR LEFT")
labelLR.config(bg='black', fg='gray')
labelLR.config(font=labelfont)
labelLR.place(x=400,y=385)

labelRF=Label(win,text="RIGHT FRONT")
labelRF.config(bg='black', fg='red')
labelRF.config(font=labelfont)
labelRF.place(x=530,y=120)

labelR=Label(win,text="RIGHT")
labelR.config(bg='black', fg='gray')
labelR.config(font=labelfont)
labelR.place(x=610,y=270)

labelRR=Label(win,text="REAR RIGHT")
labelRR.config(bg='black', fg='gray')
labelRR.config(font=labelfont)
labelRR.place(x=527,y=385)

# TPMS Sensors
tpms = Image.open("tpms.png")
tpms = tpms.resize((80,50))
newTPMS ='newtpms.png'
tpms.save(newTPMS)

# Left Front Tire 
f1=10
t1=25.0

if (f1>14 and f1<40):
    label1p=Label(win,text=f1)
    label1p.config(bg='black', fg='yellow')
    label1p.config(font=labelfont3)
    label1p.place(x=330,y=160)

    label1pp=Label(win,text="psi")
    label1pp.config(bg='black', fg='yellow')
    label1pp.config(font=labelfont3)
    label1pp.place(x=380,y=160)

    """label1t=Label(win,text=t1)
    label1t.config(bg='black', fg='yellow')
    label1t.config(font=labelfont3)
    label1t.place(x=340,y=190)

    label1tt=Label(win,text="°C")
    label1tt.config(bg='black', fg='yellow')
    label1tt.config(font=labelfont3)
    label1tt.place(x=375,y=190)"""

elif (f1<14 or f1>40):
    label1p=Label(win,text=f1)
    label1p.config(bg='black', fg='red')
    label1p.config(font=labelfont3)
    label1p.place(x=330,y=160)

    label1pp=Label(win,text="psi")
    label1pp.config(bg='black', fg='red')
    label1pp.config(font=labelfont3)
    label1pp.place(x=380,y=160)

        
    # Importar las imagenes con su nueva dimension
    tires= PhotoImage(file="/home/pi/Desktop/Library/newtpms.png")
    # Mostrar la imagen 
    labelTPMS = Label(win,image=tires)
    labelTPMS.configure(background='black')
    labelTPMS.place(x=10,y=300)


#Right Front Tire

f2=34.04
t2=26.0

if (f2>14 and f2<40):
    label2p=Label(win,text=f2)
    label2p.config(bg='black', fg='yellow')
    label2p.config(font=labelfont3)
    label2p.place(x=600,y=160)

    label2pp=Label(win,text="psi")
    label2pp.config(bg='black', fg='yellow')
    label2pp.config(font=labelfont3)
    label2pp.place(x=650,y=160)


    """label2t=Label(win,text=t2)
    label2t.config(bg='black', fg='yellow')
    label2t.config(font=labelfont3)
    label2t.place(x=600,y=190)

    label2tt=Label(win,text="°C")
    label2tt.config(bg='black', fg='yellow')
    label2tt.config(font=labelfont3)
    label2tt.place(x=635,y=190)"""
    
elif (f2<14 or f2>40):
    label2p=Label(win,text=f2)
    label2p.config(bg='black', fg='red')
    label2p.config(font=labelfont3)
    label2p.place(x=600,y=160)

    label2pp=Label(win,text="psi")
    label2pp.config(bg='black', fg='red')
    label2pp.config(font=labelfont3)
    label2pp.place(x=650,y=160)

    
    # Importar las imagenes con su nueva dimension
    tires= PhotoImage(file="/home/pi/Desktop/Library/newtpms.png")
    # Mostrar la imagen 
    labelTPMS = Label(win,image=tires)
    labelTPMS.configure(background='black')
    labelTPMS.place(x=10,y=300)

#Rear Left Tire

f3=34.04
t3=26.0

if (f3>14 and f3<40):
    label3p=Label(win,text=f3)
    label3p.config(bg='black', fg='yellow')
    label3p.config(font=labelfont3)
    label3p.place(x=330,y=310)

    label3pp=Label(win,text="psi")
    label3pp.config(bg='black', fg='yellow')
    label3pp.config(font=labelfont3)
    label3pp.place(x=380,y=310)

    """label3t=Label(win,text=t1)
    label3t.config(bg='black', fg='yellow')
    label3t.config(font=labelfont3)
    label3t.place(x=340,y=340)

    label3tt=Label(win,text="°C")
    label3tt.config(bg='black', fg='yellow')
    label3tt.config(font=labelfont3)
    label3tt.place(x=375,y=340)"""

elif (f3<14 or f3>40):
    label3p=Label(win,text=f3)
    label3p.config(bg='black', fg='red')
    label3p.config(font=labelfont3)
    label3p.place(x=330,y=310)

    label3pp=Label(win,text="psi")
    label3pp.config(bg='black', fg='red')
    label3pp.config(font=labelfont3)
    label3pp.place(x=380,y=310)

        
    # Importar las imagenes con su nueva dimension
    tires= PhotoImage(file="/home/pi/Desktop/Library/newtpms.png")
    # Mostrar la imagen 
    labelTPMS = Label(win,image=tires)
    labelTPMS.configure(background='black')
    labelTPMS.place(x=10,y=300)

#Rear Right Tire

f4=34.04
t4=25.0

if (f4>14 and f4<40):
    label4p=Label(win,text=f4)
    label4p.config(bg='black', fg='yellow')
    label4p.config(font=labelfont3)
    label4p.place(x=600,y=310)

    label4pp=Label(win,text="psi")
    label4pp.config(bg='black', fg='yellow')
    label4pp.config(font=labelfont3)
    label4pp.place(x=650,y=310)

    """label4t=Label(win,text=t1)
    label4t.config(bg='black', fg='yellow')
    label4t.config(font=labelfont3)
    label4t.place(x=600,y=340)

    label4tt=Label(win,text="°C")
    label4tt.config(bg='black', fg='yellow')
    label4tt.config(font=labelfont3)
    label4tt.place(x=635,y=340)"""

elif (f4<14 or f4>40):
    label4p=Label(win,text=f4)
    label4p.config(bg='black', fg='red')
    label4p.config(font=labelfont3)
    label4p.place(x=600,y=310)

    label4pp=Label(win,text="psi")
    label4pp.config(bg='black', fg='red')
    label4pp.config(font=labelfont3)
    label4pp.place(x=650,y=310)

    # Importar las imagenes con su nueva dimension
    tires= PhotoImage(file="/home/pi/Desktop/Library/newtpms.png")
    # Mostrar la imagen 
    labelTPMS = Label(win,image=tires)
    labelTPMS.configure(background='black')
    labelTPMS.place(x=10,y=300)









# Speed Sensors

velocidad=100
labelS=Label(win,text=velocidad)
labelS.config(bg='black', fg='white')
labelS.config(font=labelfont1)
labelS.place(x=455,y=10)

labeldim=Label(win,text="km/h")
labeldim.config(bg='black', fg='white')
labeldim.config(font=labelfont2)
labeldim.place(x=480,y=70)



speedy = Image.open("speed.png")
speedy = speedy.resize((50,50))
newSpeedy ='newSpeed.png'
speedy.save(newSpeedy)

# Aceleracion
labelAcc=Label(win,text="")
labelAcc.config(bg='black', fg='white')
labelAcc.config(font=labelfont2)
labelAcc.place(x=480,y=70)


# Importar las imagenes con su nueva dimension
newSpeed= PhotoImage(file="/home/pi/Desktop/Library/newSpeed.png")
# Mostrar la imagen 
labelSpeed = Label(win,image=newSpeed)
labelSpeed.configure(background='black')
labelSpeed.place(x=350,y=20)

# Decorativos
dec = Image.open("tesla.png")
dec = dec.resize((185,100))
newTesla ='newdec.png'
dec.save(newTesla)

# Importar las imagenes con su nueva dimension
newDec= PhotoImage(file="/home/pi/Desktop/Library/newdec.png")
# Mostrar la imagen 
labelTesla = Label(win,image=newDec)
labelTesla.configure(background='black')
labelTesla.place(x=760,y=20)

disp = Image.open("transmission.png")
disp = disp.resize((75,25))
newDisp='newdisp.png'
disp.save(newDisp)

# Importar las imagenes con su nueva dimension
display= PhotoImage(file="/home/pi/Desktop/Library/newdisp.png")
# Mostrar la imagen 
labelDisp = Label(win,image=display)
labelDisp.configure(background='black')
labelDisp.place(x=465,y=440)

icon = Image.open("icon.png")
icon = icon.resize((75,75))
newIcon='newicon.png'
icon.save(newIcon)

# Importar las imagenes con su nueva dimension
light= PhotoImage(file="/home/pi/Desktop/Library/newicon.png")
# Mostrar la imagen 
labelLight = Label(win,image=light)
labelLight.configure(background='black')
labelLight.place(x=600,y=10)




"""BatteryLevel=[]

Environment=[]
Pressure=[]
Altitude=[]
Humidity=[]

Temperature=[]

tireSpeed1=[]
tireSpeed2=[]
tireSpeed3=[]
tireSpeed4=[]

accelx=[]
accely=[]
accelz=[]

Pressure1=[]
Pressure2=[]
Pressure3=[]
Pressure4=[]

Front1=[]
Front2=[]
Right=[]
Left=[]
Back1=[]
Back2=[]

Latitude=[]
Longitude=[]


arduinoData=serial.Serial('/dev/ttyACM0',9600)
cont=0

while 1:
    
    arduinoString = arduinoData.readline()

    dataArray = arduinoString.split(',')
    
    nivel = float(dataArray[0])
    
    tempAmb = float(dataArray[1])
    presAmb = float(dataArray[2])
    altiAmb = float(dataArray[3])
    humiAmb = float(dataArray[4])

    tempMot = float(dataArray[5])

    tSpeed1 = float(dataArray[6])
    tSpeed2 = float(dataArray[7])
    tSpeed3 = float(dataArray[8])
    tSpeed4 = float(dataArray[9])

    acx = float(dataArray[10])
    acy = float(dataArray[11])
    acz = float(dataArray[12])

    p1 = float(dataArray[13])
    p2 = float(dataArray[14])
    p3 = float(dataArray[15])
    p4 = float(dataArray[16])

    proxF1 = float(dataArray[17])
    proxF2 = float(dataArray[18])
    proxL = float(dataArray[19])
    proxR = float(dataArray[20])
    proxB1 = float(dataArray[21])
    proxB2 =float(dataArray[22])

    lat = float(dataArray[23])
    lon = float(dataArray[24])
    
    cont=cont+1

    BatteryLevel.append(nivel)

    Environment.append(tempAmb)
    Pressure.append(presAmb)
    Altitude.append(altiAmb)
    Humidity.append(humiAmb)

    Temperature.append(tempMot)

    tireSpeed1.append(tSpeed1)
    tireSpeed2.append(tSpeed2)
    tireSpeed3.append(tSpeed3)
    tireSpeed4.append(tSpeed4)

    accelx.append(acx)
    accely.append(acy)
    accelz.append(acz)

    Pressure1.append(p1)
    Pressure2.append(p2)
    Pressure3.append(p3)
    Pressure4.append(p4)

    Front1.append(proxF1)
    Front2.append(proxF2)
    Right.append(proxL)
    Left.append(proxR)
    Back1.append(proxB1)
    Back2.append(proxB2)

    Latitude.append(lat)
    Longitude.append(lon)

    print BatteryLevel
    print Environment
    print Pressure
    print Altitude
    print Humidity
    print Temperature
    print tireSpeed1
    print tireSpeed2
    print tireSpeed3
    print tireSpeed4
    print accelx
    print accely
    print accelz
    print Pressure1
    print Pressure2
    print Pressure3
    print Pressure4
    print Front1
    print Front2
    print Right
    print Left
    print Back1
    print Back2
    print Latitude
    print Longitude
    
    
  
    cont=cont+2
    
    if(cont>1):
  
        BatteryLevel.pop(0)

        Environment.pop(0)
        Pressure.pop(0)
        Altitude.pop(0)
        Humidity.pop(0)

        Temperature.pop(0)

        tireSpeed1.pop(0)
        tireSpeed2.pop(0)
        tireSpeed3.pop(0)
        tireSpeed4.pop(0)

        accelx.pop(0)
        accely.pop(0)
        accelz.pop(0)

        Pressure1.pop(0)
        Pressure2.pop(0)
        Pressure3.pop(0)
        Pressure4.pop(0)

        Front1.pop(0)
        Front2.pop(0)
        Right.pop(0)
        Left.pop(0)
        Back1.pop(0)
        Back2.pop(0)

        Latitude.pop(0)
        Longitude.pop(0)"""


mainloop()



            
            

