import json
import aio_pika
import pika
import logging


async def create_connection():
    connection = await aio_pika.connect_robust(
    "amqp://rabbit:password@rabbitmq",
    )
    return connection

async def publish_event(connection, msg, request_id, routing_key):
    if connection.is_closed:
        connection = await create_connection()

    async with connection:
        channel = await connection.channel()
        try:
            await channel.default_exchange.publish(                     
                aio_pika.Message(
                    body=json.dumps(msg).encode(),
                    correlation_id = request_id
                    ),        
                routing_key=routing_key,                                
            )
        except Exception as e:
            logging.error(e, 'Could not send message')

        logging.info('Succesfully published this message')

