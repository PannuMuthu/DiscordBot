import discord
from discord.ext.commands import Bot

TOKEN = 'NTcwMzYyNjU4MzQwMjA4NjQx.XL-IkA.kbBohf6fWHW4Tph7rvkGTZzlxwY'
BOT_PREFIX = "bb$"

client = Bot(command_prefix=BOT_PREFIX)


@client.event
async def on_ready():
    print('Logged in as')
    print(client.user.name)
    print(client.user.id)
    print('------------------------')

@client.event
async def on_message(message):

    if client.user.mentioned_in(message) and ("@everyone" not in message.content) and ("@here" not in message.content):
        await channel.send("Hi!")

    await client.process_commands(message)

@client.command(pass_context = True)
async def ping(context):
    awair channel.send('pong!')


client.run(TOKEN)

client.loop.run_until_complete(client.logout())
