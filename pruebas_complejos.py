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

    def sumar(self, c1 : Complex, c2:Complex):
        c3 = Complex(c1.real + c2.real, c1.img + c2.img)
        return c3
    
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
    
    def test_suma(self, cal:Complex, esp: Complex):
        self.assertEqual(esp.real, cal.real)
        self.assertEqual(esp.img, cal.img)
 
        
if __name__ == "__main__":
    c1 = Complex(1,2)
    c2 = Complex(3,4)
    mahtComplex = MathComplex()
    c_esp = mahtComplex.sumar(c1, c2)
    c_esp.mostrarComplex()
    c_cal = Complex(4,5)

    test = TestComplexMethods()
    test.test_suma(c_esp, c_cal)
