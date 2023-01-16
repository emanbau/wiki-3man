import discord
import os
import random
import logging
from src.utils import (
    logger
)
from dotenv import load_dotenv

logging.basicConfig(
    format="[%(asctime)s] [%(filename)s:%(lineno)d] %(message)s", level=logging.INFO
)

load_dotenv()

client = discord.Bot()
token = os.getenv('TOKEN')

@client.event
async def on_ready():
        logger.info("GPT-3man has logged in as a bot {client.user}")

