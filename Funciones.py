from Cliente import Cliente
from DAO import DAO
from beautifultable import BeautifulTable
from os import system
import os

class Funciones:

    d = DAO()

    def __init__(self):
        pass

#--------------------------------------------------------------------------------------------------------

    def menu(self):
        while True:
            try:
                system("cls")
                print("--------------")
                print("---  MENU  ---")
                print("--------------")
                print("1.Registrar Clientes")
                print("2.Listar Clientes")
                print("3.Eliminar Clientes")
                print("4.Depositar Dinero")
                print("5.Salir")
                op = int(input("Digite Una Opcion : "))
                if op==1:
                    self.registrarClientes()
                elif op==2:
                    self.listarClientes()
                elif op==3:
                    self.eliminarClientes()
                elif op==4:
                    self.depositarDinero()
                elif op==5:
                    print("\n--- OK, ADIOS!! ---")
                    system("pause")
                    os._exit(1)
                else:
                    print("\n--- Error De Opcion De Menu!! ---")
                    system("pause")
            except:
                print("\n--- Error De Opcion Try!!(MENÚ) ---")
                system("pause")

#--------------------------------------------------------------------------------------------------------

    def registrarClientes(self):
        while True:
            try:
                system("cls")
                nom = input("\n--- Digite el nombre del cliente a registrar : ")
                if len(nom.strip())<1 or len(nom.strip())>20:
                    print("\n--- DEBE TENER ENTRE 1 Y 20 CARACTERES!! ---")
                    system("pause")
                else:
                    break
            except:
                print("--- ERROR AL INTENTAR REGISTRAR EL NOMBRE ---")
                system("pause")

        while True:
            try:
                system("cls")
                ape = input("\n--- Digite el apellido del cliente a registrar : ")
                if len(ape.strip())<1 or len(ape.strip())>20:
                    print("\n--- DEBE TENER ENTRE 1 Y 20 CARACTERES!! ---")
                    system("pause")
                else:
                    break
            except:
                print("--- ERROR AL INTENTAR REGISTRAR EL APELLIDO ---")
                system("pause")

        while True:
            try:
                tabla = BeautifulTable()
                tabla.rows.append(["MASCULINO"])
                tabla.rows.append(["FEMENINO"])
                tabla.rows.append(["NO ESPECIFICA"])
                tabla.column_headers = ["SEXO"]
                tabla.rows.header = ["1","2","3"]
                system("cls")
                print(tabla)
                sex = int(input("\n--- Digite el sexo del cliente a registrar : "))
                if sex<1 or sex>3:
                    print("\n--- EL SEXO DEBE ESTAR ENTRE LA OPCIÓN 1, 2 ó 3 ---")
                    system("pause")
                else:
                    break
            except:
                print("--- ERROR AL INTENTAR REGISTRAR OPCIÓN DE SEXO ---")
                system("pause")

        while True:
            try:
                system("cls")
                sal = int(input("\n--- Digite el saldo del cliente a registrar : "))
                if sal<1 or sal>1000000:
                    print("\n--- DEBE INGRESAR UN SUELDO ENTRE $1 Y $1.000.000!! ---")
                    system("pause")
                else:
                    break
            except:
                print("--- ERROR AL INTENTAR REGISTRAR EL SUELDO ---")
                system("pause")
        if sex==1:
            noms = "MASCULINO"
        elif sex==2:
            noms = "FEMENINO"
        else:
            noms = "NO ESPECIFICA"
        c = Cliente()
        c.setNomCliente(nom.upper())
        c.setApeCliente(ape.upper())
        c.setNomSexCliente(noms.upper())
        c.setSalCliente(sal)
        c.setSitCliente(1)

        self.d.agregarCliente(c)

        system("cls")
        print("--------------------------------------------")
        print("---- CLIENTE REGISTRADO CORRECTAMENTE!! ----")
        print("--------------------------------------------")
        system("pause")
        self.menu()


#--------------------------------------------------------------------------------------------------------

    def listarClientes(self):
        respuesta = self.d.obtenerClientes()
        tabla = BeautifulTable()
        for x in respuesta:
            tabla.rows.append([x[0],x[1],x[2],x[3],x[4]])
        tabla.columns.header = ["ID","NOMBRE","APELLIDO","SEXO","SALDO"]
        system("cls")
        print(tabla)
        system("pause")

#--------------------------------------------------------------------------------------------------------

    def eliminarClientes(self):
        while True:
            try:
                system("cls")
                r = self.d.obtenerClientes()
                tabla = BeautifulTable()
                for x in r:
                    tabla.rows.append([x[0],x[1],x[2],x[3],x[4]])
                tabla.columns.header = ["ID","NOMBRE","APELLIDO","SEXO","SALDO"]
                system("cls")
                print(tabla)

                idCli = int(input("Digite El ID Del Cliente a Eliminar : "))
                r = self.d.comprobarIdCliente(idCli)
                if r is None:
                    print("\n--- NO SE ENCONTRÓ AL CLIENTE CON ESA ID ---")
                    system("pause")
                else:
                    self.d.eliminarCliente(idCli)
                    system("cls")
                    print("---------------------------------------")
                    print("--- CLIENTE ELIMINADO CORRECTAMENTE ---")
                    print("---------------------------------------")
                    system("pause")
                    self.menu()
            except:
                print("\n--- ERROR AL INTENTAR ELIMINAR CLIENTE!! ---")
                system("pause")
                self.menu()

#--------------------------------------------------------------------------------------------------------

    def depositarDinero(self):
        while True:
            try:
                system("cls")
                r = self.d.obtenerClientes()
                tabla = BeautifulTable()
                for x in r:
                    tabla.rows.append([x[0],x[1],x[2],x[3],x[4]])
                tabla.columns.header = ["ID","NOMBRE","APELLIDO","SEXO","SALDO"]
                system("cls")
                print(tabla)

                idCli = int(input("Digite El ID Del Cliente a Depositar : "))
                r = self.d.comprobarIdCliente(idCli)
                if r is None:
                    print("\n--- NO SE ENCONTRÓ AL CLIENTE CON ESA ID ---")
                    system("pause")
                else:
                    break
            except:
                print("\n--- NO SE ENCONTRO AL CLIENTE CON ESA ID!! ---")
                system("pause")

        while True:
            try:
                mon = int(input("\n--- Digite el monto del deposito a realizar : "))
                if mon<1 or mon>1000000:
                    print("\n--- DEBE INGRESAR UN MONTO ENTRE $1 Y $1.000.000!! ---")
                    system("pause")
                else:
                    break
            except:
                print("\n--- ERROR AL DEPOSITAR DINERO ---")
                system("pause")
                self.menu()

        self.d.depositarDinero(mon, idCli)

        system("cls")
        print("--------------------------------------------")
        print("---- DEPOSITO REALIZADO CORRECTAMENTE!! ----")
        print("--------------------------------------------")
        system("pause")
        self.menu()
#--------------------------------------------------------------------------------------------------------

    