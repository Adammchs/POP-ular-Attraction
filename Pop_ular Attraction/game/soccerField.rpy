image bg soccerField = "images/bg soccerField.jpg"

default khyleAffection = 0

label soccerField:

    show bg soccerField with dissolve

    "Le terrain était en pleine effervescence."
    "Les Thunder Bulls, l'équipe de football star du lycée, s'entraînaient sous les projecteurs. Les cris des joueurs, le bruit des impacts et les applaudissements des spectateurs remplissaient l'air."
    "Non loin de là, sur une plateforme adjacente, une petite foule s'était rassemblée autour d'un espace dédié au Bull'air Dance."
    "Au centre de cette scène flottait [player_name]. Ses contours étaient parfaitement ronds, légèrement iridescents, et elle se déplaçait avec une grâce aérienne qui attirait les regards."
    "Personne ne reconnut [player_name], mais ses mouvements parlaient pour elle."
    "Elle enchaînait des figures, virevoltant dans l'air, ses reflets captant la lumière des projecteurs. Chaque saut, chaque pirouette semblait défier la gravité, et le public retenait son souffle à chaque acrobatie."

    "{b}Sur le terrain, Khyle,{/b} la star des Thunder Bulls, était en pleine démonstration de force, mais il remarqua que quelque chose détournait l'attention. Des joueurs pointaient vers la plateforme du Bull'air Dance."

    show lucas normal at top
    l "Hé, Khyle, regarde là-bas... Tu crois que cette bulle vient d'où? Elle est incroyable."
    hide lucas

    "Khyle, toujours avide d'être au centre de l'attention, plissa les contours et se tourna vers la plateforme. Une bulle qui brillait autant? Qui attirait plus de regards que lui? Impossible."
    "Il s'approcha du bord du terrain, les bras croisés, et observa. La bulle venait de terminer un enchaînement spectaculaire, terminant par un atterrissage gracieux qui déclencha des applaudissements enthousiastes."

    show khyle normal at top
    k "Eh, c'est pas mal... pour un spectacle de danse. Mais ici, c'est un terrain de vrais athlètes."
    "Les rires de ses coéquipiers retentirent, mais la bulle ne se laissa pas démonter. Elle flotta lentement jusqu'à Khyle, ses contours irradiant une confiance qu'il ne lui connaissait pas."
    hide khyle

    show me normal at top
    me "Les vrais athlètes? Ceux qui fuient dès qu'ils voient quelqu'un de meilleur qu'eux?"
    hide me

    show khyle normal at top
    "Khyle arqua un sourcil, décontenancé."
    k "Et toi, tu crois pouvoir me battre?"
    hide khyle

    show me normal at top
    "[player_name] esquissa un sourire discret."
    me "Ce n'est pas une question de te battre, Khyle. Mais peut-être que tu devrais essayer de suivre."
    hide me

    "Et sans attendre, elle retourna sur la plateforme, reprenant son enchaînement de Bull'air Dance."
    "Mais cette fois, elle monta la barre encore plus haut: des figures audacieuses, des envolées aériennes qui semblaient défier les lois de la physique. Le public était captivé."
    "Khyle, piqué au vif, resta sur place, à la fois impressionné et irrité."

    show lucas normal at top
    l "{size=-10}Tu crois qu'elle est qui, cette bulle?{/size}"
    hide lucas

    show khyle normal at top
    "Khyle murmura, plus pour lui-même que pour les autres."
    k "{size=-10}Je sais pas... mais elle me dit quelque chose.{/size}"
    hide khyle

    "Pendant ce temps, [player_name], le cœur battant mais le sourire fier, savait qu'elle venait de franchir une nouvelle étape. Elle n'avait plus besoin de l'approbation de Khyle, ni de personne. Ce soir, elle brillait pour elle-même."

    jump confrontationOnTheField

