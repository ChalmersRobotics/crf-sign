from sign.character import Character
from sign.effect import EffectBase
from discord.ext import commands, tasks


class Sign(commands.Cog):
    def __init__(self):
        self.c_effect = None
        self.r_inner_effect = None
        self.r_outer_effect = None
        self.f_effect = None

        self.c = Character(100)
        self.r_inner = Character(100)
        self.r_outer = Character(100)
        self.f = Character(100)

    @tasks.loop(seconds=1.0/30)
    async def run_effects(self):
        pass

    def draw(self, character: Character, effect: EffectBase, timestamp):
        pass
