import discord
from discord.ext.commands import Bot
from discord.ext import commands
import asyncio
import time
import random #random library

Client = discord.Client()
client = commands.Bot(command_prefix = "!")

Stage = ["Coal Tower",
"Groaning Storehouse",
"Ironworks of Misery",
"Shelter Woods",
"Suffocation Pit",
"Azarov's Resting Place",
"Blood Lodge",
"Gas Heaven",
"Wretched Shop",
"Wreckers' Yard",
"Fractured Cowshed",
"The Thompson House",
"Torment Creek",
"Rancid Abattoir",
"Rotten Fields",
"Disturbed Ward",
"Lampkin Lane",
"The Pale Rose",
"Grim Pantry",
"Treatment Theatre",
"Mother's Dwelling",
"Badham Preschool"]

@client.event
async def on_ready():
	print("Bot is ready!")

@client.event
async def on_message(message):
	if message.content.upper().startswith('!COMMANDS'):
		userID = message.author.id
		await client.send_message(message.channel, "try !wraith , !q , !mbs")
	if message.content.upper().startswith('!WRAITH'):
		userID = message.author.id
		await client.send_message(message.channel, "<@%s> bing-BONG!" % (userID))
	if message.content.upper().startswith('!SAY'):
		args = message.content.split(" ")
		#args[0] = !SAY
		#args[1] = Hey
		#args[2] = There
		#args[1:] = Hey There
		await client.send_message(message.channel, "%s" % (" ".join(args[1:])))
	if message.content.upper().startswith('!Q'): #& message.content.endswith('?'):
		userID = message.author.id
		toss = random.randint(0,1)
		if toss == 0:
			await client.send_message(message.channel, "<@%s> ...Yes." % (userID))
		else: #toss == 1
			await client.send_message(message.channel, "<@%s> No..." % (userID))
	if message.content.upper().startswith('!MBS'):
		userID = message.author.id
		stageNum = random.randint(0,21)
		stageTxt = str(Stage[stageNum])
		await client.send_message(message.channel, (stageTxt) +" "+ "is the MOST Billy Stage."+ " " + "<@%s>" % (userID))
		
client.run("INSERT TOKEN HERE") #token from DC/devs/apps


