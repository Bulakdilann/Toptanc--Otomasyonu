from tkinter import *
from PIL import Image, ImageTk
from tkinter.ttk import Combobox
from tkinter import ttk
import tkinter as tk
from tkinter import messagebox
import time
import mysql.connector
import mysql.connector as sql

veritab = mysql.connector.connect(
  host="localhost",
  user="root",
  passwd="",
  database="toptanci"
)


mycursor = veritab.cursor()

ekran=Tk()
q=StringVar()
ekran.state("zoomed")
ekran.title("TOPTANCILIK")
ekran.configure(bg="#47ade3")

#admin içerik kısmı    
def adminkayıtbutton():
   
          ekran4 = Toplevel(ekran)
          ekran4.title("admin içerik bilgileri")
          ekran4.state("zoomed")
          ekran4.configure(bg="#47ade3")
          resim = Image.open("toptancı.png")
          yukle = ImageTk.PhotoImage(resim)
          goruntu = Label(ekran4,text="toptancı", image=yukle ,width=150,height=150  )
          goruntu.image = yukle
          goruntu.place(x=590, y=10)
          buton2=Button(ekran4,text="Siparişler",command=siparisler,height=1,width=15 ,font=("Arial", 12, "bold"), background="#001627",activebackground="#001627",fg="white",activeforeground="white")
          buton2.place(x=15,y=200)
          buton3=Button(ekran4,text="Kayıtlı Kullanıcılar",command=kayıtlıkullanıcılar,height=1,width=15 ,font=("Arial", 12, "bold"), background="#001627",activebackground="#001627",fg="white",activeforeground="white")
          buton3.place(x=15,y=260)
          buton4=Button(ekran4,text="Şikayetler",command=sikayetler,height=1,width=15 ,font=("Arial", 12, "bold"), background="#001627",activebackground="#001627",fg="white",activeforeground="white")
          buton4.place(x=15,y=320)
          buton5=Button(ekran4,text="Çıkış",command=quit,height=1,width=15 ,font=("Arial", 12, "bold"), background="#001627",activebackground="#001627",fg="white",activeforeground="white")
          buton5.place(x=15,y=380)
          yazı1=Label(ekran4,text="ÜRÜNLER" ,font=("Arial", 15, "bold"),fg="black",bg="#47ade3")
          yazı1.place(x=350,y=205)
          buton1=Button(ekran4,text="Ürün Ekle",command=ürünekle,height=1,width=15 ,font=("Arial", 12, "bold"), background="#001627",activebackground="#001627",fg="white",activeforeground="white")
          buton1.place(x=470,y=202)

          arama=Entry(ekran4,textvariable=q)
          arama.place(x=670,y=202,width=150,height=35)

          buton2=Button(ekran4,text="Arama",command=arama,height=1,width=10,font=("Arial", 12, "bold"), background="#001627",activebackground="#001627",fg="white",activeforeground="white")
          buton2.place(x=830,y=202)
          #ürün bilgileri tutuldugu yer
          def ürün_bagla():
           global sonuclar2
           global sorgu2
          mycursor = veritab.cursor()

          sorgu2= "SELECT urun_kodu,urun_adi,urun_fiyati,stok_sayisi from urunler"

          mycursor.execute(sorgu2)

          sonuclar2 = mycursor.fetchall()

          ürün_bagla()
    
          tree3 = ttk.Treeview(ekran4)
          tree3.config(height=29)

          style = ttk.Style(ekran4)
          style.theme_use("clam")
          style.configure("Treeview", background="white",fieldbackground="white", foreground="black")

          tree3["columns"]=("Ürün Kodu","Ürün Adı","Ürün Fiyatı","Stok Sayısı")
          tree3.column("Ürün Kodu", width=130,anchor='sw')
          tree3.column("Ürün Adı", width=200,anchor='sw')
          tree3.column("Ürün Fiyatı", width=140,anchor='sw')
          tree3.column("Stok Sayısı", width=120,anchor='sw')

          tree3.heading("Ürün Kodu", text="Ürün Kodu",anchor='sw')
          tree3.heading("Ürün Adı", text="Ürün Adı",anchor='sw')
          tree3.heading("Ürün Fiyatı", text="Ürün Fiyatı",anchor='sw')
          tree3.heading("Stok Sayısı", text="Stok Sayısı",anchor='sw')
          for satir in range(len(sonuclar2)):
            for sutun in range(1):
             tree3.insert("", 0, values=(sonuclar2[satir]))
             tree3.place(x=330,y=250)
    
          def saat_goster():
           su_an=time.strftime('%H:%M:%S')
           saat['text']=su_an
           ekran4.after(1000,saat_goster)
    
          saat=Label(ekran4,font='times 30', bg="#47ade3",fg="white")
          saat.place(x=965,y=190)
          saat_goster()
