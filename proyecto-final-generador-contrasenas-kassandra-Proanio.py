import random
import string

def solicitar_longitud():
    while True:
        try:
            longitud = int(input("Ingrese la longitud de la contraseña (entre 8 y 12 caracteres): "))
            if 8 <= longitud <= 12:
                return longitud
            else:
                print("Debe tener entre 8 y 12 caracteres.")
        except ValueError:
            print("Por favor, ingrese un número válido.")

def evaluar_seguridad(contraseña):
    longitud = len(contraseña)
    tiene_mayus = any(c.isupper() for c in contraseña)
    tiene_minus = any(c.islower() for c in contraseña)
    tiene_digitos = any(c.isdigit() for c in contraseña)
    tiene_simbolos = any(c in '@#$%*' for c in contraseña)

    puntaje = sum([tiene_mayus, tiene_minus, tiene_digitos, tiene_simbolos])

    if longitud >= 10 and puntaje >= 3:
        return "Fuerte"
    elif longitud >= 8 and puntaje >= 2:
        return "Media"
    else:
        return "Débil"

def yo_ingreso_contraseña():
    longitud = solicitar_longitud()
    contraseña = input(f"Ingrese su contraseña de {longitud} caracteres: ")
    while len(contraseña) != longitud:
        print("La contraseña no cumple con la longitud especificada.")
        contraseña = input(f"Ingrese su contraseña de {longitud} caracteres: ")
    return contraseña

def contraseña_facil_de_decir():
    longitud = solicitar_longitud()
    conjunto = string.ascii_letters
    contraseña = ''.join(random.choice(conjunto) for _ in range(longitud))
    return contraseña

def contraseña_facil_de_leer():
    longitud = solicitar_longitud()
    incluir_numeros = input("¿Desea añadir números? (S/N): ").strip().lower() == 's'
    incluir_simbolos = input("¿Desea añadir símbolos? (S/N): ").strip().lower() == 's'

    letras_legibles = "abcdefghjkmnpqrstuvwxyzABCDEFGHJKMNPQRSTUVWXYZ"
    numeros_legibles = "23456789"
    simbolos_legibles = "@#$%*"

    conjunto = letras_legibles  # siempre están
    if incluir_numeros:
        conjunto += numeros_legibles
    if incluir_simbolos:
        conjunto += simbolos_legibles

    if not conjunto:
        print("No hay caracteres válidos para generar la contraseña.")
        return contraseña_facil_de_leer()

    contraseña = ''.join(random.choice(conjunto) for _ in range(longitud))
    return contraseña

def contraseña_todos_los_caracteres():
    longitud = solicitar_longitud()
    incluir_mayus = input("¿Incluir mayúsculas? (S/N): ").strip().lower() == 's'
    incluir_minus = input("¿Incluir minúsculas? (S/N): ").strip().lower() == 's'
    incluir_num = input("¿Incluir números? (S/N): ").strip().lower() == 's'
    incluir_simbolos = input("¿Incluir símbolos? (S/N): ").strip().lower() == 's'

    if sum([incluir_mayus, incluir_minus, incluir_num, incluir_simbolos]) < 3:
        print("Debe escoger al menos 3 de las combinaciones.")
        return contraseña_todos_los_caracteres()

    conjunto = ''
    if incluir_mayus: conjunto += string.ascii_uppercase
    if incluir_minus: conjunto += string.ascii_lowercase
    if incluir_num: conjunto += string.digits
    if incluir_simbolos: conjunto += '@#$%*'

    contraseña = ''.join(random.choice(conjunto) for _ in range(longitud))
    return contraseña

def menu_generar_contraseña():
    print("\n--- OPCIONES DE GENERACIÓN ---")
    print("1. Yo genero mi propia contraseña")
    print("2. Contraseña automática fácil de decir")
    print("3. Contraseña automática fácil de leer")
    print("4. Todos los caracteres")
    opcion = input("Seleccione una opción (1-4): ").strip()

    if opcion == "1":
        contraseña = yo_ingreso_contraseña()
    elif opcion == "2":
        contraseña = contraseña_facil_de_decir()
    elif opcion == "3":
        contraseña = contraseña_facil_de_leer()
    elif opcion == "4":
        contraseña = contraseña_todos_los_caracteres()
    else:
        print("Opción inválida.")
        return

    print("Contraseña generada:", contraseña)
    print("Nivel de seguridad:", evaluar_seguridad(contraseña))

def mostrar_reglas():
    print("""
REGLAS DEL GENERADOR DE CONTRASEÑAS:
- Las contraseñas deben tener entre 8 y 12 caracteres.
- Puede incluir letras mayúsculas, minúsculas, números y símbolos.
- Se recomienda combinar al menos tres tipos de caracteres para mayor seguridad.
""")

def menu_principal():
    while True:
        print("\n--- MENÚ PRINCIPAL ---")
        print("1. Generar contraseña")
        print("2. Reglas del generador de contraseña")
        print("3. Salir")
        opcion = input("Seleccione una opción (1-3): ").strip()
        if opcion == "1":
            menu_generar_contraseña()
        elif opcion == "2":
            mostrar_reglas()
        elif opcion == "3":
            print("Gracias por usar el generador. ¡Hasta pronto!")
            break
        else:
            print("Opción inválida.")

# Iniciar el programa
menu_principal()