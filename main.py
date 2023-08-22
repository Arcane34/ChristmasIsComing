import pygame
import math
import random
import os

pygame.init()
x_width = 800
y_width = 360
screen = pygame.display.set_mode((x_width, y_width))
pygame.display.set_caption("Christmas Is Coming!")

bgC = (140, 255, 251)
ground = pygame.image.load(os.path.join('images', "Ground.png"))
jesus = pygame.image.load(os.path.join('images', "Jesus.png"))
healthBar = pygame.image.load(os.path.join('images', "HealthBar.png"))
godA = [pygame.image.load(os.path.join('images', "godBolt1.png")), pygame.image.load(os.path.join('images', "godBolt2.png")),
        pygame.image.load(os.path.join('images', "godBolt3.png")), pygame.image.load(os.path.join('images', "godBolt4.png")),
        pygame.image.load(os.path.join('images', "godBolt5.png")), pygame.image.load(os.path.join('images', "godBolt6.png"))]
godT = []
for p in godA:
    for i in range(50):
        godT.append(p)
godA = []
for x in godT:
    godA.append(x)
godbs = []
spirit = pygame.image.load(os.path.join('images', "Spirit.png"))
castle = pygame.image.load(os.path.join('images', "Castle.png"))
feather = pygame.image.load(os.path.join('images', "feather.png"))
enemy = [pygame.image.load(os.path.join('images', "enemy1.png")), pygame.image.load(os.path.join('images', "enemy1a.png")),
         pygame.image.load(os.path.join('images', "enemy1b.png")), pygame.image.load(os.path.join('images', "enemy1c.png"))]
enemyA = [pygame.image.load(os.path.join('images', "enemy1A1.png")), pygame.image.load(os.path.join('images', "enemy1A2.png")),
          pygame.image.load(os.path.join('images', "enemy1A3.png")), pygame.image.load(os.path.join('images', "enemy1A4.png"))]
enemyAttack = pygame.image.load(os.path.join('images', "enemy1attack.png"))
"""enemyD = [pygame.image.load(os.path.join('images', "enemy1Da.png")), pygame.image.load(os.path.join('images', "enemy1Db.png")),
          pygame.image.load(os.path.join('images', "enemy1Dc.png")), pygame.image.load(os.path.join('images', "enemy1Dd.png")),
          pygame.image.load(os.path.join('images', "enemy1De.png")), pygame.image.load(os.path.join('images', "enemy1Df.png")),
          pygame.image.load(os.path.join('images', "enemy1Dg.png")), pygame.image.load(os.path.join('images', "enemy1Dh.png")),
          pygame.image.load(os.path.join('images', "enemy1Di.png")), pygame.image.load(os.path.join('images', "enemy1Dj.png")),
          pygame.image.load(os.path.join('images', "enemy1Dk.png")), pygame.image.load(os.path.join('images', "enemy1Dl.png")),
          pygame.image.load(os.path.join('images', "enemy1Dm.png")), pygame.image.load(os.path.join('images', "enemy1Dn.png")),
          pygame.image.load(os.path.join('images', "enemy1Do.png"))]"""
enemyD = [pygame.image.load(os.path.join('images', "enemy1Da.png")), pygame.image.load(os.path.join('images', "enemy1Dc.png")),
          pygame.image.load(os.path.join('images', "enemy1De.png")), pygame.image.load(os.path.join('images', "enemy1Dg.png")),
          pygame.image.load(os.path.join('images', "enemy1Di.png")), pygame.image.load(os.path.join('images', "enemy1Dk.png")),
          pygame.image.load(os.path.join('images', "enemy1Dm.png")), pygame.image.load(os.path.join('images', "enemy1Do.png"))]
spiritWalk = [pygame.image.load(os.path.join('images', "Spirit1.png")), pygame.image.load(os.path.join('images', "Spirit2.png")),
              pygame.image.load(os.path.join('images', "Spirit3.png")), pygame.image.load(os.path.join('images', "Spirit4.png"))]
spiritWalk1 = [pygame.image.load(os.path.join('images', "Spirit1R.png")), pygame.image.load(os.path.join('images',"Spirit2R.png")),
               pygame.image.load(os.path.join('images', "Spirit3R.png")), pygame.image.load(os.path.join('images', "Spirit4R.png"))]
