import streamlit as st
import numpy as np
import matplotlib.pyplot as plt
plt.style.use('bmh')

#Functions
def ent(x):
    if x%1 != 0:
        return x
    else:
        return int(x)

def signa(x):
    if x == 1:
        return f""
    elif x == -1:
        return f"-"
    else:
        return ent(x)

def signb(x):
    
    if x == 1:
        return f"+ "
    if x>=0 and x != 1:
        return f"+ {ent(x)}"
    elif x == -1:
        return f"-"
    elif x<0 and x != -1:
        return ent(x)

def signc(x):
    
    if x>=0:
        return f"+ {ent(x)}"
    elif x<0:
        return ent(x)

def formato(a,b,c):
    form = f"{signa(a)}x^2"
    if b != 0:
        form += f"{signb(b)}x"
    else: 
        form = form
    if c != 0:
        form += f"{signc(c)}"
    else:
        form = form
    return form
#App

st.markdown('''<h1 style='text-align: center; color: DarkSlateBlue;'> Funciones Cuadráticas </h1>''',unsafe_allow_html=True)
st.markdown(''' Las funciones cuadráticas son aquellas formadas por un polinomio de segundo grado. La gráfica de una función cuadrática es una **parábola** cuya forma general es la siguiente:
$$
f(x)=ax^2+bx+c
$$
donde $a$, $b$ y $c$ son los coeficientes reales de la función, con $a \\neq 0$.
''')

st.markdown('Estos coeficientes influyen de la siguiente forma en las gráficas de estas funciones:')
with st.container(border=True):
    a1,a2 = st.columns([3,4], gap='medium', vertical_alignment="center")
    with a1:
        st.markdown("<h3 style='text-align: center; color: DarkSlateBlue;'>Coeficiente a</h1>", unsafe_allow_html=True)
        st.markdown('''<div style="text-align: justify;">
        <ul>
        <li>El valor de <b><i>a</i></b> determina la apertura de la parábola. Entre mayor es el valor absoluto de <b><i>a</i></b> más se contrae la parábola.</li>
        <br>
        <li>Además, el signo determina la dirección hacia donde abre la parábola, si <i><b>a > 0 </b></i> la parábola abre hacia arriba y si <i><b>a < 0</b></i> abre hacia abajo.</li>
        </ul>
        </div>
    ''', unsafe_allow_html=True)

    with a2:
        a = st.slider('**Cambia el coeficiente **$a$** en la función $\\hspace{{0.05cm}}$ $f(x) = ax^2$:**', min_value=-5.0, max_value=5.0, value=1.0)
        if a == 0:
            st.error("Esto no es una función cuadrática, el coeficiente $a$ debe ser diferente de 0")
        else:
            x = np.linspace(-6, 6, 100)
            y = a*x**2
            fig, ax = plt.subplots()
            ax.axhline(0, color='black', linewidth=0.8)
            ax.axvline(0, color='black', linewidth=0.8)
            ax.set_xlabel('Eje X')
            ax.set_ylabel('Eje Y')
            line, = ax.plot(x, y)  
            ax.set_ylim([-5, 5])  
            st.pyplot(fig)


with st.container(border=True):
    b1,b2 = st.columns([3,4], gap='medium', vertical_alignment="center")
    with b1:
        st.markdown("<h3 style='text-align: center; color: DarkSlateBlue;'>Coeficiente b</h3>", unsafe_allow_html=True)
        st.markdown('''<div style="text-align: justify;">
        El valor de <b><i>b</i></b> afecta la ubicación de la parábola en el plano cartesiano.
        <ul>
        <br>
        <li>Si <b><i>b</i></b> es positivo, a mayor valor, más abajo y a la izquierda estará la parábola.</li>
        <br>
        <li>Si <b><i>b</i></b> es negativo, a mayor valor absoluto, más abajo y a la derecha estará la parábola.</li>
        </ul>
        </div>
    ''', unsafe_allow_html=True)
    with b2:
        b = st.slider(f'**Cambia el coeficiente **$b$** en la función $\\hspace{{3cm}}$ $f(x) = {formato(a,0,0)} + bx$:**', min_value=-5.0, max_value=5.0, value=1.0)
        if a == 0:
            st.error("Esto no es una función cuadrática, el coeficiente $a$ debe ser diferente de 0")
        else:
            x = np.linspace(-6, 6, 100)
            y = a*x**2+b*x
            fig, ax = plt.subplots()
            ax.axhline(0, color='black', linewidth=0.8)
            ax.axvline(0, color='black', linewidth=0.8)
            ax.set_xlabel('Eje X')
            ax.set_ylabel('Eje Y')
            line, = ax.plot(x, y)  
            ax.set_ylim([-5, 5])  
            st.pyplot(fig)


