ogrenci={}

while True:
    print("\n\n----- Öğrenci Menü Sistemi -----\n")
    print("1. Öğreci Ekle")
    print("2. Öğreci Sil")
    print("3. Öğreci Bilgilerini Göster")
    print("4. Öğreci Sınav Sonuçları")
    print("5. Çıkış")

    tercih=int(input("Lütfen yapmak istediğiniz işlemi seçin (1-5): "))
    

    if tercih==1:
        
        name=input("Öğrenci Adı: ")
        surname=input("Öğrenci Soyadı: ")
        number=input("Öğrenci No: ")
        sinav1=input("Öğrencinin 1. Sınav Notu: ")
        sinav2=input("Öğrencinin 2. Sınav Notu: ")
        
        ogrenci[number]={
            "Ad":name,
            "Soyad":surname,
            "1. Sınav Sonucu":sinav1,
            "2. Sınav Sonucu":sinav2
        }
        print("Öğrenci başarıyla eklendi.")



    elif tercih==2:
        number = input("Silmek istediğiniz öğrencinin numarasını girin: ")
        if number in ogrenci:
            del ogrenci[number]
            print("Öğrenci başarıyla silindi.")
        else:
            print("Bu numaraya sahip bir öğrenci bulunamadı.")


    elif tercih==3:
        number = input("Bilgilerini görmek istediğiniz öğrencinin numarasını girin: ")
        if number in ogrenci:
            ogrenci_0 = ogrenci[number]
            print(f"Ad: {ogrenci_0['Ad']}")
            print(f"Soyad: {ogrenci_0['Soyad']}")
            print(f"1. Sınav Sonucu: {ogrenci_0['1. Sınav Sonucu']}")
            print(f"2. Sınav Sonucu: {ogrenci_0['2. Sınav Sonucu']}")
        else:
            print("Bu numaraya sahip bir öğrenci bulunamadı.")


    elif tercih==4:
        number = input("Sınac sonuçlarını görmek istediğiniz öğrencinin numarasını girin: ")
        if number in ogrenci:
            ogrenci_0 = ogrenci[number]
            print(f"1. Sınav Sonucu: {ogrenci_0['1. Sınav Sonucu']}")
            print(f"2. Sınav Sonucu: {ogrenci_0['2. Sınav Sonucu']}")
        else:
            print("Bu numaraya sahip bir öğrenci bulunamadı.")


    elif tercih==5:
         print("Programdan çıkılıyor...")
         break

    else:
        print("Geçersiz seçim! Lütfen geçerli bir seçenek seçin.")













