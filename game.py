import random
import numpy as np

# Constants
SCREEN_WIDTH, SCREEN_HEIGHT = 640, 480
BALL_SIZE = 20
PADDLE_WIDTH, PADDLE_HEIGHT = 20, 100

class Game:
    def __init__(self):
        self.reset()

    def reset(self):
        self.ball_x = SCREEN_WIDTH // 2
        self.ball_y = SCREEN_HEIGHT // 2
        self.ball_speed_x = 5 * random.choice((1, -1))
        self.ball_speed_y = 5 * random.choice((1, -1))
        self.paddle_y = SCREEN_HEIGHT // 2 - PADDLE_HEIGHT // 2
        self.score = 0

    def update(self, paddle_move):
        self.ball_x += self.ball_speed_x
        self.ball_y += self.ball_speed_y

        if self.ball_y <= 0 or self.ball_y >= SCREEN_HEIGHT - BALL_SIZE:
            self.ball_speed_y *= -1

        if self.ball_x <= 0:
            self.ball_speed_x *= -1

        if (self.ball_x >= SCREEN_WIDTH - PADDLE_WIDTH - BALL_SIZE and
            self.paddle_y <= self.ball_y <= self.paddle_y + PADDLE_HEIGHT):
            self.ball_speed_x *= -1
            self.score += 1

        self.paddle_y += paddle_move
        self.paddle_y = max(self.paddle_y, 0)
        self.paddle_y = min(self.paddle_y, SCREEN_HEIGHT - PADDLE_HEIGHT)

        if self.ball_x >= SCREEN_WIDTH:
            return True  # Game over
        return False

    def get_state(self):
        return np.array([self.ball_x, self.ball_y, self.ball_speed_x, self.ball_speed_y, self.paddle_y])
