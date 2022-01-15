import pika
import json
from send_email import send_email
from Config.var_env import info


params = pika.URLParameters(info['URL_AMQP'])
connection = pika.BlockingConnection(params)
channel = connection.channel()# start a channel
channel.queue_declare(queue='Envio e-mail')# Declare a queue


def callback(ch, method, properties, body):
    print(" [x] Received %r" % body)
    payload = json.loads(body)
    send_email(payload["email"], payload["books"])


channel.basic_consume('Envio e-mail', callback, auto_ack=True)

print(' [*] Waiting for messages. To exit press CTRL+C')
channel.start_consuming()