clock = pygame.time.Clock()
shot = pygame.image.load(os.path.join('images', "Shot.png"))
bullets = []
enemy_bs = []
w_enemies = []
black = (0, 0, 0)
buttonColor = (255, 247, 107)
hoverColor = (220, 212, 72)
drops = []
pygame.display.set_icon(feather)

def fader(w, h):
    fade = pygame.Surface((w, h))
    fade.fill((255, 255, 255))
    for i in range(200):
        fade.set_alpha(i)
        screen.blit(fade, (0, 0))
        pygame.display.update()
        pygame.time.delay(5)

def text_objects(text, font):
    textsurface = font.render(text, True, (0, 0, 0))
    return textsurface, textsurface.get_rect()

def button(msg, x, y, w, h, ic, ac, action=None):
    mouse = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()

    if x + w > mouse[0] > x and y + h > mouse[1] > y:
        pygame.draw.rect(screen, ic, (x, y, w, h))
        if click[0] == 1 and action is not None:
            fader(860, 360)
            action()
    else:
        pygame.draw.rect(screen, ac, (x, y, w, h))
    smalltext = pygame.font.Font("freesansbold.ttf", 20)
    textsurf, textrect = text_objects(msg, smalltext)
    textrect.center = ((x + (w / 2)), (y + (h / 2)))
    screen.blit(textsurf, textrect)

def score_d(score):
    font = pygame.font.SysFont(None, 45)
    text = font.render("Score: "+ str(score), True, (0, 0, 0))
    screen.blit(text, (670, 0))

def health_bar(health):
    width = 229 * (health / 200)
    pygame.draw.rect(screen, (255, 0, 0), (20, 25, width, 25))

def shoot():
    mouse = pygame.mouse.get_pos()
    vel = 0.5
    x = 100
    y = 130
    x_calc = mouse[0] - x
    y_calc = mouse[1] - y
    if x_calc == 0:
        x_change = 0
        y_change = y_calc / vel
    else:
        angle = math.atan(y_calc / x_calc)
        x_change = math.cos(angle) * vel
        y_change = math.sin(angle) * vel

    bullets.append(projectiles(x, y, x_change, y_change, shot))

class projectiles:
    def __init__(self, x, y, x_c, y_c, img):
        self.x = x
        self.y = y
        self.x_c = x_c
        self.y_c = y_c
        self.img = img

    def draw(self, win):
        win.blit(self.img, (self.x, self.y))

def spirit_draw(c):
    x = 90
    y = 281
    change_x = 5
    length = 1300 / change_x
    if c == 0:
        screen.blit(spirit, (90, 281))
    elif c < length / 2:
        x = 90 + (c*change_x)
        y = 281
        screen.blit(spiritWalk[(c % 4) % 4], (90 + (c * change_x), 281))
    elif c > length / 2:
        x = 90 + ((length / 2) * 5) + ((c - (length / 2)) * change_x)
        y = 281
        change_x = -5
        screen.blit(spiritWalk1[(c % 4) % 4], (90 + ((length / 2) * 5) + ((c - (length / 2)) * change_x), 281))

    for a in drops:
        if x < a[0] < x+64:
            drops.pop(drops.index(a))
            for i in w_enemies:
                if w_enemies.index(i) == 3:
                    break
                if len(godbs) < 3:
                    godbs.append((i.drawFrame[0][0][0], 0))
                    (i).hits = 3


def godBolt():
    if godA == []:
        godbs.pop(0)
        for i in godT:
            godA.append(i)
    else:
        screen.blit(godA[0], godbs[0])
        godA.pop(0)


def drop(x, y):
    drops.append((x,y))

