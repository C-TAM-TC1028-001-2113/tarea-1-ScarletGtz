def main():
    smes = float(input("Dame el saldo del mes anterior:"))
    ing = float(input("Dame los ingresos:"))
    egr = float(input("Dame los egresos:"))
    nchec = int(input("Dame el número de cheques:"))
    saldo = ( smes + ing - egr - (nchec * 13) ) * (1 - 0.075)
    print("El saldo final de la cuenta es:", saldo)

if __name__ == '__main__':
    main()
