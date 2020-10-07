import time
from discord.ext import commands

from src import CommandTracking
from src.config import Config
from src.handler.CommandHandler import CommandHandler
from src.handler.DatabaseHandler import DatabaseHandler

start_time = time.time()

client = commands.Bot(command_prefix=Config.PREFIX)


@client.event
async def on_ready():  # method that is called when bot is online
    print("[DONE] Bot is now online.")
    end_time = time.time()
    print(f"[DONE] Successfully loaded bot in {end_time - start_time} seconds")


@client.event
async def on_message(ctx):  # method that is called whenever a message is sent into discord server
    await CommandHandler.handle_commands(client, ctx)


def main():  # main function
    client.run(Config.BOT_TOKEN)


if __name__ == '__main__':
    main()
