def producto(a,b)
    #función que suma los valores a y b
    return a*b

def remainder(x,a):
    return x%a

def resta(a,b):
    # función que resta los valores a y b
    return a-b

def suma(a,b):
	# Función que suma los valores a y b
	return a+b
	
def error_relativo_porcentual(valor_aproximado, valor_exacto):
    """
    Calcula el error relativo porcentual dado un valor aproximado y un valor exacto.
    
    Args:
        valor_aproximado (float): El valor aproximado.
        valor_exacto (float): El valor exacto.
    
    Returns:
        float: El error relativo porcentual.
    """
    try:
        error = abs((valor_aproximado - valor_exacto) / valor_exacto) * 100
        return error
    except ZeroDivisionError:
        print("Error: El valor exacto no puede ser cero.")
        return None

