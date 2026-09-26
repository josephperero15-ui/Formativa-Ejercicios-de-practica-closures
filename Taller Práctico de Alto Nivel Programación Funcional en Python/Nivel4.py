# ==============================================================================
# 🟣 NIVEL 4: Patrones Avanzados de Arquitectura Funcional
# ==============================================================================

# ==============================================================================
# Ejercicio 16: Validador Compuesto de Reglas de Negocio
# ==============================================================================
def crear_validador_multiple(*lambdas_criterios):
#Retorna un closure que evalúa si un objeto cumple con todas las lambdas.
    return lambda objeto: all(criterio(objeto) for criterio in lambdas_criterios)
validador_usuario = crear_validador_multiple(lambda u: len(u.get('user', '')) >= 5, lambda u: u.get('activo', False) is True)
print("Ejercicio 16 (Validador Múltiple):", validador_usuario({'user': 'admin_root', 'activo': True}))

# ==============================================================================
# Ejercicio 17: Caché con Tamaño Máximo (Memoización Profesional)
# ==============================================================================
def memoizar_avanzado(fn_costosa, max_items):
#Retorna un closure controlando una caché con límite estricto de capacidad.
    cache = {}
    orden_claves = []
    def ejecutar(*args):
        nonlocal orden_claves
        if args in cache: return cache[args]
        resultado = fn_costosa(*args)
        if len(cache) >= max_items: cache.pop(orden_claves.pop(0), None)
        cache[args] = resultado
        orden_claves.append(args)
        return resultado
    return ejecutar
cache_optimizada = memoizar_avanzado(lambda x: x * 10, max_items=2)
print("Ejercicio 17 (Memoización Calcula):", cache_optimizada(5))
print("Ejercicio 17 (Memoización Caché):", cache_optimizada(5))

# ==============================================================================
# Ejercicio 18: Motor de Pipeline Secuencial (Currying / Middleware)
# ==============================================================================
def crear_pipeline(*funciones_transformacion):
    def procesar(dato_inicial):
        actual = dato_inicial
        for fn in funciones_transformacion:
            actual = fn(actual)
        return actual
    return procesar

pipeline_limpieza = crear_pipeline(lambda s: s.strip(), lambda s: s.replace(" ", "_"), lambda s: s.upper())
print("Ejercicio 18 (Pipeline):", pipeline_limpieza("   datos de usuario   "))

# ==============================================================================
# Ejercicio 19: Sistema Pub/Sub (Event Listener con HOFs y Closures)
# ==============================================================================
def crear_sistema_eventos():
    suscriptores = {}
    def gestor(accion, evento=None, callback=None):
        nonlocal suscriptores
        if accion == "suscribir":
            if evento not in suscriptores:
                suscriptores[evento] = []
            suscriptores[evento].append(callback)
        elif accion == "emitir" and evento in suscriptores:
            for cb in suscriptores[evento]:
                cb(evento)
    return gestor

pubsub = crear_sistema_eventos()
print("Ejercicio 19 (Pub/Sub):")
pubsub("suscribir", "click", lambda ev: print(f" -> Suscriptor 1 recibió: {ev}"))
pubsub("emitir", "click")

# ==============================================================================
# Ejercicio 20: Mini-Query Engine sobre Listas de Objetos
# ==============================================================================
def crear_consultor(campo):
    return lambda lista, lambda_regla: [obj for obj in lista if lambda_regla(obj.get(campo))]

inventario = [{'nombre': 'Laptop', 'precio': 1200}, {'nombre': 'Mouse', 'precio': 25}]
consultar_precio = crear_consultor('precio')
print("Ejercicio 20 (Mini Query Engine):", consultar_precio(inventario, lambda p: p > 100))


