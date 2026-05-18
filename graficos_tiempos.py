import matplotlib.pyplot as plt

# REEMPLAZA estos números con tus tiempos reales
tiempo_original = 18.8390      
tiempo_optimizado = 0.0885
tiempo_numpy = 0.0035

tiempos = [tiempo_original, tiempo_optimizado, tiempo_numpy]
etiquetas = ['Original', 'Optimizado\n(sqrt + list comp)', 'Optimizado\n(NumPy)']

# Gráfico de barras
plt.figure(figsize=(8, 5))
plt.bar(etiquetas, tiempos, color=['red', 'skyblue', 'lightgreen'])
plt.ylabel('Tiempo (segundos)')
plt.title('Comparativa de tiempos de ejecución\n(1 a 100,000 primos)')
for i, v in enumerate(tiempos):
    plt.text(i, v + 0.2, f"{v:.4f}s", ha='center')
plt.grid(axis='y', linestyle='--', alpha=0.7)
plt.savefig('comparativa_tiempos.png')
plt.show()

# Gráfico de pastel
plt.figure(figsize=(6, 6))
plt.pie(tiempos, labels=etiquetas, autopct='%1.1f%%', startangle=90,
        colors=['red', 'skyblue', 'lightgreen'])
plt.title('Distribución de tiempos de ejecución')
plt.savefig('distribucion_tiempos.png')
plt.show()