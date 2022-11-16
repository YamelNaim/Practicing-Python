Precio_final = 0
Procesador = """
Micro Procesadores:
1 = Intel i5    $700
2 = Intel i7    $800
3 = Intel i9    $900
"""
print(Procesador)
El_proce= int(input('Elija una opcion: '))

if (El_proce== 1):
    Precio_final += 700
elif (El_proce==2):
    Precio_final += 800
elif Precio_final==3:
    Precio_final += 900
else:
    print('ERROR')
    print('Vuelva a elegir: ')
    El_proce= int(input('Elija una opcion: '))
    
Ram = """
Memoria RAM:
1 = 8GB RAM     $100
2 = 16GB RAM    $200
3 = 32GB RAM    $300 
"""
print(Ram)
El_ram= int(input('Elija una memoria RAM: '))

if El_ram==1:
    Precio_final += 100
elif El_ram==2:
    Precio_final += 200
elif El_ram==3:
    Precio_final += 300
else:
    print('ERROR')
    print('Vuelva a elegir: ')
    El_ram= int(input('Elija una memoria RAM: '))
    
disco_duro = """
1= 500GB        Gratis
2= 1TB          $300 
"""
print(disco_duro)
El_disco_duro= int(input('Elija un disco duro: '))

if El_disco_duro==1:
    Precio_final += 0
elif El_disco_duro==2:
    Precio_final +=300
else:
    print('ERROR')
    print('Vuelva a elegir: ')
    El_disco_duro= int(input('Elija un disco duro: '))

print('Total:   $'+str(Precio_final))




