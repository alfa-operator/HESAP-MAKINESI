# BASİT TEMEL İŞLEVLİ HESAP MAKİNESİ
while True :# İLE DÖNGÜYE ALIYORUZ Kİ İŞLEM BİTTİĞİNDE TEKRAR ONAY İSTESİN
    i=input('YAPMAK İSTEDİĞİNİZ İŞLEMİ SEÇİN :\nTOPLAMA İÇİN :+\nÇIKARMA İÇİN  : -\nÇARPMA İÇİN   : x\nBÖLME İÇİN      : /\nSEÇİLEN İŞLEM: ')
    #KULLANICIDAN İŞLEM SEÇMESİNİ İSTİYORUZ VE BU İŞLEMİ DEĞİKENE ATIYORUZ
    ilk_sayi=int(input('birinci sayıyı girin : '))#KULLANICIDAN ILK SAYIYI İSTİYORUZ
    ikinci_sayi=int(input('ikinci sayıyı girin : '))#KULLANICIDAN IKİNCİ SAYIYI İSTİYORUZ
    if i == '+' :#KOŞULLU İFADELER HANGİ İŞLEMİ SEÇERSEK O SATIRDAKİ KOD ÇALIŞIR
        print(f' {ilk_sayi} + {ikinci_sayi} = {ilk_sayi+ikinci_sayi}')# SÜSLÜ PARANTEZ İÇİNE DEĞİŞKEN VEYA YAILMASI İSTENEN İŞLEMİ YAZIYORUZ VEY
    
    elif i == '-' :#6.SATIRDAKİ AÇIKLAMAYA BAKINIZ!
        print(f' {ilk_sayi} - {ikinci_sayi} = {ilk_sayi-ikinci_sayi}')#7.SATIRDAKİ AÇIKLAMAYA BAKINIZ
    
    elif i == '/' :
A ,        print(f' {ilk_sayi} / {ikinci_sayi} = {ilk_sayi/ikinci_sayi}')
    
    elif i == 'x' :
        print(f' {ilk_sayi} x {ikinci_sayi} = {ilk_sayi*ikinci_sayi}')

    onay=input('başka işlem yapmak ister misiniz? :')
    if onay != 'evet' :# EŞİT DEĞİLDİR KOŞULU KULLANILDI YANİ evet DIŞINDAKİ TÜM CEVAPLAR PROGRAMI DÖNGÜYÜ SONLANDIRIR.
        break#evet DIŞINDAKİ KOMUTLAR PROGRAMI DÖNGÜYÜ SONLANDIRIR.
#HANGİ KODUN KOMUTUN NE İŞE YARADIĞINI DAHA İYİ ANLAMAK İÇİN KOD ÜZERİNDE KAFANIZA GÖRE DEĞİŞİKLİK YAPIN
#BOZULSUN BİŞEY OLMAZ  İSTERSENİZ ctrl + a   BASIP TÜMÜNÜ SEÇİN VE ctrl+ c İLE KOPYALAYIN  YENİ DOSYA OLUŞTURUN
    #ctrl + v İLE YAPIŞTIRIN FARKLI İSİMDE TEKRAR KAYDEDİN,YA DA NOT DEFTERİNE YAPIŞTIRIN farklı kaydet İ SEÇİN
    # UZANTIYI .py YAPIN ÖRNEK hesap makinesi.py GİBİ.   YEDEKLEDİĞİNİZE GÖRE KFANIZA GÖRE DÜZENLEYİN KURCALAYIN.
    # SEYİR 7 DEN SELAMLAR ALLAH A EMANET OLUN.
