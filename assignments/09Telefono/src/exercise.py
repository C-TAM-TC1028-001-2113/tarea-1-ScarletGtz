def main():
    mens = int(input("Dame el número de mensajes:"))
    meg = float(input("Dame el número de megas:"))
    min = int(input("Dame el número de minutos:"))
    m = ( mens + meg + min) * 0.8
    print("El costo mensual es:", m)



if __name__ == '__main__':
    main()
