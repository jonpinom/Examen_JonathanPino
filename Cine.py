peliculas = {
    'P101': ['Luz de Otoño', 'drama', 110, 'B', 'Español', False],
    'P102': ['Noche Neón', 'acción', 125, 'C', 'Ingles', True],
    'P103': ['Planeta Agua', 'documental', 90, 'A', 'Español', False],
    'P104': ['Risa Total', 'comedia', 105, 'A', 'Español', True],
    'P105': ['Código Zero', 'thriller', 118, 'C', 'Ingles', True],
    'P106': ['Viaje Lunar', 'ciencia ficción', 132, 'B', 'Ingles', False]
}

cartelera = {
    'P101': [5990, 40],
    'P102': [7990, 0],
    'P103': [4990, 25],
    'P104': [6990, 12],
    'P105': [8990, 8],
    'P106': [7490, 3]
}

def cupos_genero(genero):
    total_cupos = 0
    genero_buscado = genero.strip().lower()
    
    for cod, datos in peliculas.items():
        if datos[1].lower() == genero_buscado:

            if cod in cartelera:
                total_cupos += cartelera[cod][1]
                
    print(f"El total de cupos disponibles es: {total_cupos}")


def busqueda_precio(p_min, p_max):
    resultados = []
    
    for cod, datos_cartelera in cartelera.items():
        precio = datos_cartelera[0]
        cupos = datos_cartelera[1]
        
        if p_min <= precio <= p_max and cupos > 0:
            if cod in peliculas:
                titulo = peliculas[cod][0]
                resultados.append(f"{titulo}{cod}")
                
    if resultados:
        resultados.sort()
        print(f"Las películas encontradas son: {resultados}")
    else:
        print("No hay películas en ese rango de precios.")

def actualizar_precio(codigo, nuevo_precio):
    codigo_up = codigo.upper()
    if codigo_up in cartelera:
        cartelera[codigo_up][0] = nuevo_precio
        return True
    return False

def validar_codigo(codigo):
    if not codigo or codigo.isspace():
        return False
    if codigo.upper() in peliculas:
        return False
    return True

def validar_titulo(titulo):
    return bool(titulo and not titulo.isspace())

def validar_genero(genero):
    return bool(genero and not genero.isspace())

def validar_duracion(duracion):
    try:
        val = int(duracion)
        return val > 0
    except ValueError:
        return False

def validar_clasificacion(clasificacion):
    return clasificacion in ['A', 'B', 'C']

def validar_idioma(idioma):
    return bool(idioma and not idioma.isspace())

def validar_es_3d(es_3d):
    return es_3d in ['s', 'n']

def validar_precio(precio):
    try:
        val = int(precio)
        return val > 0
    except ValueError:
        return False

def validar_cupos(cupos):
    try:
        val = int(cupos)
        return val >= 0
    except ValueError:
        return False

def agregar_pelicula(codigo, titulo, genero, duracion, clasificacion, idioma, es_3d, precio, cupos):
    codigo_up = codigo.upper()
    if codigo_up in peliculas:
        return False
    
    bool_3d = True if es_3d == 's' else False
    
    peliculas[codigo_up] = [titulo, genero, int(duracion), clasificacion, idioma, bool_3d]
    cartelera[codigo_up] = [int(precio), int(cupos)]
    return True

def eliminar_pelicula(codigo):
    codigo_up = codigo.upper()
    if codigo_up in peliculas:
        del peliculas[codigo_up]
        if codigo_up in cartelera:
            del cartelera[codigo_up]
        return True
    return False

def menu_principal():
    while True:
        print("\n========== MENÚ PRINCIPAL ==========")
        print("1. Cupos por género")
        print("2. Búsqueda de películas por rango de precio")
        print("3. Actualizar precio de película")
        print("4. Agregar película")
        print("5. Eliminar película")
        print("6. Salir")
        print("="*36)
        
        opcion = input("Ingrese opción: ").strip()
        
        if opcion == '1':
            genero = input("Ingrese género a consultar: ")
            cupos_genero(genero)
            
        elif opcion == '2':
            while True:
                try:
                    p_min = int(input("Ingrese precio mínimo: "))
                    p_max = int(input("Ingrese precio máximo: "))
                    
                    if p_min >= 0 and p_max >= 0 and p_min <= p_max:
                        busqueda_precio(p_min, p_max)
                        break
                    else:
                        print("Restricción: Los precios deben ser mayores a cero y el mínimo menor o igual al máximo. Intente de nuevo.")
                except ValueError:
                    print("Debe ingresar valores enteros")
                    
        elif opcion == '3':
            while True:
                cod = input("Ingrese código de película: ")
                nuevo_p_raw = input("Ingrese nuevo precio: ")
                
                try:
                    nuevo_p = int(nuevo_p_raw)
                    if nuevo_p <= 0:
                        print("El precio debe ser un número entero positivo.")
                        continue
                except ValueError:
                    print("Debe ingresar un valor entero válido para el precio.")
                    continue
                
                if actualizar_precio(cod, nuevo_p):
                    print("Precio actualizado")
                else:
                    print("El código no existe")
                    
                resp = input("¿Desea actualizar otro precio (s/n)?: ").strip().lower()
                if resp == 'n':
                    break

        elif opcion == '4':
            cod = input("Ingrese código de película: ")
            if not validar_codigo(cod):
                if cod.upper() in peliculas:
                    print("El código ya existe")
                else:
                    print("Error: El código no puede estar vacío.")
                continue
                
            tit = input("Ingrese título: ")
            if not validar_titulo(tit):
                print("Error: Título inválido.")
                continue
                
            gen = input("Ingrese género: ")
            if not validar_genero(gen):
                print("Error: Género inválido.")
                continue
                
            dur = input("Ingrese duración (minutos): ")
            if not validar_duracion(dur):
                print("Error: La duración debe ser un entero mayor que cero.")
                continue
                
            clas = input("Ingrese clasificación: ")
            if not validar_clasificacion(clas):
                print("Error: La clasificación debe ser exactamente 'A', 'B' o 'C'.")
                continue
                
            idi = input("Ingrese idioma: ")
            if not validar_idioma(idi):
                print("Error: Idioma inválido.")
                continue
                
            t_3d = input("¿Es 3D? (s/n): ").strip().lower()
            if not validar_es_3d(t_3d):
                print("Error: Debe ingresar 's' o 'n'.")
                continue
                
            pre = input("Ingrese precio: ")
            if not validar_precio(pre):
                print("Error: El precio debe ser un entero mayor que cero.")
                continue
                
            cup = input("Ingrese cupos: ")
            if not validar_cupos(cup):
                print("Error: Los cupos deben ser un entero mayor o igual a cero.")
                continue
            
            exito = agregar_pelicula(cod, tit, gen, dur, clas, idi, t_3d, pre, cup)
            if exito:
                print("Película agregada")
            else:
                print("El código ya existe")
                
        elif opcion == '5':
            cod = input("Ingrese código de película a eliminar: ")
            if eliminar_pelicula(cod):
                print("Película eliminada")
            else:
                print("El código no existe")
                
        elif opcion == '6':
            print("Programa finalizado.")
            break
            
        else:
            print("Debe seleccionar una opción válida")

if __name__ == "__main__":
    menu_principal()
    