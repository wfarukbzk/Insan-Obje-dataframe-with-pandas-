import pandas as pd

from Insan import Insan
from Issiz import Issiz
from Calisan import Calisan
from MaviYaka import MaviYaka
from BeyazYaka import BeyazYaka

def main():
    insan1 = Insan("12345678910", "Ali", "Yılmaz", 30, "Erkek", "Türk")
    insan2 = Insan("10987654321", "Ayşe", "Demir", 25, "Kadın", "Türk")

    print(insan1)
    print(insan2)

    status_dict1 = {"mavi yaka": 5, "beyaz yaka": 10, "yönetici": 15}
    status_dict2 = {"mavi yaka": 8, "beyaz yaka": 12, "yönetici": 6}
    status_dict3 = {"mavi yaka": 2, "beyaz yaka": 4, "yönetici": 8}

    issiz1 = Issiz("98765432100", "Ahmet", "Kara", 35, "Erkek", "Türk", status_dict1)
    issiz2 = Issiz("10293847560", "Mehmet", "Yılmaz", 40, "Erkek", "Türk", status_dict2)
    issiz3 = Issiz("11223344556", "Zeynep", "Yıldız", 28, "Kadın", "Türk", status_dict3)

    print(issiz1)
    print(issiz2)
    print(issiz3)

    calisan1 = Calisan("12345678910", "Ali", "Yılmaz", 30, "Erkek", "Türk", "teknoloji", 3, 12000)
    calisan2 = Calisan("10987654321", "Ayşe", "Demir", 25, "Kadın", "Türk", "muhasebe", 5, 18000)
    calisan3 = Calisan("19283746560", "Cem", "Öztürk", 35, "Erkek", "Türk", "inşaat", 7, 25000)

    print(calisan1)
    print(calisan2)
    print(calisan3)

    mavi_yaka1 = MaviYaka("12345678910", "Ali", "Yılmaz", 30, "Erkek", "Türk", "teknoloji", 4, 14000, 0.2)
    mavi_yaka2 = MaviYaka("10987654321", "Ayşe", "Demir", 25, "Kadın", "Türk", "muhasebe", 2, 10000, 0.5)
    mavi_yaka3 = MaviYaka("19283746560", "Cem", "Öztürk", 35, "Erkek", "Türk", "inşaat", 6, 20000, 0.3)

    print(mavi_yaka1)
    print(mavi_yaka2)
    print(mavi_yaka3)

    beyaz_yaka1 = BeyazYaka("12345678910", "Ali", "Yılmaz", 30, "Erkek", "Türk", "teknoloji", 4, 14000, 500)
    beyaz_yaka2 = BeyazYaka("10987654321", "Ayşe", "Demir", 25, "Kadın", "Türk", "muhasebe", 2, 10000, 2500)
    beyaz_yaka3 = BeyazYaka("19283746560", "Cem", "Öztürk", 35, "Erkek", "Türk", "inşaat", 6, 20000, 1000)

    print(beyaz_yaka1)
    print(beyaz_yaka2)
    print(beyaz_yaka3)

    # DataFrame Oluşturma
    data = {
        "çalışan, mavi yaka, beyaz yaka": ["Çalışan", "Mavi Yaka", "Beyaz Yaka"],
        "tc_no": ["12345678910", "10987654321", "19283746560"],
        "ad": ["Ali", "Ayşe", "Cem"],
        "soyad": ["Yılmaz", "Demir", "Öztürk"],
        "yas": [30, 25, 35],
        "cinsiyet": ["Erkek", "Kadın", "Erkek"],
        "uyruk": ["Türk", "Türk", "Türk"],
        "sektor": ["teknoloji", "muhasebe", "inşaat"],
        "tecrube": [3, 5, 7],
        "maas": [12000, 18000, 25000],
        "yipranma_payi": [0.2, 0.5, 0.3],
        "tesvik_primi": [0, 2500, 1000]
    }

    df = pd.DataFrame(data)
    df["yeni_maas"] = df.apply(lambda row: calisan1.get_yeni_maas(), axis=1)  # Yeni sütun eklenmesi ve hesaplama

    # a) Gruplama ve Ortalama Hesaplama
    print(df.groupby("sektor")[["tecrube", "maas"]].mean())

    # b) Maaşı 15000TL üzerinde olanların sayısı
    print(df[df["maas"] > 15000].shape[0])

    # c) Yeni Maaşa göre sıralama
    print(df.sort_values(by="maas"))

    # d) Sektorü Yönetici olan ve tecrübesi 3'ten fazla olanlar
    print(df[(df["sektor"] == "Yönetici") & (df["tecrube"] > 3)])

    # e) Yeni Maaşı 10000 TL üzerinde olanlar arasından 2-5 satır arası olanların tc_no ve yeni maas sütunlarını seçme
    print(df[(df["yeni_maas"] > 10000)].iloc[1:5][["tc_no", "yeni_maas"]])

    # f) Yeni Maaşa göre ad, soyad, sektor ve yeni maas sütunlarından yeni bir DataFrame oluşturma
    print(df[["ad", "soyad", "sektor", "yeni_maas"]])


if __name__ == "__main__":
    main()