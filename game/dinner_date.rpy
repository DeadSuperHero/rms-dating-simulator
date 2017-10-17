init:
    $ timer_range = 0
    $ timer_jump = 0

label dinner_date:
    scene restaraunt
    show rms neutral at right

    # These display lines of dialogue.

    "You're not quite sure how this all happened, "

    show w impatient at left
    w "Bonjour, monsieur. What will you two be ordering here tonight?"

    rms "What shall we eat? I'm famished."

    $ time = 5
    $ timer_range = 5
    $ timer_jump = 'toe_cheese'
    show screen countdown
    menu:
        "Steak":
            hide screen countdown
            show rms neutral
            "You tell the waiter that you want to eat medium-rare steak."
            rms "I've been trying to watch my diet recently, but steak sounds wonderful!"
            w "Very well, your steak will be out shortly!"
            hide w
            jump questionLoop
        "Fish":
            hide screen countdown
            "You tell Richard that actually, you're in the mood for grilled swordfish."
            rms "Excellent decision; I too have been watching my weight recently."
            w "Very well, your swordfish will be out shortly!"
            hide w
            jump questionLoop
        "Salad":
            hide screen countdown
            show rms neutral
            "You loudly insist that the both of you must eat Kale Salad."
            rms "It's been a while since I've enjoyed a kale salad, but okay!"
            "The waiter sneers at you for having such disgusting taste."
            w "You may as well eat toe cheese. Your kale will be out shortly!"
            hide w
            jump questionLoop

label toe_cheese:
    hide screen countdown
    show rms neutral
    rms "Well, I guess we shall have to eat toe cheese!"
    "The waiter looks mildly uncomfortable."
    w "Two large helpings of Toe Cheese, coming right up!"
    hide w
    jump questionLoop



label questionLoop:
    show rms neutral
    rms "What shall we talk about?"
    menu:
        "Politics":
            show rms neutral
            rms "Not my favorite subject."
            jump questionLoop
        "Free Software":
            show rms neutral
            jump fsLoop


label fsLoop:
    show rms neutral
    rms "My favorite subject!"
    menu:
        "GNU":
            show rms neutral
            rms "I founded GNU in 1983 as a means to protect the development of Free Software."
            rms "GNU is a recursive acronym, which stands for GNU is Not Unix."
            jump fsLoop
        "Privacy":
            show rms neutral
            rms "Privacy is important."
            rms "This is a test2."
            jump fsLoop
