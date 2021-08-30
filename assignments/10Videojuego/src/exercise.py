def main():
    nuev = int(input("Dame la cantidad de juegos nuevos:"))
    usad = int(input("Dame la cantidad de juegos usados:"))
    t = (nuev * 1000) + (usad * 350)
    print("El total de la compra es:", t)


if __name__ == '__main__':
    main()
