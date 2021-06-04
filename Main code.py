import discord
import os
import random
from replit import db
from keep_alive import keep_alive

client = discord.Client();  

@client.event
async def on_ready():
   print("We've logged in as {0.user}".format(client)) 
   await client.get_channel(847833651303022645).send("Hello I am active")
#command terms
Greetings = ["Hi","Hello","hello","hi","Salutations","G'day","Hello sir"] 

Randnum = ["Random numbers","randnum","rand num","random numbers","random number","Random number"]
color = ["Red:red_circle: ","Blue:blue_circle: ","Green:green_circle: ","Yellow :yellow_circle: ","Lime","Purple:purple_circle: ","Brown :brown_circle: ","White:white_circle: ","Black:black_circle: "]
Goodthanks = ["I am good thanks","Good thanks","good thanks","I am good thank you very much","Thanks for asking","thanks for asking"]
Helpneeded = ["!Help","!help","Help me sir","help me","Help me"]

React = ["React to my message","Please react to my message","react to my message"]

@client.event
async def on_message(message):
  if message.author == client.user: 
    return
  msg = message.content
  if any(word in msg for word in Greetings):
    await message.channel.send("Hello how can I help you?")
  if message.content.startswith("How are you?"):
    await message.channel.send("Good thanks just doing some maths, how are you?")
  if message.content.startswith("How are you"):
    await message.channel.send("Good thanks just doing some maths, how are you?")
  if any(word in msg for word in Goodthanks):
    await message.channel.send("You need help with maths or anything?")
  if any(word in msg for word in Helpneeded):
    await message.channel.send("https://docs.google.com/document/d/e/2PACX-1vTXsrXsUuovt65Iqnjsp_4_iMeyUcuY5Eq6LiTRrbuHsUIdWuY_RKsQbTwXnIuPfD5DabfA0vAQIiWY/pub")
  if any(word in msg for word in Randnum):
    await message.channel.send(random.randint(0,1000))
  if any(word in msg for word in randcolor):
    await message.channel.send(random.choice(color))
  if any(word in msg for word in React):
    await message.add_reaction('👍')
keep_alive()
client.run("your tokens")
