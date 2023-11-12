define e = Character('Eileen')
define sound7 = 'music/epic-cinematic-trailer.mp3'
define x = 0

# image pic_1 = im.Scale('loli.jpeg', 1920, 1080)
# image pic_2 = im.Scale('loli2.jpeg', 1920, 1080)
image pic_1 = 'loli.jpeg'
image pic_2 = 'loli2.jpeg'
image pic_3 = im.Scale('2.jpg', 1920, 1080)
image logo = im.Scale('logo.png', 1920, 1080)

# label start:
    # play music 'music/MainTheme.mp3'
    # scene pic_3
    # show loli3
    # with dissolve
    # e 'Role Dialog'
    # # stop music

    # # play sound sound7
    # # hide loli2
    # # voice 'music/Demised-To-Shield.mp3'
    # # show pic_2 at left
    # # with dissolve
    # # e 'Dialog 1'

    # # play sound sound7
    # # show pic_2 at right
    # # with fade
    # # e 'Dialog 2'
    # # stop sound

    # stop music
    # menu:
    #     "Choose your role"
    #     "Choice 1":
    #         #block of code to run
    #         $ x = 1
    #     "Choice 2":
    #         #block of code to run
    #         python:
    #             x = 2
    #     "Choice 3":
    #         $ x = 3
    # "Hello"
    # if x == 1:
    #     'You choose 1'
    # elif x == 2:
    #     'You choose 2'
    # else:
    #     "You choose 3"
    
    # return


label start:
    stop music
    # a: link-hyperlink
    e 'Hello {a=call:hello}call hello label{/a}!'
    e 'Hello {a=https://www.google.com}google hyperlink{/a}!'
    # image: image
    e 'Hello {image=images/loli3.jpeg} image!'
    # size: font-size
    e 'Hello {size=45}font-size{/size}!'
    # color: font-color
    e 'Hello {color=#ef30a2}font-color{/color}!'
    # alpha: transparency
    e 'Hello {alpha=0.5}tranparency{/alpha}!'
    # font: font-style
    e 'Hello {font=Muyao-Softbrush Regular.ttf}font-style{/font}!'
    # b: bold
    e 'Hello {b}bold{/b}!'
    # i: italic
    e 'Hello {i}italic{/i}!'
    return


label hello:
    'Hello label'
    return


label quit:
    'You shut down the game!'
    return


label after_load:
    'You read the document'
    return


label splashscreen:
    scene logo
    with dissolve
    hide logo
    with fade
    return
    