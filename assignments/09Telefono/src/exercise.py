def main():
    mens = int(input("Dame el numero de mensajes:"))
    meg = float(input("Dame el numero de megas:"))
    min = int(input("Dame el numero de minutos:"))
    m = ( mens + meg + min) * 0.8
    print("El costo mensual es:$", m)



if __name__ == '__main__':
    main()
