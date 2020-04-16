from discord.ext.commands import Bot
import random

BOT_PREFIX = "?"

# Discordapp, developers, applications, me, reveal token
TOKEN = 'Njk2NzYwNzYyMzM2NjczNzkz.XotdFg._ZIbYmFfrJjQmgoFXJsRt7vCKCk'

client = Bot(command_prefix=BOT_PREFIX)


@client.command(pass_context=True)
async def news(ctx):
    possible_responses = [
        ":hash: **A Contained Calamity** :dove: \n -----------:newspaper2: *news*-----------"
    ]
    await ctx.send(possible_responses[0])

client.run(TOKEN)
