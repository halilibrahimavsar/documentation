# PANDAS TUTORIAL

*Bu Dökümantasyon basit ve temel seviye pandas fonksiyon ve metotlarını nasıl kullanmamız gerektiğini açıklar*

* **Nedir ?**

*Veri analizi için geliştirilen en iyi kütüphanelerden biridir.*
*genel olarak numpy aynı verileri kullanır iken pandas çeşitli veriler ile calışabilir.*
*örneğin bir database bilgilerini veya exel verilerinin üzerinde hakimiyet sağlar*


> alttaki bütün kod bloklarında numpy[ufak tefek bazı örneklerde kullanmak icin numpy import ediyoruz] ve pandası import ettiğimizi varsayıyoruz,
> aşşağıdaki gibi;
> ```python
> import pandas as pd
> import numpy as np
> ```


* **pd.DataFrame** oluşturmak
> DataFrame'in kolonları series'lerden oluşur (bu demektir ki data frame'i slice'larsak(dilimlersek) seriesler bize döner.

> Dict keylerini kolon başlığı olarak tanımlar

> 2 boyutlu olarak algılar

örnek;
```python
calısan_isimleri = ["ahmet", "mehmet", "ali"]
calısan_yasları =[23,12,59]
maaslar = [2300,2600,5000]

data_frame = pd.DataFrame({
    "isim" : calısan_isimleri,
    "yas" : calısan_yasları,
    "maaş" : maaslar
})

#python dictionary veri tipi ile neredeyse aynı şekilde dilimleme yapılabilir
print(data_frame)
print()
print(data_frame["isim"]) #isimlerin olduğu kolonu verir
print()
print(data_frame.values) #datayı verir
print()
print(data_frame.index)  #indexlerini verir (key)
```



* **pd.Series** oluşturmak

> series'lerde eğer biz sadece data olarak liste, ndarray, tuple verirsek

> (sıfırdan başlayarak) ototmatik olarak index tanımlar (python enumerate fonksiyonu gibi)

> ama sözlük verirsek sözlükteki key'leri index olarak kullanır

örnek;
```python
liste = list("abcdefg")
tupl = (0,1,2,3,4)
sözlük = {i:j for i, j in zip([1,2,3,4,5], ["a","b","c","d","e"])}
numpy_dizi = np.linspace(0,10, 10, endpoint=False)

print("liste ile :\n", pd.Series(liste))
print()
print("tuple ile :\n", pd.Series(tupl))
print()
print("sözlük ile [indexleri keyden alıyor] :\n", pd.Series(sözlük))
print()
print("numpy ile :\n", pd.Series(numpy_dizi))
```

> seriesler ile mantık operatörleri aritmetik işlemler gibi özellikler kullanılabilir

örnek;
```python
dictionar = {"a":20, "b":50, "c":60, "d":90, "e":100}
obj = pd.Series(dictionar)

obj[obj >= 58]=0
print(obj)

print(obj / 2)

```
> aslında dict ile cok benzerdirler (numpy == python list, pandas == python dict)





