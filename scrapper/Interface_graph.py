'''
-------------------------------------
|           Scraper GUI             |
|   Authors : Romain Rittier,       |
|             Sofiane Aiche.        |
-------------------------------------
'''

#! /usr/bin/env python
#  -*- coding: utf-8 -*-
#
# GUI module generated by PAGE version 4.26
#  in conjunction with Tcl version 8.6
#    Jan 15, 2020 04:49:07 PM CET  platform: Windows NT

import sys
import mysql.connector

from PyQt5.QtWidgets import QTreeWidget, QTreeWidgetItem, QApplication, QWidget, QVBoxLayout
from database import DBPerson, DBCompany, DBEmployment
from pojo import Person, Organization

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  passwd="",
  database="projet_tutore_s3"
)

try:
    import Tkinter as tk
except ImportError:
    import tkinter as tk

try:
    import ttk

    py3 = False
except ImportError:
    import tkinter.ttk as ttk

    py3 = True

import Interface_graph_support


def vp_start_gui():
    '''Starting point when module is the main routine.'''
    global val, w, root
    root = tk.Tk()
    Interface_graph_support.set_Tk_var()
    top = Toplevel1(root)
    Interface_graph_support.init(root, top)
    root.mainloop()


w = None


def create_Toplevel1(root, *args, **kwargs):
    '''Starting point when module is imported by another program.'''
    global w, w_win, rt
    rt = root
    w = tk.Toplevel(root)
    Interface_graph_support.set_Tk_var()
    top = Toplevel1(w)
    Interface_graph_support.init(w, top, *args, **kwargs)
    return (w, top)


def destroy_Toplevel1():
    global w
    w.destroy()
    w = None


