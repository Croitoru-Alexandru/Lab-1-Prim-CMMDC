def suma(x):
    c = 0
    for i in range(1, x + 1, 1):
        c += i
    return c


def suma_numere_date():
    a = int(input("Introduceti cate numere doriti sa introduceti:"))
    c = 0
    for i in range(0, a, 1):
        b = int(input("Introduceti numarul:"))
        c += b
    return c


def numar_prim(n):
    if n < 2:
        return False
    for i in range(2, n // 2 + 1):
        if n % i == 0:
            return False
    return True


def cmmdc(x, y):
    r = x % y
    while r != 0:
        x = y
        y = r
        r = x % y
    return y


optiune = '''
Introduceti optiunea dumneavoastra: - 'suma' pentru adunarea cifrelor dinaintea numarului dat
                                    - 'suma_date' pentru adunarea numerelor date de dumneavoastra
                                    - 'prim' pentru a afla daca numarul este prim
                                    - 'cmmdc' calculeaza cel mai mare divizor comun a doua numere
                                    - 'stop' oprire program
'''


def main():
    alegere = input(optiune)
    while alegere.lower() != 'stop':
        if alegere.lower() == 'suma':
            numar = int(input("Introduceti numarul:"))
            print(f'Suma numarului pus este: {suma(numar)}')
            break
        elif alegere.lower() == 'suma_date':
            print(f'Suma numerelor puse este: {suma_numere_date()}')
            break
        elif alegere.lower() == 'prim':
            numar = input("Introduceti numarul dumneavoastra: ")
            if numar_prim(int(numar)):
                print("Numarul este prim")
            else:
                print("Numarul nu este prim")
            break
        elif alegere.lower() == 'cmmdc':
            optiune1 = input("Introduceti primul numar ")
            optiune2 = input("Introduceti al doilea numar ")
            print(f"Cel mai mare divizor comun al celor doua numere este {cmmdc(int(optiune1), int(optiune2))}")
            break
        elif alegere.lower() == 'stop':
            break
        else:
            alegere = input(optiune)


if __name__ == '__main__':
    main()
