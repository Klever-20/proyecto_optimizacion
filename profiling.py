import cProfile
import pstats
from codigo_original import buscar_primos_original
from codigo_optimizado import buscar_primos_optimizado

limite = 100000

print("=== Profiling del codigo original ===")
cProfile.run('buscar_primos_original(limite)', 'profiling_original.prof')

print("\n=== Profiling del codigo optimizado ===")
cProfile.run('buscar_primos_optimizado(limite)', 'profiling_optimizado.prof')

# Mostrar resumen
print("\n=== RESUMEN ORIGINAL ===")
p = pstats.Stats('profiling_original.prof')
p.sort_stats('time').print_stats(5)

print("\n=== RESUMEN OPTIMIZADO ===")
p = pstats.Stats('profiling_optimizado.prof')
p.sort_stats('time').print_stats(5)