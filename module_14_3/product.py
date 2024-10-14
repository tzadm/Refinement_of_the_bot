from path import *

class Product:
    product_list = []
    def __init__(self, number, img_path):
        self.number = number
        self.img = open(img_path, 'rb')
        self.product_list.append(self)


    def __str__(self):
        return f'Название: Product{self.number}| Описание: описание {self.number} | Цена: {self.number * 100}'


product1 = Product(1, pict_1)
product2 = Product(2, pict_2)
product3 = Product(3, pict_3)
product4 = Product(4, pict_4)



