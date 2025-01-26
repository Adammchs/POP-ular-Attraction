image bg canteen = "images/bg canteen.jpg"

default jeanAffection = 0

label canteen:

    show bg canteen with dissolve

    "Jean, tout juste installé à sa table tranquille près de la fenêtre, mange paisiblement ses frites."
    "L'agitation de la cantine n'est qu'un bruit de fond pour lui, qui apprécie sa petite bulle de calme au milieu du chaos. C'est un déjeuner comme les autres, jusqu'à ce qu'une forme familière s'approche de la table."
    "Jean lève les yeux de son plateau, un peu distrait, et c'est alors qu'il aperçoit [player_name]."
    "Elle s'avance lentement entre les tables, une sorte d'assurance nouvelle dans sa démarche. Ses contours brillent légèrement sous les néons de la cantine, une aura de confiance qui ne correspond pas à la personne qu'il avait l'habitude de voir. Elle est... différente."
    "Jean fronce les sourcils, se demandant pourquoi cette bulle semble soudainement aussi frappante. Il n'a pas reconnu qui elle était au premier coup d'œil, et il ne peut s'empêcher de la suivre du regard, l'air intrigué."
    "Elle porte un look un peu plus audacieux que d'habitude, un air plus assuré… mais ce n'est pas suffisant pour qu'il se souvienne exactement de son nom."

    "[player_name] arrive près de la table de Jean, repérant une place libre à côté de lui. Elle s'assoit d'un air calme, ajustant sa silhouette avec une sorte de sérénité qu'elle n'avait pas auparavant."
    "[player_name] se sent un peu nerveuse, mais son regard est déterminé. Elle a l'impression d'être plus elle-même que jamais."

    show jean normal at top
    j "{i}Ok... c'est bizarre. Cette bulle a l'air de se transformer en une sorte de... super-bulle. Mais elle ressemble vraiment à celle que je connais, non? Ça me fait un peu bizarre de la voir ainsi, tout en confiance.{/i}"
    hide jean

    "La bulle commence à sortir son sandwich, mais elle semble hésiter un instant. Jean continue de la regarder discrètement, mais il décide finalement de prendre les devants."

    show jean normal at top
    j "Eh... salut, tu es nouvelle ici ou c'est moi qui suis complètement à côté de la plaque?"
    hide jean

    "Elle le regarde un instant, un petit sourire en coin apparaissant sur ses contours. Elle reconnaît bien Jean, mais elle préfère d'abord tester ses nouvelles frontières."
    "Elle se souvient de tous les regards détournés qu'il lui avait lancés dans le passé. Aujourd'hui, elle veut lui montrer qu'elle est plus que ce qu'il pensait."

    show me normal
    me "Non, je suis... la même personne, mais avec un peu de changement."
    hide me

    show jean normal at top
    j "Un changement, hein? Tu as... bien changé en tout cas."
    "Jean hésite encore, ne sachant pas comment réagir à ce nouveau côté d'elle. Il ne la reconnaît pas tout de suite, mais quelque chose dans sa voix, dans son attitude, lui semble différent. Pourtant, il garde une légère distance, un peu déstabilisé."
    hide jean

    menu:
        "Eh bien, parfois, il faut se réinventer, tu ne crois pas?":
            $ jeanAffection += 2
            show jean normal at top
            j "Eh bien... c'est vraiment pas mal. J'étais pas sûr de te reconnaître. T'as l'air plus... sûre de toi, et c'est cool."
            hide jean
            "Jean est clairement impressionné par sa nouvelle attitude. Il commence à la regarder sous un autre jour, la trouvant plus intéressante et attirante."
            show me normal at top
            me "Merci. J'ai mis un peu de temps à comprendre que je devais me faire confiance."
            hide me
            "Jean est touché par sa sincérité et commence à voir la bulle sous un autre angle, un peu plus humain et vulnérable."

        "J'ai juste… décidé de m'améliorer un peu.":
            show jean normal at top
            j "Tu sais, c'est bien que tu changes. C'est pas facile de le faire, surtout si t'as pas l'air d'avoir trop de soutien… mais ça te va bien."
            hide jean
            "Jean reste assez neutre, mais il montre une forme de respect discret pour le changement qu'elle a opéré."
            show me normal at top
            me "Je suppose que ça fait du bien de se sentir mieux dans sa peau."
            hide me
            "Jean commence à se sentir plus à l'aise avec la bulle et apprécie sa réponse plus authentique. La relation entre eux reste cordiale mais sans profondeur immédiate."

        "Peut-être que tu m'as sous-estimée, mais maintenant je préfère qu'on me prenne un peu plus au sérieux.":
            $ jeanAffection -= 1
            show jean normal at top
            j "Sous-estimée? C'est un peu direct comme manière de parler, non? Je pensais juste que tu faisais ta petite vie, mais là tu sembles vouloir être au centre de l'attention."
            hide jean
            "Jean perçoit son attitude comme un peu trop arrogante, et cela crée une distance. Il n'apprécie pas forcément la façon dont la bulle se positionne."
            show me normal at top
            me "Je ne veux pas de la gloire, juste qu'on me prenne un peu plus au sérieux. C'est tout."
            hide me
            "Il est possible que Jean perde un peu d'intérêt pour la bulle après cette réponse, la trouvant moins accessible et plus fermée qu'auparavant."

        "Je sais que tu ne m'avais pas vraiment remarquée avant, mais je suis un peu plus… visible aujourd'hui.":
            $ jeanAffection += 1
            show jean normal at top
            j "Oh, t'as raison, j'avoue que je ne t'avais pas vraiment vue comme ça avant. Mais c'est cool, je te vois sous un nouveau jour."
            hide jean
            "Jean se sent un peu déstabilisé par le changement, mais il l'accepte. Il semble curieux de mieux connaître cette version plus assurée de la bulle."
            show me normal at top
            me "Parfois, il faut juste se donner la chance de se montrer."
            hide me
            "Jean est touché par sa réplique et commence à s'intéresser davantage à elle. La conversation pourrait se prolonger dans un esprit plus détendu."

    "[player_name] sourit, un peu soulagée de voir que Jean ne la rejette pas complètement. Elle se sent plus légère, plus libre, et elle est prête à continuer à explorer cette nouvelle facette d'elle-même."

    show jean normal at top
    j "Alors, tu as décidé de te lancer dans une nouvelle aventure?"
    hide jean

    show me normal at top
    me "Oui, je pense que c'est le moment de changer un peu. J'ai envie de voir ce que ça donne."
    hide me

    show jean normal at top
    j "C'est bien, ça. J'espère que ça te réussira. Tu as l'air bien partie en tout cas."
    j "Et puis, si tu as besoin d'un coup de main, tu sais où me trouver."
    hide jean

    menu:
        "Merci, c'est gentil. Je te tiendrai au courant.":
            $ jeanAffection += 2
            show jean normal at top
            j "Pas de souci. Je suis là si tu as besoin de parler ou quoi que ce soit."
            hide jean
            "Jean montre une forme de soutien discret, mais sincère. Il semble prêt à aider la bulle si elle en a besoin."

        "Je préfère faire ça seule, mais merci pour la proposition.":
            show jean normal at top
            j "Pas de problème. Je comprends. Mais si tu changes d'avis, n'hésite pas."
            hide jean
            "Jean respecte sa décision et lui laisse l'espace nécessaire pour évoluer. Il semble prêt à la soutenir si elle en ressent le besoin."

        "Je crois que je vais bien m'en sortir. Merci pour ton soutien.":
            $ jeanAffection += 1
            show jean normal at top
            j "C'est cool. Je suis sûr que tu vas y arriver. Et si jamais tu as besoin d'un coup de main, tu sais où me trouver."
            hide jean
            "Jean montre une forme de soutien discret, mais sincère. Il semble prêt à aider la bulle si elle en a besoin."

    "Jean et [player_name] entendent un petit bruit de bulle qui éclate, puis se tourna tous les deux vers la source du son."
    "Éclatant tous sur son passage, Carmen se dirigea à la table de Jean et [player_name]."

    show carmen normal at top
    ca "Tu essaies encore d'aguicher un garçon, [player_name]? Tu ne comprends pas que tu n'as aucune chance?"
    hide carmen

    show me normal at top
    me "Je... je ne vois pas de quoi tu parles, Carmen. Je suis juste en train de discuter avec Jean."
    hide me

    show carmen normal at top
    ca "Discuter? Tu crois vraiment que tu as quelque chose à dire qui l'intéresse? Tu es tellement pathétique, [player_name]."
    hide carmen

    show jean normal at top
    j "Carmen, laisse-la tranquille. On discutait juste, c'est tout."
    hide jean

    show carmen normal at top
    ca "Oh, je vois. Tu as trouvé un nouveau pigeon pour te soutenir, c'est ça?"
    ca "Tu es vraiment pitoyable, [player_name]. Tu ne comprends pas que tu n'es rien, que tu ne seras jamais rien?"
    hide carmen

    show jean normal at top
    j "Carmen, c'est bon. Laisse-la tranquille. Elle n'a rien fait de mal."
    j "Et puis, tu n'as pas à lui parler comme ça. Elle est une personne comme les autres, tu sais."
    hide jean

    show carmen normal at top
    ca "Oh, vraiment? Tu crois qu'elle mérite d'être traitée comme une personne normale? Tu es vraiment naïf, Jean."
    ca "Tu ne vois pas qu'elle n'est qu'une bulle, une bulle insignifiante qui ne mérite pas d'être ici?"
    hide carmen

    show me normal at top
    me "Carmen, je... je ne sais pas pourquoi tu es si méchante avec moi. Je ne t'ai rien fait."
    hide me

    show carmen normal at top
    ca "Rien fait? Tu es là, à essayer de te faire passer pour quelqu'un d'autre, à essayer de te faire remarquer."
    hide carmen

    show me normal at top
    me "J'en ai marre de tes mensonges, Carmen. Je ne suis pas celle que tu crois."
    me "Et puis, tu n'as pas a me juger comme ça. Tu ne sais rien de moi."
    me "Tu es juste jalouse parce que je suis en train de changer, et toi, tu restes la même."
    me "Un cactus sans épine, c'est ce que tu es. Tu piques tout le monde, mais tu ne supportes pas qu'on te renvoie la pareille."
    hide me

    show carmen normal at top
    ca "Jalouse? Moi, jalouse de toi? Tu te fiche de moi, [player_name]."
    ca "J'en ai assez entendu comme ça. tu m'as coupé l'appétit, et je ne veux plus te voir."
    hide carmen

    "Carmen se tourna brusquement et partit, laissant [player_name] et Jean seuls à la table."

    show jean normal at top
    j "Tu sais, [player_name], je... je ne sais pas trop quoi dire. Mais je suis désolé pour ce qu'il s'est passé."
    j "Tu ne mérites pas d'être traitée comme ça. Tu es une personne, et tu as le droit d'être respectée."
    hide jean

    show me normal at top
    me "Merci, Jean. C'est gentil de ta part. Je ne sais pas pourquoi elle est comme ça avec moi."
    hide me

    show jean normal at top
    j "Elle a ses problèmes, c'est sûr. Mais ça ne justifie pas son comportement envers toi."
    j "Tu sais, si jamais tu as besoin de parler, je suis là. Je veux dire, je ne suis pas un expert, mais je peux écouter."
    hide jean

    show me normal at top
    me "Merci Jean."
    hide me

    if jeanAffection == 4:
        jump maxJeanAffection
    elif jeanAffection == -1:
        jump minusJeanAffection
    else:
        jump endJeanAffection

