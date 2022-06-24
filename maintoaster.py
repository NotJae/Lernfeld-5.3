from meinToaster import toaster
from supertoaster import Supertoaster 

time = input("Geben Sie die Toastzeit ein! ") #Usereingabe der Toastzeit
toast = input("Geben sie an wie viele Toast Sie Einlegen wollen! ") #Usereingabe der Toasts

mein_toaster = toaster(2, "Blau") #Übergabe der Parameter (Anzahl der Schaechte und die Farbe des Toasters)
mein_toaster.zeit_einstellen(int(time)) #Übergabe der Toastzeit

mein_toaster.toast_reinlegen(int(toast)) #Übergabe der Toastscheiben 
mein_toaster.toast_toasten()
mein_toaster.toast_fertig()