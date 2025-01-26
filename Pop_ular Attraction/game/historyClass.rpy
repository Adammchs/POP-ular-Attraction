image bg historyClass = "images/bg historyClass.jpg"

label historyClass:

    scene bg historyClass with dissolve

    "La salle de classe d'histoire, baignée par une lumière pâle d'un matin maussade, résonnait doucement du bruit des élèves s'installant."
    "Les chuchotements et quelques éclats de rire meublaient l'attente du professeur, qui n'était pas encore arrivé."
    "Au fond de la classe, un élève atypique s'était installé avec une certaine cérémonie."
    "Titus, toujours affublé d'un grand manteau même en intérieur, portait un chapeau improbable orné de pins représentant des étoiles et des éclipses."
    "Il écrivait frénétiquement dans un carnet usé, griffonnant des croquis incompréhensibles, entre un globe terrestre aux couches multiples et une sorte de \"trou géant\" au pôle Nord."
    "[player_name], désormais plus confiante après sa transformation, s'assit quelques rangs devant lui, curieuse malgré elle."
    "Elle avait entendu parler de Titus et de ses idées excentriques, mais c'était la première fois qu'elle se retrouvait à proximité."

    show titus normal at top
    t "{size=+10}Vous savez qu'on vit sur un disque flottant, hein? Mais ce n'est pas tout! Ce disque est creux... et à l'intérieur, il y a un autre monde!{/size}"
    hide titus

    "La classe éclata de rire, sauf la bulle, qui hésita. Titus semblait si passionné qu'il en devenait fascinant, même si tout le monde le prenait pour un fou."

    show carmen normal
    ca "Alors quoi, Titus? On va rencontrer des dinosaures dans ta Terre creuse? Et on va tomber dans l'espace si on va trop loin?"
    hide carmen

    show titus normal at top
    t "Exactement! Les dinosaures n'ont jamais disparu, ils ont juste migré vers l'intérieur! Et si vous allez trop loin sur la surface, vous pourriez bien tomber... mais c'est un mythe qu'il n'y a \"rien\" en dessous!"
    hide titus

    "Le professeur entra alors, coupant court à la scène. Tout le monde s'assit précipitamment, mais Titus ne semblait pas du tout perturbé par les moqueries."
    "La bulle ne put s'empêcher de se retourner légèrement pour l'observer. Il lui adressa un sourire étrange, puis lui fit un petit signe de la main."

    ph "Bien, aujourd'hui, nous continuons notre chapitre sur les grandes explorations. Sortez vos livres et prenez des notes."

    "[player_name] ouvrit son cahier, mais elle sentait le regard de Titus sur elle. Après quelques minutes, il se pencha légèrement en avant et murmura juste assez fort pour qu'elle l'entende."

    show titus normal at top
    t "T'es pas comme les autres, toi. Je vois que tu écoutes. Toi aussi, tu te demandes ce qui se passe vraiment?"
    hide titus

    "[player_name] hésita un instant, surprise qu'il lui adresse la parole, mais elle décida de répondre."

    show me normal
    me "Je ne sais pas... Peut-être que je préfère écouter avant de juger."
    hide me

    "Titus sembla ravi par cette réponse. Il s'assit un peu plus droit et se pencha vers elle."

    show titus normal at top
    t "Exactement! Il faut écouter. C'est comme ça qu'on découvre la vérité. Les autres, là, ils rient parce qu'ils ont peur. Mais toi, je vois bien que t'as un esprit ouvert."
    hide titus

    "[player_name] sourit doucement, amusée par son énergie débordante mais sincère."

    show me normal
    me "Alors, explique-moi. Comment on peut avoir une Terre plate ET creuse? Ça n'a pas l'air de marcher ensemble."
    hide me

    "Titus frappa son cahier avec excitation, ses yeux brillants de passion."

    show titus normal at top
    t "C'est simple! Imagine un disque, mais épais, tu vois? Comme une crêpe avec plusieurs couches!"
    t "Nous, on est à la surface. En dessous, il y a une autre couche où vivent des civilisations avancées, bien plus anciennes que la nôtre."
    t "Et au centre du disque… un immense noyau de lumière qui alimente tout!"
    hide titus

    "[player_name] l'écouta, fascinée malgré elle. Elle n'y croyait pas une seconde, mais elle ne pouvait pas nier qu'il avait une manière captivante de présenter ses idées."

    show me normal
    me "Et les explorateurs? Ceux qui ont fait le tour du monde?"
    hide me

    show titus normal at top
    t "Des marionnettes! Des histoires montées de toutes pièces! Tu crois vraiment qu'ils ont \"fait le tour\"? Non! Ils ont juste tourné en rond sur le disque. C'est évident!"
    hide titus

    "Le professeur interrompit leur échange en demandant à Titus de se concentrer sur le cours. Il leva les yeux au ciel, mais il obéit… tout en continuant de griffonner des croquis farfelus dans son carnet."
    "Titus, sur le point de partir, se retourne vers la bulle, son carnet contre sa poitrine comme un trésor."
    "Il semble hésiter un instant, mais finit par se pencher légèrement vers elle, baissant la voix comme s'il allait révéler un secret."

    show titus normal at top
    t "Tu sais, je n'invite pas tout le monde à mes réunions."
    t "Si je t'ai proposé de venir, c'est parce que je sens que tu es différente... et que tu pourrais comprendre ce que les autres refusent de voir. Alors? Tu vas venir?"
    hide titus

    menu:
        "Ça a l'air intéressant... Je pense que je viendrai. Après tout, c'est bien d'écouter et d'apprendre de nouvelles perspectives.":
            "Titus la fixe avec des yeux brillants d'excitation. Il est visiblement ravi de sa réponse."
            show titus normal at top
            t "Ah! Je savais que j'avais raison! Tu ne regretteras pas, je te le promets. Tu verras, ça va tout changer pour toi."
            hide titus
            "Titus semble plus détendu, et une connexion sincère commence à se former entre eux."
            jump endTitusAffection

        "Je ne sais pas encore... Mais pourquoi pas? Si j'ai le temps, je viendrai jeter un œil.":
            "Titus plisse légèrement les yeux, analysant sa réponse, mais il semble tout de même satisfait."
            show titus normal at top
            t "Hmm, je prends ça pour un peut-être. Ce n'est qu'un début... Je te garantis que tu ne regretteras pas."
            hide titus
            "Il semble modérément content, mais reste sur ses gardes quant à ses intentions."
            jump endTitusAffection

        "Sérieusement? Désolée, Titus, mais je pense que je vais passer mon tour. Ces trucs-là, c'est pas trop mon truc.":
            "Titus se fige un instant, ses traits se durcissant légèrement. Il range son carnet dans son sac avec des gestes plus brusques."
            show titus normal at top
            t "Hmpf. Évidemment. Tu fais comme les autres. Peut-être que je me suis trompé sur toi, finalement."
            hide titus
            "Il s'éloigne sans un mot de plus, son enthousiasme visiblement refroidi."
            jump endHistoryClass

