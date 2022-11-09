import os
my_secret = os.environ['TOKEN']
import discord
import random 
import requests
import json
import time
import asyncio
from discord.ext import commands

intents = discord.Intents.all()
#add your prefix as an ! for your bot commands
bot = commands.Bot(command_prefix='!seb', intents=intents)
#print a message to the console when your bot is online

@bot.event
async def on_connect():
  print("Ultron program is running.🤖")
#this function will execute when a user messages !willis since that is the prefix plus the name of the function

@bot.command()
async def Name(ctx, name):
  await ctx.reply("Hello "+name+", how are you?")



@bot.command()#addition
async def Add(ctx,number1,number2):
  numberTotal=int(number1)+int(number2)
  numberTotal=str(numberTotal)
  await ctx.reply(number1+ " + "+ number2+" = "+numberTotal)

@bot.command()#multiplication
async def Multi(ctx,number1,number2):
  numberTotal=int(number1)*int(number2)
  numberTotal=str(numberTotal)
  await ctx.reply(number1+ " * "+ number2+" = "+numberTotal)

@bot.command()#subtraction
async def Sub(ctx,number1,number2):
  numberTotal=int(number1)-int(number2)
  numberTotal=str(numberTotal)
  await ctx.reply(number1+ " - "+ number2+" = "+numberTotal)

@bot.command()#division
async def Div(ctx,number1,number2):
  numberTotal=int(number1)/int(number2)
  numberTotal=str(numberTotal)
  await ctx.reply(number1+ " / "+ number2+" = "+numberTotal)





@bot.command()#greeting based on time
async def Time(ctx, time1, time2):
  resp="Sup"
  if "am" in time2.lower():
    resp="Good Morning"
  elif "pm" in time2.lower():
    if int(time1) < 5:
      resp="Good Afternoon"
    else:
      resp="Good Evening"
  else:
    resp="That does not work. Have a good day tho"
  await ctx.send(resp)



@bot.command()#sends one picture
async def pic(ctx):
  await ctx.reply("https://static.wikia.nocookie.net/beegyoshi/images/4/48/Yoshi.png/revision/latest/scale-to-width-down/180?cb=20200605140059")

picList=["https://i.imgflip.com/2/3xjh12.jpg","https://imgflip.com/s/meme/Y-U-No.jpg","https://c4.wallpaperflare.com/wallpaper/538/253/136/humor-memes-wallpaper-preview.jpg","https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcSQmtJc767w3DNxzkq9zAsDTFdRBTww-kgrZ-QzTdVV2AvsLT6WalmxRX_yE99AdS7u4m4&usqp=CAU","https://pics.me.me/when-u-get-no-text-back-16454062.png"]


@bot.command()#picture list
async def Memes(ctx):
  await ctx.reply(random.choice(picList))

@bot.command(aliases=["8Ball","8ball"])
async def EightBall(ctx,*,phrase: str):#Eight ball question answerer
  answerList=["For sure","Maybe","Heck no","mmm probably", "unlikely","Yeah","probably not"]
  await ctx.reply(phrase+": "+random.choice(answerList))

@bot.command(aliases=["RockPaperScissors","rps","Rps"])#rock paper scissors
async def RPS(ctx,choice):
  rpsList=["rock","paper","scissors"]
  botchoice=random.choice(rpsList)
  choice=choice.lower()#makes input lowercased

  if botchoice == choice:
    await ctx.reply("Oops I guess we tied because we both played "+choice+". Try again to see who wins.")
  elif botchoice=="scissors" and choice=="rock":
      await ctx.reply("Oof I guess I lost. Since you did rock and I did scissors.")
  elif botchoice=="paper" and choice=="rock":
      await ctx.reply("Haha I won because you played rock and I played paper.")
      
  elif botchoice=="rock" and choice=="paper":
      await ctx.reply("Oops I Lost because you played paper and I played rock. I'll beat you next time")
  elif botchoice=="scissors" and choice=="paper":
      await ctx.reply("Haha I win because you played paper and I played scissors. Try again to see who wins.")
  elif botchoice=="rock" and choice=="scissors":
      await ctx.reply("Haha I win because you played scissors and I played rock. Try again to see who wins.")
  elif botchoice=="paper" and choice=="scissors":
    await ctx.reply("Oops I Lost because you played scissors and I played paper. I'll beat you next time")
    
@bot.command()
async def rick(ctx):
  await ctx.reply("https://media.tenor.com/x8v1oNUOmg4AAAAd/rickroll-roll.gif")




#use a Joke Api to get a joke setup, wait a few second and deliver puncline
@bot.command()
async def Joke(ctx):
  #variable to hold url
  url = "https://official-joke-api.appspot.com/random_joke"
  #ask our bot to go to the url
  req = requests.get(url)
  #data variable that holds the json data that the api holds
  data =req.json()

#pull the joke setup from the json data
  setup=data["setup"]
  punchline=data["punchline"]
  await ctx.reply(setup)
  
  #import asyncio
  #pause your bot, but allow it to execute other functions during that time
  await asyncio.sleep(3)
  await ctx.reply(punchline)
  


@bot.command()
async def Weather(ctx,zip):
  my_secret_weather = os.environ['weatherAPIKey']

  #variable to hold url
  url = "https://api.openweathermap.org/data/2.5/weather?zip=" +zip+ ",us&appid="+my_secret_weather

  
  
  #ask our bot to go to the url
  req = requests.get(url)
  #data variable that holds the json data that the api holds
  data =req.json()
  
  w=data["weather"][0]["description"]
  temp=data["main"]["temp"]

  #convert to f
  temp=(temp - 273.15) * 9/5 + 32   
  await ctx.reply(w+" "+str(temp)+ "degree")




















################################################################
@bot.command()
async def IP(ctx, ip):

  url = "https://ipinfo.io/" + ip + "/geo"
  req = requests.get(url)

  data = req.json()

  descCity = data["city"]
  descRegion = data["region"]
  descLocation =data["loc"] 
  await ctx.reply("analyzing"+ip)
  await asyncio.sleep(2)
  await ctx.reply("Do you live in "+descCity+", "+descRegion+"?")
  await ctx.reply("I found you 👀"+descLocation)




################################################################



# @bot.command()
# async def UD(ctx):
#   url = 




























@bot.command()
async def seb(ctx):
  await ctx.reply( "I am sleepy")
my_secret = os.environ['TOKEN']
bot.run(my_secret)

#MTAzNDIyODI1ODc2NzYzNDQ0Mg.GU3GB7.QbN2RCGqzWaHb1Ysi2L0VCAElRhqarIzPaKbDs











