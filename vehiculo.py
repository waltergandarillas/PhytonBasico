class Vehiculo:
    
    FACTOR_EMISION_GASOLINA=2.196
    FACTOR_EMISION_DIESEL=2.471
    def __init__(self,placa,color,marca,modelo,combustible,km,tanque,AC):
        self.placa=placa
        self.color=color
        self.marca=marca
        self.modelo=modelo
        self.combustible=combustible
        self.km=km
        self.tanque=tanque
        self.AC=AC
        self.encendido=False
        self.litros_consumidos=0

    def encender(self):
        self.encendido=True

    def apagado(self):
        self.encendido=False

    def tocar_bocina(self):
        print("bibibi")

    def frenar(self):
        print("frenando")

    def combustible(self):
        return(tanque)
        
    def mostrar_vehivulo(self):
        print("placa"+self.placa)
        print("color"+self.color)
        print("marca"+self.marca)
        print("modelo"+self.modelo)
        print("combustible"+self.combustible)
        print("km"+str(self.km))
        print("tanque"+ str(self.tanque))
        print("AC"+self.AC)
    
    
    def cargar_combustible(self,litros):
        self.tanque+=litros
        print("Cargando combustible")
    
    def recorrer_distancia(self,distancia):
        variante=self.obtener_variante()
        if self.encendido:                                           
            if distancia<(self.tanque*variante):
                self.km+=distancia
                total_litros=round(distancia/variante,2)
                self.tanque-=total_litros
                

                self.litros_consumidos+=total_litros
                print("Recorriendo{}kilometros".format(distancia))
            else:
                print("No tiene suficiente combustible")
        else:
            print("El  vehiculo esta apagado")
       
    def calcular_CO2(self):
        if self.combustible=="Gasolina":
            return self.FACTOR_EMISION_GASOLINA*self.litros_consumidos
        else:
            return self.FACTOR_EMISION_DIESEL*self.litros_consumidos
            
    def poner_motor(self,motor):
        self.motor=motor

    def obtener_variante(self):
        cilindrada=self.motor.obtener_cilindrada()
        if cilindrada==1000:
            return 12

        elif cilindrada==2000:
            return 10

        else:
            return 8
    def hay_combustible(self,distancia):
        variante=self.obtener_variante
        if not distancia<(variante*tanque):
            return False
        else:
            return True
    def obtener_informe(self):
        informe="\n----------------"
        informe+="\n INFORME FINAL-EMISION CO2"
        informe+="\n----------------"
        informe+="\n Ud esta conduciendo un vehivulo {},modelo {}, color {}".format(self.marca,self.modelos,self.color)
        informe+="\n Ha recorrido un total de {} km de distacia".format(self.km)
        informe+="\n Ha consumido un total de {} litros de {}".format(self.total_litros,self.combustible)
        informe+="\n Eb su tanque tiene {} litros de {}".format(self.tanque,self.combustible)
        informe+="\n Se emitio a la atmosfera un total de {} Kg de CO2".format(round(self.calcular_CO2(),2))
        return informe

        