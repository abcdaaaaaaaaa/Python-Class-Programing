import random
class Bilgisayar():
    def __init__(self,sınıf="Ana",renk="Siyah",tür="Masaüstü",para=20000,ram=500,marka="Apple",exstra=["Klavye", "Kamera", "Işıklandırma", "Vergi", "Fatura", "Mağaza", "Garanti"], oncelik =("Klavye", "Kamera", "Işıklandırma", "Vergi", "Fatura", "Mağaza", "Garanti")):
        self.sınıf = sınıf
        self.renk = renk
        self.tür = tür
        self.para = para
        self.ram = ram
        self.marka = marka
        self.exstra = exstra
        self.oncelik = oncelik

    def rastgele_ozellik(self):

        rastgele = random.randint(0,len(self.oncelik)-1)
        self.oncelik = self.exstra[rastgele]

    def __str__(self):
        return " \n Sunucu : {} \n Renk : {} \n Tür: {} \n Para: {} \n Ram: {} \n Marka: {} \n Özellikler: {} \n Mevcut özellik: {}  \n ".format(self.sınıf,self.renk,self.tür,self.para,self.ram,self.marka,self.exstra,self.oncelik)
    
    def __len__(self):

        return len(self.exstra)

    
    def bilgilerigoster(self):
        
        print("Mevcut Bilgisayar bilgileri.....")  
        print(" \n Sunucu : {} \n Renk : {} \n Tür: {} \n Para: {} \n Ram: {} \n Marka: {} \n Özellikler: {}\n Mevcut özellik: {}  \n ".format(self.sınıf,self.renk,self.tür,self.para,self.ram,self.marka,self.exstra,self.oncelik))
        
    def satinalma(self):
         print("Satın Alma İşlemlerine KDV'de dahildir.")
         a= int(input("Ödemek İstediğiniz Tutar:"))
         if a>9*self.para/8 and a>0:
            print("Satın Alma Başarıyla Tamamlandı Para Üstünüz: {}".format(a-9*self.para/8))
            print("Başarıyla Tamamlandı")
         elif a == 9*self.para/8 and a>0:
            print("Satın Alma Başarıyla Tamamlandı Tutar Bilgisayar Fiyatı ile Aynı")
            print("Başarıyla Tamamlandı")
         elif a>0:
            print("Satın Almanız için : {}tl daha paraya ihtiyacınız var".format(9*self.para/8-a))
            print("Ödemeniz Gereken Tutar:{}".format(9*self.para/8))
         else:
            print("Satın Alma İşlemine devam edebilmeniz için paranızın olması lazım")
            print("Ödemeniz Gereken Tutar:{}".format(9*self.para/8))
            
    def sınıf_x(self):
        if self.sınıf=="Ana":
          if 10000==self.para<15000:
            print("Ana Bilgisayrların C Sınıfı")
          elif 15000<=self.para<25000:
            print("Ana Bilgisayarların B Sınıfı")
          elif 25000<=self.para<50000:
            print("Ana Bilgisayarların A Sınıfı")
          elif 50000<self.para:
            print("Ana Bilgisayarların A+ Sınıfı")
          else:
            print("Bilgisayarın Henüz Sınıfı Yok Ana Sunucudur Alınması Önerlmez")
        elif self.sınıf=="Alt":
            if 6000<=self.para<8000:
              print("Sunucu Bilgisayarların C Sınıfı")
            elif 8000<=self.para<10000:
              print("Sunucu Bilgisayarların B Sınıfı")
            elif 10000<self.para:
              print("Sunucu Bilgisayarların A Sınıfı")
            else:
              print("Bilgisayarın Henüz Sınıfı Yok Alt Sunucudur Alınması Önerlmez")
    def yedek(self,yedek_a):
         self.sınıf = yedek_a
               
    def renk_degistir(self,renk):
         self.renk = renk
         
    def tür_degistir(self,yeni_tür):
         self.tür = yeni_tür
         
    def para_degistir(self,yeni_para):
         self.para = yeni_para

    def ram_degistir(self,yeni_ram):
         self.ram = yeni_ram

    def marka_degistir(self,yeni_marka):
         self.marka = yeni_marka

    def para_azalt(self,az_para):
        self.para -= az_para  
    
    def ram_azalt(self,az_ram):
        self.ram -= az_ram
    
    def para_arttır(self,fazla_para):
        self.para += fazla_para  
    
    def ram_arttır(self,fazla_ram):
        self.ram += fazla_ram
        
    def yeni_ekle(self,yeni_ek):

        self.exstra.append(yeni_ek)

