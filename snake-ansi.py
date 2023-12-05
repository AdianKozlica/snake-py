from datetime import datetime

import os
import time
import random
import keyboard

PLAYFIELD_SIZE = 32

def get_apple_coord():
    x = random.randint(0, PLAYFIELD_SIZE - 1)
    y = random.randint(0, PLAYFIELD_SIZE - 1)

    return x, y

def game_over():
    print("Game over")
    exit()

def main():
    CONTROLS = (('w', 'UP'), ('s', 'DOWN'), ('d', 'RIGHT'), ('a', 'LEFT'))
    snake = [(7, 3), (8,3), (9, 3)]
    snake_direction = 'LEFT'
    
    apple_x, apple_y = get_apple_coord()
    last_set = datetime.now()
    apple_avail = True

    while True:
        for key, direction in CONTROLS:
            if keyboard.is_pressed(key):
                snake_direction = direction
                break

        prev_x, prev_y = (head_x, head_y) = snake[0]

        match snake_direction:
            case 'UP':
                head_y -= 1

            case 'DOWN':
                head_y += 1
            
            case 'RIGHT':
                head_x += 1
            
            case 'LEFT':
                head_x -= 1

        if (head_x < 0 or head_y < 0) or (head_x > PLAYFIELD_SIZE - 1 or head_y > PLAYFIELD_SIZE - 1):
            game_over()

        elif (head_x, head_y) in snake:
            game_over()

        os.system('clear')
        
        curr_datetime = datetime.now()

        if (curr_datetime - last_set).seconds > 5:
            apple_x, apple_y = get_apple_coord()
            last_set = curr_datetime
            apple_avail = True
        
        for i in range(1, len(snake)):
            temp_prev_x, temp_prev_y = snake[i]
            snake[i] = (prev_x, prev_y)
            prev_x, prev_y = temp_prev_x, temp_prev_y

        if (head_x, head_y) == (apple_x, apple_y):
            apple_avail = False
            snake.append((prev_x, prev_y))

        snake[0] = (head_x, head_y)

        for row in range(PLAYFIELD_SIZE):
            for col in range(PLAYFIELD_SIZE):
                if (col, row) in snake:
                    print("\x1b[48;2;0;0;255m \x1b[0m", end='')
                elif (col, row) == (apple_x, apple_y) and apple_avail:
                    print("\x1b[48;2;255;0;0m \x1b[0m", end='')
                else:
                    print("\x1b[48;2;0;255;0m \x1b[0m", end='')
        
            print()

        time.sleep(0.065)

if __name__ == '__main__':
    main()
