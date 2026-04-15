import pygame
import random
pygame.init()
screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("Gold Gold GOld")
font = pygame.font.SysFont(None, 36)
running = True

Rarity = {
    "Consumer": (180, 180, 180),     # gray
    "Industrial": (120, 200, 255),   # light blue
    "Mil-Spec": (0, 120, 255),       # blue
    "Restricted": (170, 0, 255),     # purple
    "Classified": (255, 0, 200),     # pinkish
    "Covert": (255, 0, 0)            # red
}

weapons = [
    "AK-47",
    "M4A1-S",
    "AWP",
    "Glock-18",
    "Desert Eagle",
    "USP-S",
    "Karambit",
    "Butterfly Knife",
    "AK-47 | Fire Serpent",
    "AWP | Dragon Lore"
]

weapon = ""
rarity = ""
floatV = 0

while running:
    screen.fill((0, 0, 0))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                floatV = round(random.uniform(0.00, 1.00), 3)
                weapon = random.choice(weapons)
                rarity = random.choice(list(Rarity.keys()))

    text_color = Rarity .get(rarity, (255, 255, 255))
    text = font.render(
        f"{weapon}: float {floatV}",
        True,
            text_color
    )
    screen.blit(text, (40, 120))

    pygame.display.update()
pygame.quit()