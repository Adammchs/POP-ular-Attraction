label invitation_scene:

    scene bg locker

    show me normal at top

    "Voyons voir le contenu de mon casier..."
    "Tiens... J'ai reçu quelques invitations..."
    "Avec qui vais-je aller au Bulle d'Hiver ?"
    hide me

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

        "Personne":
            jump choice_personne

    return

# Labels des choix individuels
label choice_jean:
    show jean normal
    j "Merci de m'avoir choisi <3"
    hide jean
    jump choice1_done

label choice_khyle:
    show khyle normal
    k "Merci de m'avoir choisi <3"
    hide khyle
    jump choice1_done

label choice_clement:
    show clement normal
    cl "Merci de m'avoir choisi <3"
    hide clement
    jump choice1_done

label choice_sasuke:
    show sasuke normal
    s "Merci de m'avoir choisi <3"
    hide sasuke
    jump choice1_done

label choice_titus:
    show titus normal
    t "Merci de m'avoir choisi <3"
    hide titus
    jump choice1_done

label choice_personne:
    show me normal
    me "Bon... Personne ne m'as inviter, c'est pas grave, je vais me preparer et leur faire regreter !"
    hide me
    jump badEndScene
