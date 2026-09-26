# ==============================================================================
#  NIVEL 1: Closures con Inyección de Comportamiento
# ==============================================================================


#===============================================================================
# Ejercicio 1: Generador de Formateadores con Transformación
#===============================================================================
def crear_formateador(prefijo, fn_transformacion):
#Retorna un closure que transforma un texto con lambda y añade un prefijo.
    return lambda texto: f"{prefijo} {fn_transformacion(texto)}"

formato_log = crear_formateador("[SISTEMA]", lambda s: s.upper())
print("Ejercicio 1:", formato_log("inicio de seccion"))

#===============================================================================
# Ejercicio 2: Multiplicador Paramétrico con Mapeo
#===============================================================================
def crear_operador(factor, operacion_lambda):
#Retorna un closure que aplica la operación usando el factor encapsulado.
    return lambda x: operacion_lambda(x, factor)

sumar_diez = crear_operador(10, lambda a, b: a + b)
print("Ejercicio 2:", sumar_diez(25))

#===============================================================================
# Ejercicio 3: Calculador de Descuentos con Regla Dinámica
#===============================================================================
def crear_descuento_dinamico(regla_condicional_lambda, porcentaje_descuento=0.152):
#Evalúa el precio con la lambda para determinar si aplica el descuento.
    return lambda precio: precio * (1 - porcentaje_descuento) if regla_condicional_lambda(precio) else precio

aplicar_desc = crear_descuento_dinamico(lambda p: p > 200)
print("Ejercicio 3 (Aplica desc):", aplicar_desc(250))
print("Ejercicio 3 (Sin desc):", aplicar_desc(150))

#===============================================================================
# Ejercicio 4: Generador de Seriales / Nombres Únicos
#===============================================================================
def crear_generador_sufijos(patron_lambda):
#Transforma nombres de archivos basándose en una lambda de formato.
    return lambda nombre: patron_lambda(nombre)

generar_pdf = crear_generador_sufijos(lambda n: f"{n}_v2_final.pdf")
print("Ejercicio 4:", generar_pdf("facturas"))

#===============================================================================
# Ejercicio 5: Conversor de Divisas con Margen
#===============================================================================
def crear_conversor(tasa, margen_lambda):
#Convierte montos calculando dinámicamente un margen sobre la tasa.
    return lambda monto: monto * tasa * (1 + margen_lambda(monto))

conversor_euro = crear_conversor(0.92, lambda n: 0.02 if n > 100 else 0.05)
print("Ejercicio 5:", round(conversor_euro(500), 2))