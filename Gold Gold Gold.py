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
RarityValue = {
    "Consumer": 10,
    "Industrial": 25,
    "Mil-Spec": 100,
    "Restricted": 300,
    "Classified": 800,
    "Covert": 2000,
    "Gold": 10000
}
rarity_rank = {
    "Consumer": 1,
    "Industrial": 2,
    "Mil-Spec": 3,
    "Restricted": 4,
    "Classified": 5,
    "Covert": 6,
    "Gold": 7
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
max_inventory = 20
drops = []
sorted_drops = []
scroll_y = 0
top10 = []
weapon = ""
rarity = ""
worth = ""
inventory = False
loot = []
floatV = 0
text_color = (255, 255, 255)
#inventory
#Rect = pygame.Rect(50, 100, 140, 100)
RectColor = (25, 25, 25)


#------------------------------#
#"r" = read
with open("top10.json", "r") as f:
    top10 = json.load(f)

print(sorted_drops)
text1 = font.render("inventory = I", True,(255, 255, 255))

while running:
    screen.fill((0, 0, 0))
    screen.blit(text1, (620, 40))
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
                #värde kalkylator, int = avrunda
                value = int(RarityValue[rarity] * (1 + (1 - floatV) * 2))
                text_color = Rarity[rarity]
                drops.append({
                    "name": weapon,
                    "rarity": rarity,
                    "float": floatV,
                    "worth": value
                })
                loot.append({
                    "name": weapon,
                    "rarity": rarity,
                    "float": floatV,
                    "worth": value
                })
                #key är hur det sorteras
                #lambda x är anonym funktion utan namn
                #-rarity_rank gör att det blir rätt ordning högst-lägst
                #tuple är en lista som inte kan ändras
                #om rarity e samma sortera då på float
                drops_to_sort = (drops+top10)
                sorted_drops = sorted(drops_to_sort,key=lambda x: (-rarity_rank[x["rarity"]], x["float"]))
                top10 = sorted_drops[:10]
                drops = []
                #with ser till att filen stängs korrekt
                #"w" = write (skrivläge)
                #indent = mer luftigt i json filen
                #.json.dump konverterar kod till dict i json och sparar det
                with open("top10.json", "w") as f: json.dump(top10, f, indent=2)

    if len(loot) >= max_inventory:
        full_text = font.render("Inventory full!", True, (255, 255, 255))
        screen.blit(full_text, (300, 400))

    if event.type == pygame.KEYDOWN:
        if event.key == pygame.K_i:
            if inventory == False:
                inventory = True
            else:
                inventory = False

    if inventory == False:
        text = font.render(f"{weapon}: float {floatV}",True,text_color)
        text_rect = text.get_rect(center=(400, 120))
        screen.blit(text, text_rect)

        y  = 200
        #enumerate = (i, item)
        for i, item in enumerate(top10):
            x = 150
            leaderboard_name = font.render(f"{1+i}.{item["name"]}",True,Rarity[item["rarity"]])
            leaderboard_float = font.render(f"value {item["worth"]}kr", True,(255, 255, 255))

            screen.blit(leaderboard_name,(150,y))
            screen.blit(leaderboard_float,(600,y))
            y += 30
    # inventory
    if inventory == True:
        for i, item in enumerate(loot):
            if i < 20:
                rutor = 5 # antal rutor
                kolumn = i % rutor # % räkna om inom 0-4
                rad = i // rutor # // heltalsdivision

                x = 50 + kolumn * 160
                y = 100 + rad * 120
                pygame.draw.rect(screen, RectColor, pygame.Rect(x-40, y, 140, 100), border_radius=15)

                name_text = font.render(item["name"], True, Rarity[item["rarity"]])
                value_text = font.render(f'{item["worth"]}kr', True, (255, 255, 255))

                screen.blit(name_text, (x - 35, y + 10))
                screen.blit(value_text, (x - 35, y + 50))
    # ---------------------------------------------------------------------------------------------------#


    pygame.display.update()
pygame.quit()