#arama BUTONU çalışmıyorrrrr
def arama():
    global sonuclar2
    
    q2=q.get()
    sorgu2="SELECT urun_kodu,urun_adi,urun_fiyati,stok_sayisi from urunler WHERE urun_kodu LIKE '%'+q2+'%' OR urun_adi LIKE '%'+q2+'%'"
    mycursor.execute(sorgu2)
    sonuclar2=mycursor.fetchall()
    
    

#admin kullanıcı giriş kısmı
def adminbutton():
         ekran1 = Toplevel(ekran)
         ekran1.title("admin içerik")
         ekran1.state("zoomed")
         ekran1.configure(bg="#47ade3")
         resim = Image.open("toptancı.png")
         yukle = ImageTk.PhotoImage(resim)
         goruntu = Label(ekran1,text="toptancı", image=yukle ,width=150,height=150  )
         goruntu.image = yukle
         goruntu.place(x=590, y=10)
         yazı1=Label(ekran1,text="Admin Kullanıcı Adı" ,font=("Arial", 12, "bold"),fg="black",bg="#47ade3")
         yazı1.place(x=400,y=280)
         yazı2=Label(ekran1,text="Şifre" ,font=("Arial", 12, "bold"),fg="black",bg="#47ade3")
         yazı2.place(x=400,y=350)
         adminentry=Entry(ekran1)
         adminentry.place(x=600,y=280,width=200,height=35)
         adminsifreentry=Entry(ekran1)
         adminsifreentry.place(x=600,y=350,width=200,height=35)
    
         buton3=Button(ekran1,text="İPTAL",command=quit, font=("Arial", 12, "bold"), background="#001627",activebackground="#001627",fg="white",activeforeground="white")
         buton3.place(x=650,y=420)
         buton3=Button(ekran1,text="GİRİŞ",command=adminkayıtbutton, font=("Arial", 12, "bold"), background="#001627",activebackground="#001627",fg="white",activeforeground="white")
         buton3.place(x=730,y=420)
    

    
      
        
#kayıtlı kullanıcı giriş kısmı    
def kullanıcıbutton():
    ekran2 = Toplevel(ekran)
    ekran2.title("kullanıcı içerik")
    ekran2.state("zoomed")
    ekran2.configure(bg="#47ade3")
    resim = Image.open("toptancı.png")
    yukle = ImageTk.PhotoImage(resim)
    goruntu = Label(ekran2,text="toptancı", image=yukle ,width=150,height=150  )
    goruntu.image = yukle
    goruntu.place(x=590, y=10)
    yazı1=Label(ekran2,text="Kullanıcı Adı" ,font=("Arial", 12, "bold"),fg="black",bg="#47ade3")
    yazı1.place(x=400,y=280)
    yazı2=Label(ekran2,text="Şifre" ,font=("Arial", 12, "bold"),fg="black",bg="#47ade3")
    yazı2.place(x=400,y=350)
    kutu=Entry(ekran2)
    kutu.place(x=600,y=280,width=200,height=35)
    kutu2=Entry(ekran2)
    kutu2.place(x=600,y=350,width=200,height=35)
#düzenleeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeee
    
   
    buton5=Button(ekran2,text="İPTAL",command=kullanıcıkayıtbutton, font=("Arial", 12, "bold"), background="#001627",activebackground="#001627",fg="white",activeforeground="white")
    buton5.place(x=650,y=420)
    buton6=Button(ekran2,text="GİRİŞ",command=kullanıcıkayıtbutton, font=("Arial", 12, "bold"), background="#001627",activebackground="#001627",fg="white",activeforeground="white")
    buton6.place(x=730,y=420)
    