def hepsini_degistir():
    Bilgisayar2.renk_degistir(input("Değiştirmek istediğiniz Renk:"))
    Bilgisayar2.tür_degistir(input("Değiştirmek istediğiniz Tür:"))
    Bilgisayar2.para_degistir(int(input("Değiştirmek istediğiniz Para değeri:")))
    Bilgisayar2.ram_degistir(int(input("Değiştirmek istediğiniz Ram değeri:")))
    Bilgisayar2.marka_degistir(input("Değiştirmek istediğiniz Marka:"))

def ana_degistir():
    Bilgisayar3.renk_degistir(input("Değiştirmek istediğiniz Renk:"))
    Bilgisayar3.tür_degistir(input("Değiştirmek istediğiniz Tür:"))
    Bilgisayar3.para_degistir(int(input("Değiştirmek istediğiniz Para değeri:")))
    Bilgisayar3.ram_degistir(int(input("Değiştirmek istediğiniz Ram değeri:")))
    Bilgisayar3.marka_degistir(input("Değiştirmek istediğiniz Marka:"))

def hepsini_arttır():
    Bilgisayar2.para_arttır(int(input("Arttırmak istediğiniz Para değeri:")))
    Bilgisayar2.ram_arttır(int(input("Arttırmak istediğiniz Ram değeri:")))

def hepsini_azalt():
    Bilgisayar2.para_azalt(int(input("Arttırmak istediğiniz Para değeri:")))
    Bilgisayar2.ram_azalt(int(input("Arttırmak istediğiniz Ram değeri:")))
    

Bilgisayar2 = Bilgisayar("Alt","Siyah","Masaüstü",20000,500,"Apple",["Vergi", "Fatura", "Mağaza", "Garanti"],)
Bilgisayar3 = Bilgisayar("Ana","Siyah","Masaüstü",20000,500,"Apple",["Klavye", "Kamera", "Işıklandırma", "Vergi", "Fatura", "Mağaza", "Garanti"],)


print("""
Ana bilgisayarın sıfırlanması Programın Çalıştığındaki ilk andakidir ana bilgisayarların değişmesi anında 
sunucuları sıfırlamak istediğinizde ana bilgisayrın son (mevcut) bilgilerine göre sıfırlanır (Sunucu bilgisi hariç)
(Sunucu ve Sınıf Bilgilerin Değiştirilmesine izin verilmez) eğer sunucuyu ilk haline göre sıfırlamak istiyorsanız önce 
ana bilgisayarı sıfırlamalısınız sunucu bilgisayrın bazı özellikleri ana bilgisayara göre daha azdır 
(ekleme özelliğinden ekleyebilrsiniz (12)) Ana bilgisayarın 4 sınıfı vardır: bunlar sırasıyla: A+ (50000 ve üstü) sınıfı A (49999-25000)
sınıfı B (24999-15000) sınıfı ve C(14999-10000) sınıfıdır. Sunucu Bilgisayarın ise 3 sınıfı vardır bunlar sırasıyla:
A sınıfı (10000 ve üstü) B sınıfı (9999-8000) C sınıfı (7999-6000) aralığındadır. Ekonominize göre seçebilirsiniz(25)
Ana bilgisayarı telefona benzetirsek Sunucu bilgisayar telefona bağlanan cihazdır.
Sınıfı Arttıkça kalitesi artar. Seçtiğiniz işleme göre işlem yapılır işlem Numaraların görevleri aşığıda verilmiştir:
""")
print("""

1. Ana Bilgisayar Ayarları

2. Sunucu Bilgisayar Ayarları

3. Sunucu Bilgisayarı Sıfırlama

4. Ana Bilgisayarı Sıfırlama

5. Sunucu Bilgisayar Rengi

6. Sunucu Bilgisayar Türü

7. Sunucu Bilgisayar Parası

8. Sunucu Bilgisayar Ram

9. Sunucu Bilgisayar Markası

10. Sunucu Bilgisayar Azaltma Ayarları

11. Sunucu Bilgisayar Arttırma Ayarları

12. Sunucu Bilgisayara Özellik Ekleme

13. Ana Bilgisayara Rastgele Öncelikli Özellik Belirleme

14. Sunucu Bilgisayara Rastgele Öncelikli Özellik Belirleme

15. Ana Bilgisayara Özellik Ekleme

16. Sunucu Bilgisayar Mevcut Özellik Sayısını Öğrenme

17. Ana Bilgisayar Mevcut Özellik Sayısını Öğrenme

18. Mevcut Ana Bilgisayar Bilgileri

19. Sunucu Bilgisayar Ram Azaltma

20. Sunucu Bilgisayar Para Azaltma

21. Sunucu Bilgisayar Ram Arttırma

22. Sunucu Bilgisayar Para Arttırma

23. Ana Bilgisayar Satın Alma İşlemleri

24. Sunucu Bilgisayar Satın Alma İşlemleri

25. Mevcut Ekonomiye Göre Bilgisayar Önerisi

26. Sunucu Bilgisayarın Sınıfını Öğrenme (A/B/C) 

27. Ana Bilgisayarın Sınıfını Öğrenme (A+/A/B/C)

28. Programı Sonlandırma

    """)