class enemies:
    attackCounter: int

    def __init__(self, drawFrame, deathFrame, attackFrame, hits):
        self.drawFrame = drawFrame
        self.hits = hits
        self.attackFrame= attackFrame
        self.drawFrame = drawFrame
        self.deathFrame = deathFrame
        self.health = 3
        self.draw_attack = []
        for i in self.attackFrame:
            self.draw_attack.append(i)
        self.attackCounter = 0


    def draw(self, win, score):
        alive = self.drawFrame
        dead = self.deathFrame
        attack = self.attackFrame
        draw_attack = self.draw_attack
        counter = self.attackCounter
        if self.hits < 3:
            if int(alive[0][0][0]) != 160:
                win.blit(alive[0][1], alive[0][0])
                pygame.draw.rect(win, (0, 0, 0), (alive[0][0][0], (alive[0][0][1])-40, 80, 20))
                pygame.draw.rect(win, (255, 0, 0), (alive[0][0][0]+5, (alive[0][0][1]) - 35, 70, 10))
                pygame.draw.rect(win, (0, 255, 0), (alive[0][0][0] + 5, (alive[0][0][1]) - 35, (70/3)*(self.health), 10))
                alive.pop(0)
            else:
                if len(draw_attack) > 1:
                    win.blit(draw_attack[0], alive[0][0])
                    draw_attack.pop(0)
                elif len(draw_attack) == 1:
                    win.blit(draw_attack[0], alive[0][0])
                    draw_attack.pop(0)
                    for i in attack:
                        draw_attack.append(i)
                    enemy_bs.append(projectiles(145, 280,-0.1, 0, enemyAttack))

                pygame.draw.rect(win, (0, 0, 0), (alive[0][0][0], (alive[0][0][1]) - 40, 80, 20))
                pygame.draw.rect(win, (255, 0, 0), (alive[0][0][0] + 5, (alive[0][0][1]) - 35, 70, 10))
                pygame.draw.rect(win, (0, 255, 0), (alive[0][0][0] + 5, (alive[0][0][1]) - 35, (70 / 3) * (self.health), 10))
        elif self.hits > 2:
            if dead != []:
                win.blit(dead[0], alive[0][0])
                dead.pop(0)
            else:
                drop_item = random.randint(1,5)
                if drop_item == 1:
                    drop(alive[0][0][0], 312)
                w_enemies.pop(w_enemies.index(self))
                score += 10
        return score

def enemy_initialize(x, y, wave):
    if len(w_enemies) < wave:
        x_c = 0.1
        hits = 0
        state = 0
        list_frames = []
        list_framesD = []
        list_framesA = []
        distance = 700
        frame_number = int(distance / x_c)
        for i in range(frame_number):
            x -= x_c
            if i % 100 == 0:
                state += 1
            if state == 4:
                state = 0
            list_frames.append([(x, y), enemy[state]])

        for j in enemyD:
            for k in range(100):
                list_framesD.append(j)

        for l in enemyA:
            for m in range(100):
                list_framesA.append(l)

        w_enemies.append(enemies(list_frames, list_framesD, list_framesA, hits))

def enemy_update(b):
    for enemy in w_enemies:
        x = enemy.drawFrame[0][0][0]
        y = enemy.drawFrame[0][0][1]
        if x + 5 <= b.x <= x + 80 and y <= b.y <= y + 100:
            enemy.hits += 1
            enemy.health -= 1
            try:
                bullets.pop(bullets.index(b))
            except:
                p = 0

def game():
    count = 0
    play = True
    sR = True
    enemyA = True
    m_health = 200
    score = 0
    while play:
        if count == 0:
            runner = False
        time = pygame.time.get_ticks()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                play = False
                quit()

        for bullet in bullets:
            if not (bullet.x > 860 or bullet.y < 0 or bullet.y > 360 or bullet.x < 90):
                bullet.x += bullet.x_c
                bullet.y += bullet.y_c
            else:
                bullets.pop(bullets.index(bullet))
        for shots in enemy_bs:
            if not (shots.x < 80):
                shots.x += shots.x_c
            else:
                enemy_bs.pop(enemy_bs.index(shots))
                m_health -= 5
        keys = pygame.key.get_pressed()
        if time % 100 == 0:
            sR = True
        if keys[pygame.K_q] and sR == True and count == 0 and len(bullets) < 6:
            sR = False
            shoot()
        if keys[pygame.K_w] and count == 0:
            runner = True
        if runner == True and time % 5 == 0:
            count += 1
            if count == 260:
                count = 0


        if score < 150:
            random_int = random.randint(1,15)
            if time % (random_int*250) == 0:
                enemyA = True
            if enemyA == True:
                enemyA = False
                spawner()
        elif 140 < score < 300:
            random_int = random.randint(1, 12)
            if time % (random_int * 250) == 0:
                enemyA = True
            if enemyA == True:
                enemyA = False
                spawner1()
        elif 290 < score < 500:
            random_int = random.randint(1, 10)
            if time % (random_int * 250) == 0:
                enemyA = True
            if enemyA == True:
                enemyA = False
                spawner2()
        elif score > 490:
            random_int = random.randint(1, 4)
            if time % (random_int * 300) == 0:
                enemyA = True
            if enemyA == True:
                enemyA = False
                spawner3()

        if score > 1000:
            win()

        score = redrawWin(m_health, score, count)
        if m_health == 0:
            gameOver()


