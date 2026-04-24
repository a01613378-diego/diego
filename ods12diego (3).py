# Importar librerías necearias
import numpy as np
import streamlit as st
import pandas as pd

# Insertamos título
st.write(''' # ODS 12: Energia y Residuos ''')
# Insertamos texto con formato
st.markdown("""
Esta aplicación utiliza **Machine Learning** para predecir el impacto del calentamiento global
en el consumo de energia, alineado con el **ODS 12: Energia y Residuos**.
""")
# Insertamos una imagen
st.image("foto energia.jfif", caption="Impacto del consumo de energia dependiendo los residuos.")

#st.header('Datos personales')
# Definimos cómo ingresará los datos el usuario
# Usaremos un deslizador
st.sidebar.header("Parámetros Ambientales")
# Definimos los parámetros de nuestro deslizador:
  # Límite inferior: 10kg. Es el límite inferior donde no hay basura
  # Límite superior: 150kg. Es el máximo siendo muy pesimistas de kg de residuos
  # Valor inicial: 68kg. Considero que es un buen valor que está por el promedio de 
temp_input = st.sidebar.slider("Residuos (kg)", 10.0, 150.0, 68.0)

# Cargamos el archivo con los datos (.csv)
df =  pd.read_csv('ods12.csv', encoding='latin-1')
# Seleccionamos las variables
X = df[['Residuos_kg']]
y = df['Consumo_Energia_kWh']

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
st.subheader('Estado de energia')
st.write(f'El consumo de energia es: {prediccion:.2f}kWh')

if prediccion < 400:
        st.success("Estado: Saludable")
elif prediccion < 850:
        st.warning("Estado: Riesgo Moderado")
else:
        st.error("Estado: Alerta Crítica")
