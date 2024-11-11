def sayi_yazıya_cevir(sayi):
    birler = ["", "bir", "iki", "üç", "dört", "beş", "altı", "yedi", "sekiz", "dokuz"]
    onlar = ["", "on", "yirmi", "otuz", "kırk", "elli", "altmış", "yetmiş", "seksen", "doksan"]
    yuzler = ["", "yüz", "iki yüz", "üç yüz", "dört yüz", "beş yüz", "altı yüz", "yedi yüz", "sekiz yüz", "dokuz yüz"]

    # Negatif sayılar için kontrol
    if sayi < 0:
        return "eksi " + sayi_yazıya_cevir(abs(sayi))

    # Binler ve üzeri için
    elif sayi >= 1000:
        binler = sayi // 1000
        kalan = sayi % 1000
        return sayi_yazıya_cevir(binler) + " bin" + (" " + sayi_yazıya_cevir(kalan) if kalan > 0 else "")

    # Yüzler için
    elif sayi >= 100:
        yuzler_sayi = sayi // 100
        kalan = sayi % 100
        return yuzler[yuzler_sayi] + (" " + sayi_yazıya_cevir(kalan) if kalan > 0 else "")

    # Onlar ve birler için
    elif sayi >= 10:
        onlar_sayi = sayi // 10
        kalan = sayi % 10
        return onlar[onlar_sayi] + (" " + birler[kalan] if kalan > 0 else "")

    # Birler için
    else:
        return birler[sayi]

# Kullanıcıdan sayıyı al
sayi = int(input("Bir sayı girin: "))

# Sayıyı yazıya çevir ve yazdır
print(sayi_yazıya_cevir(sayi))
