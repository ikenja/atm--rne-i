print('''
******************************
Atm Makinesine Hoşgeldiniz.
İşlemler;
1. Bakiye Sorgulama
2. Para Yatırma
3. Para Çekme

Programdan çıkmak için Q ya basın.

******************************
''')


bakiye = 1000

while True:
  işlem = input("Bir İşlem Seçiniz: ")

  if(işlem == "q"):
    print("İşleminiz Sonlandı")
    break

  elif işlem == "1" :
     print(f"Bakiyeniz {bakiye} tl dir.")

  elif işlem == "2" :
      miktar = int(input("Miktarı Giriniz : "))
      bakiye += miktar
  elif işlem == "3" :
      miktar = int(input("Çekilecek Miktarı Giriniz : "))
      if (bakiye-miktar < 0):
       print("İşlem Geçersiz")
      continue
      bakiye -= miktar
  else:
    print ("Geçersiz Tuşladınız")

      