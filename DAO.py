from Cliente import Cliente
from os import system
import pymysql

class DAO:

    def __init__(self):
        pass

#--------------------------------------------------------------------------------------------------------
    def conectar(self):
        self.con = pymysql.connect(
            host = "localhost",
            user = "root",
            password = "",
            db = "eva3"
        )

        self.cursor = self.con.cursor()

#--------------------------------------------------------------------------------------------------------
    def desconectar(self):
        self.con.close()

#--------------------------------------------------------------------------------------------------------

    def agregarCliente(self, c):
        try:
            self.conectar()
            sql = "insert into clientes (nom_cli, ape_cli, sex_cli, sal_cli, sit_cli) values ( %s, %s, %s, %s, %s)"
            val = (c.getNomCliente(), c.getApeCliente(), c.getNomSexCliente(), c.getSalCliente(),c.getSitCliente())
            self.cursor.execute(sql, val)
            self.con.commit()
            self.desconectar()
        except:
            print("\n--- Error Al Agregar Cliente!! (DAO)--- ")
            system("pause")

#---------------------------------------------------------------------------------------------------------

    def obtenerClientes(self):
        try:
            self.conectar()
            sql = "select id_cli, nom_cli, ape_cli, sex_cli, sal_cli from clientes where sit_cli=1"
            self.cursor.execute(sql)
            rs = self.cursor.fetchall()
            self.desconectar()
            return rs
        except:
            print("\n--- Error Al Obtener Clientes!! (DAO) ---")
            system("pause")

#---------------------------------------------------------------------------------------------------------

    def comprobarIdCliente(self, id):
        try:
            self.conectar()
            sql = "select * from clientes where id_cli=%s and sit_cli=1"
            self.cursor.execute(sql, id)
            rs = self.cursor.fetchone()
            self.desconectar()
            return rs
        except:
            print("\n--- Error Al Comprobar ID de Cliente!! (DAO)--- ")
            system("pause")

#-----------------------------------------------------------------------------------------------------------

    def eliminarCliente(self, idCli):
        try:
            self.conectar()
            sql = "update clientes set sit_cli=2 where id_cli=%s"
            self.cursor.execute(sql, idCli)
            self.con.commit()
            self.desconectar()
        except:
            print("\n--- Error Al Eliminar Cliente!! (DAO)--- ")
            system("pause")

#-----------------------------------------------------------------------------------------------------------

    def depositarDinero(self, mon, id):
        try:
            self.conectar()
            sql = "update clientes set sal_cli=sal_cli+%s where id_cli=%s"
            val = (mon, id)
            self.cursor.execute(sql,val)
            self.con.commit()
            self.desconectar()
        except:
            print("\n--- Error Al Depositar Dinero!! (DAO)--- ")
            system("pause")
