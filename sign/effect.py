from abc import ABCMeta


class EffectBase(metaclass=ABCMeta):
    def __init__(self, **kwargs):
        pass

    def validate_args(self, *args):
        pass
