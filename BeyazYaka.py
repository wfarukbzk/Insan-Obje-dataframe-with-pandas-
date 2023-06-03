# BeyazYaka.py
from Calisan import Calisan

class BeyazYaka(Calisan):
    def __init__(self, tc_no, ad, soyad, yas, cinsiyet, uyruk, sektor, tecrube, maas, tesvik_primi):
        super().__init__(tc_no, ad, soyad, yas, cinsiyet, uyruk, sektor, tecrube, maas)
        self.__tesvik_primi = tesvik_primi

    def get_tesvik_primi(self):
        return self.__tesvik_primi

    def set_tesvik_primi(self, tesvik_primi):
        self.__tesvik_primi = tesvik_primi

    def zam_hakki(self):
        if self.get_tecrube() <= 2:
            return self.__tesvik_primi
        elif 2 < self.get_tecrube() <= 4 and self.get_maas() < 15000:
            return (self.get_maas() * 5) + self.__tesvik_primi
        elif self.get_tecrube() > 4 and self.get_maas() < 25000:
            return (self.get_maas() * 4) + self.__tesvik_primi
        else:
            return self.get_maas()

    def get_yeni_maas(self):
        return self.zam_hakki()

    def __str__(self):
        yeni_maas = self.zam_hakki()
        return super().__str__() + f"Tecrübe: {self.get_tecrube()} ay\nYeni Maaş: {yeni_maas}\n"