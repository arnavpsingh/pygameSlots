import pygame
import os
import random
import time
from pygame import mixer
os.environ['SDL_VIDEO_WINDOW_POS'] = '10, 10'
pygame.init()

def drawLights(screen, circleCounter, bgColor):
    for i in range(20, 600, 20):
        pygame.draw.circle(screen, (bgColor), (i, 25), 10)
        pygame.draw.circle(screen, (bgColor), (i, 585), 10)
        pygame.draw.circle(screen, (227, 183, 39), (i, 25), 10, 2)
        pygame.draw.circle(screen, (227, 183, 39), (i, 585), 10, 2)
    for i in range(25, 600, 20):
        pygame.draw.circle(screen, (bgColor), (20, i), 10)
        pygame.draw.circle(screen, (bgColor), (580, i), 10)
        pygame.draw.circle(screen, (227, 183, 39), (20, i), 10, 2)
        pygame.draw.circle(screen, (227, 183, 39), (580, i), 10, 2)
    
    
    if circleCounter == 20:
        for i in range(circleCounter, 600, 20):
            if i % 40 == 0:
                pygame.draw.circle(screen, (224, 227, 39), (i, 25), 8)
                pygame.draw.circle(screen, (224, 227, 39), (i, 585), 8)
            else:
                pygame.draw.circle(screen, (bgColor), (i, 25), 8)
                pygame.draw.circle(screen, (bgColor), (i, 585), 8)
        for i in range(circleCounter + 5, 600, 20):
            if (i - 5) % 40 == 0:
                pygame.draw.circle(screen, (224, 227, 39), (20, i), 8)
                pygame.draw.circle(screen, (224, 227, 39), (580, i), 8)
            else:
                pygame.draw.circle(screen, (bgColor), (20, i), 8)
                pygame.draw.circle(screen, (bgColor), (580, i), 8)

        circleCounter = 0
        return circleCounter
    else:
        for i in range(circleCounter, 600, 20):
            if i % 40 == 0:
                pygame.draw.circle(screen, (bgColor), (i, 25), 8)
                pygame.draw.circle(screen, (bgColor), (i, 585), 8)
            else:
                pygame.draw.circle(screen, (224, 227, 39), (i, 25), 8)
                pygame.draw.circle(screen, (224, 227, 39), (i, 585), 8)
        for i in range(circleCounter + 5, 600, 20):
            if (i - 5) % 40 == 0:
                pygame.draw.circle(screen, (bgColor), (20, i), 8)
                pygame.draw.circle(screen, (bgColor), (580, i), 8)
            else:
                pygame.draw.circle(screen, (224, 227, 39), (20, i), 8)
                pygame.draw.circle(screen, (224, 227, 39), (580, i), 8)
                
        circleCounter = 20
        return circleCounter

def genDeck():
    suites = ["Hearts", "Diamonds", "Clubs", "Spades"]
    ranks = ["Ace", "2", "3", "4", "5", "6", "7", "8", "9", "10", "Jack", "Queen", "King"]
    deck = []
    for suite in suites:
        for rank in ranks:
            deck.append(rank + " of " + suite)
    return deck

def startScreen(screen):
    screen.fill((50, 255, 150))


    font = pygame.font.Font('VT323-Regular.ttf', 30)

    x = 125
    y = 150
    text = font.render("Welcome to Slots!", True, (100, 198, 245))
    text_2 = font.render("Press space to start", True, (100, 198, 245))
    textRect = pygame.Surface((text.get_width(), text.get_height()))
    textRect_2 = pygame.Surface((text_2.get_width(), text_2.get_height()))
    textRect.fill((50, 255, 150))
    textRect_2.fill((50, 255, 150))
    screen.blit(textRect, (x, y))


    while x != 700:
        x += 0.5
        pygame.display.update()
        screen.blit(text, (125, 150))
        screen.blit(textRect, (x, y))
    x = 125
    y = 200
    while x != 700:
        x += 0.5
        pygame.display.update()
        screen.blit(text_2, (125, 200))
        screen.blit(textRect_2, (x, y))
    

    pygame.display.update()
    start = True
    while start:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    return True

