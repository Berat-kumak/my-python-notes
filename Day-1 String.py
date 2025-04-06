# print = Herhangi bir şeyi yazdırmak için kullandığımız bir fonksiyondur.

# String ifadeleri tırnak içine yazılır (" "), (' ')

# print('John's home) yanlıştır    print("John's home") doğrudur

# print('John\'s home')  "\"dan sonra gelen karakter stringi bitiren değil alalede bir kesme işareti demektir.

print("""hi
world""")
# Parantez içerisine üç tırnak koyup istediğin satıra boşluklu yazdırabilirsin.

print("Hello\nWorld")
# Parantez içerisine \n vb ifadeler koyma pythonda belli kısayollar ve teknikleri sağlar.
# \n nek kadar koyarsanız okadar boşluk bırakmanızı sağlar.

print("Hi\tWorld")
# \t ifadesindeki "t" tab anlamına gelir ve koyduğunuz birden fazla "\t" ifadesi koyduğunuz miktar kadar satırda boşluk bırakır.

# Bazı verileri bilgisayarın aklında tutması için yapmamız gerekenler. Bu birimlere değişken denir.

mesaj = "Merhaba Dünya"
print(mesaj)

mesaj1 = "Merhaba"
mesaj2 = "Dünya"

print(mesaj1 + " " + mesaj2)
# Bu çift tırnağa boşluk koyarsak python bu boşluğu bir string olarak algılar ve boşluk bırakır.

print(mesaj1[0])
# Python soymaya 0'dan başlar bu yüzden 0 yazdığımızda kelimenin ilk harfini gösterir.

print(mesaj1[-2])
# - koyduğumuzda kelimenin sondan ikinci harfini bize gösterir.

print(mesaj1[0:4])
# Bu ifade ilk yazdığımız sayıyı dahil edip 4'e kadar olduğunu 4'ü dahil etmez. Koyduğun sayıya kadar harfleri göster demektir.

print(mesaj1[::2])
# En başta boşluk bırakmak 0. indeksi aldırır ve sonda 2 olduğu için ikişer ikişer olarak aldırır.

print(mesaj1[::-2])
# - koyarsan tersten yazdırır ve koyduğun sayı kadar atlar.

print(mesaj1.upper())
# (.) ifadesi metod anlamına gelir ve seçtiklerine göre metni değiştirir ve metni tek seferlik değiştirir
# .upper() metodu metnin tamamını büyük harflerle yazdırır.

print(mesaj1.lower())
# .lower() metodunu kullanarak metnin tamamını küçük harflerle yazdırırsın.

print(mesaj1.capitalize())
# .capitalize() ifadesi yazdığın metnin ilk harfini büyültür.

print(mesaj1.startswith("Me"))
# .startswith("") ifadesine yazdığınız şeyin true ya da false olduğunu gösterir. Metnin neyle başladığını gösterir.

print(mesaj1.endswith("a"))
# .endswith("") ifadesine yazdığınız şeyin true ya da false olduğunu gösterir. Metnin neyle bittiğini gösterir.

print(len(mesaj1))
# Bu kavramı çağırınca yazdığımız metnin kaç karakterden oluştuğunu söyler.

print(len(mesaj1 + mesaj2))
# Böyle yaparsak içine yazdığımız metinlerin toplam kaç karakterden oluştuğunu söyler.

print("Merhaba" * 10)
# Bu ifade bir metni istediğimiz kadar yazdırmamızı sağlar.

isim = "Berat"
yas = "19"

print("{} , {} yaşındadır".format(isim, yas))

# ÖZEL KAVRAM
print(f"{isim} {mesaj1} dedi")
