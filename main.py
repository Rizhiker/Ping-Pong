from pygame import *
back = (200, 255, 255)
winf_width = 600
win_height = 500
window = display.set_mode((winf_width, win_height))
window.fill(back)

class GameSprite(sprite.Sprite):
    def __init__(self, player_image, player_x, player_y,size_x, size_y, player_speed):
        super().__init__()
        self.image = transform.scale(image.load(player_image), (size_x, size_y))
        self.speed = player_speed
        self.rect = self.image.get_rect()
        self.rect.x = player_x
        self.rect.y = player_y        
    def reset(self):
        window.blit(self.image, (self.rect.x, self.rect.y))

class Player(GameSprite):
    def update(self):
        key_pressed = key.get_pressed()
    def update_l(self):
        keys = key.get_pressed()
        if keys[K_w] and self.rect.y > 5:
            self.rect.y += self.speed
        if keys[K_s] and self.rect.y > 5:
            self.rect.y -= self.speed
    def update_r(self):
        if keys[K_UP] and self.rect.y > 5:
            self.rect.y += self.speed
        if keys[K_DOWN] and self.rect.y > 5:
            self.rect.y -= self.speed
        
racket1 = Player('racket (1).png', 30,200,4,50,150)
racket2 = Player('racket (1).png', 520,200,4,50,150)
ball = GameSprite('tenis_ball (1).png', 200,200,4,50,50)

font.init()
font = font.Font(None, 35)
lose1 = font.render('PLAYER 1 LOSE!', True, (180, 0 ,0))
lose2 = font.render('PLAYER 2 LOSE!', True, (180, 0, 0))

speed_x = 3
speed_y = 3



game = True
finish = False
clock = time.Clock()
FPS = 60

while game:
    for e in event.get():
        if e.type == QUIT:
            game = False
        if  finish != True:
            ball.rect.x += speed_x
            ball.rect.y += speed_y
    
    if finish != True:
        racket1.update_l()
        racket2.update_r()
        ball.rect.x += speed_x
        ball.rect.y += speed_y
        if ball.rect.y > win_height - 50 or ball_rect.y < 0:
            speed_y *= -1

        if sprite.collide_rect(racket1, ball) or sprite.collide_rect(racket2, ball):
            speed_x *= -1
            spped_y *= -1

        if ball.rect.x > win.width:
            finish = True
            window.blit(lose2, (200,200))

        if ball.rect.x < win.width:
            finish = True
            window.blit(lose1, (200,200))

    racket1.reset()
    racket2.reset()
    ball.reset()
    display.update()
    clock.tick(FPS)
