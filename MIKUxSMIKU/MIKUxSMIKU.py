# 11 September 2021

from tkinter.constants import FALSE, TRUE
import pygame
import os
import random
import tkinter as tk
import threading
import time

from pygame import draw
pygame.font.init()
pygame.mixer.init()


# VARIABLES

WIDTH, HEIGHT = 900, 500
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("MIKUxSMIKU")

ONGOING = False

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
SAND = (255, 213, 0)

DSPY_COLOR = WHITE

BORDER = pygame.Rect(WIDTH // 2 - 200, 0, 400, HEIGHT)

HP_FONT = pygame.font.SysFont('comicsans', 40)
BE_FONT = pygame.font.SysFont('comicsans', 40)
VICTORY_FONT = pygame.font.SysFont('comicsans', 100)

FPS = 60
VELOCITY = 5
THROWABLE_VELOCITY = 7
MAX_THROWABLES = 3
SPRITE_WIDTH, SPRITE_HEIGHT = 70, 70
ARTS_WIDTH, ARTS_HEIGHT = 500, 500
BE_WIDTH, BE_HEIGHT = 10, 10
THROWABLE_WIDTH, THROWABLE_HEIGHT = 40, 40

HATSUNE_HIT = pygame.USEREVENT + 1
SAKURA_HIT = pygame.USEREVENT + 2

ULTRA_HATSUNE_HIT = pygame.USEREVENT + 3
ULTRA_SAKURA_HIT = pygame.USEREVENT + 4

HATSUNE_BE_EVENT = pygame.USEREVENT + 5
SAKURA_BE_EVENT = pygame.USEREVENT + 6

# MUSIC

music_name = "メルト (Melt)"

MUSIC1 = pygame.mixer.Sound(os.path.join('ASSETS/MUSIC', 'melt.mp3'))
MUSIC1.set_volume(0.05)

MUSIC2 = pygame.mixer.Sound(os.path.join('ASSETS/MUSIC', 'tellyourworld.mp3'))
MUSIC2.set_volume(0.1)

MUSIC3 = pygame.mixer.Sound(os.path.join('ASSETS/MUSIC', 'senbonzakura.mp3'))
MUSIC3.set_volume(0.05)

MUSIC4 = pygame.mixer.Sound(os.path.join('ASSETS/MUSIC', 'teo.mp3'))
MUSIC4.set_volume(0.3)

MUSIC5 = pygame.mixer.Sound(os.path.join('ASSETS/MUSIC', 'worldismine.mp3'))
MUSIC5.set_volume(0.1)

MUSIC6 = pygame.mixer.Sound(os.path.join('ASSETS/MUSIC', 'ghostrule.mp3'))
MUSIC6.set_volume(0.1)

MUSIC7 = pygame.mixer.Sound(os.path.join('ASSETS/MUSIC', 'hibikase.mp3'))
MUSIC7.set_volume(0.1)

MUSIC8 = pygame.mixer.Sound(os.path.join('ASSETS/MUSIC', 'alienalien.mp3'))
MUSIC8.set_volume(0.1)

MUSIC = MUSIC1

# SFX

HEALING_SOUND = pygame.mixer.Sound(os.path.join('ASSETS/SFX', 'heal.mp3'))
HEALING_SOUND.set_volume(0.2)

HIT_SOUND = pygame.mixer.Sound(os.path.join('ASSETS/SFX', 'hit.mp3'))
HIT_SOUND.set_volume(0.5)

THROWING_SOUND = pygame.mixer.Sound(os.path.join('ASSETS/SFX', 'throwing.mp3'))
THROWING_SOUND.set_volume(0.5)

BE_SOUND = pygame.mixer.Sound(os.path.join('ASSETS/SFX', 'kaching2.mp3'))

# IMAGES

GRASS_IMG = pygame.image.load(os.path.join('ASSETS/ENVIRONMENT', 'grass.png'))
GRASS = pygame.transform.scale(GRASS_IMG, (WIDTH, HEIGHT))

OCEAN0_IMG = pygame.image.load(os.path.join('ASSETS/ENVIRONMENT', 'ocean0.png'))
OCEAN1_IMG = pygame.image.load(os.path.join('ASSETS/ENVIRONMENT', 'ocean1.png'))
OCEAN2_IMG = pygame.image.load(os.path.join('ASSETS/ENVIRONMENT', 'ocean2.png'))
OCEAN3_IMG = pygame.image.load(os.path.join('ASSETS/ENVIRONMENT', 'ocean3.png'))
OCEAN4_IMG = pygame.image.load(os.path.join('ASSETS/ENVIRONMENT', 'ocean4.png'))
OCEAN5_IMG = pygame.image.load(os.path.join('ASSETS/ENVIRONMENT', 'ocean5.png'))
OCEAN6_IMG = pygame.image.load(os.path.join('ASSETS/ENVIRONMENT', 'ocean6.png'))
OCEAN7_IMG = pygame.image.load(os.path.join('ASSETS/ENVIRONMENT', 'ocean7.png'))


SPARKLE0_IMG = pygame.image.load(os.path.join('ASSETS/VFX', 'sparkle0.png'))
SPARKLE1_IMG = pygame.image.load(os.path.join('ASSETS/VFX', 'sparkle1.png'))
SPARKLE2_IMG = pygame.image.load(os.path.join('ASSETS/VFX', 'sparkle2.png'))
SPARKLE3_IMG = pygame.image.load(os.path.join('ASSETS/VFX', 'sparkle3.png'))
SPARKLE4_IMG = pygame.image.load(os.path.join('ASSETS/VFX', 'sparkle4.png'))
SPARKLE5_IMG = pygame.image.load(os.path.join('ASSETS/VFX', 'sparkle5.png'))


OCEAN0 = pygame.transform.scale(OCEAN0_IMG, (380, HEIGHT))
OCEAN1 = pygame.transform.scale(OCEAN1_IMG, (380, HEIGHT))
OCEAN2 = pygame.transform.scale(OCEAN2_IMG, (380, HEIGHT))
OCEAN3 = pygame.transform.scale(OCEAN3_IMG, (380, HEIGHT))
OCEAN4 = pygame.transform.scale(OCEAN4_IMG, (380, HEIGHT))
OCEAN5 = pygame.transform.scale(OCEAN5_IMG, (380, HEIGHT))
OCEAN6 = pygame.transform.scale(OCEAN6_IMG, (380, HEIGHT))
OCEAN7 = pygame.transform.scale(OCEAN7_IMG, (380, HEIGHT))


SPARKLE0 = pygame.transform.scale(SPARKLE0_IMG, (260, HEIGHT))
SPARKLE1 = pygame.transform.scale(SPARKLE1_IMG, (260, HEIGHT))
SPARKLE2 = pygame.transform.scale(SPARKLE2_IMG, (260, HEIGHT))
SPARKLE3 = pygame.transform.scale(SPARKLE3_IMG, (260, HEIGHT))
SPARKLE4 = pygame.transform.scale(SPARKLE4_IMG, (260, HEIGHT))
SPARKLE5 = pygame.transform.scale(SPARKLE5_IMG, (260, HEIGHT))


BE_IMG = pygame.image.load(os.path.join('ASSETS/ENVIRONMENT', 'ether.png'))
BE = pygame.transform.scale(BE_IMG, (BE_WIDTH, BE_HEIGHT))

HATSUNE_MIKU_IMG = pygame.image.load(os.path.join('ASSETS/CHARACTERS', 'miku.png'))
HATSUNE_MIKU = pygame.transform.scale(HATSUNE_MIKU_IMG, (SPRITE_WIDTH, SPRITE_HEIGHT))
HATSUNE_MIKU = pygame.transform.flip(HATSUNE_MIKU, True, False)

MIKU_ARTS_IMG = pygame.image.load(os.path.join('ASSETS/CHARACTERS', 'miku_arts.png'))
MIKU_ARTS = pygame.transform.scale(MIKU_ARTS_IMG, (ARTS_WIDTH, ARTS_HEIGHT))

SAKURA_MIKU_IMG = pygame.image.load(os.path.join('ASSETS/CHARACTERS', 'smiku.png'))
SAKURA_MIKU = pygame.transform.scale(SAKURA_MIKU_IMG, (SPRITE_WIDTH, SPRITE_HEIGHT))
# SAKURA_MIKU = pygame.transform.flip(SAKURA_MIKU, True, False)

SMIKU_ARTS_IMG = pygame.image.load(os.path.join('ASSETS/CHARACTERS', 'smiku_arts.png'))
SMIKU_ARTS = pygame.transform.scale(SMIKU_ARTS_IMG, (ARTS_WIDTH, ARTS_HEIGHT))

NEGI_IMG = pygame.image.load(os.path.join('ASSETS/THROWABLES', 'negi.png'))
NEGI = pygame.transform.scale(NEGI_IMG, (THROWABLE_WIDTH, THROWABLE_WIDTH))
ULTRA_NEGI = pygame.transform.scale(NEGI_IMG, (THROWABLE_WIDTH * 3, THROWABLE_WIDTH * 3))

CHERRY_IMG = pygame.image.load(os.path.join('ASSETS/THROWABLES', 'cherry.png'))
CHERRY = pygame.transform.scale(CHERRY_IMG, (THROWABLE_WIDTH, THROWABLE_WIDTH))
ULTRA_CHERRY = pygame.transform.scale(CHERRY_IMG, (THROWABLE_WIDTH * 3, THROWABLE_WIDTH * 3))

# DRAW VICTOR

def draw_victor(text):
    draw_text = VICTORY_FONT.render(text, 1, WHITE)
    WIN.blit(draw_text , (WIDTH // 2 - draw_text.get_width() // 2, HEIGHT // 2 - draw_text.get_height() // 2))
    pygame.display.update()
    pygame.time.delay(5000)

# GAME

def main():
    global HATSUNE_ARTS
    global SAKURA_ARTS
    global H_CYCLE
    global S_CYCLE
    global H_ACTIVE
    global S_ACTIVE

    ONGOING = True

    HATSUNE = pygame.Rect(100, 250, SPRITE_WIDTH, SPRITE_HEIGHT)
    SAKURA = pygame.Rect(700, 250, SPRITE_WIDTH, SPRITE_HEIGHT)

    BE1 = pygame.Rect(random.randint(BORDER.x, BORDER.x + 390), random.randint(30, HEIGHT - 30), BE_WIDTH, BE_HEIGHT)
    BE2 = pygame.Rect(random.randint(BORDER.x, BORDER.x + 390), random.randint(30, HEIGHT - 30), BE_WIDTH, BE_HEIGHT)
    BE3 = pygame.Rect(random.randint(BORDER.x, BORDER.x + 390), random.randint(30, HEIGHT - 30), BE_WIDTH, BE_HEIGHT)

    # INVENTORY

    BATTLE_ETHER = [BE1, BE2, BE3]

    NEGIS = []
    CHERRIES = []

    ULTRA_NEGIS = []
    ULTRA_CHERRIES = []

    # STATS

    HATSUNE_HP = 100
    SAKURA_HP = 100

    HATSUNE_BE = 0
    SAKURA_BE = 0

    HATSUNE_ARTS = False
    SAKURA_ARTS = False

    H_CYCLE = 0
    S_CYCLE = 0

    H_ACTIVE = False
    S_ACTIVE = False

    clock = pygame.time.Clock()

    victory_text = ""

    # RUNTIME

    run = True
    FRAME = 0

    while run:
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                pygame.quit()

            if event.type == pygame.KEYDOWN:

                # THROWING

                if event.key == pygame.K_SPACE and len(NEGIS) < MAX_THROWABLES:
                    THROWABLE = pygame.Rect(HATSUNE.x + HATSUNE.width, HATSUNE.y + HATSUNE.height // 2 - 2, 10, THROWABLE_HEIGHT)
                    NEGIS.append(THROWABLE)
                    THROWING_SOUND.play()

                if event.key == pygame.K_KP_0 and len(CHERRIES) < MAX_THROWABLES:
                    THROWABLE = pygame.Rect(SAKURA.x, SAKURA.y + SAKURA.height // 2 - 2, 10, THROWABLE_HEIGHT)
                    CHERRIES.append(THROWABLE)
                    THROWING_SOUND.play()

                # ARTS

                if event.key == pygame.K_x and HATSUNE_BE >= 100:
                    HATSUNE_HP += 20
                    HATSUNE_BE -= 100
                    HEALING_SOUND.play()
                    H_ACTIVE = True
                    HATSUNE_ARTS = True
                    if S_ACTIVE == True:
                        S_ACTIVE = False
                    

                if event.key == pygame.K_KP_7 and SAKURA_BE >= 100:
                    SAKURA_HP += 20
                    SAKURA_BE -= 100
                    HEALING_SOUND.play()
                    S_ACTIVE = True
                    SAKURA_ARTS = True
                    if H_ACTIVE == True:
                        H_ACTIVE = False


                # ULTRA ARTS 

                if event.key == pygame.K_z and HATSUNE_BE >= 200:
                    ULTRA_THROWABLE = pygame.Rect(HATSUNE.x + HATSUNE.width, HATSUNE.y - HATSUNE.height // 2 + 2 * 3, 10 * 3, THROWABLE_HEIGHT * 3)
                    ULTRA_NEGIS.append(ULTRA_THROWABLE)
                    HATSUNE_BE -= 200
                    THROWING_SOUND.play()


                if event.key == pygame.K_KP_9 and SAKURA_BE >= 200:
                    ULTRA_THROWABLE = pygame.Rect(SAKURA.x, SAKURA.y - SAKURA.height // 2 + 2 * 3, 10 * 3, THROWABLE_HEIGHT * 3)
                    ULTRA_CHERRIES.append(ULTRA_THROWABLE)
                    SAKURA_BE -= 200
                    THROWING_SOUND.play()


                # CHEATS

                if event.key == pygame.K_t:
                    HATSUNE_BE += 1000
                    SAKURA_BE += 1000


                # MENU

                if event.key == pygame.K_p:
                    menu(ONGOING, music_name)

            if event.type == HATSUNE_HIT:
                HATSUNE_HP -= 10
                HIT_SOUND.play()

            if event.type == SAKURA_HIT:
                SAKURA_HP -= 10
                HIT_SOUND.play()
            
            if event.type == ULTRA_HATSUNE_HIT:
                SAKURA_HP -= 25
                HIT_SOUND.play()

            if event.type == ULTRA_SAKURA_HIT:
                SAKURA_HP -= 25
                HIT_SOUND.play()

            if event.type == HATSUNE_BE_EVENT:
                BE_SOUND.play()
                HATSUNE_BE += 12

            if event.type == SAKURA_BE_EVENT:
                BE_SOUND.play()
                SAKURA_BE += 12

        if SAKURA_HP <= 0:
            victory_text = "Hatsune Miku Wins!"
        
        if HATSUNE_HP <= 0:
            victory_text = "Sakura Miku Wins!"

        if victory_text != "":
            draw_victor(victory_text)
            break

        # FRAME

        if FRAME != 80:
            FRAME += 1
        else:
            FRAME = 0


        # BATTLE ETHER

        if BE1 not in BATTLE_ETHER:
            BE1 = pygame.Rect(random.randint(BORDER.x, BORDER.x + 390), random.randint(30, HEIGHT - 30), BE_WIDTH, BE_HEIGHT)
            BATTLE_ETHER.append(BE1)
        if BE2 not in BATTLE_ETHER:
            BE2 = pygame.Rect(random.randint(BORDER.x, BORDER.x + 390), random.randint(30, HEIGHT - 30), BE_WIDTH, BE_HEIGHT)
            BATTLE_ETHER.append(BE2)
        if BE3 not in BATTLE_ETHER:
            BE3 = pygame.Rect(random.randint(BORDER.x, BORDER.x + 390), random.randint(30, HEIGHT - 30), BE_WIDTH, BE_HEIGHT)
            BATTLE_ETHER.append(BE3)

        # KEY PRESS

        try:
            keys_pressed = pygame.key.get_pressed()
        except:
            exit()

        HATSUNE_movement(keys_pressed, HATSUNE)
        SAKURA_movement(keys_pressed, SAKURA)

        handle_throwables(NEGIS, CHERRIES, HATSUNE, SAKURA, BE1, BE2, BE3, BATTLE_ETHER, ULTRA_NEGIS, ULTRA_CHERRIES)

        draw_window(FRAME, HATSUNE, SAKURA, NEGIS, CHERRIES, HATSUNE_HP, SAKURA_HP, HATSUNE_BE, SAKURA_BE, BATTLE_ETHER, ULTRA_NEGIS, ULTRA_CHERRIES)

    main()


# DRAWING

def draw_window(FRAME, HATSUNE, SAKURA, NEGIS, CHERRIES, HATSUNE_HP, SAKURA_HP, HATSUNE_BE, SAKURA_BE, BATTLE_ETHER, ULTRA_NEGIS, ULTRA_CHERRIES):
    global HATSUNE_ARTS
    global SAKURA_ARTS
    global H_CYCLE
    global S_CYCLE
    global H_ACTIVE
    global S_ACTIVE

    WIN.fill(DSPY_COLOR)

    WIN.blit(GRASS, (0, 0))
    pygame.draw.rect(WIN, SAND, BORDER)

    HATSUNE_HP_TEXT = HP_FONT.render(f"HP: {HATSUNE_HP}", 1, WHITE)
    SAKURA_HP_TEXT = HP_FONT.render(f"HP: {SAKURA_HP}", 1, WHITE)

    HATSUNE_BE_TEXT = HP_FONT.render(f"BE: {HATSUNE_BE}", 1, WHITE)
    SAKURA_BE_TEXT = HP_FONT.render(f"BE: {SAKURA_BE}", 1, WHITE)

    WIN.blit(HATSUNE_HP_TEXT, (10, 10))
    WIN.blit(SAKURA_HP_TEXT, (WIDTH - SAKURA_HP_TEXT.get_width() - 10, 10))

    WIN.blit(HATSUNE_BE_TEXT, (10, 0 + HATSUNE_BE_TEXT.get_height() + 10))
    WIN.blit(SAKURA_BE_TEXT, (WIDTH - SAKURA_BE_TEXT.get_width() - 10, SAKURA_BE_TEXT.get_height() + 10))
    

    if FRAME >= 70:
        WIN.blit(OCEAN0, (WIDTH // 2 - 190, 0))
    elif FRAME >= 60:
        WIN.blit(OCEAN1, (WIDTH // 2 - 190, 0))
    elif FRAME >= 50:
        WIN.blit(OCEAN2, (WIDTH // 2 - 190, 0))
    elif FRAME >= 40:
        WIN.blit(OCEAN3, (WIDTH // 2 - 190, 0))
    elif FRAME >= 30:
        WIN.blit(OCEAN4, (WIDTH // 2 - 190, 0))
    elif FRAME >= 20:
        WIN.blit(OCEAN5, (WIDTH // 2 - 190, 0))
    elif FRAME >= 10:
        WIN.blit(OCEAN6, (WIDTH // 2 - 190, 0))
    elif FRAME >= 0:
        WIN.blit(OCEAN7, (WIDTH // 2 - 190, 0))

    if HATSUNE_ARTS == True:
        if H_CYCLE < 150:
            if H_CYCLE < 50 and H_ACTIVE == True:
                WIN.blit(MIKU_ARTS, (WIDTH // 2 - ARTS_WIDTH // 2, HEIGHT // 2 - ARTS_HEIGHT // 2))
            if FRAME >= 70:
                WIN.blit(SPARKLE0, (0, 0))
                H_CYCLE += 1
            elif FRAME >= 60:
                WIN.blit(SPARKLE1, (0, 0))
                H_CYCLE += 1
            elif FRAME >= 50:
                WIN.blit(SPARKLE2, (0, 0))
                H_CYCLE += 1
            elif FRAME >= 40:
                WIN.blit(SPARKLE3, (0, 0))
                H_CYCLE += 1
            elif FRAME >= 30:
                WIN.blit(SPARKLE4, (0, 0))
                H_CYCLE += 1
            elif FRAME >= 20:
                WIN.blit(SPARKLE5, (0, 0))
                H_CYCLE += 1
        else:
            HATSUNE_ARTS = False
            H_CYCLE = 0

    if SAKURA_ARTS == True:
        if S_CYCLE < 150:
            if S_CYCLE < 50 and S_ACTIVE == True:
                WIN.blit(SMIKU_ARTS, (WIDTH // 2 - ARTS_WIDTH // 2, HEIGHT // 2 - ARTS_HEIGHT // 2))
            if FRAME >= 70:
                WIN.blit(SPARKLE0, (WIDTH // 2 + 190, 0))
                S_CYCLE += 1
            elif FRAME >= 60:
                WIN.blit(SPARKLE1, (WIDTH // 2 + 190, 0))
                S_CYCLE += 1
            elif FRAME >= 50:
                WIN.blit(SPARKLE2, (WIDTH // 2 + 190, 0))
                S_CYCLE += 1
            elif FRAME >= 40:
                WIN.blit(SPARKLE3, (WIDTH // 2 + 190, 0))
                S_CYCLE += 1
            elif FRAME >= 30:
                WIN.blit(SPARKLE4, (WIDTH // 2 + 190, 0))
                S_CYCLE += 1
            elif FRAME >= 20:
                WIN.blit(SPARKLE5, (WIDTH // 2 + 190, 0))
                S_CYCLE += 1
        else:
            SAKURA_ARTS = False
            S_CYCLE = 0


    WIN.blit(HATSUNE_MIKU, (HATSUNE.x, HATSUNE.y))
    WIN.blit(SAKURA_MIKU, (SAKURA.x, SAKURA.y))

    for throwable in NEGIS:
        WIN.blit(NEGI, throwable)

    for throwable in CHERRIES:
        WIN.blit(CHERRY, throwable)

    for throwable in ULTRA_NEGIS:
        WIN.blit(ULTRA_NEGI, throwable)

    for throwable in ULTRA_CHERRIES:
        WIN.blit(ULTRA_CHERRY, throwable)

    for ether in BATTLE_ETHER:
        WIN.blit(BE, ether)

    pygame.display.update()

# MOVEMENT

def HATSUNE_movement(keys_pressed, HATSUNE):
    if keys_pressed[pygame.K_a] and HATSUNE.x - VELOCITY > 0:  # LEFT
        HATSUNE.x -= VELOCITY
    if keys_pressed[pygame.K_d] and HATSUNE.x + VELOCITY + SPRITE_WIDTH < BORDER.x:  # RIGHT
        HATSUNE.x += VELOCITY
    if keys_pressed[pygame.K_w] and HATSUNE.y - VELOCITY > 0:  # UP
        HATSUNE.y -= VELOCITY
    if keys_pressed[pygame.K_s] and HATSUNE.y + VELOCITY + SPRITE_HEIGHT < HEIGHT:  # DOWN
        HATSUNE.y += VELOCITY

def SAKURA_movement(keys_pressed, SAKURA):
    if keys_pressed[pygame.K_KP_4] and SAKURA.x - VELOCITY > BORDER.x + BORDER.width:  # LEFT
        SAKURA.x -= VELOCITY
    if keys_pressed[pygame.K_KP6] and SAKURA.x + VELOCITY + SPRITE_WIDTH < WIDTH:  # RIGHT
        SAKURA.x += VELOCITY
    if keys_pressed[pygame.K_KP_8] and SAKURA.y - VELOCITY > 0:  # UP
        SAKURA.y -= VELOCITY
    if keys_pressed[pygame.K_KP_5] and SAKURA.y + VELOCITY + SPRITE_HEIGHT < HEIGHT:  # DOWN
        SAKURA.y += VELOCITY


# THROWING

def handle_throwables(NEGIS, CHERRIES, HATSUNE, SAKURA, BE1, BE2, BE3, BATTLE_ETHER, ULTRA_NEGIS, ULTRA_CHERRIES):
    for throwable in NEGIS:
        throwable.x += THROWABLE_VELOCITY

        # BATTLE ETHER
        try:
            if BE1.colliderect(throwable):
                BATTLE_ETHER.remove(BE1)
                pygame.event.post(pygame.event.Event(HATSUNE_BE_EVENT))
            if BE2.colliderect(throwable):
                BATTLE_ETHER.remove(BE2)
                pygame.event.post(pygame.event.Event(HATSUNE_BE_EVENT))
            if BE3.colliderect(throwable):
                BATTLE_ETHER.remove(BE3)
                pygame.event.post(pygame.event.Event(HATSUNE_BE_EVENT))
        except:
            pass

    # PLAYER HIT
        if SAKURA.colliderect(throwable):
            pygame.event.post(pygame.event.Event(SAKURA_HIT))
            NEGIS.remove(throwable)
        elif throwable.x > WIDTH:
            NEGIS.remove(throwable)

    for throwable in CHERRIES:
        throwable.x -= THROWABLE_VELOCITY

        # BATTLE ETHER
        try:
            if BE1.colliderect(throwable):
                BATTLE_ETHER.remove(BE1)
                pygame.event.post(pygame.event.Event(SAKURA_BE_EVENT))
            if BE2.colliderect(throwable):
                BATTLE_ETHER.remove(BE2)
                pygame.event.post(pygame.event.Event(SAKURA_BE_EVENT))
            if BE3.colliderect(throwable):
                BATTLE_ETHER.remove(BE3)
                pygame.event.post(pygame.event.Event(SAKURA_BE_EVENT))
        except:
            pass

        # PLAYER HIT

        if HATSUNE.colliderect(throwable):
            pygame.event.post(pygame.event.Event(HATSUNE_HIT))
            CHERRIES.remove(throwable)
        elif throwable.x < 0:
            CHERRIES.remove(throwable)

    for ultra_throwable in ULTRA_NEGIS:
        ultra_throwable.x += THROWABLE_VELOCITY
        
        # PLAYER HIT

        if SAKURA.colliderect(ultra_throwable):
            pygame.event.post(pygame.event.Event(ULTRA_SAKURA_HIT))
            ULTRA_NEGIS.remove(ultra_throwable)
        elif ultra_throwable.x > WIDTH:
            ULTRA_NEGIS.remove(ultra_throwable)

    for ultra_throwable in ULTRA_CHERRIES:
        ultra_throwable.x -= THROWABLE_VELOCITY

        # PLAYER HIT

        if HATSUNE.colliderect(ultra_throwable):
            pygame.event.post(pygame.event.Event(ULTRA_HATSUNE_HIT))
            ULTRA_CHERRIES.remove(ultra_throwable)
        elif ultra_throwable.x < 0:
            ULTRA_CHERRIES.remove(ultra_throwable)


# PAUSE MENU

def menu(ONGOING, music_name):
    global top
    global root
    global display

    root = tk.Tk()
    top = tk.Toplevel()
    top.resizable(0,0)

    top.geometry('250x450') #Sets login GUI window size
    top.title('Settings') #Title of the window
    top.configure(background='light grey') #Background color

    display = tk.Text(top,width=24,height=5)
    display.place(x=25,y=278)
    display.insert(tk.END, f"Music: \n{music_name} ♪")
    display.configure(state='disabled')

    buttona= tk.Button(top, text="メルト (Melt)", command=lambda:music(1, ONGOING), width=12, bg="white") 
    buttonb = tk.Button(top, text="Tell Your World", command=lambda:music(2, ONGOING), width=12, bg="white")
    buttonc = tk.Button(top, text="Senbonzakura", command=lambda:music(3, ONGOING), width=12, bg="white")
    buttond = tk.Button(top, text="テオ (Teo)", command=lambda:music(4, ONGOING), width=12, bg="white")
    buttone = tk.Button(top, text="World Is Mine", command=lambda:music(5, ONGOING), width=12, bg="white")
    buttonf = tk.Button(top, text="Ghost Rule", command=lambda:music(6, ONGOING), width=12, bg="white")
    buttong = tk.Button(top, text="Hibikase", command=lambda:music(7, ONGOING), width=12, bg="white")
    buttonh = tk.Button(top, text="Alien Alien", command=lambda:music(8, ONGOING), width=12, bg="white")

    buttona.place(x=25,y=98)
    buttonb.place(x=126,y=98) 
    buttonc.place(x=25,y=138)
    buttond.place(x=126,y=138)
    buttone.place(x=25,y=178)
    buttonf.place(x=126,y=178)
    buttong.place(x=25,y=218)
    buttonh.place(x=126,y=218)


    if not ONGOING:
        title = tk.Label(top, text='MIKUxSMIKU\n',background='light grey') #Labels
        title.configure(font=("Times New Roman", 15, "bold"))
        title.place(x=60,y=23) 

        start_button = tk.Button(top, text='START', command=lambda:close(ONGOING), width=27)
        start_button.place(x=25,y= 383)

    else:
        restart_button = tk.Button(top, text='RESTART', command=lambda:restart(), width=27)
        restart_button.place(x=25,y=33)

        resume_button = tk.Button(top, text='RESUME', command=lambda:close(ONGOING), width=27)
        resume_button.place(x=25,y= 383)

    top.protocol("WM_DELETE_WINDOW", forced_close)

    root.withdraw() #Hides root window  
    root.mainloop() #Runs event loop

def music(num, ONGOING):
    global music_name
    global MUSIC

    MUSIC.stop()

    if num == 1:
        music_name = "メルト (Melt)"
        MUSIC = MUSIC1   
    elif num == 2:
        music_name = "Tell Your World"
        MUSIC = MUSIC2
    elif num == 3:
        music_name = "千本桜 (Senbonzakura)"
        MUSIC = MUSIC3
    elif num == 4:
        music_name = "テオ (Teo)"
        MUSIC = MUSIC4
    elif num == 5:
        music_name = "World Is Mine"
        MUSIC = MUSIC5
    elif num == 6:
        music_name = "Ghost Rule"
        MUSIC = MUSIC6
    elif num == 7:
        music_name = "Hibikase"
        MUSIC = MUSIC7
    elif num == 8:
        music_name = "Alien Alien"
        MUSIC = MUSIC8

    if ONGOING:
        MUSIC.play(-1)

    display.configure(state='normal')
    display.delete('1.0',tk.END)
    display.insert(tk.END, f"Music: \n{music_name} ♪")
    display.configure(state='disabled')



def close(ONGOING):
    top.destroy()
    root.destroy()
    # if ONGOING:
    #     MUSIC.play(-1)

def forced_close(): 
    root.destroy()


def restart():
    top.destroy()
    root.destroy()
    MUSIC.stop()
    MUSIC.play(-1)
    main()

if __name__ == "__main__":
    menu(ONGOING, music_name)
    MUSIC.play(-1)
    main()
