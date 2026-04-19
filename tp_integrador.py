# Ejercicio 1 – Caja del Kiosco

nombre = input("Ingrese el nombre del cliente: ")
while nombre == "" or not nombre.isalpha():
    print("Error: ingrese solo letras.")
    nombre = input("Ingrese el nombre del cliente: ")

cantidad = input("Cantidad de productos: ")
while not cantidad.isdigit() or int(cantidad) <= 0:
    print("Error: ingrese un número mayor a 0.")
    cantidad = input("Cantidad de productos: ")

cantidad = int(cantidad)

total_sin_descuento = 0
total_con_descuento = 0

for i in range(cantidad):
    precio = input(f"Producto {i + 1} - Precio: ")
    while not precio.isdigit() or int(precio) <= 0:
        print("Error: ingrese un número entero mayor a 0.")
        precio = input(f"Producto {i + 1} - Precio: ")

    precio = int(precio)
    total_sin_descuento += precio

    descuento = input("¿Tiene descuento? (S/N): ").lower()
    while descuento != "s" and descuento != "n":
        print("Error: ingrese S o N.")
        descuento = input("¿Tiene descuento? (S/N): ").lower()

    if descuento == "s":
        precio_con_descuento = precio * 0.90
    else:
        precio_con_descuento = precio

    total_con_descuento += precio_con_descuento

ahorro = total_sin_descuento - total_con_descuento
promedio = total_con_descuento / cantidad

print("\n--- RESUMEN ---")
print("Cliente:", nombre)
print(f"Total sin descuentos: ${total_sin_descuento}")
print(f"Total con descuentos: ${total_con_descuento:.2f}")
print(f"Ahorro total: ${ahorro:.2f}")
print(f"Promedio por producto: ${promedio:.2f}")


# Ejercicio 2 – Acceso al Campus y Menú Seguro

usuario_correcto = "alumno"
clave_correcta = "python123"

intentos = 0
acceso = False

while intentos < 3 and acceso == False:
    print(f"\nIntento {intentos + 1}/3")
    usuario = input("Usuario: ")
    clave = input("Clave: ")

    if usuario == usuario_correcto and clave == clave_correcta:
        acceso = True
        print("Acceso concedido.")
    else:
        print("Error: credenciales inválidas.")
        intentos += 1

if acceso == False:
    print("Cuenta bloqueada.")
else:
    salir = False

    while salir == False:
        print("\n1. Ver estado de inscripción")
        print("2. Cambiar clave")
        print("3. Mostrar mensaje")
        print("4. Salir")

        opcion = input("Opción: ")

        while not opcion.isdigit():
            print("Error: ingrese un número válido.")
            opcion = input("Opción: ")

        opcion = int(opcion)

        if opcion < 1 or opcion > 4:
            print("Error: opción fuera de rango.")

        elif opcion == 1:
            print("Estado: Inscripto.")

        elif opcion == 2:
            nueva = input("Nueva clave: ")

            while len(nueva) < 6:
                print("Error: la clave debe tener al menos 6 caracteres.")
                nueva = input("Nueva clave: ")

            confirmar = input("Confirmar clave: ")

            if nueva == confirmar:
                clave_correcta = nueva
                print("Clave cambiada correctamente.")
            else:
                print("Error: las claves no coinciden.")

        elif opcion == 3:
            print("Seguí practicando, cada ejercicio ayuda a aprender un poco más.")

        elif opcion == 4:
            salir = True
            print("Sesión finalizada.")


# Ejercicio 3 – Agenda de Turnos

operador = input("Nombre del operador: ")
while operador == "" or not operador.isalpha():
    print("Error: ingrese solo letras.")
    operador = input("Nombre del operador: ")

lunes1 = ""
lunes2 = ""
lunes3 = ""
lunes4 = ""

martes1 = ""
martes2 = ""
martes3 = ""

opcion = 0

