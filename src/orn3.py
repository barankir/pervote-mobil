cevap="e"

while cevap=="e":
  isim=input("Öğrencinin Adı:")
  not1=int(input("1.sınav notu:"))
  not2=int(input("2.sınav notu:"))
  ortalama=(not1+not2)/2
  print(ortalama)

  if ortalama>=70:
    print("Geçtiniz")
  else:
    print("Kaldınız")

  cevap=input("Tekrar Ortalama Hesaplamak İster misiniz?  [e]vet--[h]ayır ==>>")












