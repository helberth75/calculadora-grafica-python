# GESTOR DE TAREAS

tareas = []

def mostrar_menu():
    print("\n---GESTOR DE TAREAS---")
    print("1. Agregar tarea")
    print("2. Ver tareas")
    print("3. Marcar tarea como completada")
    print("4. Eliminar tarea")
    print("5. Salir")

def agregar_tarea():
    nombre = input("Ingrese el nombre de la tarea: ")
    tareas.append({"nombre": nombre, "completada": False})
    print(f"Tarea '{nombre}' agregada.")

def ver_tareas():
    print(f"Depuración: Tareas actuales: {tareas}")  # Depuración
    if not tareas:
        print("No hay tareas.")
    else:
        print("\nLista de tareas:")
        for i, t in enumerate(tareas, 1):
            estado = "✔️" if t["completada"] else "❌"
            print(f"{i}. {t['nombre']} [{estado}]")

def completar_tarea():
    ver_tareas()
    if not tareas:
        return
    try:
        indice = int(input("Ingrese el número de la tarea a completar: ")) - 1
        if 0 <= indice < len(tareas):
            tareas[indice]["completada"] = True
            print(f"Tarea '{tareas[indice]['nombre']}' marcada como completada.")
        else:
            print("Número de tarea inválido.")
    except ValueError:
        print("Entrada inválida. Debe ser un número.")

def eliminar_tarea():
    ver_tareas()
    if not tareas:
        return
    try:
        indice = int(input("Ingrese el número de la tarea a eliminar: ")) - 1
        if 0 <= indice < len(tareas):
            tarea_eliminada = tareas.pop(indice)
            print(f"Tarea '{tarea_eliminada['nombre']}' eliminada.")
        else:
            print("Número de tarea inválido.")
    except ValueError:
        print("Entrada inválida. Debe ser un número.")

# Bucle principal
while True:
    mostrar_menu()
    opcion = input("Seleccione una opción (1-5): ").strip()
    print(f"Depuración: Opción seleccionada: {opcion}")  # Depuración
    if opcion == "1":
        agregar_tarea()
    elif opcion == "2":
        print("Depuración: Llamando a ver_tareas()...")  # Depuración
        ver_tareas()
    elif opcion == "3":
        completar_tarea()
    elif opcion == "4":
        eliminar_tarea()
    elif opcion == "5":
        print("Saliendo del gestor de tareas.")
            
    else:
        print("Opción inválida. Intente nuevamente.")