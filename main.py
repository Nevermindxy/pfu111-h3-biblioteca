from persistencia import cargar_prestamos
from operaciones import registrar_prestamo, consultar_prestamos

def main():
    prestamos = cargar_prestamos()
    
    while True:
        print("\n=== SISTEMA DE BIBLIOTECA - LEGADO MODERNIZADO ===")
        print("1. Registrar un nuevo préstamo")
        print("2. Consultar los préstamos registrados")
        print("3. Salir")
        
        opcion = input("Seleccione una opción (1-3): ").strip()
        
        if opcion == "1":
            registrar_prestamo(prestamos)
        elif opcion == "2":
            consultar_prestamos(prestamos)
        elif opcion == "3":
            print("\nSaliendo del sistema. ¡Hasta luego!")
            break
        else:
            print("\n[Error] Opción no válida. Por favor, seleccione entre 1 y 3.")

if _name_ == "_main_":
    main()