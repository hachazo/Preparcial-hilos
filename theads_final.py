from threading import Thread
import time
import random

class Multiplicador(Thread):
    def __init__(self, a, b) -> None:
        super().__init__()
        self._a = a
        self._b = b
        self._resultado = 0
        self._tiempo = 0
    
    def run(self):
        self._tiempo = random.randint(0,9)
        time.sleep(self._tiempo)
        self._resultado = self._a * self._b
        print(f"{self._a} * {self._b} : {self._resultado} (Realizada en: {self._tiempo} segundos)")
    
    def getResultado(self):
        return self._resultado
    
def main():
    
    m1 = Multiplicador(10,2)
    m2 = Multiplicador(m1.getResultado(),3)
    m3 = Multiplicador(m2.getResultado(),4)
    
    m1.start()
    m1.join()
    m2.start()
    m2.join()
    m3.start()
    m3.join()

if __name__ == '__main__':
    main()