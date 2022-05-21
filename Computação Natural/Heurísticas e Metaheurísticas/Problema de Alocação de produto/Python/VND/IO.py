import csv
import os

class IO:
    
    def __init__(self):
        self.__data = list()
        self.__base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

    def getData(self):
        return self.__data
    
    def getProductsQuantity(self):
        return len(self.__data)

    def load(self, filename):
        path = os.path.join(self.__base_dir, 'VND\\dados\\'+filename)
        with open(path) as csv_file:
            csv_reader = csv.reader(csv_file, delimiter=';')
            for product in csv_reader:
                # product tuple: ['name', 'size', 'price', 'quantity']
                self.__data.append({
                    'name':product[0],
                    'size':float(product[1]),
                    'price':float(product[2]),
                    'quantity': int(product[-1])
                })