def menuScreen(screen, username, money, spins):
    mixer.music.load("menuMusic.wav")
    mixer.music.play(1)
    screen.fill((50, 200, 50))
    font = pygame.font.Font('VT323-Regular.ttf', 25)
    font_2 = pygame.font.Font('VT323-Regular.ttf', 75)
    text_1 = font_2.render("Play", True, (50, 100, 150))
    text_2 = font.render("Your Balance: $" + str(money), True, (100, 50, 200))
    text_3 = font.render("Your Username: " + username, True, (245, 100, 50))
    text_4 = font_2.render("Bank", True, (252, 102, 3))
    text_5 = font.render("Spins Left: " + spins, True, (100, 50, 200))
    text_6 = font_2.render("Mini-Game", True, (13, 196, 200))

    textRect_1 = text_1.get_rect()
    textRect_2 = text_2.get_rect()
    textRect_3 = text_3.get_rect()
    textRect_4 = text_4.get_rect()
    textRect_5 = text_5.get_rect()
    textRect_6 = text_6.get_rect()

    textRect_1.center = (300, 150)
    textRect_2.center = (200, 50)
    textRect_3.center = (450, 50)
    textRect_4.center = (300, 400)
    textRect_5.center = (160, 75)
    textRect_6.center = (300, 275)

    screen.blit(text_1, textRect_1)
    screen.blit(text_2, textRect_2)
    screen.blit(text_3, textRect_3)
    screen.blit(text_4, textRect_4)
    screen.blit(text_5, textRect_5)
    screen.blit(text_6, textRect_6)


    pygame.display.update()

    loop = True
    circleCounter = 20
    while loop:
        isPlaying = mixer.music.get_busy()
        if isPlaying == False:
            mixer.music.load("menuMusic loop.wav")
            mixer.music.play(1)
        clock = pygame.time.Clock()
        clock.tick(15)
        circleCounter = drawLights(screen, circleCounter, (50, 200, 50))
        pygame.display.update()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                x, y = event.pos
                if textRect_1.collidepoint((x, y)):
                    mixer.music.stop()
                    return "p"
                elif textRect_4.collidepoint((x, y)):
                    mixer.music.stop()
                    return "b"
                elif textRect_6.collidepoint((x, y)):
                    mixer.music.stop()
                    return "m"
            if event.type == pygame.MOUSEMOTION:
                x, y = event.pos
                if textRect_1.collidepoint((x, y)):
                    text_1 = font_2.render("Play", True, (25, 50, 200))
                    screen.blit(text_1, textRect_1)
                    pygame.display.update()
                elif textRect_4.collidepoint((x, y)):
                    text_4 = font_2.render("Bank", True, (255, 0, 0))
                    screen.blit(text_4, textRect_4)
                    pygame.display.update()
                elif textRect_6.collidepoint((x, y)):
                    text_6 = font_2.render("Mini-Game", True, (13, 94, 23))
                    screen.blit(text_6, textRect_6)
                    pygame.display.update()
                else:
                    text_1 = font_2.render("Play", True, (50, 100, 150))
                    text_4 = font_2.render("Bank", True, (252, 102, 3))
                    text_6 = font_2.render("Mini-Game", True, (13, 196, 200))
                    screen.blit(text_1, textRect_1)
                    screen.blit(text_4, textRect_4)
                    screen.blit(text_6, textRect_6)
                    pygame.display.update()

