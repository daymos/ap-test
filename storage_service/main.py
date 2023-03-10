import asyncio
import logging

import aio_pika

from service.logs_service import store_logs



async def main() -> None:
    logging.basicConfig(level=logging.INFO)
    connection = await aio_pika.connect_robust(
        "amqp://rabbit:password@rabbitmq/",
    )

    queue_name = "dataqueue"

    async with connection:
        channel = await connection.channel()

        await channel.set_qos(prefetch_count=10)

        queue = await channel.declare_queue(queue_name, auto_delete=True)

        async with queue.iterator() as queue_iter:
            async for message in queue_iter:
                async with message.process():
                    logging.info('Received this correlation_id: {}, with message: {}'.format(message.correlation_id,message.body))

                    store_logs(message)

                    if queue.name in message.body.decode():
                        break


if __name__ == "__main__":
    asyncio.run(main())