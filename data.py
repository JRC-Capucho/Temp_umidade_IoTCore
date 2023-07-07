# Import SDK packages
from AWSIoTPythonSDK.MQTTLib import AWSIoTMQTTClient
import json 
from time import sleep
from random import uniform, uniform

# Client id declarado no policy no AWS IoT Core
myMQTTClient = AWSIoTMQTTClient("myClientID") 

# URL para fazer o MQTT
myMQTTClient.configureEndpoint("a2pw8ijsp9wwym-ats.iot.us-east-1.amazonaws.com",8883)

# caminho das credenciais
myMQTTClient.configureCredentials("./credentials/AmazonRootCA1.pem", "./credentials/private.pem.key", "./credentials/certificate.pem.crt")
myMQTTClient.configureOfflinePublishQueueing(-1)  # Infinite offline Publish queueing
myMQTTClient.configureDrainingFrequency(2)  # Draining: 2 Hz
myMQTTClient.configureConnectDisconnectTimeout(10)  # 10 sec
myMQTTClient.configureMQTTOperationTimeout(5)  # 5 sec

myMQTTClient.connect()


#posicao
hall = [
    ["0102"],
    ["0910"],
    ["1718"],
]

#posicao
columns = [
    ["AB"],
    ["AE"],
    ["AH"],
    ["AK"],
    ["AN"],
    ["AR"],
]

#predio
place = ["CPT","DC"]

id = place[0]+"|"+place[1]+"|"+columns[0][0]+''+hall[0][0]
#           "CPT|DC|AB0102"

while True:
    topic = 'dispositivo/'+str(id)+'/dados'

    temp = round(uniform(20,50),2) # Temperatura vai de 20 a 50 valor randomico 
    hum = round(uniform(10,30),2) # umidade vai de 10 a 30  valor randomico
    aux = {"Temperatura":temp,"Umidade":hum} # auxiliar para transforma em json
    data = json.dumps(aux) # transforma em json
    myMQTTClient.publish(topic,data,0) # envia os dados para o topico

    print('send data')
    print('Topico ', topic)
    print('Data', data)
    print()

    sleep(30)  # dorme por  30 seg

myMQTTClient.disconnect()
