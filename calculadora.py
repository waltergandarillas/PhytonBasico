class Calculadora():
    def __init__ (self,numero_1,numero_2):
        self.numero_1=numero_1
        self.numero_2=numero_2

    def sumar(self):
        try:
            s=self.numero_1+self.numero_2
            print("La suma de {} y {} es:{}".format(self.numero_1,self.numero_2,s))
        except TypeError:
            print("Tipo de dato debe ser numerico")
        except:
            print("Error al dividir")

    def restar(self):
        try:
            r=self.numero_1-self.numero_2
            print("La restar de {} y {} es:{}".format(self.numero_1,self.numero_2,r))
        except TypeError:
            print("Tipo de dato debe ser numerico")
        except:
            print("Error al dividir")

    def multiplicar(self):
        try:
            m=self.numero_1*self.numero_2
            print("La multiplicacion de {} y {} es:{}".format(self.numero_1,self.numero_2,m))
        except TypeError:
            print("Tipo de dato debe ser numerico")
        except:
            print("Error al dividir")

    def dividir(self):
        try:
            d=self.numero_1/self.numero_2
            print("La division de {} y {} es:{}".format(self.numero_1,self.numero_2,d))
        except ZeroDivisionError:
            print("No se puede divider entre 0")
        except TypeError:
            print("Tipo de dato debe ser numerico")
        except:
            print("Error al dividir")

    def sacar_exponente(self):
        try:    
            exponente=self.numero_1**self.numero_2
            print("el exponente de {} y {} es:{}".format(self.numero_1,self.numero_2,exponente))
        except TypeError:
            print("Tipo de dato debe ser numerico")
        except:
            print("Error al dividir")