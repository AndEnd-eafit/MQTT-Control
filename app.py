import paho.mqtt.client as paho
import time
import streamlit as st
import json

# Variables globales
values = 0.0
act1 = "OFF"

# Callback para publicar
def on_publish(client, userdata, result):
    print("El dato ha sido publicado \n")
    pass

# Callback para mensajes recibidos
def on_message(client, userdata, message):
    global message_received
    time.sleep(2)
    message_received = str(message.payload.decode("utf-8"))
    st.write(message_received)

# Configuración MQTT
broker = "broker.mqttdashboard.com"
port = 1883
client1 = paho.Client("GIT-HUB_Yoru")
client1.on_message = on_message

# Añadir las fuentes y estilo para la imagen centrada
st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Inter:wght@400&family=Lexend:wght@600&display=swap');
    
    .title-font {
        font-family: 'Lexend', sans-serif;
        font-size: 36px;
        text-align: center;
    }
    
    .paragraph-font {
        font-family: 'Inter', sans-serif;
        font-size: 18px;
        text-align: justify;
    }
    
    .center-img {
        display: block;
        margin-left: auto;
        margin-right: auto;
    }
    
    </style>
    """, unsafe_allow_html=True)

# Título con la nueva tipografía
st.markdown('<p class="title-font">MQTT Control</p>', unsafe_allow_html=True)

# Imagen centrada
image = st.image('Yoru - MQTT - SE MUEVE.png', width=300, use_column_width='auto')

# Botón ON
if st.button('ON'):
    act1 = "ON"
    client1 = paho.Client("GIT-HUB_Yoru")
    client1.on_publish = on_publish
    client1.connect(broker, port)
    message = json.dumps({"Act1": act1})
    ret = client1.publish("cmqtt_s_Yoru", message)
else:
    st.write('')

# Botón OFF
if st.button('OFF'):
    act1 = "OFF"
    client1 = paho.Client("GIT-HUB_Yoru")
    client1.on_publish = on_publish
    client1.connect(broker, port)
    message = json.dumps({"Act1": act1})
    ret = client1.publish("cmqtt_s_Yoru", message)
else:
    st.write('')

# Slider para valores analógicos
values = st.slider('Selecciona el rango de valores', 0.0, 100.0)
st.write('Values:', values)

# Botón para enviar valor analógico
if st.button('Enviar valor analógico'):
    client1 = paho.Client("GIT-HUB_Yoru")
    client1.on_publish = on_publish
    client1.connect(broker, port)
    message = json.dumps({"Analog": float(values)})
    ret = client1.publish("cmqtt_a_Yoru", message)
else:
    st.write('')