def bank(screen, money, username, existingSpins):
    font_4 = pygame.font.Font('VT323-Regular.ttf', 15)
    if int(money) < 0:
        text = font_4.render("No balance. You must buy spins with your own money at the start of the game", True, (255, 0, 0))
        textRect = text.get_rect()
        textRect.center = (300, 300)
        screen.blit(text, textRect)
        pygame.display.update()
        pygame.time.wait(1500)
        return
    spins = [
    os.path.join("spins", "25spins.png"),
    os.path.join("spins", "50spins.png"),
    os.path.join("spins", "100spins.png"),
    ]

    screen.fill((100, 50, 250))
    font = pygame.font.Font('VT323-Regular.ttf', 20)
    font_2 = pygame.font.Font('VT323-Regular.ttf', 50)
    font_3 = pygame.font.Font('VT323-Regular.ttf', 30)
    strings = ["25 Spins: 250", "50 Spins: 500", "100 Spins: 1000"]
    text_1 = font_2.render("Welcome to the bank!", True, (245, 10, 50))
    text_2 = font.render("Your balance: " + str(money), True, (10, 50, 245))
    text_3 = font.render("Click on the spins you want to buy", True, (50, 245, 10))
    text_4 = font_2.render("Exit", True, (150, 10, 50))
    text_5 = font.render("Spins Left: " + str(existingSpins), True, (10, 245, 245))


    
    textRect_1 = text_1.get_rect()
    textRect_1.center = (300, 100)
    screen.blit(text_1, textRect_1)

    


    textRect_3 = text_3.get_rect()
    textRect_3.center = (300, 150)
    screen.blit(text_3, textRect_3)

    textRect_4 = text_4.get_rect()
    textRect_4.center = (500, 50)
    screen.blit(text_4, textRect_4)

    screen.blit(text_5, (15, 50 - (text_5.get_height() / 2)))
    screen.blit(text_2, (100 - (text_2.get_width() / 2), 30 - (text_2.get_height() / 2)))
    pygame.display.update()

    imageRects = []

    for i in range(0, 3):
        image = pygame.image.load(spins[i])
        image = pygame.transform.scale(image, (187, 187))
        imageRect = image.get_rect()
        imageRect.center = (20 + (i * 187) + (image.get_width() / 2), 210 + (image.get_height() / 2))
        imageRects.append(imageRect)
        screen.blit(image, (20 + (i * 187), 210))

        text = font_3.render(strings[i], True, (100 * (i), 50 * (i + 1), 255 / (i + 1)))
        textRect = text.get_rect()
        screen.blit(text, (50 + (i * 187) - (i * 5), 500 + (i * 25)))
    pygame.display.update()
    mixer.Channel(0).play(mixer.Sound("bankMusic.wav"))
    
    while True:
        isPlaying = mixer.Channel(0).get_busy()
        if isPlaying == False:
            mixer.Channel(0).play(mixer.Sound("bankMusic loop.wav"), -1)
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                x, y = event.pos
                if textRect_4.collidepoint((x, y)):
                    mixer.Channel(0).stop()
                    return 
                elif imageRects[0].collidepoint((x, y)):
                    mixer.Channel(0).set_volume(0.0)
                    mixer.Channel(1).play(mixer.Sound("buySpin.wav"))
                    money = int(money)
                    existingSpins = int(existingSpins)
                    existingSpins += 25 
                    money -= 250
                    updateBank(money, username)
                    updateSpins(username, existingSpins)
                elif imageRects[1].collidepoint((x, y)):
                    mixer.Channel(0).set_volume(0.0)
                    mixer.Channel(1).play(mixer.Sound("buySpin.wav"))
                    money = int(money)
                    existingSpins = int(existingSpins)
                    existingSpins += 50
                    money -= 500
                    updateBank(money, username)
                    updateSpins(username, existingSpins)
                elif imageRects[2].collidepoint((x, y)):
                    mixer.Channel(0).set_volume(0.0)
                    mixer.Channel(1).play(mixer.Sound("buySpin.wav"))
                    money = int(money)
                    existingSpins = int(existingSpins)
                    existingSpins += 100
                    money -= 1000
                    updateBank(money, username)
                    updateSpins(username, existingSpins)
                pygame.draw.rect(screen, (100, 50, 250), (100 - (text_2.get_width() / 2), 30 - (text_2.get_height() / 2), text_2.get_width(), text_2.get_height()))
                pygame.draw.rect(screen, (100, 50, 250), (15, 50 - (text_5.get_height() / 2), text_5.get_width(), text_5.get_height()))
                text_2 = font.render("Your balance: " + str(money), True, (10, 50, 245))
                text_5 = font.render("Spins Left: " + str(existingSpins), True, (10, 245, 245))
                screen.blit(text_5, (15, 50 - (text_5.get_height() / 2)))
                screen.blit(text_2, (100 - (text_2.get_width() / 2), 30 - (text_2.get_height() / 2)))


            if event.type == pygame.MOUSEBUTTONUP:
                mixer.Channel(0).set_volume(0.5)
            if event.type == pygame.MOUSEMOTION:
                x, y = event.pos
                if textRect_4.collidepoint((x, y)):
                    text_4 = font_2.render("Exit", True, (255, 0, 0))
                    screen.blit(text_4, textRect_4)
                    pygame.display.update()
                elif imageRects[0].collidepoint((x, y)):
                    image = pygame.image.load(spins[0])
                    image = pygame.transform.scale(image, (250, 250))
                    screen.blit(image, (20 + (0 * 187), 210))
                    pygame.display.update()
                elif imageRects[1].collidepoint((x, y)):
                    image = pygame.image.load(spins[1])
                    image = pygame.transform.scale(image, (250, 250))
                    screen.blit(image, (20 + (1 * 187), 210))
                    pygame.display.update()
                elif imageRects[2].collidepoint((x, y)):
                    image = pygame.image.load(spins[2])
                    image = pygame.transform.scale(image, (250, 250))
                    screen.blit(image, (20 + (2 * 187), 210))
                    pygame.display.update()
                else:
                    text_4 = font_2.render("Exit", True, (150, 10, 50))
                    screen.blit(text_4, textRect_4)
                    pygame.draw.rect(screen, (100, 50, 250), (20, 210, 580, 250))
                    for i in range(0, 3):
                        image = pygame.image.load(spins[i])
                        image = pygame.transform.scale(image, (187, 187))
                        imageRect = image.get_rect()
                        imageRect.center = (20 + (i * 187) + (image.get_width() / 2), 210 + (image.get_height() / 2))
                        imageRects.append(imageRect)
                        screen.blit(image, (20 + (i * 187), 210))
                    pygame.display.update()
               
