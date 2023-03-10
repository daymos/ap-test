import json
import aio_pika


async def create_connection():
    connection = await aio_pika.connect_robust(
    "amqp://rabbit:password@rabbitmq",
    )
    return connection



#class Rabbit_MQ_Client():
#    async def create_connection(self):
#        self.connection = await aio_pika.connect_robust(
#        "amqp://guest:guest@127.0.0.1/",
#    )
#
#    async def publish_event(self, routing_key, msg) -> None:
#
#        async with self.connection:
#
#            channel = await self.connection.channel()
#
#            await channel.default_exchange.publish(
#                aio_pika.Message(body=json.dumps(msg).encode()),
#                routing_key=routing_key,
#            )

