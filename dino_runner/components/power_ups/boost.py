from dino_runner.utils.constants import BOOST, BOOST_TYPE
from dino_runner.components.power_ups.power_up import PowerUp


class BoostSpeed(PowerUp):
    def __init__(self):
        self.image = BOOST
        self.type = BOOST_TYPE
        self.duration = 5
        super().__init__(self.image, self.type, self.duration)
