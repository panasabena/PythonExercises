lista_de_productos=['wireless', 'apparel', 'sports', 'home_improvement', 'beauty',
       'home', 'baby_product', 'pc', 'toy', 'book',
       'personal_care_appliances', 'kitchen', 'lawn_and_garden',
       'pet_products', 'drugstore', 'office_product', 'furniture',
       'electronics', 'automotive', 'shoes', 'jewelry', 'luggage',
       'camera', 'industrial_supplies', 'other', 'musical_instruments',
       'grocery', 'digital_ebook_purchase', 'video_games', 'watch']
##Creando incremental;
def incrementa_elemento(n):
  n[-1]+=1
# Programa principal
numero = [-1]   # No necesita ser global
#for i in range(5):
#   incrementa_elemento(numero)
#   print(numero[-1])
n=-1

class Contador(object):

  def __init__(self, inicial=-1):
    self.numero = inicial

  def siguiente(self):
    self.numero += 1
    return self.numero
cuenta = Contador()

for i in lista_de_productos:
   print(lista_de_productos[cuenta.siguiente()])
#print (lista_de_productos[numero])