def win():
    screen = pygame.display.set_mode((860,360))
    pygame.display.set_caption("Christmas Is Coming!")
    pygame.display.set_icon(feather)
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                quit()
        Winimg = pygame.image.load(os.path.join('images', "YouWin.png"))
        screen.blit(Winimg, (0, 0))
        pygame.draw.rect(screen, (0, 0, 0), (375, 195, 110, 45))
        button("Quit", 380, 200, 100, 35, buttonColor, hoverColor, pygame.quit)
        pygame.display.update()


def gameOver():
    screen = pygame.display.set_mode((860, 360))
    pygame.display.set_caption("Christmas Is Coming!")
    pygame.display.set_icon(feather)
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                quit()
        GOimg = pygame.image.load(os.path.join('images', "GameOver.png"))
        screen.blit(GOimg, (0, 0))
        pygame.draw.rect(screen, (0, 0, 0), (375, 195, 110, 45))
        button("Quit", 380, 200, 100, 35, buttonColor, hoverColor, pygame.quit)
        pygame.display.update()


def redrawWin(health, score, count=None):
    screen.fill(bgC)

    for bullet in bullets:
        bullet.draw(screen)
        enemy_update(bullet)
    for enem in w_enemies:
        score = enem.draw(screen, score)
    if count != None:
        spirit_draw(count)
    for shots in enemy_bs:
        shots.draw(screen)
    for item in drops:
        screen.blit(feather, item)
    for god in godbs:
        godBolt()

    health_bar(health)
    screen.blit(healthBar, (10, 15))
    score_d(score)
    screen.blit(jesus, (75, 130))
    screen.blit(castle, (0, 0))
    screen.blit(ground, (0, 344))
    pygame.display.update()
    return score

def spawner():
    enemy_initialize(860 ,260, 5)

def spawner1():
    enemy_initialize(860, 260, 7)

def spawner2():
    enemy_initialize(860, 260, 15)

def spawner3():
    enemy_initialize(860, 260, 20)

def tutorial():
    screen = pygame.display.set_mode((860, 360))
    pygame.display.set_caption("Christmas Is Coming!")
    pygame.display.set_icon(feather)
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                quit()
        tutorialimg = pygame.image.load(os.path.join('images', "tutorial.png"))
        screen.blit(tutorialimg, (0, 0))
        button("PLAY", 755, 315, 100, 35, buttonColor, hoverColor, game)
        pygame.display.update()

def prologue():
    screen = pygame.display.set_mode((860, 360))
    pygame.display.set_caption("Christmas Is Coming!")
    pygame.display.set_icon(feather)
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                quit()
        prologueimg = pygame.image.load(os.path.join('images', "prologue.png"))
        screen.blit(prologueimg, (0, 0))
        button("NEXT", 785, 320, 70, 35, buttonColor, hoverColor, tutorial)
        pygame.display.update()

def game_intro():
    running = True

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                pygame.quit()
                quit()
        screen.fill((32, 222, 255))
        startimg = pygame.image.load(os.path.join('images', "TitlePage.png"))
        screen.blit(startimg, (0, 0))
        pygame.draw.rect(screen, black, (290, 110, 220, 70))
        pygame.draw.rect(screen, black, (290, 190, 220, 70))
        button("Start", 300, 120, 200, 50, buttonColor, hoverColor, prologue)
        button("Quit", 300, 200, 200, 50, buttonColor, hoverColor, pygame.quit)

        pygame.display.update()


game_intro()