def genRandom():
    objects = ["t", "e", "f", "p", "1", "5"]
    finalObjects = []
    weight = 1
    weights = [1, 1, 1, 1, 1, 1]
    for i in range(0, 3):
        randomObjects = random.choices(objects, weights)
        randomObject = randomObjects[0]
        index = objects.index(randomObject)
        weights[index] *= 0.75
        finalObjects.append(randomObject)
    return finalObjects

def drawObjects(screen):
    counter = 0
    finalObjects = []
    finalImageList = []
    while counter < 45:
        objectsList = genRandom()
        finalObjects = objectsList
        imageList = []
        for i in objectsList:
            image = 0
            if i == "t":
                image = pygame.image.load(os.path.join("slots", "tree.png"))
            elif i == "e":
                image = pygame.image.load(os.path.join("slots", "earth.png"))
            elif i == "f":
                image = pygame.image.load(os.path.join("slots", "fish.png"))
            elif i == "p":
                image = pygame.image.load(os.path.join("slots", "no_pollution.png"))
            elif i == "1":
                image = pygame.image.load(os.path.join("slots", "1coin.png"))
            elif i == "5":
                image = pygame.image.load(os.path.join("slots", "5coin.png"))
            imageList.append(image)
        finalImageList = imageList
        for i in range(len(imageList)):
            if objectsList[i] == "1" or objectsList[i] == "5":
                pygame.draw.rect(screen, (255, 255, 255), (210 + (i * 65), 245, 45, 85))
                screen.blit(imageList[i], (232 + (i * 65) - (imageList[i].get_width() / 2), 287 - (imageList[i].get_height() / 2)))
                pygame.display.update()
            else:
                imageList[i] = pygame.transform.scale(imageList[i], (45, 85))
                screen.blit(imageList[i], (210 + (i * 65), 245))
                pygame.display.update()
        counter += 1
    return finalObjects, imageList

