import json
import aio_pika


async def create_connection():
    connection = await aio_pika.connect_robust(
    "amqp://rabbit:password@rabbitmq",
    )
    return connection

async def publish_event(connection, msg, routing_key):
    async with connection:
        channel = await connection.channel()

        await channel.default_exchange.publish(                     
            aio_pika.Message(body=json.dumps(msg).encode()),        
            routing_key=routing_key,                                
        )
