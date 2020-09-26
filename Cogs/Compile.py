import datetime
import os
import discord
from discord.ext import commands

class Compile(commands.Cog):

    def __init__(self, app):
        self.app = app
    
    @commands.command(name = "compile", pass_context = True) #Compile code in many language - v2
    async def compile_command(self, ctx, *, command):
        languages = ["java", "python", "cpp", "c", "kotlin", "py"]
        lines = command.splitlines()
        language = lines[0][3:] 
        language.lower()
        if language in languages:
            size = len(lines)
            now = datetime.datetime.now()
            nowDatetime = now.strftime('%Y-%m-%d-%H-%M-%S')
            filename = "temp_" + str(nowDatetime) + "-" + str(ctx.message.author)
            if language == "kotlin":
                filename = filename + ".kt"
            else:
                filename = filename + "." + language
            text = open(filename, "w+")
            for i in range(1, size):
                if(i == size-1):
                    if lines[i] == "```":
                        break
                    else:
                        text.write(lines[i][:3])
                        break
                text.write(lines[i] + "\n")
            text.close()
            if language == "java":
                os.system("javac " + filename)
            else:
                a = 10
        else:
            await ctx.send(language + "는 지원되지 않는 언어입니다")
            await ctx.send("사용 가능한 메세지 목록:" + languages)

def setup(app):
    app.add_cog(Compile(app))