def processWin(objects, username, screen):
    font = pygame.font.Font('VT323-Regular.ttf', 30)
    pygame.draw.rect(screen, (50, 50, 150), (225, 70, 150, 25))
    for i in objects:
        if objects.count(i) == 3:
            if i == "1" or i == "5":
                mixer.Channel(0).play(mixer.Sound("megaJackpot.wav"))
                money = getMoney(username)
                money = int(money) 
                money += 1000000
                updateBank(money, username)
                text = font.render("Mega Jackpot", True, (242, 255, 0))
                textRect = text.get_rect()
                textRect.center = (300, 80)
                screen.blit(text, textRect)
                moneyText = font.render("Money: " + str(money), True, (255, 0, 100))
                pygame.draw.rect(screen, (50, 50, 150), (35, 40, moneyText.get_width(), moneyText.get_height()))
                screen.blit(moneyText, (35, 40))
                return
            else:
                mixer.Channel(0).play(mixer.Sound("jackpot.wav"))
                money = getMoney(username)
                money = int(money) 
                money += 50000
                updateBank(money, username)
                text = font.render("Jackpot", True, (242, 255, 0))
                textRect = text.get_rect()
                textRect.center = (300, 80)
                screen.blit(text, textRect)
                moneyText = font.render("Money: " + str(money), True, (255, 0, 100))
                pygame.draw.rect(screen, (50, 50, 150), (35, 40, moneyText.get_width(), moneyText.get_height()))
                screen.blit(moneyText, (35, 40))
                return 
        if objects.count(i) == 2:
            if i == "1" or i == "5":
                mixer.Channel(0).play(mixer.Sound("win.wav"))
                money = getMoney(username)
                money = int(money) 
                money += 500
                updateBank(money, username)
                text = font.render("Mega Win", True, (242, 255, 0))
                textRect = text.get_rect()
                textRect.center = (300, 80)
                screen.blit(text, textRect)
                moneyText = font.render("Money: " + str(money), True, (255, 0, 100))
                pygame.draw.rect(screen, (50, 50, 150), (35, 40, moneyText.get_width(), moneyText.get_height()))
                screen.blit(moneyText, (35, 40))
                return 
            else:
                mixer.Channel(0).play(mixer.Sound("win.wav"))
                money = getMoney(username)
                money = int(money) 
                money += 100
                updateBank(money, username)
                text = font.render("Win", True, (242, 255, 0))
                textRect = text.get_rect()
                textRect.center = (300, 80)
                screen.blit(text, textRect)
                moneyText = font.render("Money: " + str(money), True, (255, 0, 100))
                pygame.draw.rect(screen, (50, 50, 150), (35, 40, moneyText.get_width(), moneyText.get_height()))
                screen.blit(moneyText, (35, 40))
                return
    mixer.Channel(0).play(mixer.Sound("lose.wav"))
    text = font.render("Lose", True, (242, 255, 0))
    textRect = text.get_rect()
    textRect.center = (300, 80)
    screen.blit(text, textRect)
    money = getMoney(username)
    money = int(money) 
    if money > 0:
        money -= 100
        updateBank(money, username)
    moneyText = font.render("Money: " + str(money), True, (255, 0, 100))
    pygame.draw.rect(screen, (50, 50, 150), (35, 40, moneyText.get_width(), moneyText.get_height()))
    screen.blit(moneyText, (35, 40))
    return 

def drawList(screen, imageList, objectsList):
    for i in range(len(imageList)):
        if objectsList[i] == "1" or objectsList[i] == "5":
            pygame.draw.rect(screen, (255, 255, 255), (210 + (i * 65), 245, 45, 85))
            screen.blit(imageList[i], (232 + (i * 65) - (imageList[i].get_width() / 2), 287 - (imageList[i].get_height() / 2)))
            pygame.display.update()
        else:
            imageList[i] = pygame.transform.scale(imageList[i], (45, 85))
            screen.blit(imageList[i], (210 + (i * 65), 245))
            pygame.display.update()

