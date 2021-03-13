from ..effect import EffectBase
from ..effect_factory import EffectFactory


@EffectFactory.register("rainbow")
class RainbowEffect(EffectBase):
    def validate_args(self, *args):
        raise ValueError
