def ladosTriangulo(a, b, c):
    if (a + b > c) and (a + c > b) and (b + c > a) and a > 0 and b > 0 and c > 0:
        if a == b and b == c and c == b:
            print("Equilatéro")
        elif (a == b and b != c) or (a == c and a != b) or (c == b and a != b):
            print("Isóceles")
        elif a != b and b != c and a != c:
            print("Escaleno")
        else:
            print("Não é válido")
    else:
        print("Não é possível formar um triangulo")

a = input("Digite o primeiro valor: ")
while True:
    if (not a):
        a = input("Digite o primeiro valor: ")
    elif (a):
        break
b = input("Digite o segundo valor: ")
while True:
    if (not b):
        b = input("Digite o segundo valor: ")
    elif (b):
        break
c = input("Digite o terceiro valor: ")
while True:
    if (not c):
        c = input("Digite o terceiro valor: ")
    elif (c):
        break

ladosTriangulo(a, b, c)