#KULLANICI KAYDETTİGİM KISIM
def kayıtbutton():
    ekran3 = Toplevel(ekran)
    ekran3.title("KULLANICI KAYIT ALANI")
    ekran3.state("zoomed")
    ekran3.configure(bg="#47ade3")
    yazı=Label(ekran3,text="Kullanıcı Kayıt Ekranı" ,font=("Arial", 15, "bold"),fg="black",bg="#47ade3")
    yazı.place(x=550,y=40)
    yazı1=Label(ekran3,text="Kullanıcı Adı" ,font=("Arial", 12, "bold"),fg="black",bg="#47ade3")
    yazı1.place(x=200,y=150)
    kkutu1=Entry(ekran3)
    kkutu1.place(x=350,y=150,width=200,height=35)
    yazı2=Label(ekran3,text="Adı" ,font=("Arial", 12, "bold"),fg="black",bg="#47ade3")
    yazı2.place(x=200,y=210)
    kkutu2=Entry(ekran3)
    kkutu2.place(x=350,y=210,width=200,height=35)
    yazı3=Label(ekran3,text="Soyadı" ,font=("Arial", 12, "bold"),fg="black",bg="#47ade3")
    yazı3.place(x=200,y=270)
    kkutu3=Entry(ekran3)
    kkutu3.place(x=350,y=270,width=200,height=35)
    yazı4=Label(ekran3,text="E-posta" ,font=("Arial", 12, "bold"),fg="black",bg="#47ade3")
    yazı4.place(x=200,y=330)
    kkutu4=Entry(ekran3)
    kkutu4.place(x=350,y=330,width=200,height=35)
    yazı9=Label(ekran3,text="Şifre",font=("Arial", 12, "bold"),fg="black",bg="#47ade3")
    yazı9.place(x=200,y=390)
    kkutu9=Entry(ekran3)
    kkutu9.place(x=350,y=390,width=200,height=35)
    yazı5=Label(ekran3,text="Adres" ,font=("Arial", 12, "bold"),fg="black",bg="#47ade3")
    yazı5.place(x=600,y=150)
    kkutu5=Entry(ekran3)
    kkutu5.place(x=750,y=150,width=200,height=35)
    
    
    yazı6=Label(ekran3,text="Ülke" ,font=("Arial", 12, "bold"),fg="black",bg="#47ade3")
    yazı6.place(x=600,y=210)
    
    combo1 =Combobox(ekran3, width=8, height=10)
    combo1['values'] = ("Türkiye")
    combo1.place(x=750, y=210)
    combo1.current(0)
    combo1.config(font=("Arial", 12, "bold"),background="#509CCE")
    
    yazı7=Label(ekran3,text="Şehir" ,font=("Arial", 12, "bold"),fg="black",bg="#47ade3")
    yazı7.place(x=600,y=270)
    
    combo2 =Combobox(ekran3, width=8, height=10)
    combo2['values'] = ("İstanbul","İzmir","Ankara","Trabzon","Bursa")
    combo2.place(x=750, y=270)
    combo2.current(0)
    combo2.config(font=("Arial", 12, "bold"),background="#509CCE")
    
    yazı8=Label(ekran3,text="Posta Kodu" ,font=("Arial", 12, "bold"),fg="black",bg="#47ade3")
    yazı8.place(x=600,y=330)
    kkutu8=Entry(ekran3)
    kkutu8.place(x=750,y=330,width=200,height=35)
#kullanıcı bilgilerini veri tabanına kaydettiğım kısım
    def kaydol():
        global kayıtekle
        mycursor = veritab.cursor()
        yazı1=kkutu1.get();
        yazı2=kkutu2.get();
        yazı3=kkutu3.get();
        yazı4=kkutu4.get();
        yazı5=kkutu5.get();
        yazı8=kkutu8.get();
        yazı9=kkutu9.get();
        if(yazı1=="" or yazı2=="" or yazı3=="" or yazı4=="" or yazı5=="" or  yazı8=="" or yazı9==""):
         messagebox.showinfo("UYARI","Eksik bilgi")

        else:

         kayıtekle = "INSERT INTO kullaniciler (kullanici_adi,adi,soyadi,e_posta,adres,ülke,sehir,posta_kodu,sifre) VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s)"
         deger = (kkutu1.get(), kkutu2.get() , kkutu3.get(),  kkutu4.get(), kkutu5.get(), combo1.get(),combo2.get(), kkutu8.get() ,kkutu9.get())
         mycursor.execute(kayıtekle, deger)
         messagebox.showinfo("UYARI","Kayıt başarılı")

         veritab.commit()
         kkutu1.delete(0,'end')
         kkutu2.delete(0,'end')
         kkutu3.delete(0,'end')
         kkutu4.delete(0,'end')
         kkutu5.delete(0,'end')
         combo1.delete(0,'end')
         combo2.delete(0,'end')
         kkutu8.delete(0,'end')
         kkutu9.delete(0,'end')
         Messagebox.showinfo("UYARI","Kayıt başarılı")
         veritab.close();

         print(mycursor.rowcount, "kayıt başarılı.")
         
        
    buton1=Button(ekran3,text="İPTAL",command=quit, font=("Arial", 12, "bold"), background="#001627",activebackground="#001627",fg="white",activeforeground="white")
    buton1.place(x=750,y=420)
    buton2=Button(ekran3,text="KAYDOL",command=kaydol, font=("Arial", 12, "bold"), background="#001627",activebackground="#001627",fg="white",activeforeground="white")
    buton2.place(x=850,y=420)


    

