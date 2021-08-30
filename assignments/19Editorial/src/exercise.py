def main():
    pal = int(input("Dame el numero de palabras:"))
    pag = pal / 475
    pag2 = int(pag)
    if (pag - pag2) > 0:
      pag2 = pag2 + 1
    costo = pag2 * 60 * 0.90

    print("El costo de la publicacion es:$", costo)


if __name__ == '__main__':
    main()
