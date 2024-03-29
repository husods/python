# %% pandas
"""
- hızlı güçlü ve esnek
"""

import pandas as pd

# sözlük oluştur
dictionary = {"isim" : ["ali","veli","kenan","murat","ayse","hilal"],
              "yas"  : [15,16,17,33,45,66],
              "maas" : [100,150,240,350,110,220]}

veri = pd.DataFrame(dictionary)
print(veri)

# ilk 5 satır
print(veri.head())
print(veri.columns)
# veri bilgisi
print(veri.info())

# istatistiksel özellikler
print(veri.describe())

# yas sütunu
print(veri["yas"])

# sütun eklemek
veri["sehir"] = ["Ankara","İstanbul","Konya","İzmir","Bursa","Antalya"]
print(veri)

# yas sütunu
print(veri.loc[:,"yas"])

# yas sütunu ve 3 satır
print(veri.loc[:2,"yas"])

# yas ve şehir arası sütunu ve 3 satır
print(veri.loc[:2,"yas":"sehir"])

# yas ve şehir arası sütunu ve 3 satır
print(veri.loc[:2,["yas","isim"]])

# satırları tersten yazdır.
print(veri.loc[::-1,:])

# yas sütunu with iloc
print(veri.iloc[:,1])

# ilk 3 satır ve yaş ve isim
print(veri.iloc[:3,[0,1]])

# filtreleme
dictionary = {"isim" : ["ali","veli","kenan","murat","ayse","hilal"],
              "yas"  : [15,16,17,33,45,66],
              "sehir": ["İzmir","Ankara","Konya","Ankara","Ankara","Antalya"]}

veri = pd.DataFrame(dictionary)
print(veri)

# ilk olarak yaşa göre bir filtre yas > 22
filtre1 = veri.yas > 22
filtrelenmis_veri = veri[filtre1]
print(filtrelenmis_veri)

# ortalama yas 
ortalama_yas = veri.yas.mean()

veri["YAS_GRUBU"] = ["kucuk" if ortalama_yas > i else "buyuk" for i in veri.yas]
print(veri)

# birleştirme
sozluk1 = {"isim": ["ali","veli","kenan"],
              "yas" : [15,16,17],
              "sehir": ["İzmir","Ankara","Konya"]} 
veri1 = pd.DataFrame(sozluk1)

# veri seti 2 oluşturalım
sozluk2 = {"isim": ["murat","ayse","hilal"],
              "yas" : [33,45,66],
              "sehir": ["Ankara","Ankara","Antalya"]} 
veri2 = pd.DataFrame(sozluk2)

# dikey
veri_dikey = pd.concat([veri1, veri2], axis = 0)

# yatay
veri_yatay = pd.concat([veri1, veri2], axis = 1)
