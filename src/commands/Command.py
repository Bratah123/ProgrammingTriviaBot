import json
from random import randint

import discord

from src import CommandTracking
from src.commands.CommandDecorator import command
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
            return quiz_handler.is_correct_ans(m.content) and m.channel == txt_channel and m.author == author

        try:
            msg = await client.wait_for('message', check=check, timeout=12.0)
        except:
            await txt_channel.send('Times up, maybe next time.')
            del CommandTracking.list_of_current_players[author]
            return False
        del CommandTracking.list_of_current_players[author]
        print(msg)
        await txt_channel.send('Nice, you got the answer correct!')

        return True
