
# NUMPY GİRİŞ

Bu döküman numpy giriş seviyesinde bazı özellikleri tanımamızı ve temel olarak numpy'ın bazı işlem ve fonksiyonlarını kısaca anlatır.

## ARRAY OLUŞTURMA


``` python

import numpy as np

tek_boyutlu (vektör)
tek_boyutlu = np.array([1,2,3,4,5,6,7,8,9])

# iki boyutlu (matris)
iki_boyutlu = np.array([
                        [1,2,3,5],
                        [4,5,6, 5],
                        [7,8,9, 5],
                        [10,20,30, 5],
                        [5,2,5, 5]
                                ])

# üç boyutlu (tensor)
üc_boyutlu = np.array([
    [
        [1,2,3,4,5],
        [6,7,8,9,10],
        [1,2,3,4,5]
    ],
    [
        [10,20,30,40,50],
        [60,70,80,90,100],
        [1,2,3,4,5]

    ]
])

```

## NUMPY METOTLARI


```python

def attribute_bul(nmpy_dizi):
  print("numpy dizisi :\n", nmpy_dizi)
  print("boyutu (shape) :", nmpy_dizi.shape) #boyutunu verir örneğin 3 boyutlu için (2,3,5) [iki tane üç sıralı ve beş kolondan oluşan dizi]
  print("uzunluk sayısı [same as 'len'] > (size) :::", nmpy_dizi.size) # toplam kac sayı(rakam) var ise onları döndürür
  print("kaç boyutlu ? :",nmpy_dizi.ndim) #boyutu geri döndürür
  print("kaç bayt yer kaplıyor :",nmpy_dizi.nbytes)
  print("data tipini göster :", nmpy_dizi.dtype)#hepsinin veri tipi aynı olur, örneğin bir tanesi string olursa bunu numpy dönüştürür ve
                                                #hepsini stringe dönüştürür [1, 'a', 4] gibi bir durumda upcasting denilen durum sağlanır
                                                #['1', 'a', '4'] gibi bir dönüşüm sağlanır(veya float olursa floata dönüştürür) 
  print("veri tipini değiştir :", nmpy_dizi.astype(np.float))#array fonksiyonu dtype fonk. ile ve astype methodu ile de değiştirilebilir alternatif olarak 

```

## BAZI YARARLI NUMPY FONKSİYONLARI 

> metotlar ile ilgili birkaç özellik
* BİLGİNİZE: aşşağıdaki kodlarda, yukarıdaki boyut (array/matris) kodları baz alınarak bazı fonksiyonlarda kullanılmıştır

```python

import numpy as np

np.array() # dizi oluşturma (temel dizi oluşturma fonk.)
np.arrange() # python range fonk. gibi neredeysa aynı kullanımı sağlar
np.sqrt() # kök alma işlemi
np.save("filepath/filename.npy", np_opject) # objeyi kayıt eder
np.load("filepath/filename.npy") # objeyi geri çağırır, yükler
np.zeros() # 0`lardan oluşan dizi oluşturur, (2,3,6) gibi shape özelliği verip oluşturulabilir, dtype parametre olarak verilebilir
np.ones() # 1`lardan oluşan dizi oluşturur, (2,3,6) gibi shape özelliği verip oluşturulabilir, dtype parametre olarak verilebilir
np.full((2, 3), 10) # 2 stun 3 kolondan oluşan bi matris oluştur ve 10 değerini hepsine ata
np.empty((5,6)) # 5 carpı 3 matris oluştur ve tamamen keyfi değerler ata
#    |
#    '-----full methodu ile içini istediğin bir değer ile doldurabilirsin np.empty((5,6)).full(3) > üc ile doldurucaktır hepsini

np.eye(4, k=0) # 4 carpı 4 lük diagonal döndürür  [[1 0 0 0]
#                                                  [0 1 0 0]
#                                                  [0 0 1 0]
#                                                  [0 0 0 1]] #k parametresi diagonalin değerini aşşağı veya yukarı ceker
#                                örneğin k = -2 :
#                                                 [[0 0 0 0]
#                                                  [0 0 0 0]
#                                                  [1 0 0 0]
#                                                  [0 1 0 0]]