class Toplevel1:
    def __init__(self, top=None):
        '''This class configures and populates the toplevel window.
           top is the toplevel containing window.'''
        _bgcolor = '#d9d9d9'  # X11 color: 'gray85'
        _fgcolor = '#000000'  # X11 color: 'black'
        _compcolor = '#d9d9d9'  # X11 color: 'gray85'
        _ana1color = '#d9d9d9'  # X11 color: 'gray85'
        _ana2color = '#ececec'  # Closest X11 color: 'gray92'
        font17 = "-family Lato -size 36 -weight bold -slant roman " \
                 "-underline 0 -overstrike 0"

        top.geometry("500x400+672+223")
        top.minsize(148, 1)
        top.maxsize(1924, 1055)
        top.resizable(1, 1)
        top.title("New Toplevel")
        top.configure(background="#d7d8d9")
        top.configure(highlightbackground="#d9d9d9")
        top.configure(highlightcolor="black")

        self.Frame1 = tk.Frame(top)
        self.Frame1.place(relx=0.1, rely=0.188, relheight=0.625, relwidth=0.8)
        self.Frame1.configure(relief='groove')
        self.Frame1.configure(borderwidth="3")
        self.Frame1.configure(relief="groove")
        self.Frame1.configure(background="#d9d9d9")
        self.Frame1.configure(highlightbackground="#d9d9d9")
        self.Frame1.configure(highlightcolor="black")

        self.search_button = tk.Button(self.Frame1)
        self.search_button.place(relx=0.4, rely=0.52, height=33, width=66)
        self.search_button.configure(activebackground="#ffd9da")
        self.search_button.configure(activeforeground="#ff8000")
        self.search_button.configure(background="#ffffff")
        self.search_button.configure(command=Interface_graph_support.ent1)
        self.search_button.configure(disabledforeground="#a3a3a3")
        self.search_button.configure(foreground="#000000")
        self.search_button.configure(highlightbackground="#d9d9d9")
        self.search_button.configure(highlightcolor="black")
        self.search_button.configure(pady="0")
        self.search_button.configure(text='''Rechercher''')

        self.search_bar = tk.Entry(self.Frame1)
        self.search_bar.place(relx=0.275, rely=0.32, height=20, relwidth=0.41)
        self.search_bar.configure(background="white")
        self.search_bar.configure(cursor="fleur")
        self.search_bar.configure(disabledforeground="#a3a3a3")
        self.search_bar.configure(font="TkFixedFont")
        self.search_bar.configure(foreground="#000000")
        self.search_bar.configure(insertbackground="black")

        self.Label2 = tk.Label(self.Frame1)
        self.Label2.place(relx=0.325, rely=0.2, height=21, width=127)
        self.Label2.configure(background="#d9d9d9")
        self.Label2.configure(disabledforeground="#a3a3a3")
        self.Label2.configure(foreground="#000000")
        self.Label2.configure(text='''Nom d'une entreprise :''')

        self.Radiobutton1 = tk.Radiobutton(self.Frame1)
        self.Radiobutton1.place(relx=0.275, rely=0.4, relheight=0.1
                                , relwidth=0.175)
        self.Radiobutton1.configure(activebackground="#ececec")
        self.Radiobutton1.configure(activeforeground="#000000")
        self.Radiobutton1.configure(background="#d9d9d9")
        self.Radiobutton1.configure(cursor="fleur")
        self.Radiobutton1.configure(disabledforeground="#a3a3a3")
        self.Radiobutton1.configure(foreground="#000000")
        self.Radiobutton1.configure(highlightbackground="#d9d9d9")
        self.Radiobutton1.configure(highlightcolor="black")
        self.Radiobutton1.configure(justify='left')
        self.Radiobutton1.configure(text='''En ligne''')
        self.Radiobutton1.configure(variable=Interface_graph_support.selectedButton)

        self.Radiobutton2 = tk.Radiobutton(self.Frame1)
        self.Radiobutton2.place(relx=0.475, rely=0.4, relheight=0.1
                                , relwidth=0.205)
        self.Radiobutton2.configure(activebackground="#ececec")
        self.Radiobutton2.configure(activeforeground="#000000")
        self.Radiobutton2.configure(background="#d9d9d9")
        self.Radiobutton2.configure(disabledforeground="#a3a3a3")
        self.Radiobutton2.configure(foreground="#000000")
        self.Radiobutton2.configure(highlightbackground="#d9d9d9")
        self.Radiobutton2.configure(highlightcolor="black")
        self.Radiobutton2.configure(justify='left')
        self.Radiobutton2.configure(text='''Hors ligne''')
        self.Radiobutton2.configure(variable=Interface_graph_support.selectedButton)

        self.Label3 = tk.Label(top)
        self.Label3.place(relx=0.24, rely=0.025, height=50, width=250)
        self.Label3.configure(background="#d9d9d9")
        self.Label3.configure(disabledforeground="#7c4ef8")
        self.Label3.configure(font=font17)
        self.Label3.configure(foreground="#000000")
        self.Label3.configure(highlightcolor="#636363")
        self.Label3.configure(text='''Scrapper''')

        self.search_button.configure(command=self.test)

    def test(self):
        company = self.search_bar.get()

        # Noms d'entreprise déjà présente dans la Bdd Utile pour les Tests
        c0 = mydb.cursor()
        nom_ent = """Select nom_ent from entreprise"""
        c0.execute(nom_ent)
        d0 = c0.fetchall()
        for row in d0:
            print(row)

        # Récupération du numéro d'entreprise correspondant au nom
        entreprise = (self.search_bar.get(),)
        print("\n")
        c1 = mydb.cursor(prepared=True)
        no_ent = """Select no_ent from entreprise where nom_ent = %s"""
        c1.execute(no_ent, entreprise)
        d1 = c1.fetchone()

        # Récupération du numéro d'identification des employés de l'entreprise
        c2 = mydb.cursor(prepared=True)
        id_pers = """Select id_pers from emploi where no_ent = %s"""
        c2.execute(id_pers, d1)
        d2 = c2.fetchall()

        # Affichage des informations des employés
        for row in d2:
            cursor = mydb.cursor(prepared=True)
            requete = """SELECT * FROM personne where id_pers =%s"""
            parametres = (row[0],)
            cursor.execute(requete, parametres)
            data = cursor.fetchall()

            for row in data:
                # Récupération du nom de poste des employés
                c3 = mydb.cursor(prepared=True)
                nom_poste = """SELECT nom_poste FROM personne where id_pers =%s"""
                p2 = (row[0],)
                c3.execute(nom_poste, p2)
                d3 = c3.fetchone()
            # Récupération de l'odre hierarchique des employés
            c6 = mydb.cursor(prepared=True)
            ordre_hier = """SELECT ordre_hierarchique FROM type_poste where nom_type_poste =%s """
            p4 = (d3[0].decode("utf-8"),)
            c6.execute(ordre_hier, p4)
            d6 = c6.fetchone()

        app = QApplication(sys.argv)
        window = QWidget()
        layout = QVBoxLayout(window)

        window.setWindowTitle("Arbre hiérarchique")

        window.resize(1000, 1000)

        trWidget = QTreeWidget()
        trWidget.setHeaderLabels(['Numero', 'Id des employés', 'Informations personnelles', '', ])
        # breakpoint()
        nbpersonne = 0
        i = 1
        cg = QTreeWidgetItem(trWidget, [str(d1[0])])
        for id_pers in d2:
            cursor2 = mydb.cursor(prepared=True)
            requete2 = """SELECT * FROM personne where id_pers =%s"""
            parametres2 = (id_pers[0],)
            cursor2.execute(requete2, parametres2)
            data2 = cursor2.fetchone()


            c1 = QTreeWidgetItem(cg, [str(data2[0]), str(data2[1].decode("utf-8")), str(data2[2].decode("utf-8"))])
            c2 = QTreeWidgetItem(c1, [str(data2[3].decode("utf-8"))])
            c3 = QTreeWidgetItem(c2, ["", str(data2[4].decode("utf-8"))])
            c4 = QTreeWidgetItem(c3, ["", str(data2[5].decode("utf-8"))])
            c5 = QTreeWidgetItem(c4, ["", str(data2[6].decode("utf-8"))])
            layout.addWidget(trWidget)

        window.show()

        sys.exit(app.exec_())


if __name__ == '__main__':
    vp_start_gui()
