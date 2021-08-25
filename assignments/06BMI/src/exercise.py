def main():
    # Escribe el código adecuado para completar el programa
    peso = float(input("Peso en kg: "))
    altura = float(input("Altura en m: "))
 
    if peso <= 0 or altura <= 0:
        print('Revisa tus datos, alguno de ellos es erróneo')
        exit()

    IMC = peso / (altura ** 2)

    if IMC < 20:
        print('PESO BAJO')
         
    elif IMC >= 20 and IMC < 25:
        print('NORMAL')

    elif IMC >= 25 and IMC < 30:
        print('SOBREPESO')
        
    elif IMC >= 30 and IMC < 40:
        print('OBESIDAD')

    elif IMC >= 40:
        print('OBESIDAD MORBIDA')
    pass

if __name__ == '__main__':
    main()
