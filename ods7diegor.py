# Importar librerías necearias
import numpy as np
import streamlit as st
import pandas as pd

# Insertamos título
st.write(''' # ODS 7: ENERGIA PRODUCIDA ''')
# Insertamos texto con formato
st.markdown("""
Esta aplicación utiliza **Machine Learning** para predecir el impacto del calentamiento global
en los arrecifes de coral, alineado con el **Energía Asequible y No Contaminante**.
""")
# Insertamos una imagen
st.image("7ODS.jfif", caption="ENERGIA PRODUCIDA POR LA INTENSIDAD DE LA RADIACION.")

#st.header('Datos personales')
# Definimos cómo ingresará los datos el usuario
# Usaremos un deslizador
st.sidebar.header("INTENSIDAD")
# Definimos los parámetros de nuestro deslizador:
  # Límite inferior: 150W/m2. Es el límite inferior donde no hay aire
  # Límite superior: 1150W/m2. Es el máximo donde el aire va más rápido
  # Valor inicial: 5750W/m2. Considero que es un buen valor que está por el promedio de
temp_input = st.sidebar.slider("ENERGIS (kWh)", 150.0, 575.0, 1150.0)

# Cargamos el archivo con los datos (.csv)
df =  pd.read_csv('ods7diegoo.csv', encoding='latin-1')
# Seleccionamos las variables
X = df[['VAR_2']]
y = df['VAR_4']

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
st.subheader('ENERGIA PRODUCIDA')
st.write(f'La energia es: {prediccion:.2f}kWh')

if prediccion < 20:
        st.success("Baja Productividad")
elif prediccion < 65:
        st.warning("Productividad media")
else:
        st.error("Alta productividad")
