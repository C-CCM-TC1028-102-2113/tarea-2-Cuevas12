def main():
    #escribe tu código abajo de esta línea
    #El mensaje para recibir el dato debe ser **"Dame un número: **"
    #El mensaje para la salida debe ser **"Es positivo, Es negativo ó Es cero **"
    num=int(input("Dame un número: "))
    if num < 0:
        print("Es negativo")
    if num > 0:
        print("Es positivo")
    if num == 0:
         print("Es cero")
    pass

if __name__ == '__main__':
    main()
