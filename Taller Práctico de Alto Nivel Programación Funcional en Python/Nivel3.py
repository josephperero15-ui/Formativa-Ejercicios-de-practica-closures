import time
# ==============================================================================
# NIVEL 3: HOFs Complejas combinadas con Closures y Lambdas
# ==============================================================================

# ==============================================================================
# Ejercicio 11: Pipeline de Mapeo y Filtrado Combinado
# ==============================================================================
def procesar_coleccion(lista, fn_predicado, fn_transformacion):
 # Combina filter y map pasando expresiones lambda sobre una lista.
    return list(map(fn_transformacion, filter(fn_predicado , lista)))
numeros =[1, 2, 3, 4 ,5, 6]
print("Ejercicio 11 (filtrar pares y duplicar)")

#===============================================================================
# Ejercicio 12: Reductor / Agrupador Personalizado
#=============================================================================== 

def agrupar_por(lista, fn_clave):
#Agrupa una lista de diccionarios según la clave generada por la lambda.
    resultado = {}
    for elemento in lista:
        clave = fn_clave(elemento)
        if clave not in resultado:
            resultado[clave] = []
        resultado[clave].append(elemento)
    return resultado
productos = [{'id': 1, 'cat': 'Tecnología'}, {'id': 2, 'cat': 'Muebles'}, {'id': 3, 'cat': 'Tecnología'}]
print("Ejercicio 12 (Agrupar por categoría):", agrupar_por(productos, lambda p: p['cat']))


#===============================================================================
# Ejercicio 13: Ejecutor Repetitivo con Estado Accesible
#===============================================================================
def ejecutar_y_rastrear(fn_tarea, n):
#Retorna un closure con el historial de resultados tras ejecutar la tarea N veces.
    historial = []
    for _ in range(n):
        historial.append(fn_tarea())
    return lambda ver_ultimos=None: historial[-ver_ultimos:] if ver_ultimos else historial
contador_id = 100
rastreador = ejecutar_y_rastrear(lambda: f"TK-{globals().update(contador_id=globals().get('contador_id')+1) or globals().get('contador_id')}", 3)
print("Ejercicio 13 (Historial completo):", rastreador())


#===============================================================================
# Ejercicio 14: Compositor de Cadenas de Operaciones
#===============================================================================
def componer_dos(f, g):
#Devuelve un closure que aplica f(g(x)) encapsulando transformaciones.
    return lambda x: f(g(x))

por_dos = lambda x: x * 2
mas_diez = lambda x: x + 10
composicion = componer_dos(por_dos, mas_diez)
print("Ejercicio 14 (Composición f(g(x))):", composicion(15))  


#===============================================================================
# Ejercicio 15: Decorador / HOF de Profiling y Auditoría
#===============================================================================
def auditar_ejecucion(fn_objetivo, fn_logger):
#Mide el tiempo de ejecución e invoca a la lambda del logger con la métrica.
    def envoltura(*args, **kwargs):
        inicio = time.perf_counter()
        resultado = fn_objetivo(*args, **kwargs)
        fin = time.perf_counter()
        fn_logger(fn_objetivo.__name__, fin - inicio)
        return resultado
    return envoltura

logger_consola = lambda func, t: print(f"Ejercicio 15 (Auditoría) -> '{func}' tardó {t:.6f}s.")
funcion_auditada = auditar_ejecucion(lambda n: sum(i**2 for i in range(n)), logger_consola)
funcion_auditada.__name__ = "CalcularCuadrados"
funcion_auditada(100000)

