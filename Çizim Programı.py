import tkinter as tk
from tkinter.colorchooser import askcolor
from tkinter import messagebox

ekran = {}


class Cizim(tk.Tk):
    basx = None
    basy = None

    def __init__(self, uzunluk=600, genislik=350, tuvalrenk=('#%02x%02x%02x' % (255, 255, 255))):
        super().__init__()
        self.resizable(False, False)
        self.title("Cizim Programi")
        ######Degiskenler
        self.nesneler = {}
        self.kalem_kalinligi = 2
        self.renk = None
        #################
        self.tuvalrenk = tuvalrenk
        self.uzunluk = uzunluk
        self.genislik = genislik
        self.bitx = None
        self.bity = None
        ##################
        self.olustur()
        ##################
        self.tuval.bind("<B1-Motion>", self.ciz)
        self.tuval.bind("<Button-1>", self.baslangic_al)
        self.tuval.bind("<ButtonRelease-1>", self.bit_al)
        #################
        self.mainloop()

    def olustur(self):
        self.menu = tk.Menu(self)
        self.menu.add_command(label="Yeni Tuval Olustur.", command=self.yeni_tuval)
        self.config(menu=self.menu)
        ################
        self.solframe = tk.Frame(self, height=350, width=150, bg="cyan")
        self.solframe.pack(anchor="w", fill="y", expand=True, side="left")
        self.sagframe = tk.Frame(self, height=350, width=500)  # , bg= "yellow"
        self.sagframe.pack(anchor="w", fill="y", expand=True, side="left")
        ################
        self.tuval = tk.Canvas(self.sagframe, width=self.uzunluk, height=self.genislik, bg=self.tuvalrenk,
                               relief="raised")
        self.tuval.grid(row=0, column=0)
        ################
        self.renkgir = tk.Button(self.solframe, text="Renk Ayarla", command=self.renk_ayarla)
        self.renkgir.grid(row=0, column=0, sticky="nw", pady=2, padx=3)
        ################
        self.sayacmetni = tk.Label(self.solframe, text="Kalemin Kalinligini Ayarlar")
        self.sayacmetni.grid(row=1, column=0, sticky="nw", pady=2, padx=3)
        self.sayac = tk.Scale(
            self.solframe, from_=1, to=25,
            orient="horizontal",
            command=self.kalem_ayarla
        )
        self.sayac.grid(row=2, column=0, sticky="nw", pady=2, padx=3)
        self.sayac.set(2)
        self.kalem_kalinligi = 2
        ################
        self.radiodegeri = tk.IntVar()
        self.radiodegeri.set(1)

        self.radio1 = tk.Radiobutton(self.solframe,
                                     text="Firca",
                                     variable=self.radiodegeri,
                                     value=1)
        self.radio1.grid(row=3, column=0, sticky="nw", pady=2, padx=3)

        self.radio2 = tk.Radiobutton(self.solframe,
                                     text="Cizgi",
                                     variable=self.radiodegeri,
                                     value=2)
        self.radio2.grid(row=4, column=0, sticky="nw", pady=2, padx=3)

        self.radio3 = tk.Radiobutton(self.solframe,
                                     text="Dortgen",
                                     variable=self.radiodegeri,
                                     value=3)
        self.radio3.grid(row=5, column=0, sticky="nw", pady=2, padx=3)

        self.radio4 = tk.Radiobutton(self.solframe,
                                     text="Cember",
                                     variable=self.radiodegeri,
                                     value=4)
        self.radio4.grid(row=6, column=0, sticky="nw", pady=2, padx=3)

        ##############
        self.silb = tk.Button(self.solframe, text="Hepsini Sil", command=self.sil)
        self.silb.grid(row=7, column=0, sticky="nw", pady=2, padx=3)
        ##############
        self.ekrani_ortala()

    def ekrani_ortala(self):
        self.update_idletasks()
        self.d1 = self.winfo_width()
        self.d2 = self.winfo_height()
        self.d3 = (self.winfo_screenwidth() // 2) - (self.d1 // 2)
        self.d4 = (self.winfo_screenheight() // 2) - (self.d2 // 2)
        self.geometry('{}x{}+{}+{}'.format(self.d1, self.d2, self.d3, self.d4))

    def ciz(self, event):
        self.event = event
        if (self.radiodegeri.get() == 1):
            self.nesneler[len(self.nesneler) + 1] = Nokta(self.tuval, self.event, self.kalem_kalinligi, self.renk)
        elif (self.radiodegeri.get() == 2):
            self.nesneler[len(self.nesneler) + 1] = Cizgi(self.tuval, self.event, self.basx, self.basy,
                                                          self.kalem_kalinligi, self.renk)
        elif (self.radiodegeri.get() == 3):
            self.nesneler[len(self.nesneler) + 1] = Dortgen(self.tuval, self.event, self.basx, self.basy,
                                                            self.kalem_kalinligi, self.renk)
        elif (self.radiodegeri.get() == 4):
            self.nesneler[len(self.nesneler) + 1] = Cember(self.tuval, self.event, self.basx, self.basy,
                                                           self.kalem_kalinligi, self.renk)

    def baslangic_al(self, event):
        self.basx = event.x
        self.basy = event.y

    def bit_al(self, event):
        self.bitx = event.x
        self.bity = event.y
        if (self.radiodegeri.get() == 1):
            Cizim.basx = None
            Cizim.basy = None
        elif (self.radiodegeri.get() == 2):
            Cizgi.cizgi = 0
            self.nesneler[len(self.nesneler) + 1] = Cizgi(self.tuval, self.event, self.basx, self.basy,
                                                          self.kalem_kalinligi, self.renk)
        elif (self.radiodegeri.get() == 3):
            Dortgen.dortgen = 0
            self.nesneler[len(self.nesneler) + 1] = Dortgen(self.tuval, self.event, self.basx, self.basy,
                                                            self.kalem_kalinligi, self.renk)
        elif (self.radiodegeri.get() == 4):
            Cember.cember = 0
            self.nesneler[len(self.nesneler) + 1] = Cember(self.tuval, self.event, self.basx, self.basy,
                                                           self.kalem_kalinligi, self.renk)

    def kalem_ayarla(self, event):
        self.kalem_kalinligi = self.sayac.get()

    def renk_ayarla(self):
        self.renk = askcolor(parent=self)[1]

    def sil(self):
        self.tuval.delete("all")
        self.nesneler = {}

    def yeni_tuval(self):
        ekran[len(ekran) + 1] = YeniTuval()
        self.destroy()


class YeniTuval(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Ayarlar")
        self.resizable(False, False)
        ###############
        self.tuvalrenk = '#%02x%02x%02x' % (255, 255, 255)
        self.uzunluk = 500
        self.genislik = 350
        self.metin = tk.StringVar()
        ###############
        self.olustur()

    def olustur(self):
        self.bilgi1 = tk.Label(self, text="Tuvalin Uzunlugu:")
        self.bilgi1.grid(row=0, column=0)
        self.bilgi2 = tk.Label(self, text="Tuvalin Genisligi:")
        self.bilgi2.grid(row=1, column=0)
        self.renkgir = tk.Button(self, text="Tuvalin Rengi", command=self.renk_belirle)
        self.renkgir.grid(row=2, column=0)
        self.giris1 = tk.Entry(self)
        self.giris1.grid(row=0, column=1)
        self.giris1.insert("end", '600')
        self.giris2 = tk.Entry(self)
        self.giris2.grid(row=1, column=1)
        self.giris2.insert("end", '350')
        self.tuvalolustur = tk.Button(self, text="Yeni Tuval Olustur.", command=self.yeni_tuval)
        self.tuvalolustur.grid(row=2, column=1)
        self.ekrani_ortala()

    def ekrani_ortala(self):
        self.update_idletasks()
        self.d1 = self.winfo_width()
        self.d2 = self.winfo_height()
        self.d3 = (self.winfo_screenwidth() // 2) - (self.d1 // 2)
        self.d4 = (self.winfo_screenheight() // 2) - (self.d2 // 2)
        self.geometry('{}x{}+{}+{}'.format(self.d1, self.d2, self.d3, self.d4))

    def renk_belirle(self):
        self.tuvalrenk = askcolor(parent=self)[1]

    def yeni_tuval(self):
        self.uzunluk = self.giris1.get()
        self.genislik = self.giris2.get()
        if (self.uzunluk.isnumeric() and self.genislik.isnumeric() == True):
            self.destroy()
            ekran[len(ekran) + 1] = Cizim(uzunluk=self.uzunluk, genislik=self.genislik, tuvalrenk=self.tuvalrenk)
        else:
            messagebox.showinfo("Bilgi", "Sadece rakamlardan olusan uzunluklar belirleyebilirsiniz.", parent=self)

class Nokta():
    def __init__(self, master, event, kalem, renk):
        self.master = master
        self.event = event
        self.kalem = kalem
        self.renk = renk
        ###############
        self.Koy()
        ###############

    def Koy(self):
        if Cizim.basx and Cizim.basy:
            self.master.create_line(Cizim.basx,
                                    Cizim.basy,
                                    self.event.x,
                                    self.event.y,
                                    fill=self.renk,
                                    width=self.kalem,
                                    smooth=1,
                                    splinesteps=36,
                                    capstyle="round")
        Cizim.basx = self.event.x
        Cizim.basy = self.event.y


class Cizgi(Nokta):
    cizgi = 0

    def __init__(self, master, event, basx, basy, kalem, renk):
        self.basx = basx
        self.basy = basy
        super().__init__(master, event, kalem, renk)

    def Koy(self):
        self.master.delete(Cizgi.cizgi)
        Cizgi.cizgi = self.master.create_line(self.basx,
                                              self.basy,
                                              self.event.x,
                                              self.event.y,
                                              fill=self.renk,
                                              width=self.kalem)


class Dortgen(Cizgi):
    dortgen = 0

    def __init__(self, master, event, basx, basy, kalem, renk):
        super().__init__(master, event, basx, basy, kalem, renk)

    def Koy(self):
        self.master.delete(Dortgen.dortgen)
        Dortgen.dortgen = self.master.create_rectangle(self.basx,
                                                       self.basy,
                                                       self.event.x,
                                                       self.event.y,
                                                       width=self.kalem,
                                                       outline=self.renk)


class Cember(Cizgi):
    cember = 0

    def __init__(self, master, event, basx, basy, kalem, renk):
        super().__init__(master, event, basx, basy, kalem, renk)

    def Koy(self):
        self.master.delete(Cember.cember)
        Cember.cember = self.master.create_oval(self.basx,
                                                self.basy,
                                                self.event.x,
                                                self.event.y,
                                                width=self.kalem,
                                                outline=self.renk)


ekran[len(ekran) + 1] = Cizim(uzunluk=600, genislik=350, tuvalrenk="yellow")

