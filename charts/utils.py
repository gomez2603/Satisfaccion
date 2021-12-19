import matplotlib.pyplot as plt
import base64
import math
from io import BytesIO
from collections import Counter


def get_graph():
    buffer = BytesIO()
    plt.savefig(buffer)
    buffer.seek(0)
    image_png = buffer.getvalue()
    graph = base64.b64encode(image_png)
    graph = graph.decode('utf-8')
    buffer.close()
    return graph


def get_plot(x, titulo):
    colors = ['#FF0000', '#DE9335', '#F5EC47', '#35DE4B', '#00CDFF']
    contador = Counter(x);
    plt.switch_backend('AGG')
    plt.figure(figsize=(3, 3))
    plt.title(titulo)
    plt.xlabel("Respuestas")
    plt.ylabel("Encuestados")
    plt.bar(contador.keys(), contador.values(), color=colors)
    yint = range(min([0]), math.ceil(max(contador.values())) + 1)
    plt.yticks(yint)
    plt.tight_layout()
    graph = get_graph()
    return graph


def get_pie(positivas,negativas,neutral):
    valores = [positivas,negativas,neutral]
    nombres = ['Positivas','Negativas','Neutral']
    colores = ['#FF0000','#00CDFF','#35DE4B']
    desfase = (0,0.1,0)
    plt.figure(figsize=(5, 5))
    plt.title("Resumen de Tendencia")
    plt.pie(valores, labels=nombres, autopct="% 0.1f %%", frame=False,colors=colores,explode=desfase)
    graph = get_graph()
    return graph
