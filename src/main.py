import discord
import os
import random
import logging
from utils import (
    handler,
    logger
)
from dotenv import load_dotenv

logging.basicConfig(
    format="[%(asctime)s] [%(filename)s:%(lineno)d] %(message)s", level=logging.INFO
)

load_dotenv()

intents = discord.Intents(messages=True, guilds=True)
intents.message_content = True
client = discord.Client(intents=intents)
token = os.getenv('TOKEN')

@client.event
async def on_ready():
        logger.info(f"GPT-3man has logged in as a bot {client.user}")

"""@client.event
async def on_message(message):
    username = str(message.author).split("#")[0]
    channel = str(message.channel.name)
    user_message = str(message.content)

    logger.info(f"Message {user_message} by {username} on {channel}")
    logger.info(f"Client user: {client.user}")

    if message.author == client.user:
        return
    
    if channel == "bot_testing":
        if user_message.lower() == "hello" or user_message.lower() == "hi":
            logger.info("HIT")
            await message.channel.send(f"Hello {username}")
            return
        elif user_message.lower() == "bye":
            await message.channel.send(f'Bye {username}')
        elif user_message.lower() == "rizz me up":
            jokes = ["Are you a camera? Because every time I look at you, I smile.", 
                "Do you have a map? Because I just keep getting lost in your eyes.",
                "Excuse me, but I think you dropped something: my jaw.",
                "They say that kissing is a language of love, so would you mind starting a conversation with me?",
                "Are you an eco-friendly kind of girl? The condom in my pocket goes expires tomorrow, so why don’t you help me use it?",
                "Did you have Lucky Charms for breakfast? Because you look magically delicious!",
                "Can I borrow a kiss? I promise I’ll give it back.",
                "If you’re feeling down, I can feel you up.",
                "My doctor told me I have a vitamin D deficiency. Want to go back to my place and save me?",
                "I was feeling very off today, but then you turned me on."
            ]
            await message.channel.send(random.choice(jokes))"""

client.run(token, log_handler=handler)