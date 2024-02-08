import streamlit as st
import pandas as pd
import plotly.express as px

from pandasai import SmartDataframe
from pandasai.llm import OpenAI

llm = OpenAI(api_token=st.secrets['OPENAI'])





st.set_page_config(layout='wide')

st.title(":panda_face: PanDa & Multimax :computer:")
st.write("**Panama Data Consulting**")
st.markdown("##")

st.subheader("1. Chatbots Brillantes")
st.write("Asistentes virtuales potenciados por *ChatGPT*")
st.write(" - Entrenados con información pública y privada")
st.write(" - Disponibles 24/7")
st.write(" - Capaces de captar datos y generar reportes")


cl1, cl2, cl3 = st.columns([3,3,3])
cl2.video("multimax_generar_cotizacion.mp4", 'rb')
cl2.video("bahia motors chatbot.mp4", 'rb')

st.markdown("##")

st.subheader("2. Análisis de Datos para Todos")
st.write("Tableros de inteligencia de negocios personalizados.")


# Función para cargar y preparar los datos
def cargar_datos():
    # Carga los datos desde el archivo CSV
    df = pd.read_csv('ventas_premier.csv')

    # Convierte la columna 'Fecha' a tipo datetime y extrae el mes
    df['Fecha'] = pd.to_datetime(df['Fecha'])
    df['Mes'] = df['Fecha'].dt.month
    return df

df = cargar_datos()

# Sidebar con MultiSelect para los productos
productos_seleccionados = st.multiselect(
    "Selecciona los productos",
    options=df['Producto'].unique(),
    default=df['Producto'].unique()
)

# Si no se selecciona ningún producto, se muestran todos
if not productos_seleccionados:
    productos_seleccionados = df['Producto'].unique()

# Filtrar datos basado en la selección
df_filtrado = df[df['Producto'].isin(productos_seleccionados)]

# Line Chart - Ventas por mes en términos de valor monetario
col1, col2 = st.columns(2)
ventas_por_mes = df_filtrado.groupby(['Mes', 'Producto'])['Subtotal'].sum().reset_index(name='Ventas ($)')
fig_line = px.line(ventas_por_mes, x='Mes', y='Ventas ($)', color='Producto', title='Ventas por Mes ($)')
fig_line.update_layout(legend=dict(orientation="h", y=1, yanchor="bottom", x=0.5, xanchor="center"))
col1.plotly_chart(fig_line)

# Bar Chart - Ventas Totales por Producto en términos de valor monetario
ventas_totales = df_filtrado.groupby('Producto')['Subtotal'].sum().reset_index(name='Ventas Totales ($)')
fig_bar = px.bar(ventas_totales, x='Producto', y='Ventas Totales ($)', color='Producto', title='Ventas Totales por Producto ($)')
fig_bar.update_layout(legend=dict(orientation="h", y=1, yanchor="bottom", x=0.5, xanchor="center"))
col2.plotly_chart(fig_bar)

# Pie Chart - Unidades Vendidas por Producto (sin leyenda)
unidades_vendidas = df_filtrado.groupby('Producto')['Unidades'].sum().reset_index(name='Unidades Vendidas')
fig_pie = px.pie(unidades_vendidas, names='Producto', values='Unidades Vendidas', title='Unidades Vendidas por Producto')
fig_pie.update_layout(showlegend=False)
col1.plotly_chart(fig_pie)

# Pivot Table - Ventas totales, unidades vendidas y porcentaje del total
total_ventas = ventas_totales['Ventas Totales ($)'].sum()
unidades_por_producto = df_filtrado.groupby('Producto')['Unidades'].sum().reset_index(name='Unidades Vendidas')
ventas_y_unidades = pd.merge(ventas_totales, unidades_por_producto, on='Producto')
ventas_y_unidades['Porcentaje del Total (%)'] = ((ventas_y_unidades['Ventas Totales ($)'] / total_ventas) * 100).round(2)
ventas_y_unidades['Porcentaje del Total (%)'] = ventas_y_unidades['Porcentaje del Total (%)'].astype(str) + '%'

col2.write("**Tabla Resumen**")
col2.dataframe(ventas_y_unidades, hide_index=True)



# Preguntas


prompt = st.text_area("**Pregúntale algo a la data :magic_wand:**")
adf = SmartDataframe(df, config={'llm':llm})

st.info('Puedes hacer preguntas como: "Cual fue el producto mas vendido y cuantas unidades se vendieron?", "Que porcentaje de clientes compró martillos?", "Cuanto suma la venta de destornilladores y taladros?"')
# Generate output
if st.button("Preguntar"):
    if prompt:
        # call pandas_ai.run(), passing dataframe and prompt
        with st.spinner("Pensando..."):
            respuesta = adf.chat(f"{prompt}. si tu respuesta es un porcentaje, asegurate de que el formato de tu respuesta incluya dos decimales y el símbolo %. Si tu respuesta es una cifra monetaria, debe tener dos decimales y el símbolo $ al principio. Si la pregunta es irrelevante, responde 'intenta otra pregunta'. Tus respuestas deben ser oraciones completas en español y debes explicar como llegaste al resultado.")
            st.write(respuesta)
    else:
        pass








st.markdown("####")

st.subheader("3. Automatización de Procesos y Aplicaciones Inegrales")
st.write("Utilizando las herramientas más versátiles y avanzadas del mercado, desarrollamos soluciones a la medida a una velocidad incomparable.")
st.markdown("###")
col1, col2, col3 = st.columns(3)

col1.image("python logo.jpeg")
col2.image("bubble logo.jpeg")
col3.image("chatgpt logo.png")


col1, col2, col3 = st.columns(3)

with col1.expander("Python"):
    st.write("Python es el lenguaje número 1 entre desarroladores de software. En PanDa :panda_face:, Python es la base de todas nuestras soluciones.")


with col2.expander("Bubble.io"):
    st.write("Existen infinitas alternativas para desarrollar aplicaciones, pero ninguna como Bubble. Por su velocidad y versatilidad, Bubble es nuestra herramienta de elección para el desarrollo de *business apps* personalizadas.")


with col3.expander("ChatGPT"):
    st.write("ChatGPT abrió el universo de la inteligencia artificial para todo el que quiera aprovecharlo, nosotros ya nos montamos en la ola. :surfer:")

col1, col2, col3 = st.columns([4, 2, 4])

col2.subheader("Propuesta Comercial")

col1, col2, col3 = st.columns([4, 1, 4])
# Contenedor 1
with col1.container(border=True):
    st.write("### Suscripción Panama Data Consulting :panda_face:")
    st.write("Afiliación a nuestro desarrollo a la medida y mantenimiento de aplicaciones de:")
    st.write(" - Inteligencia Artificial")
    st.write(" - Análisis de Datos")
    st.write(" - Automatización de Procesos")
    st.metric(label="Suscripción Mensual", value="$2,500")



# Contenedor 2
with col3.container(border=True):
    st.write("### Desarrollo de Chatbot :robot_face:")
    st.write("Desarrollo de chatbot *brillante* capaz de:")
    st.write(" - Captar datos de los usuarios")
    st.write(" - Generar cotizaciones PDF")
    st.write(" - Producir reportes")
    st.metric(label="Inversión Única", value="$2,800")

# Nota: Asegúrate de reemplazar los textos de título, párrafo, valor de `st.metric` y `delta` con la información específica de tus ofertas.

