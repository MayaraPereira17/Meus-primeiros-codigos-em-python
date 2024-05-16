print("Vamos Calcular a area de um triangulo!!")
def area_triangulo(base, altura):
      area = base * altura/2
      return (area)

def area_circulo(r):
    areaCirculo = 3.14* r*r 
    return(areaCirculo)
    
base= int (input("Digite o valor da base: "))
altura=int (input("Digite o valor da altura: "))
print(f'A area do triangulo é :{area_triangulo(base,altura)}')
print("\nAgora vamos calcular a circunferência de um circulo, vamos la!! ")

r= float (input(" Digite o raio do circulo: "))
print(f'A circunferência do circulo é de :{area_circulo(r)}')
#print (area_circulo(r))10