np.identity() # eye fonk gibi neredeyse aynısı
np.diag([5,4,9,2]) # eye fonksiyonundaki 1 ler yerine dizideki degerler yer değiştirir (k=0  default)
np.linspace(2, 5, 100) # 2 ile 5 arasında 100 tane sayı ver (2 ve 5  dahil). N = 50 (default). 2 ve 5 arasında belli aralıklarla bütün sayıları verir.
                         endpoint = True(default)

np.reshape([0,1,2,3,4,5,6,7,8,9], (2,2)) # 2 carpı 2 matrixlik olarak döndür, aynı zamanda ndarray objesini yeniden şekillendirme özelliği vardır

np.radnom.random((2,3)) # 0 ile 1 arasında (1 dahil değil) rasgele değerler olustur 2 carpı 3 lük matrise koy
np.random.randint(5,15, size=(4,5)) # 5 ile 15 arasında rastgele değerler oluştur ve 4 x 5 lik matrise yerleştir
np.delete(tek_boyutlu_matris, [2, 6, 7]) # matristeki 2, 6 ve 7. indexlerinde bulunan sayıları sil
    |
    '-----np.delete(cift_boyutlu_matris, [0,3], axis=1) # burada axis=1 ise iki boyutlu matrislerde stun(kolonu)u secer ve siler,
                                                          ama axis=1 ise satır(row)u siler. 
np.append(tek_boyut_matrix, [1,2]) # matrixe 1 ve 2 sayılarını en sona ekler
    |
    '-----np.append(iki_boyutlu_matris, [[1,2,3]], axis=0) # satıra eklemek icin axis=0, stuna eklemek icin axis=1, 
                |                                            (2x2lik bir matrise ancak 2 değer eklenebilir)
                '----np.append(iki_byt_mtrs, [[1], [2], [3]], axis=1) # kolon için liste icinde her elemanı liste olarak vermek gerekli
                                                                        (4,4)lük bir matrise 5 eleman eklersen hata döner 
np.insert(tek_byt_mtrs, 2, [10,20]) # matrisin 2. indexine 10 ve 20 değerlerini ekle
    |
    '-----np.insert(cift_byt_matrs, 1, [10,20,30], axis=0) # matrisin 1.satrına [10,20,30] değerlerini ata
                |
                '-----np.insert(matris, 2, [10,20,30], axis=1) > matrisin 2. stun(kolon)una [10,20,30] değerlerini ekleff
np.vstack(x, y) # x matrisi y matrisine dikey (satır olarak) ekle
np.ystack(x, y) # x matrisini y matrisine yatay (stun olarak ekle)
np.shares_memory(x, y) # x ve y aynı kaynağı mı paylaşıyor? (boolean value will be returned)
np.copy(x) # x matrisinin kopyasını al (kaynakları ayır ki biz y de değişiklik yaptığımızda x i etkilemesin)
np.any() # iki ndarrayın kıyaslaması sonucu bütün koşullar doğru ise True döner
np.all() # iki ndarrayın kıyaslaması sonucu en az biri doğru ise True döner

    >set operations (grup işlemleri )
np.intersect1d(x, y) # x'in y ye kesişimini gösterir
np.setdiff1d(x, y) # x'te olan y'de olmayan
np.union1d(x,y) # x ve y matrisinde olan sayıları gösterir, bir sayı her iki kümede var ise tek bir sayı gösterir
                  örnegin x = [1,3,5,6], y = [1,3,6,9]
                  ise, bize dönen sonuc [1,3,5,6,9] olucaktır.
np.in1d(x,y) # x'in elemanı yde var ise true dön yoksa false dön örn:
                                                                    x = [1,2,3], y = [2,6,4]
                                                                    result = [False, True, False]
np.unique(x) # xte tekrar eden sayıları bir sayı olarak gösterir örn:
                                                                    x = [0,1,2,2,1,3,5]
                                                                    result = [0,1,2,3,5]
np.sort(x_matris) # x_matrisini sıralar (tek veya iki veya üç boyut fark etmez sıralar), axis parametresi ile stun veya satıra göre sıralanabilir
                    metot olarak da kullanılabilir. e.g; x_matris.sort
np.array_equal(x,y) # x ve y eşit mi >> boolean

```


## NUMPY SLICE (DİLİMLEME) OPERATORLERİ

```python
matris[2] = 500 > dizideki 2. indexi al ve 500e eşitle 
matris[0][1][3] > liste slice gibi
matris[-1] > son elemanı cek
matris[2, 3] > 2.satırın 3. stununu cek (numpy özel slice)

