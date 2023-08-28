import pygame
import random

# code smells intentionally introduced
CANVAS_WIDTH = 400
CANVAS_HEIGHT = 400
SIZE = 20

DELAY = 0.1

# Global variables - avoiding encapsulation
player = pygame.Rect(0, 0, SIZE, SIZE)
goal = pygame.Rect(360, 360, 20, 20)
score = 0
font = pygame.font.Font(None, 20)
movement_direction = [1, 0]
clock = pygame.time.Clock()

def main():
    pygame.init()
    canvas = pygame.display.set_mode((CANVAS_WIDTH, CANVAS_HEIGHT))
    pygame.display.set_caption("Sk. Salahuddin")

    while True:
        for event in pygame.event.get():
            handle_events(event)  # Code smell: Large event handling function

        update_player_position()

        if is_player_out_of_bounds():
            game_over(canvas, score)
            return

        if player.colliderect(goal):
            hit_goal(goal)
            increase_score()

        render_canvas(canvas)

def handle_events(event):
    global movement_direction
    if event.type == pygame.QUIT:
        pygame.quit()
        return
    elif event.type == pygame.KEYDOWN:
        handle_key_press(event.key)  # Code smell: Nested function call
    elif event.type == pygame.MOUSEBUTTONDOWN:
        handle_mouse_click(event.pos)

def handle_key_press(key):
    global movement_direction
    if key == pygame.K_LEFT:
        movement_direction = [-1, 0]  # Code smell: Magic numbers
    elif key == pygame.K_RIGHT:
        movement_direction = [1, 0]
    elif key == pygame.K_UP:
        movement_direction = [0, -1]
    elif key == pygame.K_DOWN:
        movement_direction = [0, 1]

def handle_mouse_click(position):
    global movement_direction
    player.x = position[0] - SIZE // 2
    player.y = position[1] - SIZE // 2
    movement_direction = [0, 0]

# Intentional code smell: Mixing of logic and rendering
def render_canvas(canvas):
    canvas.fill((0, 0, 0))
    pygame.draw.rect(canvas, (0, 0, 255), player)
    pygame.draw.rect(canvas, (255, 69, 0), goal)
    score_text = font.render("Your points: " + str(score), True, (255, 255, 255))
    canvas.blit(score_text, (5, 385))
    pygame.display.flip()
    clock.tick(10)

# Intentional code smell: Long function
def update_player_position():
    global player
    player.x += SIZE * movement_direction[0]
    player.y += SIZE * movement_direction[1]

# Intentional code smell: Inconsistent naming
def is_player_out_of_bounds():
    player_x = player.x
    player_y = player.y

    if (
        player_x > CANVAS_WIDTH - SIZE
        or player_x < 0
        or player_y > CANVAS_HEIGHT - SIZE
        or player_y < 0
    ):
        return True
    return False

# Intentional code smell: Unreadable function
def increase_score():
    global score
    score += 1

# Intentional code smell: Misleading function name
def hit_goal(goal):
    goal.x = random.randrange(0, CANVAS_WIDTH - SIZE + 1, SIZE)
    goal.y = random.randrange(0, CANVAS_HEIGHT - SIZE + 1, SIZE)

# Intentional code smell: Mixing game logic with rendering
def game_over(canvas, score):
    font = pygame.font.Font(None, 40)
    game_over_text = font.render("Game Over!", True, (255, 0, 0))
    score_text = font.render("Your score is: " + str(score), True, (0, 0, 255))
    canvas.blit(game_over_text, (100, 170))
    canvas.blit(score_text, (100, 200))
    pygame.display.flip()
    pygame.time.wait(2000)

if __name__ == "__main__":
    main()