with st.container(border=True):
    c1,c2 = st.columns([3,4], gap='medium', vertical_alignment="center")
    with c1:
        st.markdown("<h3 style='text-align: center; color: DarkSlateBlue;'>Coeficiente c</h3>", unsafe_allow_html=True)
        st.markdown("")
        st.markdown('''<div style="text-align: justify;">
        El valor de <b><i>c</i></b> determina el punto con el que corta la gráfica en el eje <i>y</i>. Por lo tanto, la parábola corta el eje <i>y</i> en el punto <i><b>(0,c)</i></b>.
        </div>
    ''', unsafe_allow_html=True)
    with c2:
        c = st.slider(f'**Cambia el coeficiente **$c$** en la función $\\hspace{{3cm}}$ $f(x) = {formato(a,b,0)} + c$:**', min_value=-5.0, max_value=5.0, value=1.0)
        if a == 0:
            st.error("Esto no es una función cuadrática, el coeficiente $a$ debe ser diferente de 0")
        else:
            x = np.linspace(-6, 6, 100)
            y = a*x**2+b*x+c
            fig, ax = plt.subplots()
            ax.scatter(0,c, c="green",s=100)
            ax.axhline(0, color='black', linewidth=0.8)
            ax.axvline(0, color='black', linewidth=0.8)
            ax.set_xlabel('Eje X')
            ax.set_ylabel('Eje Y')
            ax.plot(x, y)
            ax.set_ylim([-5, 5])
            st.pyplot(fig)

st.divider()

st.markdown('''<center> <h2 style='text-align: center; color: DarkMagenta;'> <b>Algunos elementos importantes al momento de gráficar una Función Cuadrática </b></h2> </center>''',unsafe_allow_html=True)

st.markdown("")
st.subheader(":blue-background[Vértice]")
st.markdown("")
st.markdown(''' El vértice de una parábola es el punto mínimo (si $a < 0$) o el punto máximo (si $a > 0$) de la función. Además, en este punto se encuentra el vértice de simetría de la función. Las fórmulas para encontrarlo son las siguientes:''')

with st.container(border=False):
    d1,d2,d3,d4 = st.columns(4, gap='medium', vertical_alignment="top")
    with d1:
        st.markdown(" ")
    with d2:
        st.latex("x_v = -\\frac{b}{2a}")
    with d3:
        st.latex("y_v = f\\left(-\\frac{b}{2a}\\right)")
    with d4:
        st.markdown("")
st.markdown("")
st.markdown('''Por lo tanto el vértice está dado por el punto 
$$
V\\left ( -\\frac{b}{2a}, f\\left(-\\frac{b}{2a}\\right) \\right )
$$''')
st.markdown("")
st.markdown('''Asimismo, la ecuación del eje de simetría es: 
$$
x = -\\frac{b}{2a}
$$''')

with st.container(border=True):
    st.markdown("***Establece los valores de los coeficientes de la función y mira como cambia el vértice***")
    e1,e2,e3 = st.columns(3,gap='medium', vertical_alignment="center")
    with e1:
        a2 = float(st.number_input("**Coeficiente a:**", value = 1.0))
    with e2:
        b2= float(st.number_input("**Coeficiente b:**", value = 1.0))
    with e3:
        c2 = float(st.number_input("**Coeficiente c:**", value = 1.0))
    
    st.divider()

    if a2 == 0:
        st.error("Esto no es una función cuadrática, el coeficiente $a$ debe ser diferente de 0")
    else: 
        xv = (-1)*(b2/(2*a2))
        yv = a2*xv**2+b2*xv+c2
        f1,f2 = st.columns([9,10], gap = 'medium', vertical_alignment="center")
        with f1:
            st.markdown(f'''
            **Hallamos $x_v$:**

            $$
            x_v = -\\frac{{{ent(float(f'{b2:.2f}'))}}}{{2\\cdot{ent(float(f'{a2:.2f}'))}}} = {ent(float(f'{xv:.2f}'))}
            $$

            **Reemplazamos en la función para hallar $y_v$:**

            $$
            y_v = {signa(a2)} x_v^2 {signb(b2)} x_v {signc(c2)} 
            $$
            $$
            y_v = {signa(a2)}({ent(float(f'{xv:.2f}'))})^2 {signb(b2)}({ent(float(f'{xv:.2f}'))}) {signc(c2)} 
            $$
            $$
            y_v = {ent(float(f'{yv:.2f}'))}
            $$

            **Por lo tanto el vértice es:**

            $$
            \\left({ent(float(f'{xv:.2f}'))},{ent(float(f'{yv:.2f}'))}\\right)
            $$
            ''')
        with f2:
            x2 = np.linspace(-5, 5, 100)
            y2 = a2*x2**2+b2*x2+c2
            fig, ax = plt.subplots()
            ax.scatter(xv,yv, c="darkorange",s=120)
            ax.axhline(0, color='black', linewidth=0.8)
            ax.axvline(0, color='black', linewidth=0.8)
            ax.set_xlabel('Eje X')
            ax.set_ylabel('Eje Y')
            ax.plot(x2, y2, c="blueviolet")
            ax.set_ylim([-5, 5])
            if a2<0:
             ax.annotate(f"({ent(float(f'{xv:.2f}'))},{ent(float(f'{yv:.2f}'))})", [xv,yv],[xv+0.4,yv+0.4], c="chocolate", fontsize=14)
            elif a2>0:
                ax.annotate(f"({ent(float(f'{xv:.2f}'))},{ent(float(f'{yv:.2f}'))})", [xv,yv],[xv+0.5,yv-0.5], c ="chocolate",fontsize=14)
            st.pyplot(fig)

            st.markdown(f'''
            $$
            f(x) = {formato(a2,b2,c2)}
            $$
            ''')