# SC: 6000 SB : 8000 SA 10000 AC: 10000 AB 15000 AA 25000 A+ 50000

while True:

 işlem = int(input("İşlemi Seçiniz:"))
 match işlem:
    case 1:
        print("1. Ana Bilgisayar Ayarları")
        ana_degistir()
        print("Mevcut Ana Bilgisayar Bilgileri:")
        Bilgisayar3.bilgilerigoster()
    case 2:
        print("2. Sunucu Bilgisayar Ayarları")
        hepsini_degistir()
    case 3:
        print("3. Sunucu Bilgisayarı Sıfırlama")
        Bilgisayar2 = Bilgisayar3
        Bilgisayar2.yedek("Alt")
    case 4:
        print("4. Ana Bilgisayarı Sıfırlama")
        Bilgisayar3 == Bilgisayar("Ana","Siyah","Masaüstü",20000,500,"Apple",["Klavye", "Kamera", "Işıklandırma", "Vergi", "Fatura", "Mağaza", "Garanti"],)
        print("Mevcut Ana Bilgisayar Bilgileri:")
        Bilgisayar3.bilgilerigoster()
    case 5:
        print("5. Sunucu Bilgisayar Rengi")
        Bilgisayar2.renk_degistir(input("Değiştirmek istediğiniz Renk:"))
    case 6:
        print("6. Sunucu Bilgisayar Türü")
        Bilgisayar2.tür_degistir(input("Değiştirmek istediğiniz Tür:"))
    case 7:
        print("7. Sunucu Bilgisayar Parası")
        Bilgisayar2.para_degistir(int(input("Değiştirmek istediğiniz Para değeri:")))
    case 8:
        print("8. Sunucu Bilgisayar Ram")
        Bilgisayar2.ram_degistir(int(input("Değiştirmek istediğiniz Ram değeri:")))
    case 9:
        print("9. Sunucu Bilgisayar Markası")
        Bilgisayar2.marka_degistir(input("Değiştirmek istediğiniz Marka:"))
    case 10:
        print("10. Sunucu Bilgisayar Azaltma Ayarları")
        hepsini_azalt()
    case 11:
        print("11. Sunucu Bilgisayar Arttırma Ayarları")
        hepsini_arttır()
    case 12:
        print("12. Sunucu Bilgisayara Özellik Ekleme")
        yeni_isimleri = input("ekstra özellikleri ',' ile ayırarak girin:")
        yeni_listesi = yeni_isimleri.split(",")
        for ek in yeni_listesi:
            Bilgisayar2.yeni_ekle(ek)
    case 13:
        print("13. Ana Bilgisayara Rastgele Öncelikli Özellik Belirleme")
        Bilgisayar3.rastgele_ozellik()
        print("Mevcut Ana Bilgisayar Bilgileri:")
        Bilgisayar3.bilgilerigoster()

    case 14:
        print("14. Sunucu Bilgisayara Rastgele Öncelikli Özellik Belirleme")
        Bilgisayar2.rastgele_ozellik()
    case 15:
        print("15. Ana Bilgisayara Özellik Ekleme")
        yeni_isimleri = input("ekstra özellikleri ',' ile ayırarak girin:")
        yeni_listesi = yeni_isimleri.split(",")
        for ek in yeni_listesi:
            Bilgisayar3.yeni_ekle(ek)
        print("Mevcut Ana Bilgisayar Bilgileri:") 
        Bilgisayar3.bilgilerigoster()
    case 16:
        print("16. Sunucu Bilgisayar Mevcut Özellik Sayısını Öğrenme")
        print("Sunucu Bilgisayar Özellik Sayısı:",len(Bilgisayar2))
    case 17:
        print("17. Ana Bilgisayar Mevcut Özellik Sayısını Öğrenme")
        print("Ana Bilgisayar Özellik Sayısı:",len(Bilgisayar3))
    case 18:
        print("18. Mevcut Ana Bilgisayar Bilgileri")
        print("Mevcut Ana Bilgisayar Bilgileri:")
        Bilgisayar3.bilgilerigoster()
    case 19:
        print("19. Sunucu Bilgisayar Ram Azaltma")
        Bilgisayar2.ram_azalt(int(input("Azaltmak istediğiniz Ram değeri:")))
    case 20:
        print("20. Sunucu Bilgisayar Para Azaltma")
        Bilgisayar2.para_azalt(int(input("Azaltmak istediğiniz Para değeri:")))
    case 21:
        print("21. Sunucu Bilgisayar Ram Arttırma")
        Bilgisayar2.ram_arttır(int(input("Arttırmak istediğiniz Ram değeri:")))
    case 22:
        print("22. Sunucu Bilgisayar Para Arttırma")
        Bilgisayar2.para_arttır(int(input("Arttırmak istediğiniz Para değeri:")))
    case 23:
        print("23. Ana Bilgisayar Satın Alma İşlemleri")
        v=input("Ana Bilgisayarı Satın Almak İstedğinizden Eminmisiniz? (evet/hayır) :")
        if v == "evet":
         Bilgisayar3.satinalma()
         print("Satın Alduğınız Ana Bilgisayar Bilgileri:") 
         Bilgisayar3.bilgilerigoster()
        else:
           print("Satın Almak İçin Tekrar 23'ü Tuşlayın")
    case 24:
        print("24. Sunucu Bilgisayar Satın Alma İşlemleri")
        w=input("Sunucu Bilgisayarı Satın Almak İstedğinizden Eminmisiniz? (evet/hayır) :")
        if w == "evet":
         Bilgisayar2.satinalma()
         print("Satın Aldığınız:")
        else:
           print("Satın Almak İçin Tekrar 24'ü Tuşlayın")
    case 25:
        print("25. Mevcut Ekonomiye Göre Bilgisayar Önerisi")
        z=int(input("Ödeyebileceğiniz Maksimum Tutar:"))
        if 0<z<6000:
            print("Bilgisayar almamanızı öneriyoruz")
        elif 6000<=z<8000:
            print("Sunucu Bilgisayarların C Sınıfını Alabilirsiniz")
        elif 8000<=z<9500:
            print("Sunucu Bilgisayarların B Sınıfını Alabilirsiniz")
        elif 10000==z<15000:
            print("Sunucu Bilgisayarların A Sınıfını veya Ana Bilgisayrların C Sınıfını Alabilirsiniz")
        elif 15000<=z<25000:
            print("Ana Bilgisayarların B Sınıfını Alabilirsiniz")
        elif 25000<=z<50000:
            print("Ana Bilgisayarların A Sınıfını Alabilirsiniz")
        elif 50000<z:
            print("Ana Bilgisayarların A+ Sınıfını Alabilirsiniz")
    case 26:
        print("26. Sunucu Bilgisayarın Sınıfını Öğrenme (A/B/C)") 
        Bilgisayar2.sınıf_x()
    case 27:
        print("27. Ana Bilgisayarın Sınıfını Öğrenme (A+/A/B/C)") 
        Bilgisayar3.sınıf_x()
    case 28:
        print("Program Sonlanıyor...")
        break

 print("Mevcut Sunucu Bilgisayar Bilgileri:")
 Bilgisayar2.bilgilerigoster()