def getMoney(username):
    file = open(username + ".txt", "r")
    lines = file.readlines()
    money = lines[1]
    file.close()
    return money

def getLuckyCard(username):
    file = open(username + ".txt", "r")
    lines = file.readlines()
    luckyCard = lines[3]
    file.close()
    return luckyCard

def getSpins(username):
    file = open(username + ".txt", "r")
    lines = file.readlines()
    spins = lines[2]
    file.close()
    return spins

def updateBank(money, username):
    file = open(username + ".txt", "r")
    lines = file.readlines()
    lines[1] = str(money) + "\n"
    file.close()

    file = open(username + ".txt", "w")
    file.writelines(lines)
    file.close()

def updateSpins(username, spins):
    file = open(username + ".txt", "r")
    lines = file.readlines()
    lines[2] = str(spins) + "\n"
    file.close()
    
    file = open(username + ".txt", "w")
    file.writelines(lines)
    file.close()

def login():
    username = str(input("Enter your username: "))
    password = str(input("Enter your password: "))
    try: 
        file = open(username + ".txt", "r")
        line = None
        lines = []
        isCorrect = False
        for line in file:
            if line != "\n":
                lines.append(line)
            if line[:-1] == password:       
                isCorrect = True         
        if isCorrect == True:
            print("Welcome back, " + username)
            return True, username, lines[1], lines[2]
        else:
            print("Wrong password")
            return False, None, None, None

                
    except:
        print("User not found.")
        return False, username, 0, None
    
def register():
    username = str(input("Enter your username: "))
    password = str(input("Enter your password: "))
    money = str(input("Please enter the amount of money you would like to wager(minimum $1000 allowed): "))
    card = str(input("Choose a lucky card (Please enter in the format 'Ace of Spades' or '2 of Spades'): "))
    spins = int(money) / 10
    spins = int(spins)
    print("You Get ", spins, "spin(s)")
    
    file = open(username + ".txt", "a")
    file.write(password + "\n" + "0" + "\n" + str(spins) + "\n" + card)
    file.close()
    return username, money, spins

