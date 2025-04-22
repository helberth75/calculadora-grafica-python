#GESTOR DE TAREAS
tareas = []
def mostrar_menu():
    print( "\n---GESTOR DE TAREAS---")
    print("1. Agregar tarea")
    print("2. Ver tareas")
    print("3. Marcar tarea como completada")
    print("4. Eliminar tarea")
    print("5. Salir")

def agregar_tarea():
    nombre = input("Ingrese el nombre de la tarea: ")
    tareas.append({"nombre": nombre, "completada": False})
    print(f"Tarea '{nombre}' agregada.")

def ver_tareas():  #muestra las tareas  antes de marcarlas como completadas
    if not tareas:
        print("No hay tareas.")
        return #si no hay tareas, termina la funcion
    print("\n---TAREAS---")
    for i, tarea in enumerate(tareas):
        estado = "Completada" if tarea["completada"] else "Pendiente"
        print(f"{i + 1}. {tarea['nombre']} - {estado}")
def completar_tarea():
    ver_tareas()
    if not tareas:
        return
    try:
        indice = int(input("Ingrese el número de la tarea a completar: ")) - 1 #resta 1 por que la lista empieza en 0
        if 0 <= indice < len(tareas): #verifica si el indice es valido
            tareas[indice]["completada"] = True #marca la tarea como completada
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
        ver_tareas()
        if not tareas:
            return
        try:
            indice = int(input("Ingrese el número de la tarea a eliminar: ")) - 1 #resta 1 por que la lista empieza en 0
            if 0 <= indice < len(tareas): #verifica si el indice es valido
                tarea_eliminada = tareas.pop(indice) #elimina la tarea de la lista y la guarda en una variable
                print(f"Tarea '{tarea_eliminada['nombre']}' eliminada.")
            else:
                print("Número de tarea inválido.")
        except ValueError:
            print("Entrada inválida. Debe ser un número.")

# Bucle principal para ejecutar el gestor de tareas
while True:
    mostrar_menu()
    opcion = input("Seleccione una opción (1-5): ").strip() #m
    if opcion == "1":
        agregar_tarea()
    elif opcion == "2":
        print(">> Estoy dentor de la opcion 2")
        ver_tareas()
    elif opcion == "3":
        completar_tarea()
    elif opcion == "4":
        eliminar_tarea()
    elif opcion == "5":
        print("Saliendo del gestor de tareas.")
        break
    else:
        print("Opción inválida. Intente nuevamente.") #si la opcion no es valida, vuelve a mostrar el menu

    