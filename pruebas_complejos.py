import unittest


class Complex():

    def __init__(self, real=0, img=0):
        """Real y img deben ser reales"""
        self.real = real
        self.img = img
    
    def mostrarComplex(self):
        print('({} , {}i)'.format(self.real, self.img))

class MathComplex():
    def __init__(self):
        pass

    @classmethod       # metodos staticos
    def sumar(self, c1 : Complex, c2:Complex):
        c3 = Complex(c1.real + c2.real, c1.img + c2.img)
        return c3

    @classmethod       # metodos staticos
    def resta(self, c1 : Complex, c2:Complex):
        c3 = Complex(c1.real - c2.real, c1.img - c2.img)
        return c3

    def multiplicar(self, c1 : Complex, c2:Complex):
        c3 = Complex()
        c3.real = c1.real * c2.real + c1.img * c2.img
        c3.img = c1.real * c2.img + c1.img * c2.real
        return c3
    
    def dividir(self, c1 : Complex, c2:Complex):
        c3 = Complex()
        c3.real = c1.real / c2.real
        c3.img = c1.img / c2.img
        return c3
    

class TestComplexMethods(unittest.TestCase):
    def test_setup(self):
        print('hola')
        pass

    #@classmethod
    def test_suma(self):
        esp ,cal = MathComplex.sumar(Complex(1,2), Complex(3,4)), Complex(4,6)
        self.assertEqual(esp.real, cal.real)
        self.assertEqual(esp.img, cal.img)
  
    #def test_resta(self):
        
if __name__ == "__main__":
    unittest.main()     # ejecuta todos los metodos de unitesst que tengan 'test_-----()'
    