# THE ULTIMATE BASKETBALL SHOOTOUT!

> Testing your precision and accuracy in the basketball realm.

![screenshot]("Assets/Images/gamepic.png")


## Description

What is this project? Describe the interactive experience: what kind of game/experience it is, what the player is trying to do, and what makes it interesting. (2 to 4 sentences.)

This project is a basketball game inspired by the love of the sport of the creator. Players experience fun precision aiming with sound effects and music. All the player will do is aim and shoot the ball into the hoop, moving side to side. This is interesting because getting the timing and aiming right takes a while, which keeps players intrigued.

## How to Run

1. Make sure you have **Python 3.13** installed.
2. Install the dependencies:
   *For most of you, this is just `pip install pygame-ce`.*
3. Run the game:
   ```
   python main.py
   ```

## Controls

| Input | Action |
| left mouse click | shoot ball |
| move cursor side to side | aim |

## Features

- [ ] Hoop moves side-to-side
- [ ] Beach background
- [ ] Timer and Score Counter on the sides
- [ ] Gravity and Physics of the ball!!!

## Dependencies

- none beyond pygame

## Assets

List any images, sounds, fonts, or other files in the `assets/` folder, and where each came from:

- `assets/[file]` - [made by me / source + link]
- 'assets/images/[court.jpg]' - [https://www.magnific.com/free-vector/realistic-galaxy-background_14960493.htm#fromView=keyword&page=1&position=0&uuid=3b4aef00-c4d4-473c-91ad-1410532df86c&query=Background+space]
- 'assets/images/[hoop.png]' - [https://pngtree.com/freepng/high-performance-basketball-rim-for-professional-courts_16326564.html]
- 'assets/sounds/[bball.mp3]' - [https://pixabay.com/music/beats-basketball-285178/]
- 'assets/sounds/[miss.mp3]' - [https://pixabay.com/sound-effects/people-boo-6377/]
- 'assets/sounds/[score.mp3]' - [https://pixabay.com/sound-effects/technology-cash-register-1-513922/]


## Starting Point (Class Code)

State which code from class you used as a starting point, as required by the guardrails:

- Started from `[boilerplate_pygame.py]` - used for the colors used for the ball and the texts seen. It helped with the title and the sizing of objects. It helped organize the main code, the main game loop, and the game logic that consists of the building of the ball, movement of the ball and hoop, and everything else.

## AI Disclosure

**Model(s) used:** ChatGPT

| Lines / Commit | What it does (in my own words) | Why I used it | AI vs. my own |
|----------------|--------------------------------|---------------|---------------|
| `main.py` lines [x-y] / commit [hash] | [explain the code] | [why] | [pasted / adapted / written by me with AI help] |
| 'main.py' lines [129-158] | / gravity and physics and ball going into the hoop and resetting the ball | I have used the help of AI in these lines because I had a hard time figuring it out through past lessons and notes. My understanding of physics has now evolved through the help of AI. | All I could find and understand was the example on May 12th" def calc_grav(self):
        """ Calculate effect of gravity. """
        if self.change_y == 0:
            self.change_y = 1
        else:
            self.change_y += .35 ",         This part was my initial idea of gravity, but it confused me, so I had the help of AI mixed with my knowledge of gravity to create the ball movement of the game. In the end, the code that you see in lines 129-159 is the best that AI and I could come up with!

## Known Bugs / Limitations

- none!

## Possible Future Improvements

- harder and more levels
- nicer ball or upgradable ball with effects
- ability to pick different balls, backgrounds, and music sections
- maps
- buffs 

## Author

Noah Ongcarranceja
