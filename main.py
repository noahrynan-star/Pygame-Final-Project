# Pygame Final
# Author: Noah Ongcarranceja
# May 27

import math
import random

import pygame

pygame.mixer.init()
pygame.init()

# COLOURS - (R, G, B)
# CONSTANTS ALL HAVE CAPS FOR THEIR NAMES
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
GREY = (128, 128, 128)
ORANGE = (255, 140, 0)


# CONSTANTS
WIDTH = 800
HEIGHT = 600
SIZE = (WIDTH, HEIGHT)

BALL_RADIUS = 13
BALL_START_X = WIDTH // 2
BALL_START_Y = HEIGHT - 60

HOOP_INNER_WIDTH = 120
HOOP_Y = int(HEIGHT * 0.30)

GRAVITY = 0.45
GAME_DURATION = 30


def main():

    # screen
    screen = pygame.display.set_mode(SIZE)
    pygame.display.set_caption("Basketball Shootout!")

    clock = pygame.time.Clock()

    # background music and volume
    pygame.mixer.music.load("Assets/Sounds/bball.mp3")
    pygame.mixer.music.set_volume(0.5)

    pygame.mixer.music.play(0)

    # shooting sound through "data"
    score_sound = pygame.mixer.Sound("Assets/Sounds/score.mp3")
    miss_sound = pygame.mixer.Sound("Assets/Sounds/miss.mp3")

    # fonts using the systemfonts
    font = pygame.font.SysFont(None, 48)
    big_font = pygame.font.SysFont(None, 80)
    small_font = pygame.font.SysFont(None, 30)

    # hoop set up
    hoopx = WIDTH // 2
    hoopvel = 3

    # ball set up
    ballx = BALL_START_X
    bally = BALL_START_Y
    ballvx = 0
    ballvy = 0
    ball_in_play = False
    score = 0

    # time in ms
    start_ticks = pygame.time.get_ticks()

    game_over = False
    done = False

    # ------------ MAIN GAME LOOP
    while not done:
        # ------ MAIN EVENT LISTENER
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done = True

            if event.type == pygame.MOUSEBUTTONDOWN:
                if pygame.mouse.get_pressed()[0] == True:
                    if ball_in_play == False:
                        if game_over == False:
                            mx, my = pygame.mouse.get_pos()
                            dx = mx - BALL_START_X
                            dy = my - BALL_START_Y
                            dist = math.sqrt(dx * dx + dy * dy)
                            if dist == 0:
                                dist = 1
                            speed = 20
                            ballvx = (dx / dist) * speed
                            ballvy = (dy / dist) * speed
                            ballx = BALL_START_X
                            bally = BALL_START_Y
                            ball_in_play = True
        # ------ GAME LOGIC

        # timer
        elapsed = (pygame.time.get_ticks() - start_ticks) // 1000

        time_left = max(0, GAME_DURATION - elapsed)

        if time_left == 0:
            game_over = True

        # move hoop sidetoside
        if game_over == False:
            hoopx += hoopvel

            leftlmt = HOOP_INNER_WIDTH // 2 + 30
            rightlmt = WIDTH - HOOP_INNER_WIDTH // 2 - 30

            if hoopx >= rightlmt:
                hoopx = rightlmt
                hoopvel *= -1

            if hoopx <= leftlmt:
                hoopx = leftlmt
                hoopvel *= -1

        # ball movement/gravity (SLIGHTLY GUIDED BY AI)
        if ball_in_play:
            ballvy += GRAVITY
            ballx += ballvx
            bally += ballvy
            rim_left = hoopx - HOOP_INNER_WIDTH // 2
            rim_right = hoopx + HOOP_INNER_WIDTH // 2

            # scoring( count if ball falls through hoop )
            if (
                rim_left + 6 < ballx < rim_right - 6
                and abs(bally - HOOP_Y) < 16
                and ballvy > 0
            ):
                score += 2
                score_sound.play()
                ball_in_play = False

            # miss ( reset ball when miss/ leaves screen )
            if bally > HEIGHT + 40:
                miss_sound.play()
                ball_in_play = False

            if ballx < -40:
                miss_sound.play()
                ball_in_play = False

            if ballx > WIDTH + 40:
                miss_sound.play()
                ball_in_play = False

        # ------ DRAWING TO SCREEN

        # background image using uploadeed image in assets and sizing
        court = pygame.image.load("Assets/images/court.jpg")
        court = pygame.transform.scale(court, (SIZE))

        # background start up
        screen.blit(court, (0, 0))

        # images
        hoop_img = pygame.image.load("Assets/images/hoop.png")
        hoop_img = pygame.transform.scale(hoop_img, (200, 180))
        rimy = HOOP_Y

        # hoop

        hoop_int = int(hoopx)
        screen.blit(
            hoop_img,
            (hoop_int - 100, rimy - 70),
        )

        # starting ball at the middle bottom of screen
        pygame.draw.circle(
            screen,
            BLACK,
            (BALL_START_X, BALL_START_Y),
            BALL_RADIUS,
        )

        pygame.draw.circle(
            screen,
            ORANGE,
            (BALL_START_X, BALL_START_Y),
            BALL_RADIUS,
            2,
        )

        # draw ball ( main ball )
        if ball_in_play:
            bx = int(ballx)
            by = int(bally)

            pygame.draw.circle(
                screen,
                ORANGE,
                (bx, by),
                BALL_RADIUS,
            )

            pygame.draw.circle(
                screen,
                ORANGE,
                (bx, by),
                BALL_RADIUS,
                2,
            )

            pygame.draw.line(
                screen,
                BLACK,
                (bx - BALL_RADIUS, by),
                (bx + BALL_RADIUS, by),
                2,
            )

            pygame.draw.line(
                screen,
                BLACK,
                (bx, by - BALL_RADIUS),
                (bx, by + BALL_RADIUS),
                2,
            )

        # score text
        score_text = font.render(f"Score: {score}", True, BLUE)
        screen.blit(score_text, (90, 525))

        # time text
        if time_left <= 10:
            color = RED
        else:
            color = WHITE
        time_text = font.render(f"Time: {time_left}s", True, BLUE)
        screen.blit(
            time_text,
            (WIDTH - time_text.width - 90, 525),
        )

        # instructions
        inst = small_font.render("AIM AND CLICK!", True, BLUE)
        screen.blit(inst, (WIDTH // 2 - inst.width // 2, HEIGHT - 45))

        # game over
        if game_over:
            overlay = pygame.Surface(SIZE)
            overlay.fill(BLACK)
            screen.blit(overlay, (0, 0))
            over_text = big_font.render(
                "GAME OVER!",
                True,
                ORANGE,
            )

            points_text = font.render(
                f"Final Score: {score} pts",
                True,
                WHITE,
            )

            screen.blit(
                over_text,
                (WIDTH // 2 - over_text.width // 2, HEIGHT // 2 - 80),
            )

            screen.blit(
                points_text,
                (WIDTH // 2 - points_text.width // 2, HEIGHT // 2 + 10),
            )

            # Update screen

        pygame.display.flip()

        # ------ CLOCK TICK
        clock.tick(75)  # fps/speed

    pygame.quit()


if __name__ == "__main__":
    main()
