import discord
from discord.ext.commands import Bot
from discord.ext import commands
import asyncio
import time
import random #random library

# ~WS~
from urllib.request import urlopen as uReq #grab the page itself
from bs4 import BeautifulSoup as soup #parse html text

my_url = 'http://steamcharts.com/app/381210#48h'

# opening up connection, grabbing the page
uClient = uReq(my_url)
# off load content into a variable
page_html = uClient.read()
# close client
uClient.close()

# html parsing
page_soup = soup(page_html, "html.parser")

# grab info we want
pop_game = page_soup.findAll("span",{"class":"num"})
heading_app = page_soup.findAll("div",{"id":"app-heading"})



#my_url2 = 'http://steamcommunity.com/id/INSERT STEAM ID HERE/games/'

#uClient = uReq(my_url2)
#page_html = uClient.read()
#uClient.close()
#page_soup = soup(page_html, "html.parser")

#game_rows = page_soup.findAll("div",{"id":"games_list_rows"})

my_url3 = 'https://www.timeanddate.com/countdown/halloween'

uClient = uReq(my_url3)
page_html = uClient.read()
uClient.close()
page_soup = soup(page_html, "html.parser")

digits = page_soup.findAll("div",{"class":"csvg-digit"})
dates = page_soup.findAll("div",{"class":"csvg-date"})

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

Players = ["campers",
"Absolute Idiots",
"Meatbags",
"Salty Individuals",
"Horror Fiends",
"Michael Fangirls",
"Self Loathers",
"Entity Worshipers",
"Dead Hard Users",
"BBQ Users"] 

Time_suffix = ["days",
"hours",
"minutes",
"seconds"]

@client.event
async def on_ready():
	print("Bot is ready!")

@client.event
async def on_message(message):
	if message.content.upper().startswith('!COMMANDS'):
		userID = message.author.id
		await client.send_message(message.channel, "try !wraith , !q , !mbs, !players, !hw")
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
	if message.content.upper().startswith('!PLAYERS'):
		userID = message.author.id
		
		population = pop_game[0].text.strip() #removes white space
		popTxt = str(population)
		playersNum = random.randint(0,len(Players))
		playersTxt = str(Players[playersNum])
		
		appHeader = heading_app[0]
		time_game = appHeader.div.abbr["title"]
		hour = int(time_game[11] + time_game[12])-6
		txt12h = "AM"
		if hour < 0:
			hour += 24
		if hour > 12:
			hour -= 12
			txt12h = "PM"
		min = time_game[14] + time_game[15]
		sec = time_game[17] + time_game[18]
		timeTxt = str(hour) + ":" + min + ":" + sec + " " + txt12h
		await client.send_message(message.channel,"There are " +(popTxt) + " " + (playersTxt) + " " + "playing DBD as of " + (timeTxt) + " CST. " + "<@%s>" % (userID))
	#if message.content.upper().startswith('!HOURS'):
	#	userID = message.author.id
	#	
	#	game_row = game_rows[0]
	#	if game_row.div["id"] == "game_381210":
	#		await client.send_message(message.channel, "<@%s> bing-BONG!" % (userID))
		#game = container.div.div["id"]
	if message.content.upper().startswith('!HW'):
		userID = message.author.id
		HwTxt = " " #initialize
		time_count = 0
		for digit in digits:
			hwTxt = digit.div.text
			HwTxt = HwTxt + " " + hwTxt + " " + Time_suffix[time_count]
			if time_count < 3:
				HwTxt += ","
			time_count += 1
		date = dates[0]
		zone = date.a["title"]
		zoneTxt = zone[20:] #truncate beginning of string so that we just have location
		await client.send_message(message.channel, (HwTxt) + " until Halloween in " + (zoneTxt) + "<@%s>" % (userID))
			
client.run("INSERT TOKEN HERE") #token from DC/devs/apps