label endHistoryClass:

    "Titus s'éloigne, mais avec un sourire satisfait. Avant de passer la porte, il se retourne une dernière fois."

    show titus normal at top
    t "On se revoit bientôt, Bulle. Oh, et prépare-toi à voir des choses que tu n'aurais jamais imaginées."
    hide titus

    "[player_name] reste assise, légèrement amusée mais aussi intriguée. Elle ne sait pas si elle doit prendre ses théories au sérieux, mais elle apprécie la passion qui anime Titus."

    show carmen normal
    ca "Alors, [player_name], même toi tu t'intéresses à ses délires?"
    ca "Je pensais que tu étais plus... rationnelle. Mais bon, chacun ses goûts."
    hide carmen

    "La bulle se sent un peu gênée, mais elle ne peut s'empêcher de sourire. Titus était peut-être excentrique, mais il avait quelque chose d'authentique qui la touchait."

    jump ringBell

label endTitusAffection:

    $ titusDancing = False

    "Titus quitte la pièce, et la bulle ressent un mélange de gêne et de culpabilité."
    "Il a peut-être des idées étranges, mais elle réalise qu'elle a peut-être été trop dure avec lui."

    ca "Alors comme ça, on peut être d'accord toi et moi."

    "Carmen, toujours prompte à commenter, s'approche de la bulle avec un sourire en coin."

    show me normal
    me "De quoi tu parles?"
    hide me

    show carmen normal
    ca "Bah même toi, tu peux être cassante. C'est pas très sympa, tu sais."
    ca "Mais bon, je suppose que c'est mieux que de se laisser embarquer dans ses délires."
    hide carmen

    "La bulle se sent un peu mal à l'aise, mais elle sait que Carmen a raison. Elle n'a pas été très gentille avec Titus, même si elle n'était pas d'accord avec lui."

label ringBell:

    "La cloche retentit, mettant fin au cours d'histoire. Les élèves se lèvent, bavardant joyeusement en se dirigeant vers la sortie."
    "La bulle se sent un peu étourdie par tout ce qui vient de se passer. Elle se demande si elle a bien fait de s'engager dans cette conversation avec Titus."
    "Mais malgré ses doutes, elle ne peut s'empêcher de ressentir une pointe d'excitation sur la décourverte d'un point de vue si différent du sien."

    "Elle range ses affaires, prête à affronter la suite de sa journée. Elle sait que les cours de l'après-midi seront plus difficiles, mais elle se sent plus forte après cette rencontre inattendue."
    "Sur le chemin de la cantine, elle ne peut devenir de plus en plus excitée à l'idée de revoir Jean."
    "Elle se demande s'il sera là, s'il lui parlera, s'il la regardera comme il l'a fait ce matin."

    jump canteen