import discord
import os
import random
from keep_alive import keep_alive
from discord.ext import commands
import math

#declare the client as a variable
client = discord.Client()

@client.event
#When the bot has been activated
async def on_ready():
  #Say the the bot has been logged in as its username
    print("We've logged in as {0.user}".format(client))
    #Change the bot status into gaming
    await client.change_presence(activity=discord.Game('Coolmaths game'))

#comment terms
Greetings = [
    "Hi Nathan Chiu", "Hello", "hello", "hi Nathan Chiu", "Salutations",
      "G'day", "Hello Nathan Chiu", "Hey Nathan Chiu", "Hey"
]

React = [
    "React to my message", "Please react to my message", "react to my message",
    "Can you react to my message", "Nathan Chiu react to my message",
    "please react to my message", "Nathan Chiu please react to my message",
    "Add reaction", "React to my messages", "Please react",
    "react to my messages"
]

twoptwo = [
    "What's 2+2", "What is 2+2", "2+2", "Two plus two", "two plus two",
    "What's two plus two", "What is two plus two", "what's 2+2"
]

randcolor = [
    "Name me a color", "Random color", "random color", "random colour",
    "random colour", "What is your favourite color",
    "What is your favorite color", "What is your favourite colour",
    "What's your favourite color", "randcolor", "rand color"
]

Rudeswearwords = [
    "Nigger", "nigger", "Fuck you", "Shit", "Cum", "Piece of shit bot",
    "Piece of shit", "nigga"
]
Randnum = [
    "Random numbers", "randnum", "rand num", "random numbers", "random number",
    "Random number","Randnum"
]

Goodthanks = [
    "I am good thanks", "Good thanks", "good thanks",
    "I am good thank you very much", "Thanks for asking", "thanks for asking"
]
Helpneeded = [
    "!Help", "!help", "Help me Nathan Chiu", "help me nathan chiu",
    "Help me Nathan"
]
Quorapage = [
    "Quora page", "Send me your quora page", "quora page",
    "Please send me your quora page", "What's your quora", "What is your quora"
]
Wherefrom = [
    "Where are you from?", "Where are you from", "Which country are you from?",
    "where are you from?", "Are you from San Francisco"
]
Storethis = [
    "Store this","Natan can you please store this for me","Store this variable","store this","store this variable","Store this variables"
]
#Replies
NathanChiuarticle = [
    "https://medium.com/@nathan_chiu/from-sprinter-to-marathoner-d6b695e282f8",
    "https://medium.com/@nathan_chiu/finessing-your-way-through-sf-f2f3f8f12d35",
    "https://medium.com/@nathan_chiu/memorable-books-of-2017-according-to-an-english-and-business-major-c8dbbaedaeee",
    "https://medium.com/@nathan_chiu/changing-whartons-culture-one-mind-at-a-time-50b1e26a0366",
    "https://medium.com/@nathan_chiu/concreteness-in-teaching-math-79d7261094ce",
    "https://medium.com/@nathan_chiu/finding-the-courage-to-grow-c2a0cddb316b",
    "https://medium.com/@nathan_chiu/cello-from-the-other-side-reflections-of-a-cellist-bb683bf7a60c",
    "https://medium.com/@nathan_chiu/philadelphia-restaurant-week-highlights-793f79b5432e"
]
color = [
    "Red:red_circle: ", "Blue:blue_circle: ", "Green:green_circle: ",
    "Yellow :yellow_circle: ", "Lime", "Purple:purple_circle: ",
    "Brown :brown_circle: ", "White:white_circle: ", "Black:black_circle: "
]

@client.event
async def on_message(message):
  #Check if the message is sent by the user or not
    if message.author == client.user:
            return
      #put the message into the variable
    msg = message.content
    if any(word in msg for word in Greetings):
        await message.channel.send(
            "Hello, I am Nathan Chiu your favourite San Francisco math teacher, how can I help you?"
        )
    if message.content.startswith("How are you?"):
        await message.channel.send(
            "Good thanks just doing some maths, how are you?")
    if message.content.startswith("How are you"):
        await message.channel.send(
            "Good thanks just doing some maths, how are you?")
    if any(word in msg for word in Goodthanks):
        await message.channel.send("You need help with maths or anything?")
    if any(word in msg for word in Rudeswearwords):
        await message.channel.send("No you",tts=True)
        await message.add_reaction('🤡')
    if any(word in msg for word in Helpneeded):
        await message.channel.send(
            "https://docs.google.com/document/d/e/2PACX-1vTXsrXsUuovt65Iqnjsp_4_iMeyUcuY5Eq6LiTRrbuHsUIdWuY_RKsQbTwXnIuPfD5DabfA0vAQIiWY/pub"
        )
    if message.content.startswith("Send me one of your articles"):
        await message.channel.send(random.choice(NathanChiuarticle))
    if any(word in msg for word in Quorapage):
        await message.channel.send(
            "https://www.quora.com/profile/Nathan-Chiu-2")
    if any(word in msg for word in Randnum):
        await message.channel.send(random.randint(0, 1000))
    if any(word in msg for word in Wherefrom):
        await message.channel.send(":flag_us:")
    if any(word in msg for word in randcolor):
        await message.channel.send(random.choice(color))
    if any(word in msg for word in React):
        await message.add_reaction('👍')
    if any(word in msg for word in twoptwo):
        await message.channel.send("2+2=4-1=3 quick maths")
    if message.content.startswith("Kefir" or "kefir"):
        await message.channel.send("Ewww")
    if message.content.startswith("Solve this shit x^2 -2x - 8" or "Solve x^2 -2x - 8"):
      await message.reply(
                "x=4 x=-2", mention_author=True
            )
            #Search for trigger words in the array
    if any(word in msg for word in Storethis):
         await message.reply(
                "What do you want me to store?", mention_author=True #Mentions the author username
            )  
    if message.content.startswith("!say"):
      #Reply what the user have said
      await message.reply(msg)
      #Delete user messages
      await message.delete()
         
      
               
        
keep_alive()
client.run(os.getenv("Token"))