#ana giriş admin kullanıcı ve kayıt ekranına yönlendirme yapılır.o yuzden def koymadın unutmaaa    
resim = Image.open("toptancı.png")
yukle = ImageTk.PhotoImage(resim)
goruntu = Label(ekran,text="toptancı", image=yukle ,width=150,height=150  )
goruntu.image = yukle
goruntu.place(x=590, y=10)
    
buton1=Button(text="ADMİN GİRİŞ",command=adminbutton,height=6,width=25 ,font=("Arial", 12, "bold"), background="#001627",activebackground="#001627",fg="white",activeforeground="white")
buton1.place(x=250,y=300)

buton2=Button(text="KULLANICI GİRİŞ",command=kullanıcıbutton,height=6,width=25 ,font=("Arial", 12, "bold"), background="#001627",activebackground="#001627",fg="white",activeforeground="white")
buton2.place(x=800,y=300)

buton3=Button(text="Kayıt olmak için tıklayınız",command=kayıtbutton, font=("Arial", 12, "bold"), background="#001627",activebackground="#001627",fg="white",activeforeground="white")
buton3.place(x=825,y=450)
#tüm çıkışlar
def Quit(ekran):
    Quit()


    
    
   


def siparisler():
   ekran6 = Toplevel(ekran)
   ekran6.title("Sipariş bilgileri")
   ekran6.state("zoomed")
   ekran6.configure(bg="#47ade3")
   resim = Image.open("toptancı.png")
   yukle = ImageTk.PhotoImage(resim)
   goruntu = Label(ekran6,text="toptancı", image=yukle ,width=150,height=150  )
   goruntu.image = yukle
   goruntu.place(x=590, y=10)
   yazı1=Label(ekran6,text="SİPARİŞLER" ,font=("Arial", 15, "bold"),fg="black",bg="#47ade3")
   yazı1.place(x=175,y=210)

  
    
   tree = ttk.Treeview(ekran6)
   tree.config(height=29)

   style = ttk.Style(ekran6)
   style.theme_use("clam")
   style.configure("Treeview", background="white",fieldbackground="white", foreground="black")

   tree["columns"]=("Kullanıcı Adı","Ürün Kodu","Ürün Adı","Sipariş Tarihi","Adet","Tutar")
   tree.column("Kullanıcı Adı", width=150,anchor='sw')
   tree.column("Ürün Kodu", width=130,anchor='sw')
   tree.column("Ürün Adı", width=140,anchor='sw')
   tree.column("Sipariş Tarihi", width=140,anchor='sw')
   tree.column("Adet", width=100,anchor='sw')
   tree.column("Tutar", width=100,anchor='sw')

   tree.heading("Kullanıcı Adı", text="Kullanıcı Adı",anchor='sw')
   tree.heading("Ürün Kodu", text="Ürün Kodu",anchor='sw')
   tree.heading("Ürün Adı", text="Ürün Adı",anchor='sw')
   tree.heading("Sipariş Tarihi", text="Sipariş Tarihi",anchor='sw')
   tree.heading("Adet", text="Adet",anchor='sw')
   tree.heading("Tutar", text="Tutar",anchor='sw')
   
   tree.place(x=170,y=250)
def kayıtlıkullanıcılar():
   ekran7 = Toplevel(ekran)
   ekran7.title("Sipariş bilgileri")
   ekran7.state("zoomed")
   ekran7.configure(bg="#47ade3")
   resim = Image.open("toptancı.png")
   yukle = ImageTk.PhotoImage(resim)
   goruntu = Label(ekran7,text="toptancı", image=yukle ,width=150,height=150  )
   goruntu.image = yukle
   goruntu.place(x=590, y=10)
   yazı1=Label(ekran7,text="KAYITLI KULLANICILAR" ,font=("Arial", 15, "bold"),fg="black",bg="#47ade3")
   yazı1.place(x=115,y=210)
   def kayıtlıkullanıcılar_bagla():
     global sonuclar
     global sorgu1
     mycursor = veritab.cursor()

     sorgu1 = "SELECT kullanici_adi,adi,soyadi,e_posta,adres,ülke,sehir,posta_kodu from kullaniciler"

     mycursor.execute(sorgu1)

     sonuclar = mycursor.fetchall()

   kayıtlıkullanıcılar_bagla()
    
   tree2 = ttk.Treeview(ekran7)
   tree2.config(height=29)

   style = ttk.Style(ekran7)
   style.theme_use("clam")
   style.configure("Treeview", background="white",fieldbackground="white", foreground="black")

   tree2["columns"]=("Kullanıcı Adı","Adı","Soyadı","E-posta","Adres","Şehir","Ülke","Posta Kodu")
   tree2.column("Kullanıcı Adı", width=150,anchor='sw')
   tree2.column("Adı", width=130,anchor='sw')
   tree2.column("Soyadı", width=140,anchor='sw')
   tree2.column("E-posta", width=140,anchor='sw')
   tree2.column("Adres", width=100,anchor='sw')
   tree2.column("Şehir", width=100,anchor='sw')
   tree2.column("Ülke", width=100,anchor='sw')
   tree2.column("Posta Kodu", width=100,anchor='sw')


   tree2.heading("Kullanıcı Adı", text="Kullanıcı Adı",anchor='sw')
   tree2.heading("Adı", text="Adı",anchor='sw')
   tree2.heading("Soyadı", text="Soyadı",anchor='sw')
   tree2.heading("E-posta", text="E-posta",anchor='sw')
   tree2.heading("Adres", text="Adres",anchor='sw')
   tree2.heading("Şehir", text="Şehir",anchor='sw')
   tree2.heading("Ülke", text="Ülke",anchor='sw')
   tree2.heading("Posta Kodu", text="Posta Kodu",anchor='sw')

   for satir in range(len(sonuclar)):
     for sutun in range(1):
        tree2.insert("", 0, values=(sonuclar[satir]))

   tree2.place(x=115,y=250)
 
