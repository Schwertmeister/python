import time
from tkinter import *
import tkinter.simpledialog as inp
import tkinter.messagebox as out

root = Tk()
w = Label(root, text="Mein Programm")
w.pack()
out.showinfo("Willkommen","Danke, dass sich sich für unser Produkt entschieden haben! ^^")

class Mensch:
    def __init__(self, name, alter):
        self.name = name
        self.alter = alter

    def hallo(self):
        out.showinfo("Moin",("Hallo,",self.name))

    def Streicheln(self):
        inp.askstring("Frage", "Wen möchtest du streicheln?")
        Meerschweinchen.quiecken(self)
        
      
Benutzer = Mensch(inp.askstring("Name", "Wie heißt du?" ), inp.askinteger("Alter","Wie alt bist du?"))
Mensch.hallo(Benutzer)


class Meerschweinchen:
#Für  alle verfügbar machen!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!1
 def __init__(self, name, alter):
     self.name=name
     self.alter=alter
     

 def quiecken(self):
     
     out.showinfo("Begrüßung", self.name +" quieckt")
     time.sleep(0.25)
  
 
Ralf = Meerschweinchen("Ralf", 2)
Larry = Meerschweinchen("Larry", 3)
Mini = Meerschweinchen("Mini", 2)


Ralf.quiecken()
Larry.quiecken()
Mini.quiecken()

New = Meerschweinchen(inp.askstring("Name","Wie heißt denn das Meerschweinchen, dass du mitgebracht hast?"),inp.askinteger("Alter","Und wie alt ist es?"))
New.quiecken()
Mensch.Streicheln(Benutzer)







  

