import matplotlib.pyplot as plt
import pandas as pd
import io
import base64

class Estadistica:

    def __init__(self):

        self.df = pd.read_excel('info/HistorialBitcoin.xlsx')
    
    def datosExcel(self):
        return self.df

    def graficoFechaDolares(self):

        img = io.BytesIO()

        fecha = self.df['Fecha'].unique()
        precio = []
        for i in fecha:
            suma = self.df.loc[self.df['Fecha'] == i, ['Ultimo_Valor']].sum()[0]
            precio.append(suma)

        plt.figure(figsize=(10,5))
        plt.bar(fecha, precio, color="cyan")
        plt.title('Valor del Bitcoin en el mercado por fecha')
        plt.xticks(rotation=10)
        plt.ylabel('Valor de 1 bitcoin en el mercado ')
        plt.savefig(img, format='png')
        img.seek(0)

        img_url = base64.b64encode(img.getvalue()).decode()
        return img_url

    def graficoFrecuenciaPrecio(self):

        img = io.BytesIO()

        x = self.df['Ultimo_Valor']
        plt.figure(figsize=(10,5))
        plt.hist(x, bins=None, color="cyan")
        plt.title('Frecuencia del Valor de un Bitcoins en el Mercado ')
        plt.xticks(rotation=10)
        plt.ylabel('Frecuencia')

        plt.savefig(img, format='png')
        img.seek(0)

        img_url = base64.b64encode(img.getvalue()).decode()
        return img_url
        
    def graficocriptomonedas(self):
    
        img = io.BytesIO()

        fecha = self.df['Fecha'].unique()
        pagos = []
        for i in fecha:
            suma = self.df.loc[self.df['Fecha'] == i, ['Valor_Maximo']].sum()[0]
            pagos.append(suma)

        plt.figure(figsize=(10,5))
        plt.bar(fecha, pagos, color="cyan")
        plt.title('Valor Máximo del Bitcoin en el mercado por fecha')
        plt.xticks(rotation=10)
        plt.ylabel('Valor Máximo del Bitcoin en el mercado ')
        plt.savefig(img, format='png')
        img.seek(0)

        img_url = base64.b64encode(img.getvalue()).decode()
        return img_url