label maxJeanAffection:

    "Jean et [player_name] continuent de discuter, partageant des moments de complicité et de rire. Leur relation évolue doucement, mais sûrement, vers quelque chose de plus profond et sincère."
    "Jean commence à voir [player_name] sous un jour nouveau, plus humain et authentique. Il apprécie sa compagnie et se sent de plus en plus proche d'elle."
    show jean normal at top
    j "Tu sais, je suis content de te connaître un peu mieux. Tu es vraiment quelqu'un de spécial, [player_name]."
    "[player_name] sourit, touchée par ses paroles. Elle se sent plus confiante et plus heureuse, sachant qu'elle a un ami sur qui compter."
    j "Je voulais savoir si... tu avait déjà pensé à aller au bal de fin d'année?"
    hide jean

    show me normal at top
    me "Oh, euh... non, pas vraiment. Je ne sais pas si c'est vraiment mon truc, tu vois."
    hide me

    show jean normal at top
    j "Je comprends. Mais si jamais tu changes d'avis, je serais ravi d'y aller avec toi."
    hide jean

    show me normal at top
    me "Vraiment? Tu es sérieux?"
    hide me

    show jean normal at top
    j "Oui, vraiment!"
    j "Oh! Euh je veux dire... c'est juste que je pense qu'on passerait un bon moment ensemble, tu vois?"
    j "Je... Euh... Tu n'as pas à dire oui tout de suite, hein. Prends ton temps pour réfléchir."
    hide jean

    "Jean se leva de sa chaise, un peu gêné par sa propre audace. Il ne savait pas trop comment réagir"
    "Il se tourna et partit, laissant [player_name] seule à la table, le cœur battant la chamade."

    jump afterLunch