def sikayetler():
   ekran8 = Toplevel(ekran)
   ekran8.title("Sipariş bilgileri")
   ekran8.state("zoomed")
   ekran8.configure(bg="#47ade3")
   resim = Image.open("toptancı.png")
   yukle = ImageTk.PhotoImage(resim)
   goruntu = Label(ekran8,text="toptancı", image=yukle ,width=150,height=150  )
   goruntu.image = yukle
   goruntu.place(x=590, y=10)
   yazı1=Label(ekran8,text="ŞİKAYETLER" ,font=("Arial", 15, "bold"),fg="black",bg="#47ade3")
   yazı1.place(x=300,y=210)

   def s():
           global sonuclar2
           global sorgu2
   mycursor = veritab.cursor()

   sorgu2= "select kullanici_adi,adi,soyadi,sikayeti from kullaniciler inner join sikayet on kullaniciler.id=sikayet.kullanici_id"

   mycursor.execute(sorgu2)

   sonuclar2 = mycursor.fetchall()

   s()
    
   tree = ttk.Treeview(ekran8)
   tree.config(height=29)

   style = ttk.Style(ekran8)
   style.theme_use("clam")
   style.configure("Treeview", background="white",fieldbackground="white", foreground="black")

   tree["columns"]=("Kullanıcı Adı","Adı","Soyadı","Şikayeti")
   tree.column("Kullanıcı Adı", width=150,anchor='sw')
   tree.column("Adı", width=130,anchor='sw')
   tree.column("Soyadı", width=140,anchor='sw')
   tree.column("Şikayeti", width=100,anchor='sw')
   

   tree.heading("Kullanıcı Adı", text="Kullanıcı Adı",anchor='sw')
   tree.heading("Adı", text="Adı",anchor='sw')
   tree.heading("Soyadı", text="Soyadı",anchor='sw')
   tree.heading("Şikayeti", text="Şikayeti",anchor='sw')
   for satir in range(len(sonuclar2)):
            for sutun in range(1):
             tree.insert("", 0, values=(sonuclar2[satir]))

             tree.place(x=300,y=250)
    
