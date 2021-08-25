def main():
    edad = int(input("Ingresa tu edad: "))
    # Escribe el código adecuado para completar el programa
    # Para pedir el dato de la idetificación oficial emplea este mensaje:
    # "¿Tienes identificación oficial? (s/n): "

    if edad > 0 and edad < 18:
        print('No cumples requisitos')
        exit()

    elif edad < 0:
        print('Respuesta incorrecta')
        exit()

    iden = input('¿Tienes identificación oficial? (s/n): ')

    if iden != 's' and iden != 'n':
        print('Respuesta incorrecta')
    
    elif edad >= 18:
        if iden == 'n':
            print('No cumples requisitos')
        elif iden == 's':
            print('Trámite de licencia concedido')
    pass


if __name__ == '__main__':
    main()
