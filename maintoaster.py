from meinToaster import toaster
from supertoaster import Supertoaster 


mein_toaster = toaster(2, "Blau") #Übergabe der Parameter (Anzahl der Schaechte und die Farbe des Toasters)
mein_toaster.zeit_einstellen(10) #Übergabe der Toastzeit

mein_toaster.toast_reinlegen(2) #Übergabe der Toastscheiben 
mein_toaster.toast_toasten()
mein_toaster.toast_fertig()