while opcion != 5:
    print("\n1. Reservar turno")
    print("2. Cancelar turno")
    print("3. Ver agenda del día")
    print("4. Ver resumen")
    print("5. Cerrar sistema")

    opcion = input("Opción: ")
    while not opcion.isdigit():
        print("Error: ingrese una opción válida.")
        opcion = input("Opción: ")

    opcion = int(opcion)

    if opcion == 1:
        dia = input("Día (1=Lunes, 2=Martes): ")
        while dia != "1" and dia != "2":
            print("Error: ingrese 1 para Lunes o 2 para Martes.")
            dia = input("Día (1=Lunes, 2=Martes): ")

        paciente = input("Nombre del paciente: ")
        while paciente == "" or not paciente.isalpha():
            print("Error: ingrese solo letras.")
            paciente = input("Nombre del paciente: ")

        if dia == "1":
            if paciente == lunes1 or paciente == lunes2 or paciente == lunes3 or paciente == lunes4:
                print("Ese paciente ya tiene turno en Lunes.")
            elif lunes1 == "":
                lunes1 = paciente
                print("Turno reservado correctamente.")
            elif lunes2 == "":
                lunes2 = paciente
                print("Turno reservado correctamente.")
            elif lunes3 == "":
                lunes3 = paciente
                print("Turno reservado correctamente.")
            elif lunes4 == "":
                lunes4 = paciente
                print("Turno reservado correctamente.")
            else:
                print("No hay lugares disponibles en Lunes.")

        else:
            if paciente == martes1 or paciente == martes2 or paciente == martes3:
                print("Ese paciente ya tiene turno en Martes.")
            elif martes1 == "":
                martes1 = paciente
                print("Turno reservado correctamente.")
            elif martes2 == "":
                martes2 = paciente
                print("Turno reservado correctamente.")
            elif martes3 == "":
                martes3 = paciente
                print("Turno reservado correctamente.")
            else:
                print("No hay lugares disponibles en Martes.")

    elif opcion == 2:
        dia = input("Día (1=Lunes, 2=Martes): ")
        while dia != "1" and dia != "2":
            print("Error: ingrese 1 para Lunes o 2 para Martes.")
            dia = input("Día (1=Lunes, 2=Martes): ")

        nombre = input("Paciente a cancelar: ")
        while nombre == "" or not nombre.isalpha():
            print("Error: ingrese solo letras.")
            nombre = input("Paciente a cancelar: ")

        if dia == "1":
            if nombre == lunes1:
                lunes1 = ""
                print("Turno cancelado correctamente.")
            elif nombre == lunes2:
                lunes2 = ""
                print("Turno cancelado correctamente.")
            elif nombre == lunes3:
                lunes3 = ""
                print("Turno cancelado correctamente.")
            elif nombre == lunes4:
                lunes4 = ""
                print("Paciente no encontrado.")
            else:
                print("Paciente no encontrado.")

        else:
            if nombre == martes1:
                martes1 = ""
                print("Turno cancelado correctamente.")
            elif nombre == martes2:
                martes2 = ""
                print("Turno cancelado correctamente.")
            elif nombre == martes3:
                martes3 = ""
                print("Turno cancelado correctamente.")
            else:
                print("Paciente no encontrado.")

    elif opcion == 3:
        dia = input("Ver día (1=Lunes, 2=Martes): ")
        while dia != "1" and dia != "2":
            print("Error: ingrese 1 para Lunes o 2 para Martes.")
            dia = input("Ver día (1=Lunes, 2=Martes): ")

        if dia == "1":
            print("\nAgenda de Lunes")
            print("Turno 1:", lunes1 if lunes1 != "" else "(libre)")
            print("Turno 2:", lunes2 if lunes2 != "" else "(libre)")
            print("Turno 3:", lunes3 if lunes3 != "" else "(libre)")
            print("Turno 4:", lunes4 if lunes4 != "" else "(libre)")
        else:
            print("\nAgenda de Martes")
            print("Turno 1:", martes1 if martes1 != "" else "(libre)")
            print("Turno 2:", martes2 if martes2 != "" else "(libre)")
            print("Turno 3:", martes3 if martes3 != "" else "(libre)")

    elif opcion == 4:
        ocupados_lunes = 0
        ocupados_martes = 0

        if lunes1 != "":
            ocupados_lunes += 1
        if lunes2 != "":
            ocupados_lunes += 1
        if lunes3 != "":
            ocupados_lunes += 1
        if lunes4 != "":
            ocupados_lunes += 1

        if martes1 != "":
            ocupados_martes += 1
        if martes2 != "":
            ocupados_martes += 1
        if martes3 != "":
            ocupados_martes += 1

        print("\n--- RESUMEN ---")
        print("Lunes ocupados:", ocupados_lunes)
        print("Lunes libres:", 4 - ocupados_lunes)
        print("Martes ocupados:", ocupados_martes)
        print("Martes libres:", 3 - ocupados_martes)

        if ocupados_lunes > ocupados_martes:
            print("El día con más turnos es Lunes.")
        elif ocupados_martes > ocupados_lunes:
            print("El día con más turnos es Martes.")
        else:
            print("Hay empate entre ambos días.")

    elif opcion == 5:
        print("Sistema cerrado.")

    else:
        print("Error: opción fuera de rango.")


