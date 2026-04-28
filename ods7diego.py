# Importar librerías necearias
import numpy as np
import streamlit as st
import pandas as pd

# Insertamos título
st.write(''' # ODS 7: Energía Asequible y No Contaminante ''')
# Insertamos texto con formato
st.markdown("""
Esta aplicación utiliza **Machine Learning** para predecir el impacto dela eficiencia energética, alineado con la  **Velocidad del aire**.
""")
# Insertamos una imagen
st.image("foto ods7.jfif", caption="Impacto de la eficiencia energética con la velocidad del aire.")

#st.header('Datos personales')
# Definimos cómo ingresará los datos el usuario
# Usaremos un deslizador
st.sidebar.header("Parámetros Ambientales")
# Definimos los parámetros de nuestro deslizador:
  # Límite inferior: 0ms. Es el límite inferior donde no hay aire
  # Límite superior: 30ms. Es el máximo donde el aire va más rápido
  # Valor inicial: 15ms. Considero que es un buen valor que está por el promedio de
temp_input = st.sidebar.slider("Velocidad (ms)", 0.0, 30.0, 15.0)

# Cargamos el archivo con los datos (.csv)
df =  pd.read_csv('ods7diego.csv', encoding='latin-1')
# Seleccionamos las variables
X = df[['Velocidad_Viento_ms']]
y = df['Eficiencia_Energetica_kWh']

# Creamos y entrenamos el modelo
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.30, random_state=0)
LR = LinearRegression()
LR.fit(X_train,y_train)

# Hacemos la predicción con el modelo y la temperatura seleccionada por el usuario
b1 = LR.coef_
b0 = LR.intercept_
prediccion = b0 + b1[0]*temp_input

# Presentamos loa resultados
st.subheader('Eficiencia Energética')
st.write(f'La eficiencia energética es: {prediccion:.2f}kWh')

if prediccion < 100:
        st.success("Baja eficiencia")
elif prediccion < 200:
        st.warning("Eficiencia media")
else:
        st.error("Alta eficiencia")
