class Car(object):
 
    def factory(type):
        if type == "CarroDeCarreras": 
            return CDC()
        elif type == "TransportePublico": 
            return TP()
        elif type == "CarroParticular":
            return CP()
        
        assert 0, "No se pudo crear el carro: " + type
 
    factory = staticmethod(factory)
 
class CDC(Car):
    def drive(self): print("Manejando carro de carreras")
 
class TP(Car):
    def drive(self): print("Manejando transporte publico")
 
class CP(Car):
    def drive(self): print("Manejando carro particular")
    
# Crear objeto usando el factory method
obj = Car.factory("CarroParticular")
obj.drive()
obj = Car.factory("CarroDeCarreras")
obj.drive()
obj = Car.factory("TransportePublico")
obj.drive()
obj = Car.factory("OtroCarro")
obj.drive()
#obj = Car.factory("OtroCarro")
#obj.drive()