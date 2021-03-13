from discord.ext import commands, tasks
from datetime import datetime
from sign.effect_factory import EffectFactory


class SignControl(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.opc = bot.get_cog("OpcControl")
        #self.run_effects.start()
        self.test = "a"

    @commands.command()
    async def all(self, ctx, *args):
        await self.set_effect(ctx, "all", args)
        return 0

    @commands.command()
    async def c(self, ctx, *args):
        await self.set_effect(ctx, "c", args)
        return 0

    @commands.command()
    async def r(self, ctx, *args):
        await self.set_effect(ctx, "r", args)
        return 0

    @commands.command()
    async def r_inner(self, ctx, *args):
        await self.set_effect(ctx, "r_inner", args)
        return 0

    @commands.command()
    async def r_outer(self, ctx, *args):
        await self.set_effect(ctx, "r_outer", args)
        return 0

    @commands.command()
    async def f(self, ctx, *args):
        await self.set_effect(ctx, "f", args)
        return 0

    async def set_effect(self, ctx, letter, args):
        effect = EffectFactory.create_effect(args[0])
        effect.validate_args(args)
        return 0

    @tasks.loop(seconds=1.0/30)
    async def run_effects(self):
        print(self.test)
        return 0
