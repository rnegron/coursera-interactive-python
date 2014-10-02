#pong.py by rucury

import simplegui
import random

WIDTH = 600
HEIGHT = 400       
BALL_RADIUS = 20
PAD_WIDTH = 8
PAD_HEIGHT = 80
HALF_PAD_WIDTH = PAD_WIDTH / 2
HALF_PAD_HEIGHT = PAD_HEIGHT / 2
LEFT = False
RIGHT = True

paddle1_pos = [HALF_PAD_WIDTH, (HEIGHT / 2) - HALF_PAD_HEIGHT]
paddle2_pos = [(WIDTH - HALF_PAD_WIDTH), (HEIGHT / 2) - HALF_PAD_HEIGHT]
paddle1_vel = 0
paddle2_vel = 0

ball_pos = [WIDTH / 2, HEIGHT / 2]
ball_vel = [0, 0]

score1 = 0
score2 = 0

def spawn_ball(direction):
    global ball_pos, ball_vel 
    
    x = random.randrange(120, 240) / 60
    y = random.randrange(60, 180) / 60
    
    ball_pos = [WIDTH / 2, HEIGHT / 2]
    if direction == RIGHT:
        ball_vel = [x, -y]
    if direction == LEFT:
        ball_vel = [-x, -y]
        
def new_game():
    global paddle1_pos, paddle2_pos, paddle1_vel, paddle2_vel
    global score1, score2  
    score1 = 0
    score2 = 0
    spawn = random.randint(0, 1)
    spawn_ball(spawn)

def draw(c):
    global score1, score2, paddle1_pos, paddle2_pos, ball_pos, ball_vel, paddle1_vel, paddle2_vel
  
    c.draw_line([WIDTH / 2, 0],[WIDTH / 2, HEIGHT], 1, "White")
    c.draw_line([PAD_WIDTH, 0],[PAD_WIDTH, HEIGHT], 1, "White")
    c.draw_line([WIDTH - PAD_WIDTH, 0],[WIDTH - PAD_WIDTH, HEIGHT], 1, "White")
        
    ball_pos[0] += ball_vel[0]
    ball_pos[1] += ball_vel[1]
      
    if ball_pos[1] <= 0 + BALL_RADIUS:
        ball_vel[1] = -ball_vel[1]
    
    elif ball_pos[1] >= (HEIGHT - 1) - BALL_RADIUS:
        ball_vel[1] = -ball_vel[1]
                    
    if ball_pos[0] <= (0 + PAD_WIDTH) + BALL_RADIUS:
        if ball_pos[1] >= paddle1_pos[1] and ball_pos[1] <= paddle1_pos[1] + 80:
            ball_vel[0] = -ball_vel[0]
            ball_vel[0] *= 1.1        
        else: 
            score2 += 1
            spawn_ball(RIGHT)          
            
    if ball_pos[0] >= (WIDTH - 1 - PAD_WIDTH) - BALL_RADIUS:
        if ball_pos[1] >= paddle2_pos[1] and ball_pos[1] <= paddle2_pos[1] + 80:
               ball_vel[0] *= 1.1
               ball_vel[0] = -ball_vel[0]
        else:
            score1 += 1
            spawn_ball(LEFT)
            
    c.draw_circle([ball_pos[0], ball_pos[1]], BALL_RADIUS, 2, "White", "White")
    
    if paddle1_pos[1] + paddle1_vel >= 0 and paddle1_pos[1] + paddle1_vel <= 320:
       paddle1_pos[1] += paddle1_vel
        
    if paddle2_pos[1] + paddle2_vel >= 0 and paddle2_pos[1] + paddle2_vel <= 320:
        paddle2_pos[1] += paddle2_vel
    
    c.draw_line([paddle1_pos[0], paddle1_pos[1]],[HALF_PAD_WIDTH, paddle1_pos[1] + PAD_HEIGHT], PAD_WIDTH, "White") 
    c.draw_line([paddle2_pos[0], paddle2_pos[1]], [WIDTH - HALF_PAD_WIDTH, paddle2_pos[1] + PAD_HEIGHT], PAD_WIDTH, "White")
   
    c.draw_text(str(score1), [150, 100], 80, "White")
    c.draw_text(str(score2), [450, 100], 80, "White")
    
def keydown(key):
    global paddle1_vel, paddle2_vel
    
    if key==simplegui.KEY_MAP["w"]:
        paddle1_vel -= 4
    elif key==simplegui.KEY_MAP["s"]:
        paddle1_vel += 4
    elif key==simplegui.KEY_MAP["up"]:
        paddle2_vel -= 4
    elif key==simplegui.KEY_MAP["down"]:
        paddle2_vel += 4
   
def keyup(key):
    global paddle1_vel, paddle2_vel
    
    if key==simplegui.KEY_MAP["w"]:
        paddle1_vel += 4
    elif key==simplegui.KEY_MAP["s"]:
        paddle1_vel -= 4
    elif key==simplegui.KEY_MAP["up"]:
        paddle2_vel += 4
    elif key==simplegui.KEY_MAP["down"]:
             paddle2_vel -= 4

frame = simplegui.create_frame("Pong", WIDTH, HEIGHT)
frame.set_draw_handler(draw)
frame.set_keydown_handler(keydown)
frame.set_keyup_handler(keyup)
frame.add_button("Restart", new_game)

new_game()
frame.start()
