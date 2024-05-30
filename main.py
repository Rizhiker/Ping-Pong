from pygame import *
back = (200, 255, 255)
win_width = 600
win_height = 500
window = display.set_mode((win_width, win_height))
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
    key_pressed = key.get_pressed()
    def update_l(self):
        keys = key.get_pressed()
        if keys[K_w] and self.rect.y < win_height:
            self.rect.y -= self.speed
        if keys[K_s]:
            self.rect.y += self.speed
    def update_r(self):
        keys = key.get_pressed()
        if keys[K_UP] and self.rect.y < win_height:
            self.rect.y -= self.speed
        if keys[K_DOWN]:
            self.rect.y += self.speed
        
racket1 = Player('racket (1).png', 30,200,20,100,5)
racket2 = Player('racket (1).png', 520,200,20,100,5)
ball = GameSprite('tenis_ball (1).png', 200,200,50,50,50)

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
        window.fill((200,255,255))
        racket1.update_l()
        racket2.update_r()
        ball.rect.x += speed_x
        ball.rect.y += speed_y
        if ball.rect.y > win_height - 50 or ball.rect.y < 0:
            speed_y *= -1

        if sprite.collide_rect(racket1, ball) or sprite.collide_rect(racket2, ball):
            speed_x *= -1
            speed_y *= -1

        if ball.rect.x > win_width:
            finish = True
            window.blit(lose2, (200,200))

        if ball.rect.x < 0:
            finish = True
            window.blit(lose1, (200,200))

        racket1.reset()
        racket2.reset()
        ball.reset()
    display.update()
    clock.tick(FPS)
