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
        logger.info(f"GPT-3man has logged in as a bot {client.user}")

@client.event
async def on_message(message):
    username = str(message.author).split("#")[0]
    channel = str(message.channel.name)
    user_message = str(message.content)

    logger.info(f"Message {user_message} by {username} on {channel}")

    if message.author == client.user:
        return
    
    if channel == "random":
        if user_message.lower() == "hello" or user_message.lower() == "hi":
            await message.channel.send(f"Hello {username}")
            return
        elif user_message.lower() == "bye":
            await message.channel.send(f'Bye {username}')
        elif user_message.lower() == "rizz me up":
            jokes = ["Are you a camera? Because every time I look at you, I smile.", 
                "Do you have a map? Because I just keep getting lost in your eyes.",
                "Excuse me, but I think you dropped something: my jaw."
            ]
            await message.channel.send(random.choice(jokes))

client.run(token)