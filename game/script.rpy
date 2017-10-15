# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define rms = Character("Richard Stallman")


# The game starts here.

label start:

    # Show a background. This uses a placeholder by default, but you can
    # add a file (named either "bg room.png" or "bg room.jpg") to the
    # images directory to show it.

    scene bg room

    # This shows a character sprite. A placeholder is used, but you can
    # replace it by adding a file named "eileen happy.png" to the images
    # directory.

    show rms happy

    # These display lines of dialogue.

    "You find yourself in front of GNU's greatest leader, your personal weakness, Richard Stallman."

    rms "I hope you're running Free Software!"

    rms "Once you add a story, pictures, and music, you can release it to the world!"

    # This ends the game.

    return