label confrontationOnTheField:

    "Khyle, intrigué par la transformation de la bulle et vexé d'avoir été mis en retrait, reste planté devant elle. Mais au fond, il commence à se demander qui elle est vraiment."
    "10 minutes plus tard, Khyle réalise que cette mystérieuse bulle est en fait [player_name]."

    show khyle normal at top
    k "T'es pas comme les autres. Avant, on t'aurait même pas remarquée, et maintenant, tout le monde te regarde. Alors, c'est quoi ton secret?"
    "[player_name] le fixe, ses contours oscillant légèrement. Elle sent que cette question est plus profonde qu'il n'y paraît."
    hide khyle

    menu:
        "Parfois, il suffit qu'une bulle se rende compte de sa valeur. Mais merci de l'avoir remarqué, Khyle. Peut-être que t'as plus de profondeur que je pensais.":
            $ khyleAffection += 2
            show khyle normal at top
            k "Eh, tu sais, je suis peut-être pas parfait, mais j'aime pas qu'on pense que je suis qu'un gros ballon de muscles. T'es... différente, dans le bon sens."
        "Oh, ça? C'est un secret. Mais si t'es sage, peut-être que je te le dirai au bal... si tu trouves le courage de demander.":
            $ khyleAffection += 1
            show khyle normal at top
            k "Le bal, hein? T'es sérieuse? J'savais pas que t'étais le genre de bulle à aimer ce genre de trucs."
        "Pas besoin de secret, Khyle. Parfois, les gens changent parce qu'ils en ont marre qu'on les ignore ou qu'on les rabaisse. Ça te parle, non?":
            $ khyleAffection -= 1
            show khyle normal at top
            k "Wow, calme-toi, ok? J'te faisais juste un compliment. Mais bon, si t'es si parfaite, t'as sûrement pas besoin de moi."

    "Khyle, encore indécis sur ce qu'il pense de [player_name], décide de rester pour discuter un peu plus. Il croise les bras, son air arrogant remplacé par de la curiosité sincère."
    k "Ok, je vais être honnête. T'as changé. Mais pourquoi maintenant? Pourquoi t'es plus... comme avant?"
    hide khyle

    menu:
        "Parce que j'en avais marre d'être invisible. J'en avais marre que des bulles comme toi pensent que je valais rien. Alors j'ai décidé de changer... pour moi.":
            $ khyleAffection += 2
            show khyle normal at top
            k "Ouais, je vois. T'as bien fait. J'aurais pas dû te juger si vite. T'es... tu sais, t'es cool."
        "Peut-être que t'étais pas assez attentif avant. Mais c'est pas grave. Moi, je me vois maintenant, et c'est ce qui compte.":
            show khyle normal at top
            k "Ouais, ouais, je comprends. J'ai pas toujours été le meilleur, c'est vrai. Mais tu m'as ouvert les yeux. Merci."
        "Oh, ça te dérange que je sois plus dans ton ombre? Ça doit être dur de plus avoir toute l'attention pour toi.":
            $ khyleAffection -= 1
            show khyle normal at top
            k "Wow, t'es vraiment... tu sais quoi? T'as raison. J'ai été bête. J'aurais pas dû te sous-estimer."
        "Peut-être que j'attendais juste que quelqu'un comme toi remarque que j'étais là... Mais fallait que je prenne les devants.":
            $ khyleAffection += 1
            show khyle normal at top
            k "Ouais, ouais, je comprends. J'aurais dû être plus attentif. Mais bon, c'est pas trop tard, non?"

    if khyleAffection == 4:
        jump maxAffectionSoccerField
    elif khyleAffection == -2:
        jump minusAffectionSoccerField
    else:
        hide khyle
        jump endOfTheField

label maxAffectionSoccerField:

    "Khyle, touché par la sincérité de [player_name], décide de lui faire une proposition."

    k "Écoute, [player_name], je sais que j'ai pas toujours été sympa avec toi. Mais... tu veux bien être ma cavalière pour le bal de demain soir?"
    "Les contours de [player_name] frémissent, surprise. Elle ne s'attendait pas à une telle proposition, surtout pas de la part de Khyle."
    k "Je sais que c'est un peu... bizarre. Mais je me dis que... peut-être que tu pourrais m'apprendre à danser, ou... enfin, tu vois ce que je veux dire."
    "Khyle, mal à l'aise, se gratte la tête, ses contours rosissant légèrement."
    k "Tu n'es pas obligée de répondre tout de suite. Juste... réfléchis-y, ok?"
    hide khyle

    "Khyle, après avoir fait sa demande, se détourne, laissant [player_name] seule sur la plateforme. Elle reste là, les contours frémissants, le cœur battant."
    "Elle n'a jamais été au bal, jamais eu de cavalier. Mais Khyle... il n'est pas comme les autres. Peut-être que ce bal pourrait être le début de quelque chose de nouveau."

    return # A changer

label minusAffectionSoccerField:

    "En ressentant la froideur de [player_name], Khyle se renfrogne et se détourne. Laissant [player_name] seule sur la plateforme, il s'éloigne sans un mot."
    $ khyleDancing = False

    return # A changer

label endOfTheField:

    "Secouée par le changement de [player_name], Khyle hésita un instant, puis lui parla à nouveau."

    k "Si on se retrouve au bal, ne m'évite pas, ok? J'ai... j'ai envie de te connaître un peu plus."
    hide khyle

    return # A changer
