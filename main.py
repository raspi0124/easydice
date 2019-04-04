import discord
import random
import configparser
config = configparser.ConfigParser()
config.read('/home/pi/easydice.conf')
client = discord.Client()
section1 = 'production'
#status defines if its main server or backup server. Main server: 1, Sub server: 2 and 3
#status = config.get(section1, 'status')
discord_token = config.get(section1, 'discord_token')
@client.event
async def on_ready():
	print('Logged in as')
	print(client.user.name)
	print(client.user.id)
	print('------')
	await client.change_presence(game=discord.Game(name='!ed help'))
@client.event #noqa
async def on_message(message):
#	if status == "2":
#		main_server_status = is_page_available(main_server_address)
	if message.content.startswith("!ed"):
		print(message.content)
		if message.content.startswith("!ed help"):
			m = "Usage: !ed dice [Number of result]Choice1 Choice2 Choice3"
			await client.send_message(message.channel, m)
		if message.content.startswith("!ed dice"):
			msg = message.content
			msg.replace("!ed dice ", "")
			splited = msg.split(" ")
			numofchoice = splited[0]
			splited.remove("numofchoice")
			m = random.sample(splited, int(numofchoice))
			print(random.sample(splited, int(numofchoice)))
			await client.send_message(message.channel, m)



client.run(discord_token)
