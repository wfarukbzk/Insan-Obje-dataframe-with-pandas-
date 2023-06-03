from Insan import Insan

class Issiz(Insan):
    def __init__(self, tc_no, ad, soyad, yas, cinsiyet, uyruk, status_dict):
        super().__init__(tc_no, ad, soyad, yas, cinsiyet, uyruk)
        self.__status_dict = status_dict

    def get_status_dict(self):
        return self.__status_dict

    def set_status_dict(self, status_dict):
        self.__status_dict = status_dict

    def statu_bul(self):
        max_status = max(self.__status_dict, key=self.__status_dict.get)
        return max_status

    def __str__(self):
        max_status = self.statu_bul()
        return super().__str__() + f"En Uygun Statü: {max_status}\n"