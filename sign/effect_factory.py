from typing import Callable
from .effect import EffectBase
import logging


class EffectFactory:
    registry = {}

    @classmethod
    def create_effect(cls, effect_name: str, args) -> EffectBase:
        if effect_name not in cls.registry:
            raise ValueError(f"Effect {effect_name} does not exist")

        effect_class = cls.registry[effect_name]
        effect = effect_class(args)

        return effect

    @classmethod
    def register(cls, name: str) -> Callable:
        def decorator(wrapped_class: EffectBase) -> EffectBase:
            if name in cls.registry:
                logging.warning('Executor %s already exists. Will replace it', name)
            cls.registry[name] = wrapped_class
            return wrapped_class

        return decorator
