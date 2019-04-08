import discord
import random
import configparser
import sys
config = configparser.ConfigParser()
config.read('../easydice.conf')
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
	userid = message.author.id
#	if status == "2":
#		main_server_status = is_page_available(main_server_address)
	if message.content.startswith("!ed"):
		print(message.content)
		if message.content.startswith("!ed help"):
			m = "Random command: Usage: !ed random [Number of result] Choice1 Choice2 Choice3 (No limit set for number of choice))\n\
			Example: !ed random 2 Minecraft Wows Netflix → ['Minecraft', 'Netflix']\n\
			Dice thing: Usage: !ed dice [Number of surface on dice]\n\
			Example: !ed dice 6 → 1\n\
			!ed help ja で日本語のヘルプも出せます。"
			await client.send_message(message.channel, m)
		if message.content.startswith("!ed help ja"):
			m = "使い方: ルーレット的なやつ: !ed random [結果を何個出すか] 選択肢1 選択肢2 選択肢3 ..etc（選択肢は何個でも大丈夫です)\n\
さいころみたいなやつ: !ed dice [面の数]\n\
例: ルーレットみたいなやつ: !ed random 1 たいやき 今川焼 おにぎり → ['今川焼']\n\
さいころみたいなやつ: !ed dice 6 "
			await client.send_message(message.channel, m)
		if message.content.startswith("!ed random"):
			msg = message.content
			msg = msg.replace("!ed random ", "")
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
		if message.content.startswith("!ed dice"):
			msg = message.content
			msg = msg.replace("!ed dice ", "")
			numsurface = int(msg)
			m = str(random.randint(1, numsurface))
			await client.send_message(message.channel, m)
		if message.content.startswith("!ed stop"):
			if userid == "326091178984603669":
				m = "Stopping process.."
				await client.send_message(message.channel, m)
				sys.exit()
			else:
				m = "You have no permission to do that!"
				await client.send_message(message.channel, m)
		if message.content == "!ed":
			m = "Type !ed help for help. !ed help ja で日本語のhelpも出せます。"
			await client.send_message(message.channel, m)


client.run(discord_token)
