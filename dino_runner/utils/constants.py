import pygame
import os

# Global Constants
TITLE = "Snowy King"
SCREEN_HEIGHT = 600
SCREEN_WIDTH = 1100
FPS = 30
IMG_DIR = os.path.join(os.path.dirname(__file__), "..", "assets")

# Assets Constants
ICON = pygame.image.load(os.path.join(IMG_DIR, "Dino/KingRun1.png"))

RUNNING = [
    pygame.image.load(os.path.join(IMG_DIR, "Dino/KingRun1.png")),
    pygame.image.load(os.path.join(IMG_DIR, "Dino/KingRun2.png")),
    pygame.image.load(os.path.join(IMG_DIR, "Dino/KingRun3.png")),
    pygame.image.load(os.path.join(IMG_DIR, "Dino/KingRun4.png")),
    pygame.image.load(os.path.join(IMG_DIR, "Dino/KingRun5.png")),
    pygame.image.load(os.path.join(IMG_DIR, "Dino/KingRun6.png")),
    pygame.image.load(os.path.join(IMG_DIR, "Dino/KingRun7.png")),
    pygame.image.load(os.path.join(IMG_DIR, "Dino/KingRun8.png")),
]

RUNNING_SHIELD = [
    pygame.image.load(os.path.join(IMG_DIR, "Dino/Shield1.png")),
    pygame.image.load(os.path.join(IMG_DIR, "Dino/Shield2.png")),
    pygame.image.load(os.path.join(IMG_DIR, "Dino/Shield3.png")),
    pygame.image.load(os.path.join(IMG_DIR, "Dino/Shield4.png")),
    pygame.image.load(os.path.join(IMG_DIR, "Dino/Shield5.png")),
    pygame.image.load(os.path.join(IMG_DIR, "Dino/Shield6.png")),
    pygame.image.load(os.path.join(IMG_DIR, "Dino/Shield7.png")),
    pygame.image.load(os.path.join(IMG_DIR, "Dino/Shield8.png")),
]

RUNNING_BOOST = [
    pygame.image.load(os.path.join(IMG_DIR, "Dino/KingRunBoost.png")),
    pygame.image.load(os.path.join(IMG_DIR, "Dino/KingRun2.png")),
    pygame.image.load(os.path.join(IMG_DIR, "Dino/KingRun3.png")),
    pygame.image.load(os.path.join(IMG_DIR, "Dino/KingRun4.png")),
    pygame.image.load(os.path.join(IMG_DIR, "Dino/KingRunBoost2.png")),
    pygame.image.load(os.path.join(IMG_DIR, "Dino/KingRun6.png")),
    pygame.image.load(os.path.join(IMG_DIR, "Dino/KingRun7.png")),
    pygame.image.load(os.path.join(IMG_DIR, "Dino/KingRun8.png")),
]

RUNNING_HAMMER = [
    pygame.image.load(os.path.join(IMG_DIR, "Dino/KingRun1.png")),
    pygame.image.load(os.path.join(IMG_DIR, "Dino/KingRun2.png")),
    pygame.image.load(os.path.join(IMG_DIR, "Dino/KingRun3.png")),
    pygame.image.load(os.path.join(IMG_DIR, "Dino/Attack1.png")),
    pygame.image.load(os.path.join(IMG_DIR, "Dino/Attack2.png")),
    pygame.image.load(os.path.join(IMG_DIR, "Dino/KingRun6.png")),
    pygame.image.load(os.path.join(IMG_DIR, "Dino/KingRun7.png")),
    pygame.image.load(os.path.join(IMG_DIR, "Dino/KingRun8.png")),
]

JUMPING = [
    pygame.image.load(os.path.join(IMG_DIR, "Dino/Pulo1.png")),
    pygame.image.load(os.path.join(IMG_DIR, "Dino/Pulo2.png")),
    pygame.image.load(os.path.join(IMG_DIR, "Dino/Pulo3.png")),
    pygame.image.load(os.path.join(IMG_DIR, "Dino/Pulo4.png")),
]

