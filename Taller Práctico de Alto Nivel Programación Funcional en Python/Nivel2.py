# ==============================================================================
#  NIVEL 2: Estado Encapsulado Avanzado (nonlocal + Lambdas)
# ==============================================================================

# ==============================================================================
# Ejercicio 6: Contador Ponderado
# ==============================================================================
def crear_contador_peso(fin_paso):
    cuenta = 0
    def incrementar():
        nonlocal cuenta
        cuenta = fin_paso(cuenta)
        return cuenta
    return incrementar
contador = crear_contador_peso(lambda c: c + 3)
print("\nEjercicio 6 - Iteración 1:", contador())
print("Ejercicio  - Iteración 2:", contador())

# ==============================================================================
# Ejercicio 7: Acumulador con Filtro de Aceptación
# ==============================================================================
def crear_acumulador_validado(criterio_lambda):
    total = 0
    def acumular(valor):
        nonlocal total
        if criterio_lambda(valor):
            total += valor
        return total
    return acumular
acumular = crear_acumulador_validado(lambda x: x > 0)
print("\nEjercicio 7 (Suma 10):", acumular(10))   
print("Ejercicio  (Ignora -5):", acumular(-5))  
print("Ejercicio  (Suma 20):", acumular(20))   

# ==============================================================================
# Ejercicio 8: Promediador con Eliminación de Valores Extremos
# ==============================================================================
def crear_promediador_filtrado(filtro_ruido_lambda):
    datos = []
    def agregar(valor):
        nonlocal datos # Garantiza el control estricto del estado encapsulado
        if filtro_ruido_lambda(valor):
            datos.append(valor)
        return sum(datos) / len(datos) if datos else 0
    return agregar
promedio = crear_promediador_filtrado(lambda x: 0 <= x <= 100)
print("\nEjercicio 8 (Agrega 80):", promedio(80))   
print("Ejercicio (Agrega 100):", promedio(100)) 
print("Ejercicio (Ignora 200):", promedio(200)) 

# ==============================================================================
# Ejercicio 9: Limitador de Tasa Inteligente
# ==============================================================================
def crear_limitador_avanzado(max_intentos, fn_alerta):
    intentos = 0
    def intentar():
        nonlocal intentos
        intentos += 1
        if intentos > max_intentos:
            fn_alerta(intentos)
            return False
        return True
    return intentar
alerta = lambda it: print(f"¡Alerta! Límite excedido en intento: {it}")
limitar = crear_limitador_avanzado(2, alerta)
print("\nEjercicio 9 (Intento 1):", limitar())  
print("Ejercicio  (Intento 2):", limitar())  
print("Ejercicio (Intento 3):", limitar())  

# ==============================================================================
# Ejercicio 10: Interruptor Múltiple (Máquina de Estados)
# ==============================================================================
def crear_conmutador(lista_estados):
    idx = 0
    def siguiente():
        nonlocal idx
        estado_actual = lista_estados[idx]
        idx = (idx + 1) % len(lista_estados)
        return estado_actual
    return siguiente
semaforo = crear_conmutador(["ROJO", "AMARILLO", "VERDE"])
print("\nEjercicio 10 - Estado 1:", semaforo()) 
print("Ejercicio  - Estado 2:", semaforo()) 
print("Ejercicio  - Estado 3:", semaforo())  
print("Ejercicio - Estado 4:", semaforo())  
