#Ouestion 1

"""Verilen string ifadenin tüm harflerini büyük harfe çeviriniz. Virgül ve nokta yerine space koyunuz,
kelime kelime ayırınız."""

text="The goal is to turn data into information,and into insight. "
text_new=text.upper().replace(","," ").replace("."," ").split(" ")

print(text_new)

#Question2
"""
Verilen listeye aşağıdaki adımları uygulayınız.
Adım 1: Verilen listenin eleman sayısına bakınız.
Adım 2: Sıfırıncı ve onuncu indeksteki elemanları çağırınız.
Adım 3: Verilen liste üzerinden ["D", "A", "T", "A"] listesi oluşturunuz.
Adım 4: Sekizinci indeksteki elemanı siliniz.
Adım 5: Yeni bir eleman ekleyiniz.
Adım 6: Sekizinci indekse "N" elemanını tekrar ekleyiniz.
"""
lst=["D","A","T","A","S","C","I","E","N","C","E"]
#1
eleman_sayisi=len(lst)
print(eleman_sayisi)
#2
sifirinci_eleman=lst[0]
onuncu_eleman=lst[10]
# Sonuçları yazdıralım
print("Sıfırıncı indeksteki eleman:", sifirinci_eleman)
print("Onuncu indeksteki eleman:", onuncu_eleman)
#3
data=lst[0:4]
print(data)

#4
del lst[8]
print(lst)
#5
lst.append("e")
print(lst)

#6
lst.insert(8,"N")
print(lst)

#question5
"""
:Argüman olarak bir liste alan, listenin içerisindeki tek ve çift sayıları ayrı listelere atayan ve bu listeleri
return eden fonksiyon yazınız.
"""
l=[2,13,18,93,22]
even_list=[]
odd_list=[]
def func():
    for number in l:
        if number%2==0:
            even_list.append(number)
         else:
            odd_list.append(number)
func()
print(even_list)
print(odd_list)

#6
"""
Aşağıda verilen listede mühendislik ve tıp fakülterinde dereceye giren öğrencilerin isimleri
bulunmaktadır. Sırasıyla ilk üç öğrenci mühendislik fakültesinin başarı sırasını temsil ederken son üç öğrenci de
tıp fakültesi öğrenci sırasına aittir. Enumarate kullanarak öğrenci derecelerini fakülte özelinde yazdırınız.
"""