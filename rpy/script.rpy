define e = Character(
    'Eileen',
    what_size = 30,
    who_size = 40,
    who_color="#ed7bb8",
    who_outlines=[(4, '#fff', 0, 0)],
    who_font='Muyao-Softbrush Regular.ttf',
    what_font='Muyao-Softbrush Regular.ttf',
    what_prefix='[[',
    what_suffix=']',
    who_bold=True,
    image='avatar',
    ctc='ctc',
    ctc_position='nestled'
)

define config.say_attribute_transition = Dissolve(0.4)

define sound7 = 'music/epic-cinematic-trailer.mp3'
define x = 0

# image pic_1 = im.Scale('loli.png', 1920, 1080)
# image pic_2 = im.Scale('loli2.png', 1920, 1080)
image pic_1 = 'images/loli.png'
image pic_2 = 'images/loli2.png'
image pic_3 = im.Scale('2.jpg', 1920, 1080)
image logo = im.Scale('logo.png', 1920, 1080)
image bg = im.Scale('bg.jpeg', 1920, 1080)

# add side to indicate as avatar
image side avatar = 'images/avatar.png'
image side avatar b = 'images/avatar.png'
image side avatar c = 'images/avatar2.png'

image avatar = 'images/avatar_large.png'
image avatar b = 'images/avatar_large.png'
image avatar c = 'images/avatar2_large.png'

image ctc = 'images/pink.png'

# image black:
#     contains:
#         '#000000'
#         topleft
#         size(640, 360)
#     contains:
#         '#fff'
#         topright
#         size(640, 360)
#     contains:
#         '#aaa'
#         left
#         size(640, 360)
#     contains:
#         '#666'
#         right
#         size(640, 360)

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


# label start:
#     stop music
#     # a: link-hyperlink
#     e 'Hello {a=call:hello}call hello label{/a}!'
#     e 'Hello {a=https://www.google.com}google hyperlink{/a}!'
#     # image: image
#     e 'Hello {image=images/loli3.png} image!'
#     # size: font-size
#     e 'Hello {size=45}font-size{/size}!'
#     # color: font-color
#     e 'Hello {color=#ef30a2}font-color{/color}!'
#     # alpha: transparency
#     e 'Hello {alpha=0.5}tranparency{/alpha}!'
#     # font: font-style
#     e 'Hello {font=Muyao-Softbrush Regular.ttf}font-style{/font}!'
#     # b: bold
#     e 'Hello {b}bold{/b}!'
#     # i: italic
#     e 'Hello {i}italic{/i}!'
#     return


# label hello:
#     'Hello label'
#     return


# label quit:
#     'You shut down the game!'
#     return


# label after_load:
#     'You read the document'
#     return


# label splashscreen:
#     scene logo
#     with dissolve
#     hide logo
#     with fade
#     return

label start:
    scene bg
    show avatar:
        # xpos 0
        # ypos 0
        subpixel True
        xalign 0.0
        yalign 1.0
        zoom 1.2
        alpha 0.9
        rotate 0
        rotate_pad False
        transform_anchor True
        # rotate 360 in 3 seconds
        # linear 3 rotate 360

        pause 1.0
        parallel:
            # move to right
            easein 3 xalign 1.0
        parallel:
            # move to right
            easein 3 yalign 0.0
    e b "Hello my friend! My first avatar"
    e "My default avatar"
    e c 'My another avatar'
    return


label before_main_menu:
    scene black
    # pause
    show logo
    with dissolve
    hide logo
    with fade
    return
