image bg informatiqueClass = "images/bg informatiqueClass.jpg"

default clementAffection = 0

label informatiqueClass:

    scene bg informatiqueClass with dissolve

    "La salle d'informatique était baignée par la lumière bleutée des écrans d'ordinateurs, le bruit des ventilateurs remplissant l'air de bourdonnements constants."
    "Les élèves s'installaient en silence, certains pianotant déjà sur leurs claviers tandis que d'autres se connectaient lentement, encore ensommeillés."
    "Au fond de la classe, une figure familière pour beaucoup: {b}Clément{/b}, reconnaissable à son sweat-shirt floqué de l'emblème du Bataillon d'Exploration et à son sac sur lequel pendait un porte-clés Levi Ackerman en pleine action."
    "Une pile de goodies SNK dépassait de son sac, à moitié dissimulée sous son bureau."
    "La bulle entra dans la salle, plus confiante qu'avant, mais toujours légèrement nerveuse. Elle prit place non loin de Clément, à une table vide."
    "Clément, absorbé par son écran, ne lui prêta d'abord aucune attention."

    pi "Bien, aujourd'hui nous allons explorer la programmation d'interfaces utilisateur. Prenez vos consignes sur le bureau et ouvrez Visual Studio. Suivez les étapes, mais je veux que vous ajoutiez une touche personnelle à vos projets. Surprenez-moi."

    "La bulle ouvrit son cahier et commença à se concentrer, naviguant dans le logiciel avec une aisance qu'elle n'avait pas il y a encore quelques semaines."
    "Au bout de quelques minutes, Clément releva brièvement la tête en entendant les touches de son clavier. Il fronça les sourcils en jetant un coup d'œil discret vers elle."

    show clement normal
    cl "{size=-10}Huh... Une nouvelle?{/size}"
    hide clement

    "Il hésita un instant, puis tourna légèrement son fauteuil vers elle."

    show clement normal
    cl "Hé... Excuse-moi, mais t'es dans cette classe depuis quand? Je t'ai jamais vue ici avant."
    hide clement

    show me normal
    me "Depuis toujours, Clément."
    hide me

    "Clément plissa les yeux, intrigué. Il la détailla un moment, puis écarquilla soudainement les yeux en la reconnaissant."

    show clement normal
    cl "Attends... Tu... Tu es [player_name]?! Genre... la même bulle qu'avant?"
    hide clement

    show me normal
    me "Oui, c'est bien moi. Quoi, je te surprends?"
    hide me

    "Clément se passa une main dans les cheveux, visiblement troublé."

    show clement normal
    cl "Bah… ouais! C'est que... T'as changé, quoi. Genre… vraiment changé. Je t'aurais jamais reconnue."
    hide clement

    show me normal
    me "En bien, j'espère?"
    hide me

    "Clément rougit légèrement, évitant son regard."

    show clement normal
    cl "Oui... enfin, je veux dire... euh... oui, bien sûr! Bref. Bon, t'as besoin d'un coup de main avec le projet?"
    hide clement

    show me normal
    me "Je m'en sors très bien, merci. Mais toi, tu fais quoi? Une interface pour gérer les Titans?"
    hide me

    "Clément écarquilla les yeux, comme si elle avait touché un point sensible."

    show clement normal
    cl "Attends, c'est pas une mauvaise idée, ça! Imagine une application pour simuler les stratégies du Bataillon d'Exploration… avec des cartes des Murs, des plans d'évasion! Ce serait génial, non?"
    hide clement

    "[player_name] éclata de rire, amusée par son enthousiasme débordant."

    show me normal
    me "Et tu l'appellerais comment? \"Shingeki Simulator\"?"
    hide me

    show clement normal
    cl "Oui! Et avec une option pour analyser les déplacements des Titans, un mode survie, et pourquoi pas… la possibilité d'incarner Levi! Attends, je vais noter ça quelque part..."
    hide clement

    "Clément sortit un carnet de son sac, griffonnant frénétiquement ses idées, oubliant presque qu'il était en cours. [player_name], divertie par la scène, retourna à son projet."

    pi "Clément, concentre-toi sur le sujet, s'il te plaît! On n'est pas en train de planifier un jeu vidéo ici."

    "Clément releva la tête, visiblement agacé d'être interrompu dans son élan créatif. Il murmura en direction de [player_name]."

    show clement normal
    cl "{size=-10}T'as vu? Ils comprennent rien au potentiel de mes idées... Mais toi, au moins, t'as l'air cool. Je sens qu'on va bien s'entendre."
    hide clement

    show me normal
    me "On verra. Mais concentre-toi, sinon ton Bataillon va finir encerclé par des Titans."
    hide me

    "Clément lâcha un petit rire, puis retourna à son écran, toujours un peu troublé par la transformation de la bulle."
    "Une amitié naissait peut-être entre eux, mais le reste de la classe semblait déjà intrigué par cette bulle qu'ils redécouvraient sous un jour nouveau."

    "Une sonnerie retentit, annonçant la fin du cours. Les élèves commencèrent à ranger leurs affaires, Clément rangeant son carnet avec soin."
    "Il se retourna vers [player_name] timidement."

    show clement normal
    cl "Euh... Je voulais te demander quelque chose."
    hide clement

    show me normal
    me "Oui?"
    hide me

    "Clément hésita un instant, puis se lança."

    show clement normal
    cl "Sérieusement, t'es vraiment impressionnante maintenant... C'est comme si tu étais une toute autre personne. Comment t'as fait? C'est quoi ton secret?"
    hide clement

    menu:
        "J'ai juste pris confiance en moi. Je me suis dit qu'il était temps de montrer qui je suis vraiment":
            $ clementAffection += 1
            show clement normal
            cl "Ha ! Le sérum du Titan… Pas mal, pas mal. Mais sérieusement, c'est cool de voir que t'as gagné en confiance. Ça te va bien."
        "J'ai trouvé le sérum du Titan Colossal, ça aide pas mal.":
            $ clementAffection += 2
            show clement normal
            cl "Ha ! Le sérum du Titan… Pas mal, pas mal. Mais sérieusement, c'est cool de voir que t'as gagné en confiance. Ça te va bien."
        "Ça te regarde pas, Clément.":
            $ clementAffection -= 1
            show clement normal
            cl "Oh... OK, désolé. Je voulais pas te déranger."


    cl "Alors, tu travailles sur quoi, là? J'espère que ton interface n'a rien à voir avec le Bataillon d'exploration, hein?"
    hide clement

    menu:
        "Qui sait? Peut-être que je prépare une application pour éradiquer les Titans... ou te recruter dans mon équipe.":
            $ clementAffection += 1
            show clement normal
            cl "Oui, c'est ça! T'imagines, un simulateur où tu peux recréer les batailles? Ça serait trop bien. Tu pourrais même jouer un Titan avec un mode survie."
        "Je suis juste concentrée sur ce que demande le prof, pas comme toi avec tes délires sur SNK.":
            $ clementAffection -= 1
            show clement normal
            cl "Ah... Ouais, t'as raison, faut rester sérieux. Désolé si je t'embête avec mes délires."
        "Franchement, une appli pour les stratégies du Bataillon serait une idée géniale. Tu devrais y réfléchir sérieusement.":
            $ clementAffection += 2
            show clement normal
            cl "Oui, c'est ça! T'imagines, un simulateur où tu peux recréer les batailles? Ça serait trop bien. Tu pourrais même jouer un Titan avec un mode survie."

    cl "Tu sais, je dis ça, mais tu m'impressionnes. D'habitude, personne ne me parle autant de mes passions. Toi, t'es différente."
    hide clement

    menu:
        "Merci, Clément. Ça me fait plaisir. Et puis, tes passions, elles sont cool. Ça te rend unique.":
            $ clementAffection += 2
            show clement normal
            cl "C'est vrai? Merci... T'es sympa, toi. Franchement, je suis content qu'on ait discuté aujourd'hui."
            hide clement
        "Oh, arrête, tu vas me faire rougir! Enfin, si c'est possible pour une bulle.":
            $ clementAffection += 1
            show clement normal
            cl "C'est vrai? Merci... T'es sympa, toi. Franchement, je suis content qu'on ait discuté aujourd'hui."
            hide clement
        "Oui, oui... Bon, je dois me concentrer sur mon projet.":
            $ clementAffection -= 1
            show clement normal
            cl "Oh... OK. Désolé, je te laisse bosser alors."
            hide clement

    if clementAffection == 6:
        jump maxClementAffection
    elif clementAffection == -3:
        jump minusClementAffection
    else:
        jump endClementAffection

