from dino_runner.utils.constants import HAMMER, HAMMER_TYPE
from dino_runner.components.power_ups.power_up import PowerUp


class Hammer(PowerUp):
    def __init__(self):
        self.image = HAMMER
        self.type = HAMMER_TYPE
        self.duration = 8
        super().__init__(self.image, self.type, self.duration)
