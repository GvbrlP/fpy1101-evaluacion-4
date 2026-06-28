from ejercicio1 import (
    mostrar_menu, leer_opcion, agregar_libro, buscar_libro, 
    eliminar_libro, actualizar_disponibilidad, mostrar_libros
)

def main():
    biblioteca = []
    
    while True:
        mostrar_menu()
        opcion = leer_opcion()
        
        if opcion == 1:
            agregar_libro(biblioteca)
        elif opcion == 2:
            titulo_b = input("Ingrese el título a buscar: ")
            posicion = buscar_libro(biblioteca, titulo_b)
            
            if posicion != -1:
                libro = biblioteca[posicion]
                estado_texto = "DISPONIBLE" if libro["disponible"] else "SIN COPIAS"
                print(f"\n[Libro Encontrado en posición {posicion}]")
                print(f"Título: {libro['titulo']} | Copias: {libro['copias']} | Préstamo: {libro['prestamo']} días | Estado: {estado_texto}")
            else:
                print(f"El libro '{titulo_b}' no se encuentra registrado.")
                
        elif opcion == 3:
            eliminar_libro(biblioteca)
        elif opcion == 4:
            actualizar_disponibilidad(biblioteca)
            print("Disponibilidad de todos los libros actualizada correctamente.")
        elif opcion == 5:
            mostrar_libros(biblioteca)
        elif opcion == 6:
            print("“Gracias por usar el sistema. Vuelva Pronto”")
            break
        else:
            print("Opción inválida. Por favor, intente nuevamente.")

if __name__ == "__main__":
    main()