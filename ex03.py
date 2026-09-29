# # Atributos Privado ( __)
class Smartphone:
  def __init__(self, marca, modelo):
    self.marca = marca #Público
    self.__modelo = modelo #Privado
    
  def get_marca(self):
    if self.marca == '':
      return "Marca não foi atribuído!"
    else:
      return self.marca
   
  def set_marca(self, valor):
     if valor == '':
       return 'valor vazio!'
     else:
       self.marca = valor
       return 'marca adicionada!'

##########################
celular1 = Smartphone('Samsung',"S26")

# erro no acesso e modificação direta
print(celular1.marca)
celular1.__modelo = "iPhone 18"
print(celular1.__modelo)