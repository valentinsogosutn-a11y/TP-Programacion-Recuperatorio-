def validar_es_numero(cadena: str) -> bool:
    """Verifica manualmente si una cadena contiene solo digitos (algoritmia propia)."""
    if len(cadena) == 0:
        return False
    
    es_numerico = True
    for i in range(len(cadena)):
        # Comparamos el caracter segun su valor ASCII o directamente
        if cadena[i] < '0' or cadena[i] > '9':
            es_numerico = False
            break # Detenemos el bucle si encontramos algo que no es numero
    return es_numerico


def pedir_entero_positivo(mensaje: str) -> int:
    """Pide un entero mayor a cero usando validacion manual."""
    valido = False
    while not valido:
        entrada = input(mensaje)
        if validar_es_numero(entrada):
            numero = int(entrada)
            if numero > 0:
                return numero
            else:
                print("Error: no se permiten numeros negativos ni el cero")
        else:
            print("Error: tenes que ingresar un numero entero")


def pedir_opcion_menu() -> int:
    """Pide una opcion del menu entre 0 y 12 con validacion manual."""
    while True:
        entrada = input("Ingrese una opcion: ")
        if validar_es_numero(entrada):
            opcion = int(entrada)
            if opcion >= 0 and opcion <= 12:
                return opcion
            else:
                print("Error: la opcion debe estar entre 0 y 12")
        else:
            print("Error: tenes que ingresar un numero")