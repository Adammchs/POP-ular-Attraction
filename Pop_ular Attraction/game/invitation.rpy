label invitation_scene:

    scene bg casier

    show me normal at top

    "Voyons voir le contenu de mon casier..."
    "Tiens... J'ai reçu quelques invitations..."
    "Avec qui vais-je aller au Bulle d'Hiver ?"

    # Construction dynamique du menu
    menu:
        "Jean le normy" if jeanDancing:
            jump choice_jean

        "Khyle le sportif" if khyleDancing:
            jump choice_khyle

        "Sasuke le bizarre" if sasukeDancing:
            jump choice_sasuke

        "Clement le geek" if clementDancing:
            jump choice_clement

        "Titus le complotiste" if titusDancing:
            jump choice_titus

    return

# Labels des choix individuels
label choice_jean:
    j "Merci de m'avoir choisi <3"
    jump choice1_done

label choice_khyle:
    k "Merci de m'avoir choisi <3"
    jump choice1_done

label choice_clement:
    cl "Merci de m'avoir choisi <3"
    jump choice1_done

label choice_sasuke:
    s "Merci de m'avoir choisi <3"
    jump choice1_done

label choice_titus:
    t "Merci de m'avoir choisi <3"
    jump choice1_done

# Label final après un choix
label choice1_done:
    "Maintement, il faut que je me prépare pour le bulle d'hiver..."
    return
