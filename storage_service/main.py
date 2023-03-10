import os
import asyncio
import logging
import aio_pika

from service.logs_service import store_logs

RABBITMQ_USERNAME = os.environ['RABBITMQ_USERNAME']
RABBITMQ_HOST = os.environ['RABBITMQ_HOST']
DB_PATH = os.environ['DB_PATH']
RABBITMQ_PASSWORD = os.environ['RABBITMQ_PASSWORD']
QUEUE_NAME = os.environ['RABBITMQ_QUEUE']

async def main() -> None:
    logging.basicConfig(level=logging.INFO)

    connection = await aio_pika.connect_robust(
        "amqp://{}:{}@{}/".format(RABBITMQ_USERNAME, RABBITMQ_PASSWORD, RABBITMQ_HOST),
    )

    async with connection:
        channel = await connection.channel()
        queue = await channel.declare_queue(QUEUE_NAME, auto_delete=True)

        async with queue.iterator() as queue_iter:
            async for message in queue_iter:
                async with message.process():
                    logging.info('Received this event: {}'.format( message.body))
                    try:
                        store_logs(message, DB_PATH)
                    except Exception as e:
                        logging.error(e)


if __name__ == "__main__":
    asyncio.run(main())