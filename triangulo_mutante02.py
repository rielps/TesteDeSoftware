def ladosTriangulo(a, b, c):
    try:
        a_num = float(a)
        b_num = float(b)
        c_num = float(c)
    except Exception:
        return "Não é válido"

    a = a_num
    b = b_num
    c = c_num

    if (a + b > c) and (a - c < b) and (b + c > a) and a > 0 and b > 0 and c > 0:
        if a == b and b == c:
            return "Equilátero"
        elif (a == b and b != c) or (a == c and a != b) or (c == b and a != b):
            return "Isóceles"
        elif a != b and b != c and a != c:
            return "Escaleno"
        else:
            return "Não é válido"
    else:
        return "Não é possível formar um triangulo"


def _main():
    a = input("Digite o primeiro valor: ")
    while not a:
        a = input("Digite o primeiro valor: ")
    b = input("Digite o segundo valor: ")
    while not b:
        b = input("Digite o segundo valor: ")
    c = input("Digite o terceiro valor: ")
    while not c:
        c = input("Digite o terceiro valor: ")

    print(ladosTriangulo(a, b, c))


if __name__ == "__main__":
    _main()