label minusJeanAffection:

    "Jean et [player_name] continuent de discuter, mais la conversation devient de plus en plus tendue. Leurs échanges sont moins fluides, et une certaine distance s'installe entre eux."
    "Jean commence à se sentir mal à l'aise en présence de [player_name], et il préfère garder ses distances pour éviter tout malentendu."
    show jean normal at top
    j "Je... crois que je vais y aller. On se reparle plus tard, d'accord?"
    hide jean

    show me normal at top
    me "D'accord, à plus tard..."

    $ jeanDancing = False

    jump afterLunch

label endJeanAffection:

    "Jean et [player_name] continuent de discuter. Leurs discussions sont maladroites par moments, mais ils parviennent à trouver un terrain d'entente."
    "Jean hésite encore un peu, mais il semble prêt à donner une chance à cette nouvelle version de [player_name]."
    show jean normal at top
    j "[player_name], cette facette de toi est... intéressante. J'espère qu'on pourra discuter un peu plus à l'avenir."
    hide jean

    show me normal at top
    me "Ça me ferait plaisir. J'apprécie ta compagnie, Jean."
    hide me

    show jean normal at top
    j "Moi aussi. Peut-être qu'on se croisera au bal de fin d'année, qui sait?"
    hide jean

    "Jean se leva de sa chaise, un sourire timide aux lèvres. Il semblait un peu plus détendu, un peu plus ouvert à la possibilité de lier une amitié avec [player_name]."
    "Il partit, laissant [player_name] seule à la table, pensant à ce leurs conversations futures avec une pointe d'excitation."

    jump afterLunch