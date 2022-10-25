import os
import discord

from dotenv import load_dotenv

# Load the .env file containing the token required to run the bot.
load_dotenv()

# Get the token from the .env file.
TOKEN = os.getenv('DISCORD_TOKEN')

from discord.ext.commands import Bot
from discord.ext import commands

import asyncio
import time
import random

intents = discord.Intents.all()
client = discord.Client(intents = intents)
bot = commands.Bot(command_prefix = "/")

# Set "Valhalla" as the game activity, and print a message if the bot launched successfully.
@client.event
async def on_ready():
    await client.change_presence(activity = discord.Game(name = "Valhalla"))
    print("Valkyria is ready")

# The channel ID where the bot will, providing it has the necessary permissions, send embedded messages. 
channel_id = 948332733267054623

# Send an embed with particular colors, random messages, and the user's avatar as a thumbnail when a user joins the server.
@client.event
async def on_member_join(member):
    print('Someone joined the server')
    embed = discord.Embed()
    embed.title = ":green_circle: Join"
    welcome_message_list = ['has joined the party', 'has been chosen', 'is here',
                            'has joined us', 'has entered Valhalla', 'has joined the server']          
    welcome_message = welcome_message_list[random.randint(0, len(welcome_message_list) - 1)]
    welcome_comment_list = [':wave:', 'Greetings and salutations.', 'Welcome to the club.',
                            'Welcome!', 'We hope you brought a cake.', "I've been waiting for ages for someone to come along.",
                            'Ciao!', 'Hola!', 'Hello!',
                            'Hallo!', 'Salut!', 'Hey there.',
                            'Howdy, partner.', "It's good to see you.", 'How is life sailing?',
                            'Enjoy your stay.', 'So, we meet at last.', "Cool.",
                            '']
    welcome_comment = welcome_comment_list[random.randint(0, len(welcome_comment_list) - 1)]
    embed.description = "{} **{}**. ".format(member.mention, welcome_message) + welcome_comment
    embed.set_thumbnail(url = member.avatar_url)
    embed.color = 0x78b159
    channel = client.get_channel(channel_id)
    await channel.send(embed = embed)

# Do the same as above when a user leaves the server. 
@client.event
async def on_member_remove(member):
    print('Someone left the server')
    embed = discord.Embed()
    embed.title = ":red_circle: Leave"
    unwelcome_comment_list = [':wave:', 'Take care, butterfly.', "Don't forget to come back!",
                              "Don't say goodbye!", 'Fare thee well.', "In case I don't see you - good afternoon, good evening, and good night!",
                              'Bye.', 'What a pity.', 'Catch you on the rebound.',
                              'Adieu!', 'Auf Wiedersehen!', 'Adios.',
                              'Ciao ciao.', 'Au revoir!', "Goodbye and don't cry, we won't.",
                              'It has been emotional.', 'Oh well.', 'It was fun while it lasted.', 
                              'Did I say something wrong?', 'That means more cake for us.', "We will probably never forget you... probably.",
                              '']
    unwelcome_comment = unwelcome_comment_list[random.randint(0, len(unwelcome_comment_list) - 1)]
    embed.description = "{} **has left the server**. ".format(member.mention) + unwelcome_comment
    embed.set_thumbnail(url = member.avatar_url)
    embed.color = 0xff473e
    channel = client.get_channel(channel_id)
    await channel.send(embed = embed)

# Run the bot's token.
client.run(TOKEN)