#admin sayfasında ürün ekle
def ürünekle():
   ekran9 = Toplevel(ekran)
   ekran9.title("Ürün ekle")
   ekran9.state("zoomed")
   ekran9.configure(bg="#47ade3")
   resim = Image.open("toptancı.png")
   yukle = ImageTk.PhotoImage(resim)
   goruntu = Label(ekran9,text="toptancı", image=yukle ,width=150,height=150  )
   goruntu.image = yukle
   goruntu.place(x=590, y=10)
   yazı1=Label(ekran9,text="ÜRÜN EKLE" ,font=("Arial", 15, "bold"),fg="black",bg="#47ade3")
   yazı1.place(x=300,y=190)
   
   
   yazı2=Label(ekran9,text="Ürün Kodu" ,font=("Arial", 12, "bold"),fg="black",bg="#47ade3")
   yazı2.place(x=450,y=270)
   kutu2=Entry(ekran9)
   kutu2.place(x=600,y=270,width=200,height=35)
   yazı3=Label(ekran9,text="Ürün Adı" ,font=("Arial", 12, "bold"),fg="black",bg="#47ade3")
   yazı3.place(x=450,y=340)
   kutu3=Entry(ekran9)
   kutu3.place(x=600,y=340,width=200,height=35)
   yazı4=Label(ekran9,text="Ürün Fiyatı" ,font=("Arial", 12, "bold"),fg="black",bg="#47ade3")
   yazı4.place(x=450,y=410)
   kutu4=Entry(ekran9)
   kutu4.place(x=600,y=410,width=200,height=35)
   yazı5=Label(ekran9,text="Stok Sayısı" ,font=("Arial", 12, "bold"),fg="black",bg="#47ade3")
   yazı5.place(x=450,y=480)
   kutu5=Entry(ekran9)
   kutu5.place(x=600,y=480,width=200,height=35)

   #yeni ürün ekleme butonu
   def ürünekledim():
        global kayıtekle
        mycursor = veritab.cursor()
        yazı2=kutu2.get();
        yazı3=kutu3.get();
        yazı4=kutu4.get();
        yazı5=kutu5.get();
        
        if(yazı1=="" or yazı2=="" or yazı3=="" or yazı4=="" or yazı5==""):
         messagebox.showinfo("UYARI","Ürün ekleme tamamlanamıyor")

        else:

         kayıtekle = "INSERT INTO urunler (urun_kodu,urun_adi,urun_fiyati,stok_sayisi) VALUES (%s,%s,%s,%s)"
         deger = (kutu2.get() , kutu3.get(),  kutu4.get(), kutu5.get())
         mycursor.execute(kayıtekle, deger)
         messagebox.showinfo("UYARI","Yeni ürün kaydedildi")

         veritab.commit()
         kutu2.delete(0,'end')
         kutu3.delete(0,'end')
         kutu4.delete(0,'end')
         kutu5.delete(0,'end')
         Messagebox.showinfo("UYARI","Kayıt başarılı")
         veritab.close();

         print(mycursor.rowcount, "kayıt başarılı.")
   buton1=Button(ekran9,text="KAYDET",command=ürünekledim,height=1,width=15 ,font=("Arial", 12, "bold"), background="#001627",activebackground="#001627",fg="white",activeforeground="white")
   buton1.place(x=850,y=550)
   buton2=Button(ekran9,text="İPTAL",command=quit,height=1,width=15 ,font=("Arial", 12, "bold"), background="#001627",activebackground="#001627",fg="white",activeforeground="white")
   buton2.place(x=650,y=550)


#kullanıcı içerik kısmı
def kullanıcıkayıtbutton():
    ekran10 = Toplevel(ekran)
    ekran10.title("kullanıcı içerik bilgi")
    ekran10.state("zoomed")
    ekran10.configure(bg="#47ade3")
    resim = Image.open("toptancı.png")
    yukle = ImageTk.PhotoImage(resim)
    goruntu = Label(ekran10,text="toptancı", image=yukle ,width=150,height=150  )
    goruntu.image = yukle
    goruntu.place(x=590, y=10)
    buton2=Button(ekran10,text="Siparişlerim",command=siparislerim,height=1,width=15 ,font=("Arial", 12, "bold"), background="#001627",activebackground="#001627",fg="white",activeforeground="white")
    buton2.place(x=15,y=200)
    buton3=Button(ekran10,text="Şikayet Et",command=sikayetet,height=1,width=15 ,font=("Arial", 12, "bold"), background="#001627",activebackground="#001627",fg="white",activeforeground="white")
    buton3.place(x=15,y=260)
    buton5=Button(ekran10,text="Çıkış",command=quit,height=1,width=15 ,font=("Arial", 12, "bold"), background="#001627",activebackground="#001627",fg="white",activeforeground="white")
    buton5.place(x=15,y=320)
    yazı1=Label(ekran10,text="ÜRÜN SİPARİŞ ET" ,font=("Arial", 15, "bold"),fg="black",bg="#47ade3")
    yazı1.place(x=350,y=205)


    
    
    yazı2=Label(ekran10,text="Ürün Seç" ,font=("Arial", 12, "bold"),fg="black",bg="#47ade3")
    yazı2.place(x=250,y=300)

    mycursor.execute("select urun_adi from urunler")
    result = mycursor.fetchall()
    combo1 =Combobox(ekran10, width=14, height=12)
    urunler = ["Ürün Seçiniz"]
    for urun in result:
        urunler.append(urun)
    combo1['values'] = urunler
    
    combo1.place(x=400, y=300)
    combo1.current(0)
    combo1.config(font=("Arial", 12, "bold"),background="#509CCE")

    adet=Label(ekran10,text="Ürün Adedi" ,font=("Arial", 12, "bold"),fg="black",bg="#47ade3")
    adet.place(x=250,y=350)
    adetyaz=Entry(ekran10)
    adetyaz.place(x=400,y=350,width=200,height=35)
    def ürün():
           global sonuclar4
           global sorgu4
           mycursor = veritab.cursor()

           sorgu4= "SELECT urun_adi,urun_fiyati from urunler"

           mycursor.execute(sorgu4)

           sonuclar4 = mycursor.fetchall()

    ürün()
    tree4 = ttk.Treeview(ekran10)
    tree4.config(height=29)

    style = ttk.Style(ekran10)
    style.theme_use("clam")
    style.configure("Treeview", background="white",fieldbackground="white", foreground="black")

    tree4["columns"]=("Ürün Adı","Ürün Fiyatı")
    
    tree4.column("Ürün Adı", width=150,anchor='sw')
    tree4.column("Ürün Fiyatı", width=140,anchor='sw')

    tree4.heading("Ürün Adı", text="Ürün Adı",anchor='sw')
    tree4.heading("Ürün Fiyatı", text="Ürün Fiyatı",anchor='sw')
    for satir in range(len(sonuclar4)):
            for sutun in range(1):
             tree4.insert("", 0, values=(sonuclar4[satir]))
    tree4.place(x=790,y=250)
    
    


    
    buton6=Button(ekran10,text="İPTAL",command=quit,height=1,width=15 ,font=("Arial", 12, "bold"), background="#001627",activebackground="#001627",fg="white",activeforeground="white")
    buton6.place(x=300,y=570)
    buton7=Button(ekran10,text="SATIN AL",command=satınalkartbilgileri,height=1,width=15 ,font=("Arial", 12, "bold"), background="#001627",activebackground="#001627",fg="white",activeforeground="white")
    buton7.place(x=500,y=570)

    
    def saat_goster():
     su_an=time.strftime('%H:%M:%S')
     saat['text']=su_an
     ekran10.after(1000,saat_goster)
    
    saat=Label(ekran10,font='times 30', bg="#47ade3",fg="white")
    saat.place(x=965,y=190)
    saat_goster()
    
    