print(iki_boyutlu[1:4, 1:3]) # > [stunbası:stunsonu, satırbası:satırsonu] (satırsonu ve stunsonu + 1 yap endpoint sayılmıyor)

Not:Fancy indexing;

    TEK BOYUT İÇİN:
        x = np.array([1, 2, 6])
        y = np.array([1,2,3,4,5,6,7,8,9])
        örneğinde 
        print(y[x]) > diye slice edersek bize y'nin [2,3,7] değerini slice edecektir(basitce arrayı slice olarak kullanabiliriz)

      İKİ BOYUT İÇİN:
        x = np.arange(25).reshape(5,5)
        y = np.array([1,3])
        print(x[y, :]) > bu sefer satırların 1den 3e kadar olanını al ve stundan ise hepsini demiş oluruz

Not:boolean indexing

        x = np.arange(10)
        print(x[(x % 2 == 0)]) 


        x = np.random.randint(10, size=10)
        y = np.random.randint(10, size=10)

        print(x)
        print(y)
        bool_index_kıyaslama = x>y
        print(bool_index_kıyaslama)


###fancy ve boolean indexinde orjinal değişmez (otomatik olarak copy oluşturur numpy) ama slice ile orjinali değişir

#genelde makine öğrenmesi için boolean index kullanılır ufak bir örnek vermek gerekir ise

#örn:

x = np.arange(21) #tek boyutlu bir dizi oluşturalım
mask = (x % 4 == 0)#eğer xin elemanlarının 4e bölümünden kalan sıfır ise ture döner.
print(mask)
print(x[mask])#bana x'in mask ile uyuşan elemanlarını ver demiş oluruz (fancy index)
x[mask] = 1 #x in elemanlarından hangisi maska uyuyor ise  hepsine 1 değerini ver
print(x)

```


## ARİTMETİK İŞLEMLER


> Broadcast, iki tane benzemeyen arrayın benzetilip işlem yapılması olarak gecer (element-wise yapar)[eğer hiç benzer yanları yok ise broadcas hatası döner]

broadcast ile ilgili bir görsel;
![Broadcast](broadcast.png)


> element-wise   ve    array-wise olarak iki tür aritmetik işlem vardır;

  * array-wise matrisin içindeki bütün sayıları baz alır
  *  element-wise matrisin içindeki tek boyutta olan sayıları baz alır
 

>> not: axis parametresi birçok fonksiyonda kullanılabiliyor


```python
np.add(x, y) > iki matrisin 0. indexinden son indexe kadar sırayla toplar örn:
                                                                             x = [0,2,3,5]
                                                                             y = [5,4,1,6]
                                                                               işlem sonucu = [5,6,4,11] 'dir
                np.add yerine >>  x_matrisi + y_matrisi <<< kullanılabilir alternatif olarak ("+" operatörü)

np.subtract(x, y) > iki matrisin ckarma sonucu , operatör : "-"
np.multiply(x, y) > iki matrisi carpar, operatörü : "*"
np.divide(x, y) > iki matrisi böler, öperatörü : "/"

print(np.array([5,1,6,7]) + 3) > tüm elemanlara üç ekler. dört işlem için geçerlidir

np.sum(x) > x matrisini topla, metot olarak da kullanılabilir. ve axis belirtilebilir
np.min(x) > min sayı
np.max(x) > max sayı
np.argmin(x) > min sayının indexini döner
np.argmin(x) > max sayının indexini döner
np.mean(x) > x teki sayıların ortalamasını döner
np.median(x) > xtexi medianı döndürür örn:
                                          x = [0,2,5,6,4,1,3,4]
                                          > [0, 1, 2, 3, 4, 4, 5, 6] > medianı ortadakidir. veya cift ise bu örnekteki gibi ortadaki iki sayının ortalamasını verir 
np.std > standart sapma (netten araştır bu askıda kaldı)

```
* 4 işlem harici diğer işlemleri numpy org.kısmından bakabilirsin


## MANTIK OPERATÖRLERİ

not: Mantık operatörlerinde (==, <=, >=, <, >... gibi) liste içindekileri tek tek kıyaslayıp yeni bir boolean array döner



