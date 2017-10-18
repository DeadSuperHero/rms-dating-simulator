# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define rms = Character("Richard Stallman")
define w = Character("Waiter")
image rms neutral = "stallman.jpg"
image boston_plaza = "boston_plaza.jpg"


# The game starts here.

label splashscreen:
    scene black
    with Pause(1)

    show text "{size=+10} This program is {b}Free Software{/b}, \n and licensed under the{/size} \n {size=+20}GNU GPL v3.{/size}"
    with Pause(2)

    hide text with dissolve
    with Pause(1)

    return

label start:
    # For now, just jump into the Strange Dream loop.
    jump strangeDream
    # This ends the game.

    return
