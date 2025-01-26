# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define ca = Character("Carmen", color="#c8ffce")
define l = Character("Luacs", color="#ffcc99")
define k = Character("Khyle", color="#ffcc99")
define cl = Character("Clément", color="#ffcc99")
define s = Character("Sasuke", color="#ffcc99")
define j = Character("Jean", color="#ffcc99")
define t = Character("Titus", color="#ffcc99")

default player_name = "Hendrik"
define me = Character("[player_name]", color="#ffcc99")

default khyleDancing = True
default jeanDancing = True
default titusDancing = True
default sasukeDancing = True
default clementDancing = True

image bg playgrounds = "images/bg playgrounds.jpg"
image bg playgroundsBench = "images/bg playgroundsBench.jpg"



# The game starts here.

label start:

    show bg playgrounds with dissolve

    $ player_name = renpy.input("Enter your name:")
    $ player_name = player_name.strip()
    if player_name == "":
        $ player_name = "Hendrik"

    "[player_name] flottait à peine, ses contours tremblotants. Son bleu grisâtre et ses petits plis irréguliers la faisaient paraître encore plus effacée."
    "Elle avançait discrètement, espérant atteindre le tableau des annonces sans croiser personne."
    "Mais, comme toujours, la vie était cruelle avec elle."

    ca "{size=+10}{b}Tiens donc, si ce n'est pas [player_name] La Nulle !{/size}{/b}"

    "[player_name] se figea immédiatement. Elle aurait voulu se dégonfler complètement, disparaître dans l'air."
    "Mais c'était impossible. Lentement, elle se retourna, ses contours frémissant sous la pression."

    show carmen normal at top
    ca "Alors, prête pour le grand bal de demain?"
    ca "Oh, pardon, j'avais oublié... Avec ton look, tu n'as sûrement pas encore trouvé de cavalier."
    ca "J'ai raison, pas vrai?"
    hide carmen

    show me normal at top
    "[player_name] ouvrit la bouche, mais aucun mot ne sortit."
    "Elle voulait répondre, dire quelque chose, n'importe quoi, mais tout ce qu'elle sentit fut une tension dans ses parois fragiles."
    hide me

    show carmen normal at top
    ca "\"Oh non, je suis juste trop moche et bizarre, personne ne veut aller au bal avec moi!\""
    hide carmen

    show crowd normal at top
    "Les bulles du lycée autour éclatèrent de rire."
    hide crowd

    show me normal at top
    "La bulle baissa son regard, fixant le sol en espérant qu'il l'engloutirait."
    me "Je... Je n'ai pas encore demandé..."
    hide me

    show carmen normal at top
    ca "Pas encore demandé?!"
    ca "Ma pauvre, il ne reste plus personne."
    ca "Les bulles comme toi ne vont pas au bal. Elles restent à la maison pour ne pas embarrasser les autres."
    ca "Tu devrais essayer, ça te ferait gagner du temps."
    "Les épines de Carmen scintillèrent sous la lumière du soleil, renforçant son air dominateur."
    hide carmen

    show me normal at top
    "[player_name] ne répondit pas. Ses contours se contractèrent un instant, comme si elle allait éclater de tristesse."
    "Mais au lieu de ça, elle fit demi-tour, flottant péniblement dans l'air."
    "Dans sa tête, les mots de Carmen résonnaient en boucle, comme un écho cruel."
    "\"Les bulles comme toi ne vont pas au bal.\""
    "Peut-être avait-elle raison."
    "Peut-être valait-il mieux rester chez elle demain soir, seule, plutôt que de risquer de devenir la risée de tout le monde."
    "Elle flotta jusqu'à un petit coin tranquille derrière les casiers, là où personne ne la trouverait."
    "Là, à l'abri des regards, elle laissa échapper un petit souffle de tristesse, une minuscule bulle dans la bulle."
    me "{size=-10}Pourquoi est-ce que je ne peux pas être... normale?{/size}"
    "Un silence s'installa. La bulle resta là, seule, à contempler l'idée de ne pas aller au bal. Peut-être que Cléa avait gagné cette fois."
    hide me

    jump miroir_scene

    return

label afterLunch:

    show bg playgroundsBench with dissolve

    "Après le déjeuner, [player_name] se retrouva seule dans la cour de récréation."
    "Elle s'assit sur un banc, les contours frémissants, le cœur battant."
    "Elle se rendit compte qu'elle avait cours de sport l'après-midi."
    show me normal at top
    me "{i}Si je vais en cours, je vais devoir affronter les bulles.{/i}"
    me "{i}Mais surtout... je vais devoir affronter Khyle.{/i}"
    hide me

    menu:
        "Je vais en cours!":
            show me normal at top
            me "{i}Je ne peux pas me défiler.{/i}"
            me "{i}Je vais y aller, et je vais montrer à tout le monde que je suis forte.{/i}"
            hide me
            $ sasukeDancing = False
            jump soccerField

        "Je vais sécher.":
            show me normal at top
            me "{i}Je ne peux pas...{i}"
            me "{i}Je ne peux pas affronter ça.{/i}"
            hide me

            $ khyleDancing = False

            return # A changer
