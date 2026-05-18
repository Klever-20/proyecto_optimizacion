import time
import numpy as np
import math

def es_primo_optimizado(n):
    if n < 2:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False
    for i in range(3, int(math.sqrt(n)) + 1, 2):
        if n % i == 0:
            return False
    return True

def buscar_primos_optimizado(limite):
    primos = [num for num in range(2, limite + 1) if es_primo_optimizado(num)]
    return primos

def buscar_primos_con_numpy(limite):
    numeros = np.arange(2, limite + 1)
    es_primo_array = np.ones(len(numeros), dtype=bool)
    for i in range(2, int(np.sqrt(limite)) + 1):
        if es_primo_array[i-2]:
            es_primo_array[i*2-2::i] = False
    return numeros[es_primo_array].tolist()

if __name__ == "__main__":
    limite = 100000
    
    inicio = time.time()
    primos_opt = buscar_primos_optimizado(limite)
    fin = time.time()
    print(f"Tiempo optimizado (sqrt + list comp): {fin - inicio:.4f} segundos")
    
    inicio = time.time()
    primos_np = buscar_primos_con_numpy(limite)
    fin = time.time()
    print(f"Tiempo con NumPy: {fin - inicio:.4f} segundos")
    
    print(f"Cantidad de primos encontrados: {len(primos_opt)}")