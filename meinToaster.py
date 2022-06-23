import time

class toaster:


    def __init__(self, schaechte, farbe): #Konstruktor
        self.farbe = farbe                 #Properties des Toasters
        self.schaechte = schaechte
        self.anzahl_toasts = 0
        self.zustand = 0
        self.toast_zeit= 0
        print("Der Toaster hat die Farbe" +" "+ farbe)
        print("Der Toaster hat"+ " " + str(schaechte) + " Schaechte für die Toasts")
        print ("--------------------------------------------------------------------")
    

#Methoden des Toasters

    def toast_reinlegen(self, anzahl):
        if anzahl <= self.schaechte:
            self.zustand = 0
            self.anzahl_toasts = anzahl
        else:
            print("Der Toaster hat zu wenig Platz!")
            print ("--------------------------------------------------------------------")

    def toast_toasten(self):
        if self.anzahl_toasts == 0:
            print("Es sind keine Toasts im Toaster" )
            print ("--------------------------------------------------------------------")
        else:
            time.sleep(self.toast_zeit)
            self.zustand = 2
            print("Die Toasts wurden fertig getoastet")
            print ("--------------------------------------------------------------------")


    def toast_fertig(self):
        time.sleep(1)
        print("Alle Toasts wurden ausgeworfen!")
        print ("--------------------------------------------------------------------")
        self.anzahl_toasts = 0
            
           

    def zeit_einstellen(self, zeit): #Die tost Zeit wird übergeben und gleichzeitig wird geguckt wie getostet das toast wird
        self.toast_zeit = zeit
        time.sleep(2)
        if self.toast_zeit > 30: 
            print("Die Toasts werden verbrannt!")
            print ("--------------------------------------------------------------------")
        elif self.toast_zeit > 15:
            print("Die Toasts werde stark getoastet")
            print ("--------------------------------------------------------------------")
        elif self.toast_zeit <=15:
            print("Die Toasts werden leicht getoastet")
            print ("--------------------------------------------------------------------")
        elif self.toast_zeit == 0:
            print("Die Toasts sind ungetoastet")
            print ("--------------------------------------------------------------------")
        

 