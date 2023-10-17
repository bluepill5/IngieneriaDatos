
if __name__ == '__main__':
    lista = [1, 2, 3, 4]
    iterador = iter(lista)

    print(type(iterador))

    try:
        while True:
            print(iterador.__next__())
    except:
        print('Ya no hay elementos')

class Invertir:
    def __init__(self, cadena):
        self.cadena = cadena
        self.indice = len(cadena)
    
    def __iter__(self):
        return self
    
    def __next__(self):
        if self.indice == 0:
            self.indice = len(self.cadena)
            raise StopIteration
        self.indice = self.indice - 1
        return self.cadena[self.indice]

# from collections import Iterable
cadena_inveertida = Invertir('Hola, mundo')
for caracter in cadena_inveertida:
    print(caracter)

print(list(cadena_inveertida))





