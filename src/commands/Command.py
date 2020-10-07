import json
from random import randint

import discord

from src import CommandTracking
from src.commands.CommandDecorator import command
from src.handler.DatabaseHandler import DatabaseHandler
from src.handler.QuizHandler import QuizHandler


class Command:

    @staticmethod
    @command(cmd=["trivia", "quiz", "questions"])
    async def handle_trivia(client, txt_channel, author, msg) \
            -> "Sends author a programming problem to solve.":
        if CommandTracking.list_of_current_players.get(author) is not None:
            await txt_channel.send('Please complete your first trivia first.')
            return False
        else:
            CommandTracking.list_of_current_players[author] = True
        with open('D:/TriviaBot/ProgrammingTriviaBot/questions/Questions.json', 'r') as json_file:
            data = json.load(json_file)
            quiz_handler = QuizHandler(str(randint(0, len(data) - 1)))
            json_file.close()

        embed_msg = discord.Embed(title="Programming Trivia", description="You have 12 seconds to answer! \n"
                                                                          "Note: Type in 'error' if the answer will "
                                                                          "return an error.",
                                  colour=0x00FFFF)
        embed_msg.add_field(name="Language", value=quiz_handler.language, inline=False)
        embed_msg.add_field(name="Code", value=quiz_handler.code, inline=False)
        await txt_channel.send(embed=embed_msg)

        def check(m):
            return quiz_handler.is_correct_ans(m.content) and m.author == author and m.channel == txt_channel

        amount_of_points = randint(1, 10)
        try:
            user_msg = await client.wait_for('message', check=check, timeout=12.0)
            del CommandTracking.list_of_current_players[author]
            if DatabaseHandler.is_already_user(author.id):
                DatabaseHandler.add_points(author.id, amount_of_points)
            else:
                DatabaseHandler.add_user(author.id)
            await txt_channel.send('Nice, you got the answer correct! Have some points!')
        except:
            await txt_channel.send('Times up, maybe next time.')
            del CommandTracking.list_of_current_players[author]
            return False

        return True

    @staticmethod
    @command(cmd=["stats"])
    async def handle_stats(client, txt_channel, author, msg) \
            -> "Show user's their stats.":
        if not DatabaseHandler.is_already_user(author.id):
            DatabaseHandler.add_user(author.id)

        embed_msg = discord.Embed(title="Stats", description=f"{author.name}'s stats", colour=0x00FFFF)
        embed_msg.add_field(name="Quiz Points", value=DatabaseHandler.get_points(author.id), inline=False)

        await txt_channel.send(embed=embed_msg)

    @staticmethod
    @command(cmd=["debug", "test"])
    async def handle_debug_trivia(client, txt_channel, author, msg) \
            -> "Lets you test specific trivia questions":
        args = msg.split(" ")
        if author.id != 207371595113562124:
            await txt_channel.send("You do not have permissions for this command.")
            return False
        if len(args) < 2:
            await txt_channel.send("Please provide more arguments, !debug <id>")
            return False
        question = args[1]

        quiz_handler = QuizHandler(question)

        embed_msg = discord.Embed(title="Programming Trivia", description="You have 12 seconds to answer! \n"
                                                                          "Note: Type in 'error' if the answer will "
                                                                          "return an error.",
                                  colour=0x00FFFF)
        embed_msg.add_field(name="Language", value=quiz_handler.language, inline=False)
        embed_msg.add_field(name="Code", value=quiz_handler.code, inline=False)
        await txt_channel.send(embed=embed_msg)
        return True
