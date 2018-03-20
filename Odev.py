# Programlama-Odev
def kdcHesaplama(x,y,z,t,r):
    kdc=x-(y+z+t+r)
    return kdc
x=int(input("Toplam satış maliyetini giriniz:"))
y=int(input("Hammadde maliyetini giriniz:"))
z=int(input("Bakım ve onarım giderlerini giriniz:"))
t=int(input("Sevkiyat giderlerini giriniz:"))
r=int(input("Satın alınan hizmet giderlerini giriniz:"))
k=kdcHesaplama(x,y,z,t,r)
print("Katma Değer Cironuz:",k)
if (x-(y+z+t+r))>1000:
    print("İşletme katma değer cirosu yüksek.")
elif 500<(x-(y+z+t+r))<999:
    print("İşletme katma değer cirosu normal")
else:
    print("İşletme katma değer cirosu düşük.")


def mcs2016(x,y):
    mcs=x/y
    return mcs
x=int(170)
y=int(50)
m=mcs2016(x,y)
print("2016 Müşterilerle Çalışma Süresi:",m)
def mcs2017(t,r):
    mcs2=t/r
    return mcs2
t=int(220)
r=int(70)
n=mcs2017(t,r)
print("2017 Müşterilerle Çalışma Süresi:",n)
def fark2016_2017(m,n):
    fark=(m)-(n)
    return fark
f=fark2016_2017(m,n)
print("2016-2017 Yılları Farkı:",f)


def gelirIlk6Ay(x,y,z):
    gilk6=(x+y+z)
    return gilk6
x=int(input("Yazılım Geliri:"))
y=int(input("Finansman Geliri:"))
z=int(input("Ürün Satış Geliri:"))
q=gelirIlk6Ay(x,y,z)
print("İlk 6 Ay Geliriniz:",q)
def giderIlk6Ay(p,r,t):
    gidilk6=(p+r+t)
    return gidilk6
p=int(input("Çalışan Maaşları:"))
r=int(input("Kira Gideri:"))
t=int(input("Donanım Maliyeti:"))
w=giderIlk6Ay(p,r,t)
print("İlk & ay gideriniz:",w)
def gelirSon6Ay(a,b,c,d):
    gson6=(a+b+c+d)
    return gson6
a=int(input("Yazılım Geliri:"))
b=int(input("Sponsorluk Geliri:"))
c=int(input("E-Ticaret Geliri:"))
d=int(input("Ürün satış Geliri:"))
h=gelirSon6Ay(a,b,c,d)
print("Son 6 Ay Geliriniz:",h)
def giderSon6Ay(e,f,g):
    gson6=(e+f+g)
    return gson6
e=int(input("Çalışan maaşları:"))
f=int(input("Kira gideri:"))
g=int(input("Bakım Maliyetleri:"))
s=giderSon6Ay(e,f,g)
print("İşletmenin Son 6 Ay gideri:",s)
def ilk6Kar(q,w):
    i6kar=q-w
    return i6kar
u=ilk6Kar(q,w)
print("İlk 6 Ay Karı:",u)
def son6Kar(h,s):
    s6kar=h-s
    return s6kar
o=son6Kar(h,s)
print("Son 6 Ay Karı:",o)
if u-o>5000:
    print("İşletme çok karda.")
elif 1000<u-o<5000:
    print("İşletme karı normal.")
else:
    print("İşletme yeterince karda değil.")


def donemBasiStok(x,y,z):
    global dbasi
    dbasi=x+y+z
    return dbasi
x=int(input("Dönem Başı Koltuk Sayısını Giriniz:"))
y=int(input("Dönem Başı Yatak Sayısını Giriniz:"))
z=int(input("Dönem Başı Dolap Sayısını Giriniz:"))
t=donemBasiStok(x,y,z)
print("Dönem Başı Stoğunuz:",t)
def donemSonuStok(x,y,z):
    dsonu=(x+15)+(y+5)+(z+5)
    return dsonu

r=donemSonuStok(x,y,z)
print("Dönem Sonu Stoğunuz:",r)
def ortalamaStok(t,r):
    ortStok=(t+r)/2
    return ortStok
s=ortalamaStok(t,r)
print("Bir Yıllık Ortalama Stoğunuz:",s)
