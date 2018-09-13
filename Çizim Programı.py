import tkinter as tk
from tkinter.colorchooser import askcolor

ekran = {}

class Çizim(tk.Tk):
    basx = None
    basy = None
    
    def __init__(self, uzunluk = 500, genislik= 350, tuvalrenk = ('#%02x%02x%02x' % (255, 255, 255)) ):
        super().__init__()
        self.resizable(False, False)
        self.title("Çizim Programı")
        ######Değişkenler
        self.nesneler = {}
        self.kalemKalınlığı = 2
        self.renk = None
        #################
        self.tuvalrenk = tuvalrenk
        self.uzunluk = uzunluk
        self.genislik = genislik
        self.bitx = None
        self.bity = None
        ##################
        self.Oluştur()
        ##################
        self.tuval.bind( "<B1-Motion>", self.Çiz )
        self.tuval.bind( "<Button-1>", self.baslangıcAl )
        self.tuval.bind( "<ButtonRelease-1>", self.bitAl )
        #################
        self.mainloop()
        
    
    def Oluştur(self):
        self.menu = tk.Menu(self)
        self.menu.add_command(label="Yeni Tuval Olustur.", command= self.yeniTuval)
        self.config(menu=self.menu)
        ################
        self.solframe = tk.Frame(self,height = 350,width= 150 , bg= "cyan")
        self.solframe.pack(anchor="w", fill="y", expand=True, side="left")
        self.sagframe = tk.Frame(self,height = 350,width= 500 )#, bg= "yellow"
        self.sagframe.pack(anchor="w", fill="y", expand=True, side="left")
        ################
        self.tuval = tk.Canvas(self.sagframe,width= self.uzunluk,height=self.genislik,bg= self.tuvalrenk,
                               relief="raised")
        self.tuval.grid(row= 0,column= 0)
        ################
        self.renkgir = tk.Button(self.solframe,text="Renk Ayarla",command=self.renkAyarla)
        self.renkgir.grid(row = 0, column = 0, sticky ="nw", pady = 2, padx = 3)
        ################
        self.sayac_metni = tk.Label(self.solframe,text= "Kalemin Kalınlığını Ayarlar")
        self.sayac_metni.grid(row = 1, column = 0, sticky ="nw", pady = 2, padx = 3)
        self.sayac = tk.Scale(
                            self.solframe, from_ = 1, to = 25,
                            orient = "horizontal",
                            command = self.kalemAyarla
                            )
        self.sayac.grid(row = 2, column = 0, sticky ="nw", pady = 2, padx = 3)     
        self.sayac.set(2)
        self.kalemKalınlığı = 2
        ################
        self.radiodegeri = tk.IntVar()
        self.radiodegeri.set(1)
        
        self.radio1 = tk.Radiobutton(self.solframe,
                                text="Fırça",
                                variable=self.radiodegeri,
                                value=1).grid(row = 3, column = 0, sticky ="nw", pady = 2, padx = 3)
        self.radio2 = tk.Radiobutton(self.solframe,
                                text="Çizgi",
                                variable=self.radiodegeri,
                                value=2).grid(row = 4, column = 0, sticky ="nw", pady = 2, padx = 3)
        self.radio3 = tk.Radiobutton(self.solframe,
                                text="Kare",
                                variable=self.radiodegeri,
                                value=3).grid(row = 5, column = 0, sticky ="nw", pady = 2, padx = 3)

        self.radio4 = tk.Radiobutton(self.solframe,
                                text="Çember",
                                variable=self.radiodegeri,
                                value=4).grid(row = 6, column = 0, sticky ="nw", pady = 2, padx = 3)
        ##############
        self.silb = tk.Button(self.solframe, text = "Hepsini Sil",command= self.sil)
        self.silb.grid(row = 7, column = 0, sticky ="nw", pady = 2, padx = 3)
        ##############
        self.ekraniOrtala()
        
    def ekraniOrtala(self):
        self.update_idletasks()
        self.d1 = self.winfo_width()
        self.d2 = self.winfo_height()
        self.d3 = (self.winfo_screenwidth() // 2) - (self.d1 // 2)
        self.d4 = (self.winfo_screenheight() // 2) - (self.d2 // 2)
        self.geometry('{}x{}+{}+{}'.format(self.d1, self.d2, self.d3, self.d4))
    
    def Çiz(self,event):
        self.event = event
        if (self.radiodegeri.get() == 1):
            self.nesneler[len(self.nesneler)+1] = Nokta(self.tuval,self.event,self.kalemKalınlığı,self.renk)
        elif (self.radiodegeri.get() == 2):
            self.nesneler[len(self.nesneler)+1] = Çizgi(self.tuval,self.event,self.basx,self.basy,self.kalemKalınlığı,self.renk)
        elif (self.radiodegeri.get() == 3):
            self.nesneler[len(self.nesneler)+1] = Kare(self.tuval,self.event,self.basx,self.basy,self.kalemKalınlığı,self.renk)
        elif (self.radiodegeri.get() == 4):
            self.nesneler[len(self.nesneler)+1] = Çember(self.tuval,self.event,self.basx,self.basy,self.kalemKalınlığı,self.renk)

    def baslangıcAl(self,event):
        self.basx = event.x
        self.basy = event.y

    def bitAl(self,event):
        self.bitx = event.x
        self.bity = event.y
        if (self.radiodegeri.get() == 1):
            Çizim.basx = None
            Çizim.basy = None
        elif (self.radiodegeri.get() == 2):
            Çizgi.çizgi = 0
            self.nesneler[len(self.nesneler)+1] = Çizgi(self.tuval,self.event,self.basx,self.basy,self.kalemKalınlığı,self.renk)
        elif (self.radiodegeri.get() == 3):
            Kare.kare = 0
            self.nesneler[len(self.nesneler)+1] = Kare(self.tuval,self.event,self.basx,self.basy,self.kalemKalınlığı,self.renk)
        elif (self.radiodegeri.get() == 4):
            Çember.çember = 0
            self.nesneler[len(self.nesneler)+1] = Çember(self.tuval,self.event,self.basx,self.basy,self.kalemKalınlığı,self.renk)

    def kalemAyarla(self, event):      
        self.kalemKalınlığı = self.sayac.get()

    def renkAyarla(self):
        self.renk= askcolor(parent=self)[1]

    def sil(self):
        self.tuval.delete("all")
        self.nesneler = {}

    def yeniTuval(self):
        ekran[len(ekran)+1] = YeniTuval()
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
        self.bilgi1 = tk.Label(self,text="Tuvalin Uzunlugu:").grid(row=0,column=0)
        self.bilgi2 = tk.Label(self,text="Tuvalin Genisligi:").grid(row=1,column=0)
        self.renkgir = tk.Button(self,text= "Tuvalin Rengi", command = self.renkBelirle).grid(row=2,column=0)
        self.giris1 = tk.Entry(self)
        self.giris1.grid(row=0,column=1)
        
        self.giris2 = tk.Entry(self)
        self.giris2.grid(row=1,column=1)
        self.tuvalolustur = tk.Button(self,text= "Yeni Tuval Olustur.",command = self.YeniTuval).grid(row=2,column=1)
        self.ekraniOrtala()

    def ekraniOrtala(self):
        self.update_idletasks()
        self.d1 = self.winfo_width()
        self.d2 = self.winfo_height()
        self.d3 = (self.winfo_screenwidth() // 2) - (self.d1 // 2)
        self.d4 = (self.winfo_screenheight() // 2) - (self.d2 // 2)
        self.geometry('{}x{}+{}+{}'.format(self.d1, self.d2, self.d3, self.d4))
    
    def renkBelirle(self):
        self.tuvalrenk = askcolor(parent=self)[1]
        


    def YeniTuval(self):
        self.uzunluk = self.giris1.get()
        self.genislik = self.giris2.get()
        if (self.uzunluk.isnumeric() and self.genislik.isnumeric() == True):
            self.destroy()
            ekran[len(ekran)+1] = Çizim(uzunluk=self.uzunluk,genislik=self.genislik, tuvalrenk= self.tuvalrenk)

            


class Nokta():
    def __init__(self,master,event,kalem,renk):
        self.master = master
        self.event = event
        self.kalem = kalem
        self.renk = renk
        ###############
        self.Koy()
        ###############

    def Koy(self):
        if Çizim.basx and Çizim.basy:
            self.master.create_line(Çizim.basx,
                            Çizim.basy,
                            self.event.x,
                            self.event.y,
                            fill = self.renk,
                            width=self.kalem,
                            smooth=1,
                            splinesteps=36,
                            capstyle="round")
        Çizim.basx = self.event.x
        Çizim.basy = self.event.y


class Çizgi(Nokta):
    çizgi = 0
    def __init__(self,master,event,basx,basy,kalem,renk):
        self.basx = basx
        self.basy = basy
        super().__init__(master,event,kalem,renk)


        

    def Koy(self):
        self.master.delete(Çizgi.çizgi)
        Çizgi.çizgi = self.master.create_line(self.basx,
                                self.basy,
                                self.event.x,
                                self.event.y,
                                fill=self.renk,
                                width=self.kalem)
        
        


class Kare(Çizgi):
    kare = 0
    def __init__(self,master,event,basx,basy,kalem,renk):
        super().__init__(master,event,basx,basy,kalem,renk)

    def Koy(self):
        self.master.delete(Kare.kare)
        Kare.kare = self.master.create_rectangle(self.basx,
                                     self.basy,
                                     self.event.x,
                                     self.event.y,
                                     width=self.kalem,
                                     outline=self.renk)

class Çember(Çizgi):
    çember = 0
    def __init__(self,master,event,basx,basy,kalem,renk):
        super().__init__(master,event,basx,basy,kalem,renk)

    def Koy(self):
        self.master.delete(Çember.çember)
        Çember.çember = self.master.create_oval(self.basx,
                                     self.basy,
                                     self.event.x,
                                     self.event.y,
                                     width=self.kalem,
                                     outline=self.renk)

ekran[len(ekran)+1] = Çizim(uzunluk=600,genislik=350,tuvalrenk="yellow")

