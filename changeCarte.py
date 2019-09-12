import unittest
import math as m

#----------------------------------------
#           CODIGO DE CLASES
#----------------------------------------

class Cartesiano():
    def __init__(self, x=0, y=0):
        # Redondeamos a 4 cifras
        self.x = round(x,4)
        self.y = round(y,4)
    
    def mostrarCartesiano(self):
        print('({} , {}i)'.format(self.x, self.y))

class Polar():
    def __init__(self, r=0, ang=0):
        # Redondeamos a 4 cifras
        self.r = round(r,4)
        self.ang = round(ang,4)
    
    def mostrarPolar(self):
        print('({} , {}i)'.format(self.r, self.ang))

class MathChange():
    def __init__(self):
        pass
        
    @classmethod       # metodos staticos
    def polar_to_C(self, p : Polar):
        c = Cartesiano(x = p.r*m.cos(p.ang), y = p.r*m.sin(p.ang))
        return c

    @classmethod       # metodos staticos
    def c_to_Polar(self, c:Cartesiano):
        p = Polar(r = m.hypot(c.x, c.y), ang = m.atan2(c.y, c.x))
        return p

#-------------------------------------------------------
#             CODIGO DE UNIDAD DE PRUEBAS
#-------------------------------------------------------

class TestComplexMethods(unittest.TestCase):
    
    def test_to_C(self):
        
        polar = Polar(2.0 ,m.pi/2)
        esp_c ,cal_c = MathChange.polar_to_C(polar) , Cartesiano(0.0, 2.0)
        
        #El radio debe diferente de 0
        self.assertNotEqual(polar.r, 0.0)

        self.assertEqual(esp_c.x, cal_c.x)
        self.assertEqual(esp_c.y, cal_c.y)
        
    def test_to_Polar(self):

        cart = Cartesiano(-2.0 ,0.0)
        esp_p ,cal_p = MathChange.c_to_Polar(cart) , Polar(2.0, m.pi)
        
        # El componente x debe diferente de 0
        if (cart.x == 0 and cart.y ==0):
            self.assertNotEqual(cart.x, 0.0)
            self.assertNotEqual(cart.y, 0.0)
        
        # Verificar si los valores son correctos
        self.assertEqual(esp_p.r, cal_p.r)
        self.assertEqual(esp_p.ang, cal_p.ang)
    

if __name__ == "__main__":
    unittest.main()     # ejecuta todos los metodos de unitesst que tengan 'test_-----()'
    