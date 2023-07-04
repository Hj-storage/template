import discord
from discord.ext import commands

class Bot(commands.Bot):
    def __init__(self):
        super().__init__(
            command_prefix=commands.when_mentioned_or('b'),
            strip_after_prefix=True,
            allowed_mentions=discord.AllowedMentions(everyone=False, roles=False),
            case_insensitive=True,
            intents = discord.Intents.all(),
            owner_ids = {724447396066754643}
        )

    async def setup_hook(self):
        await self.load_extension('jishaku')

if __name__ == '__main__':
    bot = Bot()
    bot.run()