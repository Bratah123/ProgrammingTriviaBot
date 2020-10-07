from discord import Member, Guild, TextChannel

from src.commands.Command import Command
from src.config import Config


class CommandHandler:
    @staticmethod
    async def handle_commands(client, message):
        author = message.author
        msg = message.content
        guild = message.guild
        txt_channel = message.channel

        if not str(msg).startswith(Config.PREFIX):
            return

        can_use = author != client

        if not can_use:
            return

        cmds = [func for func in dir(Command) if callable(getattr(Command, func)) and not func.startswith("__")]
        for cmd in cmds:
            await getattr(Command, cmd)(client, txt_channel, author, msg)

    @staticmethod
    async def print_stacktrace(client, message, stacktrace):
        author = Member(message.author)
        msg = message.content
        guild = Guild(message.guild)
        txt_channel = TextChannel(message.channel)

        await txt_channel.send(str(stacktrace))
