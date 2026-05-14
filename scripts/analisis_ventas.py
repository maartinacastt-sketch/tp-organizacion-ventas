import pandas as pd
import matplotlib.pyplot as plt

def analizar():
    try:
        df = pd.read_csv('datos/ventas.csv')
        total = (df['precio'] * df['cantidad vendida']).sum()
        top = df.groupby('producto')['cantidad vendida'].sum().idxmax()
        
        with open('resultados/indicadores.txt', 'w') as f:
            f.write(f"Ventas Totales: ${total}\nProducto Estrella: {top}")
            
        df.groupby('producto')['cantidad vendida'].sum().plot(kind='bar', color='orange')
        plt.title('Ventas por Producto')
        plt.savefig('resultados/grafico_ventas.png')
        print("Analisis KAN-5 terminado")
    except:
        print("Error: falta el archivo datos/ventas.csv")

if __name__ == "__main__":
    analizar()
