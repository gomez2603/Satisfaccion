from collections import Counter

from django.shortcuts import render
from cuestionario.models import encuesta
from .utils import get_plot, get_pie


def chart(request):
    qs = encuesta.objects.all()
    x = [x.p1 for x in qs]
    y = [y.p2 for y in qs]
    z = [z.p3 for z in qs]
    a = [a.p4 for a in qs]
    b = [b.p5 for b in qs]
    c = [c.p6 for c in qs]
    d = [d.p7 for d in qs]
    f = [f.p8 for f in qs]
    g = [g.p9 for g in qs]
    h = [h.p10 for h in qs]

    contadorx = Counter(x)
    contadory = Counter(y)
    contadorz = Counter(z)
    contadora = Counter(a)
    contadorb = Counter(b)
    contadorc = Counter(c)
    contadord = Counter(d)
    contadorf = Counter(f)
    contadorg = Counter(g)
    contadorh = Counter(h)

    positivo =0
    negativo = 0
    neutral = 0


    positivo = positivo + contadorx.get('B',0) + contadory.get('A',0) + contadory.get('B',0) + contadorz.get('A',0) + contadorz.get('B',0) + contadorz.get('A',0) +contadora.get('B',0) + contadora.get('A',0) +contadorb.get('B', 0) + contadorb.get('A', 0) +contadorc.get('B', 0) + contadorc.get('A', 0) +contadord.get('B', 0) + contadord.get('A', 0) +contadorf.get('B', 0) + contadorf.get('A', 0)  + contadorg.get('B', 0) + contadorg.get('A', 0)
    + contadorh.get('B', 0) + contadorh.get('A', 0)


    negativo = negativo + + contadorx.get('D',0) + contadory.get('E',0) + contadory.get('D',0) + contadorz.get('E',0) + contadorz.get('D',0) + contadorz.get('E',0) +contadora.get('D',0) + contadora.get('E',0) +contadorb.get('D', 0) + contadorb.get('E', 0) +contadorc.get('D', 0) + contadorc.get('E', 0) +contadord.get('D', 0) + contadord.get('E', 0) +contadorf.get('D', 0) + contadorf.get('E', 0)  + contadorg.get('D', 0) + contadorg.get('E', 0)
    + contadorh.get('D', 0) + contadorh.get('E', 0)
    neutral = neutral + contadorx.get('C',0) + contadory.get('C',0) + contadorz.get('C',0) +contadora.get('C',0) + contadorb.get('C',0) + contadorc.get('C',0) + contadord.get('C',0) +contadord.get('C',0) + contadorf.get('C',0) +contadorg.get('C',0) + contadorg.get('C',0)  + contadorh.get('C',0)




    chart = get_plot(x,'Pregunta 1')
    chart1 = get_plot(y,'Pregunta 2')
    chart2 =  get_plot(z,'Pregunta 3')
    chart3 = get_plot(a, 'Pregunta 4')
    chart4 = get_plot(b, 'Pregunta 5')
    chart5 = get_plot(c, 'Pregunta 6')
    chart6 = get_plot(d, 'Pregunta 8')
    chart7 = get_plot(f, 'Pregunta 9')
    chart8 = get_plot(g, 'Pregunta 10')
    chart9 = get_plot(h, 'Pregunta 11')

    pie = get_pie(positivo,negativo,neutral)
    return render(request, 'chart.html',{'chart':chart,'chart1':chart1,'chart2':chart2,'chart3':chart3,'chart4':chart4,'chart5':chart5,'chart6':chart6,'chart7':chart7,'chart8':chart8,'chart9':chart9,'pie':pie})
