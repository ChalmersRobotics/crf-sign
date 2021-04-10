from discord.ext import commands
from sign.effect_factory import EffectFactory
from sign.sign import Sign


class SignControl(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.sign: Sign = bot.get_cog("Sign")

    @commands.command()
    async def all(self, ctx, *args):
        effect = EffectFactory.create_effect(args[0], args[1:])
        self.sign.c_effect = effect
        self.sign.r_inner_effect = effect
        self.sign.r_outer_effect = effect
        self.sign.f_effect = effect

    @commands.command()
    async def c(self, ctx, *args):
        effect = EffectFactory.create_effect(args[0], args[1:])
        self.sign.c_effect = effect

    @commands.command()
    async def r(self, ctx, *args):
        effect = EffectFactory.create_effect(args[0], args[1:])
        self.sign.r_inner_effect = effect
        self.sign.r_outer_effect = effect

    @commands.command()
    async def r_inner(self, ctx, *args):
        effect = EffectFactory.create_effect(args[0], args[1:])
        self.sign.r_inner_effect = effect

    @commands.command()
    async def r_outer(self, ctx, *args):
        effect = EffectFactory.create_effect(args[0], args[1:])
        self.sign.r_outer_effect = effect

    @commands.command()
    async def f(self, ctx, *args):
        effect = EffectFactory.create_effect(args[0], args[1:])
        self.sign.f_effect = effect
