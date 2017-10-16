# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define rms = Character("Richard Stallman")
define w = Character("Waiter")
image rms neutral = "stallman.jpg"

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

    # Show a background. This uses a placeholder by default, but you can
    # add a file (named either "bg room.png" or "bg room.jpg") to the
    # images directory to show it.

    scene bg room
    with fade

    "It's fall, and you've just moved into the Boston area for school."
    "Through an unexpected set of circumstances, you are on a date with Richard Stallman."

    jump dinner_date
    # This ends the game.

    return
