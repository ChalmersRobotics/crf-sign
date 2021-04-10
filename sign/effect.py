from abc import ABCMeta, abstractmethod

from sign.character import Character


class EffectBase(metaclass=ABCMeta):
    def __init__(self, args):
        pass

    @abstractmethod
    def validate_args(self, *args):
        pass

    @abstractmethod
    def draw_frame(self, character: Character, timestamp):
        pass
