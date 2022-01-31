#!/usr/bin/env python2
import os
import Tkinter
from time import sleep
import tkMessageBox
import keyboard


class Hendrix:
    def __init__(self):
        self.nombre = ' '
        self.passw = ' '

    def escribirDatos(self, copy_window, nip_input, passw_input):
        self.nombre = nip_input.get()
        self.passw = passw_input.get()       
        with open("/home/" + os.getlogin() + "/gestorHendrix/hendrix.conf", 'w') as f:
                   f.write(str(self.nombre))
                   f.write('\n')
                   f.write(str(self.passw))
                   f.close()        
        copy_window.destroy()
        tkMessageBox.showinfo(title="Informacion actualizada", message="La informacion se ha guardado correctamente. Puede continuar")

    def leerDatos(self):
        try:            
            if open('/home/' + os.getlogin() + '/gestorHendrix/hendrix.conf'):
                with open('/home/' + os.getlogin() + '/gestorHendrix/hendrix.conf') as f:
                    self.nombre = f.readline()
                    self.passw = f.readline()
        except:
           copy_window = Tkinter.Toplevel()
           copy_window.geometry("800x500")
           nip_input_label = Tkinter.Label(copy_window, text="Introduce tu NIP empezando por una 'a' al principio")
           nip_input_label.pack(pady=(20, 0))
           nip_input = Tkinter.Entry(copy_window, width=15)
           nip_input.pack(pady=(10, 0))
           passw_input_label = Tkinter.Label(copy_window, text="Introduce tu password de hendrix")
           passw_input_label.pack(pady=(20, 0))
           passw_input = Tkinter.Entry(copy_window, width=15)
           passw_input.pack(pady=(10, 0))
           os.system('mkdir /home/' + os.getlogin() + '/gestorHendrix')
           os.system('touch /home/' + os.getlogin() + '/gestorHendrix/hendrix.conf')         
           continue_bttn = Tkinter.Button(copy_window,  text="Continuar", fg="green",bg="white", command=lambda: self.escribirDatos(copy_window, nip_input, passw_input))
           continue_bttn.pack(pady=(10, 0))                  


           #VERSION TERMINAL SIN INTERFAZ (GUI)
           #print("Es la primera vez que usas el gestor por lo que necesitamos los siguientes datos: ")
           #self.nombre = raw_input("Introduce tu NIP empezando con una a: ")
           #self.passw = raw_input("Introduce tu password de hendrix: ")
           #os.system('touch hendrix.conf')
           #with open('hendrix.conf', 'w') as f:
               #f.write(str(self.nombre))
               #f.write('\n')
               #f.write(str(self.passw))
           #print("Sus datos se han guardado correctamente a partir de ahora ya no necesitara volver a introducirlos mas")
           #print("Si por error ha introducido alguno de los datos incorrectamente modifique el archivo \'hendrix.conf\' que contiene sus datos")

    def enterHendrix(self):
        self.leerDatos()
        self.nombre = self.nombre.replace("\n", '')        
        os.system('ssh -X {nip}@hendrix.cps.unizar.es'.format(nip = self.nombre))
        #sleep(1)
        #keyboard.write(self.passw) #para los usuarios que necesitan meter la password para loguearse (no hayan hecho ssh-keygen y ssh-copy-id)
        #pyautogui.press('enter')

    def copyHendrix(self,copy, txt_input):
        #archivo = raw_input('Introduce el nombre de un archivo a copiar: ')
        archivo = txt_input.get()
        self.leerDatos()
        self.nombre = self.nombre.replace("\n", '')
        print("Archivo: ", archivo)
        os.system('scp {filename} {nip}@hendrix.cps.unizar.es:'.format(filename=archivo, nip = self.nombre))        
        #keyboard.write(self.passw) #para los usuarios que necesitan meter la password para loguearse (no hayan hecho ssh-keygen y ssh-copy-id)
        #pyautogui.press('enter')
        copy.destroy()
        tkMessageBox.showinfo(title="Archivo copiado", message="El archivo se ha copiado en hendrix correctamente. Puede continuar")

    def ventanaCopy(self):
        copy = Tkinter.Toplevel()
        copy.geometry("800x500")
        copy.title("COPIAR ARCHIVO A HENDRIX")
        input_label = Tkinter.Label(copy, text="Introduce el nombre del archivo a copiar")
        input_label.pack(pady=(20, 0))
        txt_input = Tkinter.Entry(copy, width=15) #caja de texto para introducir datos
        txt_input.pack(pady=(10, 0))       
        copy_bttn = Tkinter.Button(copy,  text="Copiar archivo a Hendrix", fg="green",bg="white", command= lambda: self.copyHendrix(copy, txt_input)) 
        copy_bttn.pack(pady=(10, 0))


    def uninstall(self, ventana):
        os.system('rm -r /home/' + os.getlogin() + '/hendrix')
        os.system('rm /home/' + os.getlogin() + '/gestorHendrix/hendrix.conf')
        tkMessageBox.showinfo(title="Programa desinstalado", message="El programa se ha desinstalado correctamente. Puede continuar")
        ventana.destroy()

    def exit(self, ventana):
        ventana.destroy()
  

    def inicio(self):

        ventana = Tkinter.Tk()
        ventana.geometry("800x500")
        ventana.title("GESTOR DE HENDRIX")
        label = Tkinter.Label(ventana, text="GESTOR DE HENDRIX")
        label.config(font=("Helvetica", 18))
        label.pack(pady=(90,0)) #colocamos la etiqueta sin necesidad de indicar una posicion concreta        
        txt_input = Tkinter.Entry(ventana, width=15) #caja de texto para introducir datos
        connect_bttn = Tkinter.Button(ventana,  text="Conectarse Hendrix", font=("Helvetica", 12), fg="green",bg="white", pady=10, command=self.enterHendrix)
        connect_bttn.pack(pady=(20, 0))


        #INPUT PARA INTRODUCIR NOMBRE DE ARCHIVO A COPIAR
        copy_bttn = Tkinter.Button(ventana,  text="Copiar archivo a Hendrix",font=("Helvetica", 12), fg="green",bg="white",pady=10, command=self.ventanaCopy)
        copy_bttn.pack(pady=(30,0))
        exit_bttn = Tkinter.Button(ventana,  text="Salir del programa",font=("Helvetica", 12), fg="green",bg="white", pady=10, command=lambda: self.exit(ventana))
        exit_bttn.pack(pady=(30, 0))
        uninstall_bttn = Tkinter.Button(ventana,  text="Desinstalar programa",font=("Helvetica", 12), fg="white",bg="red", pady=10, command= lambda: self.uninstall(ventana))
        uninstall_bttn.pack(pady=(50, 0))
        ventana.mainloop()


        #VERSION SIN INTERFAZ (GUI) DIRECTAMENTE DESDE TERMINAL
        #while True:
           # print("------------------------------------------------")
           # print("\tBienvenido a tu gestor de Hendrix".upper())
           # print("------------------------------	------------------")
           # print("\t1. Conectarse a hendrix")
           # print("\t2. Copiar un archivo a hendrix")	
           # print("\t3. Salir del programa")
           # opcion = int(input("Introduce una opcion: "))
           # if opcion == 1:
           #     self.enterHendrix()
           # elif opcion == 2:
           #     self.copyHendrix()
           # else:
           #     return
           


if __name__ == '__main__':
    hendrix = Hendrix()
    hendrix.inicio()

