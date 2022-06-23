import time 
from meinToaster import toaster

class Supertoaster(toaster):

    def __init__(self, schaechte, farbe):
        super().__init__(schaechte ,farbe )
        self.temperatur = 0

    def toasten (self):
        if self.anzahl_toasts == 0:
            print("Es sind keine Toasts im Toaster")
        elif self._temperatur > 500:
            print ("der Toaster ist heissgleaufen")
        else :
            time.sleep(self.toast_zeit)
            self.zustand = 2 
            print("Die Toasts wurden getoastet")