# Ejercicio 4 – Escape Room: La Bóveda

agente = input("Nombre del agente: ")
while agente == "" or not agente.isalpha():
    print("Error: ingrese solo letras.")
    agente = input("Nombre del agente: ")

energia = 100
tiempo = 12
cerraduras_abiertas = 0
alarma = False
codigo_parcial = ""
racha_forzar = 0

while energia > 0 and tiempo > 0 and cerraduras_abiertas < 3:
    if alarma == True and tiempo <= 3:
        print("La alarma bloqueó la bóveda. Perdiste.")
        break

    print("\n--- ESTADO ACTUAL ---")
    print("Energía:", energia)
    print("Tiempo:", tiempo)
    print("Cerraduras abiertas:", cerraduras_abiertas)

    print("\n1. Forzar cerradura")
    print("2. Hackear panel")
    print("3. Descansar")

    opcion = input("Opción: ")
    while not opcion.isdigit() or int(opcion) < 1 or int(opcion) > 3:
        print("Error: ingrese una opción válida.")
        opcion = input("Opción: ")

    opcion = int(opcion)

    if opcion == 1:
        racha_forzar += 1
        energia -= 20
        tiempo -= 2

        if racha_forzar == 3:
            alarma = True
            print("La cerradura se trabó y se activó la alarma.")
        else:
            if energia < 40:
                numero = input("Riesgo de alarma. Elige un número del 1 al 3: ")
                while not numero.isdigit() or int(numero) < 1 or int(numero) > 3:
                    print("Error: ingrese un número entre 1 y 3.")
                    numero = input("Elige un número del 1 al 3: ")

                if numero == "3":
                    alarma = True
                    print("Se activó la alarma.")

            if alarma == False:
                cerraduras_abiertas += 1
                print("Abriste una cerradura.")

    elif opcion == 2:
        racha_forzar = 0
        energia -= 10
        tiempo -= 3

        for i in range(4):
            codigo_parcial += "A"
            print("Hackeando...", codigo_parcial)

        if len(codigo_parcial) >= 8 and cerraduras_abiertas < 3:
            cerraduras_abiertas += 1
            print("Se abrió una cerradura automáticamente.")

    elif opcion == 3:
        racha_forzar = 0
        energia += 15
        if energia > 100:
            energia = 100

        tiempo -= 1

        if alarma == True:
            energia -= 10
            print("La alarma sigue activa y perdés energía adicional.")

if cerraduras_abiertas == 3:
    print("Victoria. Abriste la bóveda.")
elif energia <= 0 or tiempo <= 0:
    print("Derrota. Te quedaste sin energía o sin tiempo.")


# Ejercicio 5 – La Arena del Gladiador

print("--- BIENVENIDO A LA ARENA ---")

