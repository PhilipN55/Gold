import pygame
import random
import json

pygame.init()
screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("Gold Gold Gold")
font = pygame.font.SysFont(None, 36)
running = True

Rarity = {
    "Consumer": (180, 180, 180),
    "Industrial": (120, 200, 255),
    "Mil-Spec": (0, 120, 255),
    "Restricted": (170, 0, 255),
    "Classified": (255, 0, 200),
    "Covert": (255, 0, 0),
    "Gold": (255,255,0)
}
RarityChans = {
    "Consumer": 39.75,
    "Industrial": 30,
    "Mil-Spec": 10,
    "Restricted": 5,
    "Classified": 3,
    "Covert": 2,
    "Gold": 0.25,
}
rarity_rank = {
    "Consumer": 1,
    "Industrial": 2,
    "Mil-Spec": 3,
    "Restricted": 4,
    "Classified": 5,
    "Covert": 6
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

drops = []
sorted_drops = []

top10 = []
weapon = ""
rarity = ""
floatV = 0
text_color = (255, 255, 255)

#"r" = read
with open("top10.json", "r") as f:
    top10 = json.load(f)
with open("top10.json", "r") as f:
    drops = json.load(f)

print(sorted_drops)
while running:
    screen.fill((0, 0, 0))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                floatV = round(random.uniform(0.00, 1.00), 3)
                weapon = random.choice(weapons)
                rarities = list(RarityChans.keys())
                chans = list(RarityChans.values())
                #weights bestämmer hur stor chans varje element har med hjälp av dict
                #k hur många värden den tar, [0] vilket värde den tar.
                #choices() kan man sätta vikter/chanser på inte choice()
                #[0] konverterar ["rarity"] till "rarity"
                rarity = random.choices(rarities, weights=chans, k=1)[0]
                text_color = Rarity[rarity]
                drops.append({
                    "name": weapon,
                    "rarity": rarity,
                    "float": floatV
                })
                #key är hur det sorteras
                #lambda x är anonym funktion utan namn
                #-rarity_rank gör att det blir rätt ordning högst-lägst
                #tuple är en lista som inte kan ändras
                #om rarity e samma sortera då på float
                sorted_drops = sorted(drops,key=lambda x: (-rarity_rank[x["rarity"]], x["float"]))
                top10 = sorted_drops[:10]
                #with ser till att filen stängs korrekt
                #"w" = write (skrivläge)
                #indent = mer luftigt i json filen
                #.json.dump konverterar kod till dict i json och sparar det
                with open("top10.json", "w") as f: json.dump(top10, f, indent=2)

    text = font.render(f"{weapon}: float {floatV}",True,text_color)
    text_rect = text.get_rect(center=(400, 120))
    screen.blit(text, text_rect)


    y  = 200
    for i, item in enumerate(top10):
        x = 150
        leaderboard_name = font.render(f"{1+i}.{item["name"]}",True,(255,255,255))
        leaderboard_rarity = font.render(f"{item["rarity"]}", True,Rarity[item["rarity"]])
        leaderboard_float = font.render(f"{item["float"]}", True,(255, 255, 255))

        screen.blit(leaderboard_name,(150,y))
        x += leaderboard_name.get_width()
        screen.blit(leaderboard_rarity,(x+10,y))

        screen.blit(leaderboard_float,(600,y))
        y += 30


    pygame.display.update()
pygame.quit()