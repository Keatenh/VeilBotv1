import discord
from discord.ext.commands import Bot
from discord.ext import commands
import asyncio
import time
import random #random library

# ~WS~
from urllib.request import urlopen as uReq #grab the page itself
from bs4 import BeautifulSoup as soup #parse html text

my_url1 = 'http://steamcharts.com/app/381210#48h'

my_url3 = 'https://www.timeanddate.com/countdown/halloween'
my_url4 = 'https://deadbydaylight.gamepedia.com/Dead_by_Daylight_Wiki'

def prepareSoup(url):
	# opening up connection, grabbing the page
	uClient = uReq(url)
	# off load content into a variable
	page_html = uClient.read()
	# close client
	uClient.close()
	# html parsing
	p_s = soup(page_html, "html.parser")
	return p_s

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

Characters = ["Dwight Fairfield",
"Meg Thomas",
"Claudette Morel",
"Jake Park",
"Nea Karlsson",
'William "Bill" Overbeck',
"David King",
"Laurie Strode",
"Ace Visconti",
"Feng Min",
"Quentin Smith",
"Trapper",
"Wraith",
"Hillbilly",
"Nurse",
"Huntress",
"Shape",
"Hag",
"Cannibal",
"Doctor",
"Nightmare"]

Prices = ["550",
"750"]

@client.event
async def on_ready():
	print("Bot is ready!")

@client.event
async def on_message(message):
	if message.content.upper().startswith('!COMMANDS'):
		#Diplays message letting the DC user know some commands they can type
		#userID = message.author.id
		await client.send_message(message.channel, 'try !wraith , !q , !mbs, !players, !hw, !shrine, !hours steamid')
	if message.content.upper().startswith('!WRAITH'):
		#Gives a joke response related to a game character
		userID = message.author.id
		await client.send_message(message.channel, "<@%s> bing-BONG!" % (userID))
	if message.content.upper().startswith('!SAY'):
		#Takes an input string from the user and displays it as a msg from the bot
		args = message.content.split(" ")
		#args[0] = !SAY
		#args[1] = Hey
		#args[2] = There
		#args[1:] = Hey There
		await client.send_message(message.channel, "%s" % (" ".join(args[1:])))
	if message.content.upper().startswith('!Q'): #& message.content.endswith('?'):
		#crystal ball / coinflip response to any input flagged as a question
		userID = message.author.id
		toss = random.randint(0,1)
		if toss == 0:
			await client.send_message(message.channel, "<@%s> ...Yes." % (userID))
		else: #toss == 1
			await client.send_message(message.channel, "<@%s> No..." % (userID))
	if message.content.upper().startswith('!MBS'):
		#picks a general response based on a random pick from a predefined list of words
		userID = message.author.id
		stageNum = random.randint(0,21)
		stageTxt = str(Stage[stageNum])
		await client.send_message(message.channel, (stageTxt) +" "+ "is the MOST Billy Stage."+ " " + "<@%s>" % (userID))
	if message.content.upper().startswith('!PLAYERS'):
		#scrapes the Steam webpage for info on how many users are playing DBD and displays last update time in CST
		userID = message.author.id
		
		page_soup = prepareSoup(my_url1)
		# grab info we want
		pop_game = page_soup.findAll("span",{"class":"num"})
		heading_app = page_soup.findAll("div",{"id":"app-heading"})
		
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
	if message.content.upper().startswith('!HOURS'):
		#gives feedback on the number of hours a steam user has logged in dbd based on steam profile
		userID = message.author.id
		#the user we are requesting info about
		userQmsg = message.content.split(" ")
		userQ = " ".join(userQmsg[1:])
		my_url2 = 'http://steamcommunity.com/id/' + (userQ) + '/'
		page_soup = prepareSoup(my_url2)
		# grab info we want
		game_rows = page_soup.findAll("div",{"class":"game_info"})
		
		game_name = " "
		for game_row in game_rows:
			game_names = game_row.findAll("div",{"class":"game_name"})
			game_n = game_names[0]
			game_name = game_n.text.strip()
			if game_name == "Dead by Daylight":
				game_details = game_row.findAll("div",{"class":"game_info_details"})
				game_d = game_details[0]
				game_detail = game_d.text.strip()
		
			
		if game_name == " ":
			game_detail = "Error: Not Found"
		
		await client.send_message(message.channel, (game_detail) + " " + "<@%s>" % (userID))
		
	if message.content.upper().startswith('!HW'):
		#Displays the current time until Halloween for the DC user's current global location
		userID = message.author.id
		
		page_soup = prepareSoup(my_url3)
		# grab info we want
		digits = page_soup.findAll("div",{"class":"csvg-digit"})
		dates = page_soup.findAll("div",{"class":"csvg-date"})
		
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
		
	if message.content.upper().startswith('!SHRINE'):
		userID = message.author.id
		
		page_soup = prepareSoup(my_url4)
		# grab info we want
		tables = page_soup.findAll("table",{"class":"wikitable"})
		
		table = tables[0].text.strip()
		table = " ".join(table.split())
		table = table[30:] #cut out labels in string
		for Character in Characters:
			table = table.replace(Character,"-> " + Character + " |")
		for Price in Prices:
			table = table.replace(Price, Price + '\n')
		#tableTxt = str(table)
		await client.send_message(message.channel, (table) + "<@%s>" % (userID))
		
			
client.run("INSERT TOKEN HERE") #token from DC/devs/apps


