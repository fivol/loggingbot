import asyncio
import os

from fastapi import FastAPI
from bot import send_text_broadcast, dp
from loguru import logger

app = FastAPI()


@app.get("/")
def read_root():
    return {"Hello": "World"}


async def run_bot():
    while True:
        try:
            await dp.start_polling()
        except RuntimeError:
            logger.info('STOP')
            break
        except:
            logger.exception('Pooling error')


@app.on_event('startup')
async def startup():
    print(os.getenv('API_TOKEN'))
    asyncio.create_task(run_bot())


@app.get("/text")
async def send_text(text: str):
    await send_text_broadcast(text)
    return {'status': 'done'}

