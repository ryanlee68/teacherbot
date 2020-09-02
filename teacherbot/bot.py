import discord
from discord.ext import commands, tasks
from teacherbot.commands import MainCommandsCog

class bot(commands.Bot):
    def __init__(self, *args, **kwargs):
        self.current_guild_id = kwargs.pop('current_guild')
        self.current_channel_id = kwargs.pop('current_channel')
        token = kwargs.pop('token')
        super().__init__(*args, **kwargs)
        self.add_cog(MainCommandsCog(self))
        self.run(token)


    async def on_ready(self):
        print('Bot activated')
        self.current_guild = self.get_guild(self.current_guild_id)
        self.current_channel = self.current_guild.get_channel(self.current_channel_id)
        self.take_attendance.start()
        self.check_other_tasks.start()

    @tasks.loop(seconds=1)
    async def check_other_tasks(self):
        if not self.take_attendance.is_running():
            error = self.take_attendance.get_task().exception()
            print(f"take_attendance() {error!r}")

    @tasks.loop(hours=24)
    async def take_attendance(self):
        # TODO: For now the attendence message
        # will just be basic text but in the future
        # the attendence message should be a nice looking embed
        print("take_attendance succesfully ran!")
        message = "Take attendence here!"

        self.periods = [1, 2, 3, 4, 5]

        message = await self.current_channel.send(message)
        print(message)

        for period in self.periods:
            await message.add_reaction(self.num2emoji(period))

    @staticmethod
    def num2emoji(num):
        num = int(num)
        if num == 1:
            return "1️⃣"
        elif num == 2:
            return "2️⃣"
        elif num == 3:
            return "3️⃣"
        elif num == 4:
            return "4️⃣"
        elif num == 5:
            return "5️⃣"
        elif num == 6:
            return "6️⃣"
        elif num == 7:
            return "7️⃣"
        elif num == 8:
            return "8️⃣"
        elif num == 9:
            return "9️⃣"
        elif num == 10:
            return "🔟"
        else:
            raise ValueError("num2emoji() does not support values larger than 10")

    async def close(self):
        print("Stopping the bot!")
        # self.check_other_tasks.stop()
        # self.take_attendance.stop()
        await super().close()
