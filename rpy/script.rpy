define e = Character('Eileen')
define sound7 = 'music/epic-cinematic-trailer.mp3'
define x = 0

# image pic_1 = im.Scale('loli.jpeg', 1920, 1080)
# image pic_2 = im.Scale('loli2.jpeg', 1920, 1080)
image pic_1 = 'loli.jpeg'
image pic_2 = 'loli2.jpeg'
image pic_3 = im.Scale('2.jpg', 1920, 1080)

label start:
    # play music 'music/MainTheme.mp3'
    scene pic_3
    show loli3
    with dissolve
    e 'Role Dialog'
    # stop music

    # play sound sound7
    # hide loli2
    # voice 'music/Demised-To-Shield.mp3'
    # show pic_2 at left
    # with dissolve
    # e 'Dialog 1'

    # play sound sound7
    # show pic_2 at right
    # with fade
    # e 'Dialog 2'
    # stop sound

    stop music
    menu:
        "Choose your role"
        "Choice 1":
            #block of code to run
            $ x = 1
        "Choice 2":
            #block of code to run
            python:
                x = 2
        "Choice 3":
            $ x = 3
    "Hello"
    if x == 1:
        'You choose 1'
    elif x == 2:
        'You choose 2'
    else:
        "You choose 3"
    
    return
        
    