def play(screen, username):
    mixer.Channel(1).play(mixer.Sound("playMusic loop.wav"))
    mixer.Channel(1).set_volume(0.5)
    spins = int(getSpins(username))
    
    screen.fill((50, 50, 150))
    font = pygame.font.Font('VT323-Regular.ttf', 30)
    font_2 = pygame.font.Font('VT323-Regular.ttf', 60)
    if spins <= 0:
        text = font_2.render("You have no spins Left", True, (150, 50, 25))
        screen.blit(text, (35, 40))
        pygame.display.update()
        pygame.time.wait(1000)
        return
    spinsText = font.render("Spins Left: " + str(spins), True, (0, 255, 255))
    screen.blit(spinsText, (35, 80))
    text = font_2.render("Exit", True, (150, 50, 25))
    textRect = text.get_rect()
    textRect.center = (500, 60)
    screen.blit(text, textRect)
    
    text_2 = font.render("Click The Stick to play!", True, (255, 50, 100))
    textRect_2 = text_2.get_rect()
    textRect_2.center = (300, 500)
    screen.blit(text_2, textRect_2)

    slotMachine = pygame.image.load(os.path.join("slots", "machine.png"))
    slotMachine = pygame.transform.scale(slotMachine, (500, 500))
    screen.blit(slotMachine, (50, 100))

    money = getMoney(username)
    moneyText = font.render("Money: " + str(money), True, (255, 0, 100))
    screen.blit(moneyText, (35, 40))
    objectsList, imagesList = [], []
    pygame.display.update()
    
    circleCounter = 20
    colorCounter = 0
    while True:
        isPlaying = mixer.Channel(1).get_busy()
        if isPlaying == False:
            mixer.Channel(1).play(mixer.Sound("playMusic loop.wav"))
            mixer.Channel(1).set_volume(0.5)
        circleCounter = drawLights(screen, circleCounter, (50, 50, 150))

        if colorCounter == 0:
            text_2 = font.render("Click The Stick to play!", True, (255, 50, 100))
            screen.blit(text_2, textRect_2)
        elif colorCounter == 5:
            text_2 = font.render("Click The Stick to play!", True, (50, 100, 255))
            screen.blit(text_2, textRect_2)
        elif colorCounter == 10:
            text_2 = font.render("Click The Stick to play!", True, (100, 255, 50))
            screen.blit(text_2, textRect_2)
        elif colorCounter == 15:
            colorCounter = -1
        

        clock = pygame.time.Clock()
        clock.tick(15)
        pygame.display.update()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                x, y = event.pos
                stickRect = pygame.Rect(400, 190, 70, 160)
                if textRect.collidepoint((x, y)):
                    mixer.Channel(1).stop()
                    return True
                if stickRect.collidepoint((x, y)):
                    circleCounter = drawLights(screen, circleCounter, (50, 50, 150))
                    blankRect = pygame.draw.rect(screen, (50, 50, 150), (50, 150, slotMachine.get_width(), slotMachine.get_height() - 200))
                    slotMachine = pygame.image.load(os.path.join("slots", "machine_2.png"))
                    slotMachine = pygame.transform.scale(slotMachine, (500, 500))
                    screen.blit(slotMachine, (50, 100))
                    pygame.display.update()
                    pygame.draw.rect(screen, (50, 50, 150), (35, 80, spinsText.get_width(), spinsText.get_height()))
                    spins -= 1
                    updateSpins(username, spins)
                    spinsText = font.render("Spins Left: " + str(spins), True, (0, 255, 255))
                    screen.blit(spinsText, (35, 80))
                    objectsList, imagesList = drawObjects(screen)
                    mixer.Channel(1).set_volume(0.0)
                    processWin(objectsList, username, screen)
                    mixer.Channel(1).set_volume(0.5)
            if event.type == pygame.MOUSEBUTTONUP:
                x, y = event.pos
                stickRect = pygame.Rect(400, 190, 70, 160)
                if stickRect.collidepoint((x, y)):
                    circleCounter = drawLights(screen, circleCounter, (50, 50, 150))
                    blankRect = pygame.draw.rect(screen, (50, 50, 150), (50, 150, slotMachine.get_width(), slotMachine.get_height() - 200))
                    slotMachine = pygame.image.load(os.path.join("slots", "machine.png"))
                    slotMachine = pygame.transform.scale(slotMachine, (500, 500))
                    screen.blit(slotMachine, (50, 100))
                    drawList(screen, imagesList, objectsList)
                    pygame.display.update()

                    
            if event.type == pygame.MOUSEMOTION:
                x, y = event.pos
                if textRect.collidepoint((x, y)):
                    text = font_2.render("Exit", True, (255, 0, 0))
                    screen.blit(text, textRect)
                    pygame.display.update()
                else:
                    text = font_2.render("Exit", True, (150, 50, 25))
                    screen.blit(text, textRect)
                    pygame.display.update()
    
        colorCounter += 1

