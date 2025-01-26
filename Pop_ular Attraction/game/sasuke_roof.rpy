label sasuke_roof:
    scene bg high_school_roof

    show me normal at left
    me "Hey, mais que fait tu là toi tu sèches aussi ?"

    "???" "La lumière du savoir ne m'atteint plus. Aujourd'hui, je me perds dans les ombres, là où les cours ne peuvent me suivre. Bonjour."
    show sasuke normal at right

    me "Ah, que fais-tu ?"
    s "Les jours qui passent sont comme des ombres qui s'étirent dans le silence. Ils ne laissent derrière eux que des fragments de ce que nous étions, tandis que l'avenir s'efface sous le poids de nos choix."

    menu:
        "C'est l'une des premières fois que je te vois, tu fais quoi d'habitude ?":
            jump choice1_first_time
        "Waw, c'est magnifique ce que tu viens de dire là":
            jump choice2_beautiful
        "Je ne comprend pas ce que tu viens de dire":
            jump choice3_dont_understand

label choice1_first_time:
    $ sasukeDancing = False
    me "C'est l'une des premières fois que je te vois, tu fais quoi d'habitude ?"
    s "Rien de spécial, je laisse mes pensées vagabonder dans l'immensité du monde"
    me "Waw, super."
    s "Je vais te laisser, mais ce n'est pas un adieu, juste une ombre qui s'éloigne."
    s "Ne cherche pas à me suivre... Là où je vais, la lumière n'a pas sa place."
    "*Sasuke part"
    me "Étrange comme conversation"

    jump invitation_scene

label choice2_beautiful:
    $ sasukeDancing = True
    me "Waw, c'est magnifique ce que tu viens de dire là"
    s "Vraiment ? Merci, tu es la première personne à me dire ça."
    s " Tu es... Spécial."
    "*Part"

    jump invitation_scene

label choice3_dont_understand:
    $ sasukeDancing = False
    me "Je ne comprend pas ce que tu viens de dire"
    s "De toute façon, personne ne me comprend"
    "*Il se rapproche du vide*"
    me "Qu'est ce que tu fais ?"
    s "Laisse, moi seul. Ne cherche pas à me suivre... Là où je vais, la lumière n'a pas sa place."
    "*Il saute*"
    me "nooooooooooooooooooo..."
    me "oooooooooooooooooooo..."
    me "oooooooooooooooooooooon"
    me "Bon, moi, je vais draguer quelqu'un d'autre"

    jump invitation_scene
