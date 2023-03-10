import json
import aio_pika
import logging
import os

RABBITMQ_USERNAME = os.environ['RABBITMQ_USERNAME']
RABBITMQ_HOST = os.environ['RABBITMQ_HOST']
RABBITMQ_PASSWORD = os.environ['RABBITMQ_PASSWORD']
QUEUE_NAME = os.environ['RABBITMQ_QUEUE']


async def create_connection():
    connection = await aio_pika.connect_robust(
    'amqp://{}:{}@{}'.format(RABBITMQ_USERNAME, RABBITMQ_PASSWORD, RABBITMQ_HOST),
    )
    return connection

async def publish_event(connection, event, routing_key=QUEUE_NAME):
    if connection.is_closed:
        logging.info('Creating a new rabbitmq connection')
        connection = create_connection()
    channel = await connection.channel()
    try:
        await channel.default_exchange.publish(                     
            aio_pika.Message(
                body=json.dumps(event).encode(),
                ),        
            routing_key=routing_key,                                
        )
    except Exception as e:
        logging.error(e, 'Could not send message')

    logging.info('Succesfully published this message')

