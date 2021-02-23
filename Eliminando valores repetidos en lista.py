lista_de_productos=['wireless', 'apparel', 'sports', 'home_improvement', 'beauty',
       'home', 'baby_product', 'pc', 'toy', 'book',
       'personal_care_appliances', 'kitchen', 'lawn_and_garden',
       'pet_products', 'drugstore', 'office_product', 'furniture',
       'electronics', 'automotive', 'shoes', 'jewelry', 'luggage',
       'camera', 'industrial_supplies', 'other', 'musical_instruments',
       'grocery', 'digital_ebook_purchase', 'video_games', 'watch']
print('Largo de lista inicial: ',len(lista_de_productos))
print("La lista inicial es:\n",lista_de_productos)


comentadas=['wireless','lawn_and_garden',
            'electronics','book','digital_ebook_purchase',
            'luggage','musical_instruments','video_games']

print('Largo de lista inicial: ',len(comentadas))
print('La lista con elementos que contiene la inicial es:\n',comentadas)
#for i in lista_de_productos:
#    for j in comentadas:
#        if j==i:
#            lista_de_productos.remove(j)
for j in comentadas:
    for i in lista_de_productos:
        if j==i:
            lista_de_productos.remove(j)
print('Largo de la nueva lista: ',len(lista_de_productos))
print('La lista nueva es:\n',lista_de_productos)

