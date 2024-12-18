import paho.mqtt.client as mqtt


# Se llama a esta función cuando el cliente se quiere conectar al broker 
# También se hacen las suscripciones a tópicos
def on_connect(client, userdata, flags, reason_code, properties):
    print(f"Connected with result code {reason_code}")
    client.subscribe("temperatura")
    print("Me suscribí al tópico temperatura")


# Se llama esta función cuando llega un mensaje a la suscripción
def on_message(client, userdata, msg):
    print(msg.topic+" "+str(msg.payload))
    # if msg.topic == "temperatura1":
    #     client.publish("temperatura2", "Recibí mensaje")
    

mqttc = mqtt.Client(mqtt.CallbackAPIVersion.VERSION2)
mqttc.on_connect = on_connect
mqttc.on_message = on_message

mqttc.connect("192.168.0.106", 1883, 60)
mqttc.loop_forever()
