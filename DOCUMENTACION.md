# Documentación del Proyecto: Optimización de Código para Cálculo de Primos

## Introducción
El código original implementa un algoritmo de búsqueda de números primos entre 1 y 100,000 usando un bucle anidado (O(n²)), lo que resulta en un tiempo de ejecución elevado (~12 segundos). Se identificaron como problemas principales:
- Iteración completa hasta `n` en la función `es_primo`.
- Uso de bucles tradicionales en lugar de comprensiones de listas.
- No aprovechamiento de operaciones vectorizadas.

## Técnicas de optimización aplicadas
1. **Reducción del rango de búsqueda:** Se itera solo hasta la raíz cuadrada de `n`.
2. **Exclusión de pares:** Se saltan números pares después del 2.
3. **List comprehensions:** Reemplazan bucles `for` tradicionales.
4. **Uso de NumPy:** Vectorización de operaciones con arrays.

## Resultados comparativos (valores de ejemplo)

| Versión | Tiempo (segundos) | Mejora |
|--------|------------------|--------|
| Original | 18.8390 | - |
| Optimizada (sqrt + list comp) | 0.0885 | 35x |
| Optimizada con NumPy | 0.0035 | 140x |

## Análisis con cProfile
- **Original:** La función `es_primo` consume el 98% del tiempo.
- **Optimizada:** La carga se distribuye mejor, con menor tiempo en división de módulo y mayor en creación de listas.

## Conclusiones
- La optimización del rango de búsqueda produce la mayor ganancia (pasa de O(n) a O(√n)).
- NumPy mejora aún más el rendimiento gracias a operaciones en C.
- Se recomienda siempre perfilar el código antes y después de optimizar.
- Buenas prácticas como PEP 8 y modularización facilitan el mantenimiento.

## Enlace al repositorio GitHub
https://github.com/Klever-20/proyecto_optimizacion