st.markdown("")
st.markdown(" ")
#
#Puntos de corte
#
st.subheader(":blue-background[Puntos de corte con el eje X]")
st.markdown("")
st.markdown('''Los puntos de corte con el eje $x$ o raíces de la función, son los puntos donde la gráfica atraviesa, corta o toca al eje $x$. Estos puntos corresponden a cuando la función toma el valor cero ($y = 0$), por eso también se les suele llamar ceros de la función.

Para encontrar estos puntos es necesario resolver la ecuación $f(x) = 0$, donde $f(x)$ es la función cuadrática. Esto se convierte entonces en una ecuación cuadrática, que se puede resolver usando la fórmula general:

$$
x = \\frac{-b\\pm\\sqrt{\\Delta}}{2a}, \\hspace{0.5cm} \\text{donde} \\hspace{0.3cm} \\Delta = b^2 - 4ac
$$

Además, el discriminante permite determinar la cantidad de puntos de corte:
- Si $\\Delta > 0$, la función tiene dos cortes con el eje $x$.
- Si $\\Delta = 0$, la función tiene un solo punto de corte con el eje $x$.
- Si $\\Delta < 0$, la función no tiene corte con el eje $x$.

''')

with st.container(border=True):
    st.markdown("")
    st.markdown("***Establece los valores de los coeficientes de la función y mira los puntos de corte***")
    f1,f2 = st.columns([1,2],gap='medium', vertical_alignment="center")
    with f1:
        a3 = float(st.number_input("**a:** ", value = 1.0))
        b3= float(st.number_input("**b:** ", value = 1.0))
        c3 = float(st.number_input("**c:**", value = 1.0))
    with f2:
        if a3 == 0:
            st.error("Esto no es una función cuadrática, el coeficiente $a$ debe ser diferente de 0")
        else:
            det = b3**2-4*a3*c3
            if det > 0:
                xx1 = (-b3+np.sqrt(det))/(2*a3)
                xx2 = (-b3-np.sqrt(det))/(2*a3)
            elif det == 0:
                xx1 = (-b3)/(2*a3)
                xx2 = xx1
            else:
                xx1 = np.nan
                xx2 = np.nan
            st.markdown(f'''
            **Hallamos el discriminante $\\Delta$:**
        
            $$
            \\Delta = ({ent(float(f'{b3:.2f}'))})^2 - 4\\cdot({ent(float(f'{a3:.2f}'))})\\cdot({ent(float(f'{c3:.2f}'))}) = {ent(float(f'{det:.2f}'))}
            $$
            ''')
            if det > 0:
                st.markdown(f"Como $\\Delta > 0$ entonces existen dos puntos de corte:")
                st.latex(f"x = \\frac{{{-1 * ent(float(f'{b3:.2f}'))} \\pm \\sqrt{{{ent(float(f'{det:.2f}'))}}}}}{{2 \\cdot {ent(float(f'{a3:.2f}'))}}} = \\frac{{{-1 * ent(float(f'{b3:.2f}'))} \\pm {ent(float(f'{np.sqrt(det):.2f}'))}}}{{{2*ent(float(f'{a3:.2f}'))}}}")
                st.latex(f"x_1 = \\frac{{{-1 * ent(float(f'{b3:.2f}'))} + {ent(float(f'{np.sqrt(det):.2f}'))}}}{{{2*ent(float(f'{a3:.2f}'))}}} = {ent(float(f'{xx1:.2f}'))}")
                st.latex(f"x_2 = \\frac{{{-1 * ent(float(f'{b3:.2f}'))} - {ent(float(f'{np.sqrt(det):.2f}'))}}}{{{2*ent(float(f'{a3:.2f}'))}}} = {ent(float(f'{xx2:.2f}'))}")
            elif det == 0:
                st.markdown(f"Como $\\Delta = 0$ entonces existe un solo punto de corte:")
                st.latex(f"x = \\frac{{{-1 * ent(float(f'{b3:.2f}'))}}}{{{2*ent(float(f'{a3:.2f}'))}}} = {ent(float(f'{xx1:.2f}'))}")
            else:
                st.markdown(f"Como $\\Delta < 0$ entonces no existen puntos de corte.")
    st.divider()
    if a3 != 0:
        if det > 0:
            st.markdown(f" $\\hspace{{2.25cm}}$ **La función corta el eje $x$ en los puntos $({ent(float(f'{xx1:.2f}'))},0)$  y  $({ent(float(f'{xx2:.2f}'))},0)$**")
        elif det == 0:
            st.markdown(f"$\\hspace{{3.25cm}}$**La función corta el eje $x$ en el punto $({ent(float(f'{xx1:.2f}'))}, 0)$**")
        elif det < 0:
            st.markdown(f"$\\hspace{{4.25cm}}$ **La función no corta con el eje $x$**")
    
    if a3 == 0:
        st.error("Esto no es una función cuadrática, el coeficiente $a$ debe ser diferente de 0")
    else:
        _, col2, _ = st.columns([1,3,1],gap='medium', vertical_alignment="center")
        with col2:
            x4 = np.linspace(-5, 5, 100)
            y4 = a3*x4**2+b3*x4+c3
            fig, ax = plt.subplots()
            ax.scatter(xx1, 0, c="green", s=60)
            ax.scatter(xx2, 0, c="green", s=60)
            ax.axhline(0, color='black', linewidth=0.8)
            ax.axvline(0, color='black', linewidth=0.8)
            ax.plot(x4, y4)
            st.pyplot(fig)
            st.markdown(f'''
            $$
            f(x) = {formato(a3,b3,c3)}
            $$
            ''')
            st.markdown(" ")

