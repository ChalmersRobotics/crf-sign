from ..character import Character
from ..effect import EffectBase
from ..effect_factory import EffectFactory


@EffectFactory.register("rainbow")
class RainbowEffect(EffectBase):
    def __init__(self, args):
        super().__init__(args)
        self.validate_args(args)

    def validate_args(self, args):
        pass

    def draw_frame(self, character: Character, timestamp):
        pass
