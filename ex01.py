# Atributos públicos

class Smartphone:
  def __init__(self, marca, modelo):
    self.marca = marca #Público
    self.modelo = modelo
    
##########################
celular1 = Smartphone('Samsung',"S26")

# acesso e modificação direta
print(celular1.marca)
celular1.modelo = "iPhone 18"
print(celular1.modelo)