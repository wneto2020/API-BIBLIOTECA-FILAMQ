import pika
from Config.var_env import info


def send(body):
    params = pika.URLParameters(info["URL_AMQP"])
    connection = pika.BlockingConnection(params)
    channel = connection.channel() #start a channel
    channel.queue_declare(queue='Envio e-mail') #Declare a queue
    channel.basic_publish(exchange='',
                          routing_key='Envio e-mail',
                          body=body)

    print(" [x] Sent 'Hello World!'")
    connection.close()