nombre = input("Nombre del Gladiador: ")
while nombre == "" or not nombre.isalpha():
    print("Error: solo se permiten letras.")
    nombre = input("Nombre del Gladiador: ")

vida_jugador = 100
vida_enemigo = 100
pociones = 3
danio_pesado = 15
danio_enemigo = 12

while vida_jugador > 0 and vida_enemigo > 0:
    print("\n=== NUEVO TURNO ===")
    print(f"{nombre} (HP: {vida_jugador}) vs Enemigo (HP: {vida_enemigo}) | Pociones: {pociones}")

    print("1. Ataque pesado")
    print("2. Ráfaga veloz")
    print("3. Curar")

    opcion = input("Opción: ")
    while not opcion.isdigit() or int(opcion) < 1 or int(opcion) > 3:
        print("Error: ingrese un número válido.")
        opcion = input("Opción: ")

    opcion = int(opcion)

    if opcion == 1:
        danio = danio_pesado

        if vida_enemigo < 20:
            danio = int(danio * 1.5)
            print("¡Golpe crítico!")

        vida_enemigo -= danio
        print(f"¡Atacaste al enemigo por {danio} puntos de daño!")

    elif opcion == 2:
        print("¡Inicias una ráfaga de golpes!")
        for i in range(3):
            vida_enemigo -= 5
            print("> Golpe conectado por 5 de daño")

    elif opcion == 3:
        if pociones > 0:
            vida_jugador += 30
            pociones -= 1

            if vida_jugador > 100:
                vida_jugador = 100

            print("Te curaste 30 puntos de vida.")
        else:
            print("No quedan pociones.")

    if vida_enemigo > 0:
        vida_jugador -= danio_enemigo
        print(f"¡El enemigo te atacó por {danio_enemigo} puntos de daño!")

if vida_jugador > 0:
    print(f"¡VICTORIA! {nombre} ha ganado la batalla.")
else:
    print("DERROTA. Has caído en combate.")

# Ejercicio 5 – La Arena del Gladiador

print("--- BIENVENIDO A LA ARENA ---")

nombre = input("Nombre del Gladiador: ")
while nombre == "" or not nombre.isalpha():
    print("Error: solo se permiten letras.")
    nombre = input("Nombre del Gladiador: ")

vida_jugador = 100
vida_enemigo = 100
pociones = 3
danio_pesado = 15
danio_enemigo = 12

while vida_jugador > 0 and vida_enemigo > 0:
    print("\n=== NUEVO TURNO ===")
    print(f"{nombre} (HP: {vida_jugador}) vs Enemigo (HP: {vida_enemigo}) | Pociones: {pociones}")

    print("1. Ataque pesado")
    print("2. Ráfaga veloz")
    print("3. Curar")

    opcion = input("Opción: ")
    while not opcion.isdigit() or int(opcion) < 1 or int(opcion) > 3:
        print("Error: ingrese un número válido.")
        opcion = input("Opción: ")

    opcion = int(opcion)

    if opcion == 1:
        danio = danio_pesado

        if vida_enemigo < 20:
            danio = int(danio * 1.5)
            print("¡Golpe crítico!")

        vida_enemigo -= danio
        print(f"¡Atacaste al enemigo por {danio} puntos de daño!")

    elif opcion == 2:
        print("¡Inicias una ráfaga de golpes!")
        for i in range(3):
            vida_enemigo -= 5
            print("> Golpe conectado por 5 de daño")

    elif opcion == 3:
        if pociones > 0:
            vida_jugador += 30
            pociones -= 1

            if vida_jugador > 100:
                vida_jugador = 100

            print("Te curaste 30 puntos de vida.")
        else:
            print("No quedan pociones.")

    if vida_enemigo > 0:
        vida_jugador -= danio_enemigo
        print(f"¡El enemigo te atacó por {danio_enemigo} puntos de daño!")

if vida_jugador > 0:
    print(f"¡VICTORIA! {nombre} ha ganado la batalla.")
else:
    print("DERROTA. Has caído en combate.")

