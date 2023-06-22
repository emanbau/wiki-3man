import discord
import os
import logging
import wikipediaapi
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

wikipedia = wikipediaapi.Wikipedia('en')

@client.event
async def on_ready():
        logger.info(f"Wiiki-3man has logged in as a bot {client.user}")

@client.event
async def on_message(message):
    # Ignore messages from the bot itself
    if message.author == client.user:
        return
    
    if message.content.startswith('!wiki'):
        # Extract the query from the user's message
        query = message.content[6:].strip()
        
        # Search for the Wikipedia page
        page = wikipedia.page(query)

        # if exists
        if page.exists():
            # Send the page summary as a response
            print(page.title)
            print(page.summary[0:100])
            await message.channel.send(f"**{page.title}**\n\n{page.summary[0:1500]} -------- ({page.fullurl})")
        else:
            await message.channel.send(f"{query} cannot be found at the moment.")
        



client.run(token, log_handler=handler)