def satınalkartbilgileri():
    ekran11 = Toplevel(ekran)
    ekran11.title("kART BİLGİLERİ")
    ekran11.state("zoomed")
    ekran11.configure(bg="#47ade3")
    resim = Image.open("toptancı.png")
    yukle = ImageTk.PhotoImage(resim)
    goruntu = Label(ekran11,text="toptancı", image=yukle ,width=150,height=150  )
    goruntu.image = yukle
    goruntu.place(x=590, y=10)
    yazı1=Label(ekran11,text="KART BİLGİLERİ" ,font=("Arial", 15, "bold"),fg="black",bg="#47ade3")
    yazı1.place(x=350,y=180)
    yazı2=Label(ekran11,text="Adı" ,font=("Arial", 12, "bold"),fg="black",bg="#47ade3")
    yazı2.place(x=450,y=230)
    kutu2=Entry(ekran11)
    kutu2.place(x=670,y=230,width=200,height=35)
    yazı3=Label(ekran11,text="Soyadı" ,font=("Arial", 12, "bold"),fg="black",bg="#47ade3")
    yazı3.place(x=450,y=300)
    kutu3=Entry(ekran11)
    kutu3.place(x=670,y=300,width=200,height=35)
    yazı4=Label(ekran11,text="Kart Numarası" ,font=("Arial", 12, "bold"),fg="black",bg="#47ade3")
    yazı4.place(x=450,y=370)
    kutu4=Entry(ekran11)
    kutu4.place(x=670,y=370,width=200,height=35)
    yazı5=Label(ekran11,text="Son Kullanma Tarihi(AA/YY)" ,font=("Arial", 12, "bold"),fg="black",bg="#47ade3")
    yazı5.place(x=450,y=440)
    kutu5=Entry(ekran11)
    kutu5.place(x=670,y=440,width=200,height=35)
    yazı6=Label(ekran11,text="Güvenlik Kodu(CVV)" ,font=("Arial", 12, "bold"),fg="black",bg="#47ade3")
    yazı6.place(x=450,y=510)
    kutu6=Entry(ekran11)
    kutu6.place(x=670,y=510,width=200,height=35)
    buton1=Button(ekran11,text="İPTAL",command=quit,height=1,width=15 ,font=("Arial", 12, "bold"), background="#001627",activebackground="#001627",fg="white",activeforeground="white")
    buton1.place(x=650,y=600)
    buton2=Button(ekran11,text="SATIN AL",command=satınal,height=1,width=15 ,font=("Arial", 12, "bold"), background="#001627",activebackground="#001627",fg="white",activeforeground="white")
    buton2.place(x=850,y=600)
def satınal():
    pass