JUMPING_SHIELD = [ 
    pygame.image.load(os.path.join(IMG_DIR, "Dino/Sub1.png")),
    pygame.image.load(os.path.join(IMG_DIR, "Dino/Sub2.png")),
    pygame.image.load(os.path.join(IMG_DIR, "Dino/Sub3.png")),
    pygame.image.load(os.path.join(IMG_DIR, "Dino/Sub4.png")),                  
]

JUMPING_BOOST = [
    pygame.image.load(os.path.join(IMG_DIR, "Dino/Pulo1.png")),
    pygame.image.load(os.path.join(IMG_DIR, "Dino/PuloBoost1.png")),
    pygame.image.load(os.path.join(IMG_DIR, "Dino/Pulo3.png")),
    pygame.image.load(os.path.join(IMG_DIR, "Dino/PuloBoost2.png")),
    ]

JUMPING_HAMMER =[ pygame.image.load(os.path.join(IMG_DIR, "Dino/Pulo1.png")),
                 pygame.image.load(os.path.join(IMG_DIR, "Dino/Attack1.png")),
                 pygame.image.load(os.path.join(IMG_DIR, "Dino/Attack2.png")),
                 pygame.image.load(os.path.join(IMG_DIR, "Dino/Pulo4.png")),
]
                

DUCKING = [
    pygame.image.load(os.path.join(IMG_DIR, "Dino/DUCK.png")),
    pygame.image.load(os.path.join(IMG_DIR, "Dino/DUCK2.png")),
]

DUCKING_SHIELD = [
    pygame.image.load(os.path.join(IMG_DIR, "Dino/DUCKSHIELD.png")),
    pygame.image.load(os.path.join(IMG_DIR, "Dino/DUCK2.png")),
]

DUCKING_HAMMER = [
    pygame.image.load(os.path.join(IMG_DIR, "Dino/DUCK.png")),
    pygame.image.load(os.path.join(IMG_DIR, "Dino/Attack2.png")),
]

DUCKING_BOOST = [
    pygame.image.load(os.path.join(IMG_DIR, "Dino/BuckBoost.png")),
    pygame.image.load(os.path.join(IMG_DIR, "Dino/DUCK2.png")),
]

SMALL_CACTUS = [
    pygame.image.load(os.path.join(IMG_DIR, "Cactus/SmallCactus1.png")),
    pygame.image.load(os.path.join(IMG_DIR, "Cactus/SmallCactus2.png")),
    pygame.image.load(os.path.join(IMG_DIR, "Cactus/SmallCactus3.png")),
]

LARGE_CACTUS = [
    pygame.image.load(os.path.join(IMG_DIR, "Cactus/LargeCactus1.png")),
    pygame.image.load(os.path.join(IMG_DIR, "Cactus/LargeCactus2.png")),
    pygame.image.load(os.path.join(IMG_DIR, "Cactus/LargeCactus3.png")),
]

BIRD = [
    pygame.image.load(os.path.join(IMG_DIR, "Bird/Bird1.png")),
    pygame.image.load(os.path.join(IMG_DIR, "Bird/Bird2.png")),
]

CLOUD = pygame.image.load(os.path.join(IMG_DIR, 'Other/Cloud.png'))
SHIELD = pygame.image.load(os.path.join(IMG_DIR, 'Other/shield.png'))
HAMMER = pygame.image.load(os.path.join(IMG_DIR, 'Other/hammer.png'))
BOOST = pygame.image.load(os.path.join(IMG_DIR,"Other/BoostSpeed.png"))

BG = pygame.image.load(os.path.join(IMG_DIR, 'Other/Track.png'))

HEART = pygame.image.load(os.path.join(IMG_DIR, 'Other/SmallHeart.png'))

PARALLAX = pygame.image.load(os.path.join(IMG_DIR, 'Other/mountains.png'))

DEFAULT_TYPE = "default"
SHIELD_TYPE = "shield"
HAMMER_TYPE = "hammer"
BOOST_TYPE = "boost"

MOUNTAINS = pygame.image.load(os.path.join(IMG_DIR, 'Other/mountains.png'))
