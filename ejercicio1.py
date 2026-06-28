# =====================================================================
# FUNCIONES DE MENÚ
# =====================================================================

def mostrar_menu():
    print("\n========== MENÚ PRINCIPAL ==========")
    print("1. Agregar libro")
    print("2. Buscar libro")
    print("3. Eliminar libro")
    print("4. Actualizar disponibilidad")
    print("5. Mostrar libros")
    print("6. Salir")
    print("=====================================")

def leer_opcion():
    try:
        opcion = int(input("Seleccione una opción: "))
        return opcion
    except ValueError:
        return 0

# =====================================================================
# FUNCIONES DE VALIDACIÓN
# =====================================================================

def validar_titulo(titulo):
    return titulo.strip() != ""

def validar_copias(copias_str):
    try:
        valor = int(copias_str)
        return valor >= 0
    except ValueError:
        return False

def validar_prestamo(prestamo_str):
    try:
        valor = int(prestamo_str)
        return valor > 0
    except ValueError:
        return False

# =====================================================================
# FUNCIONES DE OPERACIONES DEL SISTEMA
# =====================================================================

def agregar_libro(biblioteca):
    titulo = input("Ingrese el título del libro: ")
    copias_raw = input("Ingrese la cantidad de copias: ")
    prestamo_raw = input("Ingrese el período de préstamo (en días): ")

    if not validar_titulo(titulo):
        print("Error: El título no puede estar vacío ni contener solo espacios.")
        return

    if not validar_copias(copias_raw):
        print("Error: Las copias deben ser un número entero mayor o igual que cero.")
        return

    if not validar_prestamo(prestamo_raw):
        print("Error: El período de préstamo debe ser un número entero mayor que cero.")
        return

    nuevo_libro = {
        "titulo": titulo.strip(),
        "copias": int(copias_raw),
        "prestamo": int(prestamo_raw),
        "disponible": False
    }
    
    biblioteca.append(nuevo_libro)
    print(f"Libro '{nuevo_libro['titulo']}' agregado con éxito.")

def buscar_libro(biblioteca, titulo_buscar):
    for i in range(len(biblioteca)):
        if biblioteca[i]["titulo"].lower() == titulo_buscar.strip().lower():
            return i
    return -1

def eliminar_libro(biblioteca):
    titulo_eliminar = input("Ingrese el título del libro que desea eliminar: ")
    posicion = buscar_libro(biblioteca, titulo_eliminar)

    if posicion != -1:
        libro_eliminado = biblioteca.pop(posicion)
        print(f"El libro '{libro_eliminado['titulo']}' ha sido eliminado.")
    else:
        print(f"El libro '{titulo_eliminar}' no se encuentra registrado.")

def actualizar_disponibilidad(biblioteca):
    for libro in biblioteca:
        if libro["copias"] >= 1:
            libro["disponible"] = True
        else:
            libro["disponible"] = False

def mostrar_libros(biblioteca):
    actualizar_disponibilidad(biblioteca)
    
    if not biblioteca:
        print("\nNo hay libros registrados en la biblioteca.")
        return

    print("\n=== LISTA DE LIBROS ===")
    for libro in biblioteca:
        estado_texto = "DISPONIBLE" if libro["disponible"] else "SIN COPIAS"
        print(f"Título: {libro['titulo']}")
        print(f"Copias: {libro['copias']}")
        print(f"Préstamo: {libro['prestamo']}")
        print(f"Estado: {estado_texto}")
        print("********************************************")