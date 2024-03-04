
def fact(num):
    if num <= 0:
        return 'No existe el factorial para este número'
    
    if num == 1:
        return 0
    
    factorial =1
    for n in range(1, num+1):
        factorial *= n
    return factorial

def prod(list):
    product = 1
    for num in list:
        product *= num
    return product
        
def calcular(**kwargs):
    for key,value in kwargs.items():
        if 'fact' in key:
            print(f'El factorial de {value} es {fact(value)}')
        elif 'prod' in key:
            print(f'La productoria de {value} es {prod(value)}')

calcular(fact_1 = 5, prod_1 = [4, 6, 7, 4, 3], fact_2 = 6)
calcular(fact_1 = 10)
calcular(fact_1 = 3, prod_1 = [1,2,3,4,5,6,7,8,9,10], fact_2 = 6, fact_3 = 7, fact_4 = 2)
calcular(fact_1 = 0, prod_1 = [3,6,4,2,8], prod_2 = [10,9,8,7,6,5,4,3])



