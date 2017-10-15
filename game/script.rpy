# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define rms = Character("Richard Stallman")
define w = Character("Waiter")
image rms neutral = "stallman.jpg"

# The game starts here.

label start:

    # Show a background. This uses a placeholder by default, but you can
    # add a file (named either "bg room.png" or "bg room.jpg") to the
    # images directory to show it.

    scene bg room
    with fade

    "It's fall, and you've just moved into the Boston area for school."
    "Through an unexpected set of circumstances, you are on a date with Richard Stallman."

    show rms neutral

    # These display lines of dialogue.

    "You're not quite sure how this all happened, "

    show w impatient
    w "Bonjour, monsieur. What will you two be ordering here tonight?"

    rms "What shall we eat? I'm famished."

    menu:
        "Steak":
            show rms happy
            "You tell the waiter that you want to eat medium-rare steak."
            rms "I've been trying to watch my diet recently, but steak sounds wonderful!"
            w "Very well, your steak will be out shortly!"
            hide w
            jump questionLoop
        "Fish":
           "You tell Richard that actually, you're in the mood for grilled swordfish."
           rms "Excellent decision; I too have been watching my weight recently."
           w "Very well, your swordfish will be out shortly!"
           hide w
           jump questionLoop
        "Salad":
            show rms unhappy
            "You loudly insist that the both of you must eat Kale Salad."
            rms "It's been a while since I've enjoyed a kale salad, but okay!"
            "The waiter sneers at you for having such disgusting taste."
            w "You may as well eat toe cheese. Your kale will be out shortly!"
            hide w
            jump questionLoop


label questionLoop:
    show rms neutral
    rms "What shall we talk about?"
    menu:
        "Politics":
            show rms unhappy
            rms "Not my favorite subject."
            jump questionLoop
        "Free Software":
            show rms happy
            rms "My favorite subject!"
            jump questionLoop


    # This ends the game.

    return