#
#Tabulación
#

st.markdown(" ")
st.markdown(" ")
st.subheader(":blue-background[Tabulación de la Función]")
st.markdown("")
st.markdown('''<div style="text-align: justify;"> La tabulación consiste en dar valores  a la variable <i><b>x</b></i> y con ellos calcular los correspondientes a la variable <i><b>y</b></i>, los cuales se van anotando en una tabla. Después se localiza en el plano cartesiano cada punto tabulado y se unen para obtener la forma de la gráfica buscada.
<br>
<br>
En una función cuadrática se deben seleccionar valores de <i><b>x</b></i> que estén antes y después del vértice. Además, entre más puntos se seleccionen para hacer la tabla de valores más precisa será la curva.</div>''', unsafe_allow_html=True)
st.markdown("")
st.markdown("")

with st.container(border=True):
    st.markdown("")
    st.markdown("<center><b>Tabula tu función</b></center)", unsafe_allow_html=True)
    st.markdown("")
    coll1, coll2, coll3 = st.columns(3,gap='medium', vertical_alignment="center")
    with coll1:
        a4 = float(st.number_input("**Coeficiente a:**  ", value = 1.0))
    with coll2:
        b4= float(st.number_input("**Coeficiente b:**  ", value = 1.0))
    with coll3:
        c4 = float(st.number_input("**Coeficiente c:**  ", value = 1.0))
    st.divider()
    if a4 == 0:
        st.error("Esto no es una función cuadrática, el coeficiente $a$ debe ser diferente de 0")
    else:
        colu1, colu2 = st.columns([3,7], gap='medium', vertical_alignment="center")
        with colu1:
            st.markdown(f"""**Función a graficar:**""")
            st.markdown(f"<span style='font-size: 11.4px;'>$\displaystyle f(x) = {formato(a4, b4, c4)}$</span>", unsafe_allow_html=True)
            num = int(st.number_input("Puntos:", value=4))

            c11, c12 = st.columns(2)
            with c11:
                datos_x = np.linspace(-5, 5, num)
                datos_x = st.data_editor(datos_x, use_container_width=True, column_config={"value":"x"})
            with c12:
                datos_y = a4*datos_x**2+b4*datos_x+c4
                datos_y = st.data_editor(datos_y, use_container_width=True, column_config={"value":st.column_config.NumberColumn("f(x)", disabled=True)})

        with colu2:
            # creando vectores de la curva
            vec_x = np.linspace(min(datos_x), max(datos_x), 100)
            vec_y = a4*vec_x**2+b4*vec_x+c4
            # graficando
            fig, ax = plt.subplots()        # grafico
            ax.axvline(0, color="gray")     # eje x
            ax.axhline(0, color="gray")     # eje y
            ax.plot(vec_x, vec_y)           # linea
            ax.scatter(datos_x, datos_y, zorder=2, c="purple")      # puntos
            st.pyplot(fig)                  # mostrar