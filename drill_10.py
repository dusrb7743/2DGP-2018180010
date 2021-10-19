from pico2d import *
import random

# Game object class here

class Grass:
    def __init__(self): # 생성자
        self.image = load_image('grass.png')

    def draw(self):
        self.image.draw(400, 30)


class Boy: # 클래스는 만들었고
    def __init__(self):
        self.image = load_image('run_animation.png')
        self.x, self.y = random.randint(100, 700), 90
        self.frame = random.randint(0, 7)

    def update(self): # 소년의 행위 구현.
        self.x += 5   # 속성값을 바꿈으로써, 행위(오른쪽으로 이동)를 구현.
        self.frame = (self.frame + 1) % 8

    def draw(self):
        self.image.clip_draw(self.frame*100, 0, 100, 100, self.x, self.y)

class Ball:
    def __init__(self):
        self.big_ball = load_image('ball41x41.png')
        self.small_ball = load_image('ball21x21.png')
        self.x, self.y = random.randint(100, 700), 599
        self.jump_y = 0
        self.gravity = random.randint(0, 20)

    def B_update(self):

        self.gravity += 4
        self.y += self.jump_y - self.gravity

        if self.y <= 70:
            self.y = 70
            self.gravity = 0

    def S_update(self):
        self.gravity += 2
        self.y += self.jump_y - self.gravity

        if self.y <= 60:
            self.y = 60
            self.gravity = 0

    def B_draw(self):
        self.big_ball.draw(self.x, self.y)

    def S_draw(self):
        self.small_ball.draw(self.x, self.y)

def handle_events():
    global running
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            running = False
        elif event.type == SDL_KEYDOWN and event.key == SDLK_ESCAPE:
            running = False

# initialization code
open_canvas()

grass = Grass() # 잔디 객체를 생성
ball = Ball()
t = 0

# boy = Boy() # 소년 객체 생성

# team
team = [ Boy() for i in range(10 + 1) ]
team_sball = [ Ball() for i in range(10 + 1)]
team_bball = [ Ball() for i in range(10 + 1)]

running = True

# game main loop code
while running:
    handle_events() # 키 입력을 받아들이는 처리..

    for boy in team:
        boy.update()

    for ball in team_sball:
        ball.S_update()

    for ball in team_bball:
        ball.B_update()

    # Game drawing
    clear_canvas()

    grass.draw()
    for boy in team:
        boy.draw()

    for ball in team_sball:
        ball.S_draw()

    for ball in team_bball:
        ball.B_draw()

    update_canvas()

    if t == 0:
        delay(2)
        t = 1

    delay(0.07)

# finalization code

