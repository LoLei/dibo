"""
Wow, creating a Discord bot using discord.py is *much* simpler than making an
IRC bot from scratch. Just wanted to do some tests here.
"""
import os
from discord.ext.commands import Bot

# Settings/globals
TOKEN = os.environ['DIBO_TOKEN']
SETTINGS = {
    'prefix': '&',
    'owner': os.environ['DIBO_OWNER'],
    'owner_id': os.environ['DIBO_OWNER_ID']
}
BOT = Bot(command_prefix=SETTINGS['prefix'])


@BOT.event
async def on_ready():
    print('Logged in as {0.user}'.format(BOT))


# Commands
@BOT.command()
async def echo(ctx, arg):
    await ctx.send(arg)


@BOT.command()
async def info(ctx):
    await ctx.send('Bot owner: {}'.format(SETTINGS['owner']))


@BOT.command()
async def kick(ctx):
    if ctx.message.author.id == int(SETTINGS['owner_id']):
        await ctx.send('Leaving guild.')
        await ctx.guild.leave()


def main():
    BOT.run(TOKEN)


if __name__ == "__main__":
    main()