def miniGame(username, screen):
    screen.fill((196, 16, 16))
    font = pygame.font.Font('VT323-Regular.ttf', 30)
    luckyCard = getLuckyCard(username)
    deck = genDeck()
    cards = []
    random.shuffle(deck)
    for i in range(0, 3):
        card = random.choice(deck)
        deck.remove(card)
        cards.append(card)
    isWin = False
    if luckyCard in cards:
        isWin = True
    backOfCard = pygame.image.load("backofcard.png")
    backOfCard = pygame.transform.scale(backOfCard, (100, 150))
    backOfCardRect = backOfCard.get_rect()
    backOfCardRect.center = (25 + backOfCardRect.width / 2, 30 + backOfCardRect.height / 2)
    screen.blit(backOfCard, (25, 30))
    luckyCard = luckyCard.replace(" ", "")
    luckyCard = luckyCard.lower()
    luckyCardImage = pygame.image.load(os.path.join("cards", luckyCard + ".png"))
    luckyCardImage = pygame.transform.scale(luckyCardImage, (100, 150))
    screen.blit(luckyCardImage, (450, 30))
    text = font.render("Draw 3 cards from the deck", True, (50, 200, 200))
    textRect = text.get_rect()
    textRect.center = (290, 100)
    screen.blit(text, textRect)
    money = getMoney(username)
    moneyText = font.render("Money: " + str(money), True, (255, 0, 100))
    moneyRect = moneyText.get_rect()
    moneyRect.center = (290, 50)
    screen.blit(moneyText, moneyRect)
    pygame.display.update()
    counter = 0
    
    
    while True:
        pygame.display.update()
        if len(cards) == 0:
            if isWin == True:
                mixer.music.load("win.wav")
                mixer.music.play()
                text = font.render("You Win!", True, (0, 255, 0))
                textRect = text.get_rect()
                textRect.center = (290, 150)
                screen.blit(text, textRect)
                money = getMoney(username)
                money = int(money) + 10000000
                updateBank(money, username)
                pygame.draw.rect(screen, (196, 16, 16), moneyRect)
                moneyText = font.render("Money: " + str(money), True, (255, 0, 100))
                screen.blit(moneyText, moneyRect)
                pygame.display.update()
                pygame.time.wait(1000)
                return 
            else:
                mixer.music.load("lose.wav")
                mixer.music.play()
                text = font.render("You Lose!", True, (0, 0, 255))
                textRect = text.get_rect()
                textRect.center = (290, 150)
                screen.blit(text, textRect)
                money = getMoney(username)
                if int(money) > 0:
                    money = int(money) - 100
                    updateBank(money, username)
                pygame.draw.rect(screen, (196, 16, 16), moneyRect)
                moneyText = font.render("Money: " + str(money), True, (255, 0, 100))
                screen.blit(moneyText, moneyRect)
                pygame.display.update()
                pygame.time.wait(1000)
                return 
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                x, y = event.pos
                if backOfCardRect.collidepoint((x, y)):
                    if len(cards) > 0:
                        cardPath = cards[0]
                        cardPath = cardPath.replace(" ", "")
                        cardPath = cardPath.lower()
                        cardImage = pygame.image.load(os.path.join("cards", cardPath + ".png"))
                        cardImage = pygame.transform.scale(cardImage, (150, 250))
                        cards.remove(cards[0])
                        screen.blit(cardImage, (25 + (counter * 200), 250))
                        counter += 1
                        pygame.display.update()
                    else:
                        pass
    
def main():
    option = int(input("1. Login\n2. Create new Account\n3. Buy Spins\nChoose an option: "))
    success = False
    username = None
    money = 0
    if option == 1:
        success, username, money, spins = login()
    elif option == 2:
        username, money, spins = register()
        success = True
    elif option == 3:
        print("Login to Buy spins")
        success, username, money, spins = login()
        moreSpins = int(input("Please enter the amount of money you wish to wager(minimum 1000): "))
        moreSpins /= 10
        spins = int(spins) + int(moreSpins)
        updateSpins(username, spins)
        success = True

    if success == True:
        screen = pygame.display.set_mode((600, 600))
        pygame.display.set_caption("Slot Machine")
        start = startScreen(screen)

        mixer.pre_init()
        mixer.init()
        mixer.music.load("menuMusic.wav")
        mixer.music.play(1)
        mixer.music.set_volume(0.5)
        while start:
            money = getMoney(username)
            spins = getSpins(username)
            option = menuScreen(screen, username, money, spins)
            screen.fill((0, 0, 0))
            if option == "p":
                play(screen, username)
            elif option == "b":
                bank(screen, money, username, spins)
            elif option == "m":
                miniGame(username, screen)
            for event in pygame.event.get():  
                if event.type == pygame.QUIT:
                    pygame.quit()
                    exit()
                if event.type == pygame.MOUSEBUTTONDOWN:
                    pos = pygame.mouse.get_pos()
            pygame.display.update()

main()