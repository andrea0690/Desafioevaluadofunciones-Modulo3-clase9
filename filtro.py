
import sys
print(len(sys.argv), sys.argv)

umbral = int(sys.argv[1])
operador = 'mayor'


if len(sys.argv) == 3:
    operador = sys.argv[2] 

precios = {
    'Notebook': 700000,
    'Teclado': 25000,
    'Mouse': 12000,
    'Monitor': 250000,
    'Escritorio': 135000,
    'Tarjeta de Video': 1500000
 }

def filtrar(precios, umbral):
    if operador == 'menor':
        return ', '.join([k for k,v in precios.items() if v < umbral])
    else:
        return ', '.join([k for k,v in precios.items() if v > umbral])


if operador not in ['mayor', 'menor']:
    print('Lo sentimos, no es una operación válida')
else:
    result = filtrar(precios,umbral)
    print(f'Los productos {operador}es al umbral son:', result)