def siparislerim():
   ekran12 = Toplevel(ekran)
   ekran12.title("Sipariş bilgileri")
   ekran12.state("zoomed")
   ekran12.configure(bg="#47ade3")
   resim = Image.open("toptancı.png")
   yukle = ImageTk.PhotoImage(resim)
   goruntu = Label(ekran12,text="toptancı", image=yukle ,width=150,height=150  )
   goruntu.image = yukle
   goruntu.place(x=590, y=10)
   yazı1=Label(ekran12,text="SİPARİŞLERİM" ,font=("Arial", 15, "bold"),fg="black",bg="#47ade3")
   yazı1.place(x=220,y=210)
    
   tree = ttk.Treeview(ekran12)
   tree.config(height=29)

   style = ttk.Style(ekran12)
   style.theme_use("clam")
   style.configure("Treeview", background="white",fieldbackground="white", foreground="black")

   tree["columns"]=("Ürün Adı","Ürün Kodu","Ürün Fiyatı","Siparis Tarihi","Adet","Tutar")
   tree.column("Ürün Adı", width=150,anchor='sw')
   tree.column("Ürün Kodu", width=130,anchor='sw')
   tree.column("Ürün Fiyatı", width=140,anchor='sw')
   tree.column("Siparis Tarihi", width=140,anchor='sw')
   tree.column("Adet", width=140,anchor='sw')
   tree.column("Tutar", width=100,anchor='sw')
   

   tree.heading("Ürün Adı", text="Ürün Adı",anchor='sw')
   tree.heading("Ürün Kodu", text="Ürün Kodu",anchor='sw')
   tree.heading("Ürün Fiyatı", text="Ürün Fiyatı",anchor='sw')
   tree.heading("Siparis Tarihi", text="Siparis Tarihi",anchor='sw')
   tree.heading("Adet", text="Adet",anchor='sw')
   tree.heading("Tutar", text="Tutar",anchor='sw')

   tree.place(x=220,y=250)
def sikayetet():
   ekran13 = Toplevel(ekran)
   ekran13.title("Şikayet et")
   ekran13.state("zoomed")
   ekran13.configure(bg="#47ade3")
   resim = Image.open("toptancı.png")
   yukle = ImageTk.PhotoImage(resim)
   goruntu = Label(ekran13,text="toptancı", image=yukle ,width=150,height=150  )
   goruntu.image = yukle
   goruntu.place(x=590, y=10)
   yazı1=Label(ekran13,text="ŞİKAYET ET" ,font=("Arial", 15, "bold"),fg="black",bg="#47ade3")
   yazı1.place(x=300,y=190)
   
   yazı2=Label(ekran13,text="Kullanıcı Adı" ,font=("Arial", 12, "bold"),fg="black",bg="#47ade3")
   yazı2.place(x=450,y=270)
   kutu2=Entry(ekran13)
   kutu2.place(x=600,y=270,width=200,height=35)
   yazı3=Label(ekran13,text="Adı" ,font=("Arial", 12, "bold"),fg="black",bg="#47ade3")
   yazı3.place(x=450,y=340)
   kutu3=Entry(ekran13)
   kutu3.place(x=600,y=340,width=200,height=35)
   yazı4=Label(ekran13,text="Soyadı" ,font=("Arial", 12, "bold"),fg="black",bg="#47ade3")
   yazı4.place(x=450,y=410)
   kutu4=Entry(ekran13)
   kutu4.place(x=600,y=410,width=200,height=35)
   yazı5=Label(ekran13,text="Şikayet" ,font=("Arial", 12, "bold"),fg="black",bg="#47ade3")
   yazı5.place(x=450,y=480)
   kutu5=Entry(ekran13)
   kutu5.place(x=600,y=480,width=200,height=70)

   def sikayetyolla():
        global kayıtekle
        mycursor = veritab.cursor()
       
        yazı5=kutu5.get();
        
        if( yazı5==""):
         messagebox.showinfo("UYARI","Ürün ekleme tamamlanamıyor")
         
#else olmuyorrr
        else:

         kayıtekle = "INSERT INTO sikayet(sikayet) VALUES %s"
         deger = ( kutu5.get())
         mycursor.execute(kayıtekle, deger)
         messagebox.showinfo("UYARI","Yeni ürün kaydedildi")

         veritab.commit()
        
         kutu5.delete(0,'end')
         Messagebox.showinfo("UYARI","Kayıt başarılı")
         veritab.close();
        
         print(mycursor.rowcount, "kayıt başarılı.")
   buton1=Button(ekran13,text="GÖNDER",command=sikayetyolla,height=1,width=15 ,font=("Arial", 12, "bold"), background="#001627",activebackground="#001627",fg="white",activeforeground="white")
   buton1.place(x=850,y=610)
   buton2=Button(ekran13,text="İPTAL",command=quit,height=1,width=15 ,font=("Arial", 12, "bold"), background="#001627",activebackground="#001627",fg="white",activeforeground="white")
   buton2.place(x=650,y=610)


    
 
    
