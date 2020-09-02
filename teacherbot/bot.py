import discord
from discord import ext
from commands import MainCommandsCog

class bot(ext.commands.Bot):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.add_cog(MainCommandsCog(self))

    async def on_ready(self):
        print('Bot activated')
