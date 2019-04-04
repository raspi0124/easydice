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
			m = "Usage: !ed dice [Number of result] Choice1 Choice2 Choice3 (No limit set for number of choice))\n\
			使い方: !ed dice [結果を何個出すか] 選択肢1 選択肢2 選択肢3 ..etc（選択肢は何個でも大丈夫です)\n\
			Example: !ed dice 2 Minecraft Wows Netflix → ['Minecraft', 'Netflix']\n\
			例: !ed dice 1 たいやき 今川焼 おにぎり → ['今川焼']"
			await client.send_message(message.channel, m)
		if message.content.startswith("!ed dice"):
			msg = message.content
			msg = msg.replace("!ed dice ", "")
			splited = msg.split(" ")
			print(splited)
			numofchoice = splited[0]
			#print(numofchoice)
			splited.pop(0)
			if len(splited) < int(numofchoice):
				m = "Error. Place specify Number that is less than total number of list"
			else:
				print(splited)
				m = random.sample(list(splited), int(numofchoice))
				print(random.sample(list(splited), int(numofchoice)))
			await client.send_message(message.channel, m)



client.run(discord_token)
