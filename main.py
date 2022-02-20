import os, time, discord, random
from dotenv import load_dotenv
from discord.ext import commands 

# creates a list of inspirational quotes
file = open('quotes.txt', 'r')
quotes = file.read().split('\n')

# function to pick a random quote
def random_quote():
    return quotes[random.randrange(0, len(quotes))]

# retrieves environment variables
load_dotenv()
token = os.getenv('TOKEN')

# initializes the bot and commands
bot = commands.Bot(command_prefix='!')

# logs the bot status
@bot.event 
async def on_ready():
    print("running!") # a test message
    print(bot.user) # prints the bot id to the terminal


# defines the mindfulness session command
@bot.command(name='mindfulness', help='Begin a work session with mindfulness breaks! \nEnter all times in minutes.')
async def mindfulness(ctx, session_length: int, frequency: int):

    session_length *= 60 #length of the work session
    frequency *= 60.0 # frequency of the reminders
    break_length = 300 # length of the mindfulness break: 5 min
    curr_time = time.time() # sets the current time
    stop = curr_time + session_length # sets session duration
    
    while curr_time <= stop:
        # mindfulness reminder message, generated after user-set time intervals
        time.sleep(frequency)
        await ctx.send('• take a break; take a breath-- it\'s time for a mindfulness session. •')

        # sends a randomly chosen quote
        time.sleep(5)
        await ctx.send(random_quote())

        # alerts user of the session's end
        time.sleep(break_length)
        await ctx.send('• time to reignite and get back to work! •')
        curr_time = time.time()

# defines the hydration reminder command
@bot.command(name='hydrate', help='Stay happy and hydrated! Set periodic water reminders. \nEnter all times in minutes.')
async def hydrate(ctx, session_length: int, frequency: int):
        session_length *= 60 #length of the work session
        frequency *= 60.0 # frequency of the reminders
        curr_time = time.time()
        stop = curr_time + session_length
        
        while curr_time <= stop:
            time.sleep(frequency)
            await ctx.send('• don\'t forget to drink-- take a sip of water and keep up the good work! •')
            curr_time = time.time()

# runs the bot!
bot.run(token)