label maxClementAffection:

    "Clément sourit, visiblement touché par les réponses de [player_name]."
    "Il se leva, ramassant ses affaires avec soin."
    "Il se mit à rougir et hésita un instant, puis se lança."

    show clement normal
    cl "Écoute, [player_name], je sais qu'on se connaît à peine, mais... Est-ce que tu voudrais bien... venir au bal avec moi?"
    hide clement

    "[player_name] resta bouche bée, surprise par sa demande. Elle hésita un instant."

    show clement normal
    cl "Tu n'es pas obligée de répondre tout de suite, hein. Prends ton temps. On se verra au bal, de toute façon."
    hide clement

    "Clément lui adressa un sourire timide, puis sortit de la salle."
    "Laissant [player_name] seule, perdue dans ses pensées."

label minusClementAffection:

    $ clementDancing = False

    "Clément se leva, ramassant ses affaires en toute hâte."
    "Il jeta un dernier regard à [player_name], puis sortit de la salle sans un mot."
    "Laissant [player_name] seule, le cœur lourd."

label endClementAffection:

    "Clément se leva, ramassant ses affaires avec soin tout en discutant avec [player_name]."

    show clement normal
    cl "Bon, je vais y aller. À demain, peut-être?"
    hide clement

    "La bulle hocha la tête, un sourire aux lèvres, puis retourna à son projet, le cœur léger."
