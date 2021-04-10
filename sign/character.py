class Character:
    def __init__(self, number_of_leds):
        self.number_of_leds = number_of_leds
        self.state = []

        for n in range(number_of_leds):
            self.state.append((0, 0, 0))
