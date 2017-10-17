init:
    $ timer_range = 0
    $ timer_jump = 0
    $ points = 0

label dinner_date:
    scene restaraunt
    show rms neutral at right

    # These display lines of dialogue.

    "You're not quite sure how this all happened, "

    show w impatient at left
    w "Bonjour, monsieur. What will you two be ordering here tonight?"

    rms "What shall we eat? I'm famished."

    $ time = 1
    $ timer_range = 1
    $ timer_jump = 'toe_cheese'
    show screen countdown
    menu:
        "Steak":
            hide screen countdown
            $ dinner = "steak"
            show rms neutral
            "You tell the waiter that you want to eat medium-rare steak."
            rms "I've been trying to watch my diet recently, but steak sounds wonderful!"
            w "Very well, your steak will be out shortly!"
            hide w
            jump dinnerTransition
        "Fish":
            hide screen countdown
            $ dinner = "swordfish"
            "You tell Richard that actually, you're in the mood for grilled swordfish."
            rms "Excellent decision; I too have been watching my weight recently."
            w "Very well, your swordfish will be out shortly!"
            hide w
            jump dinnerTransition
        "Salad":
            hide screen countdown
            $ dinner = "kale"
            show rms neutral
            "You loudly insist that the both of you must eat Kale Salad."
            rms "It's been a while since I've enjoyed a kale salad, but okay!"
            "The waiter sneers at you for having such disgusting taste."
            w "You may as well eat toe cheese. Your kale will be out shortly!"
            hide w
            jump dinnerTransition

label toe_cheese:
    $ dinner = "toe_cheese"
    hide screen countdown
    show rms neutral
    rms "Well, I guess we shall have to eat toe cheese!"
    "The waiter looks mildly uncomfortable."
    w "Two large helpings of Toe Cheese, coming right up!"
    hide w
    jump dinnerTransition


label dinnerTransition:
    rms "What shall we talk about?"
    jump questionLoop


label questionLoop:
    show rms neutral
    if points > 3:
        jump foodLoop
    else:
        menu:
            "Politics":
                show rms neutral
                rms "Not my favorite subject."
                jump politicsLoop
            "Free Software":
                show rms neutral
                rms "My favorite subject!"
                jump fsLoop


label fsLoop:
        menu:
            "History of Free Software":
                $ points +=1
                show rms neutral
                rms "I founded GNU in 1983 as a means to protect the development of Free Software."
                rms "GNU is a recursive acronym, which stands for GNU is Not Unix."
                jump questionLoop
            "Privacy":
                $ points +=1
                show rms neutral
                rms "People have the right to privacy."
                rms "The problem with proprietary software is that those systems inherently prevent you from looking inside of them."
                rms ""
                jump questionLoop
            "GNU":
                $ points +=1
                show rms neutral
                rms "GNU is my child project, and I am very proud of what it has become."
                rms "It is a completely free operating system."
                jump questionLoop
            "Open Source":
                $ points +=1
                show rms neutral
                rms "Don't get me started."
                jump questionLoop

label politicsLoop:
    menu:
        "Liberals":
            $ points +=1
            show rms neutral
            rms "Something about liberal politics."
            jump questionLoop
        "Donald Trump":
            $ points +=1
            show rms neutral
            rms "He's pretty greedy."
            jump questionLoop
        "Gun Control":
            $ points +=1
            show rms neutral
            rms "Guns are out there."
            jump questionLoop


label foodLoop:
    show w
    rms "Oh boy, the food is here!"
    "You ordered [dinner]! Eat up!"
