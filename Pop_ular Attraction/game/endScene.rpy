image bg hallRoom = "images/bg hallRoom.jpg"
image bg end = "images/bg end.jpg"

label badEndScene:

    show bg hallRoom with dissolve

    "La salle était baignée d'une lumière tamisée, et la musique rythmait les rires et les conversations animées. Des couples et des groupes d'amis dansaient sous les guirlandes lumineuses."
    "Au centre de tout ce tumulte festif, [player_name], la bulle, avançait seule. Sa robe en satin clair flottait élégamment, captant la lumière comme une étoile discrète. Pourtant, malgré sa tenue parfaite et sa récente montée en confiance, elle sentait le poids de la solitude."
    "Elle se dirigea vers la table des boissons, attrapa un verre de punch, et tenta de s'intégrer à l'ambiance. Mais une voix familière, stridente et teintée de sarcasme, brisa son moment de calme."

    show carmen normal
    ca "Oh, mais regarde ça, les filles. La bulle! Toute seule, comme d'habitude. C'est mignon… ou pathétique ? J'hésite encore."
    hide carmen

    "Les rires mesquins de sa clique résonnèrent autour d'elle. Carmen s'approcha, son regard brillant de malice. Sa robe verte pailletée semblait aussi piquante que son attitude, chaque détail rappelant qu'elle aimait être au centre de l'attention."

    show carmen normal
    ca "Sérieusement, [player_name]... Qu'est-ce que tu fais ici? Personne ne t'a invitée, hein? Tu te dis que si tu restes près de la table des boissons, quelqu'un aura peut-être pitié de toi? "
    hide carmen

    "Les rires s'amplifièrent, mais [player_name] ne bougea pas. Son cœur battait fort, mais elle respira profondément. Le silence s'étira, et Carmen sembla perdre patience devant l'absence de réaction."

    show carmen normal
    ca "Oh, allez, dis quelque chose. Ne me dis pas que tu es muette maintenant! Ou peut-être que tu veux juste que je te laisse tranquille? Pauvre bulle, toute seule dans un monde trop grand pour elle..."
    hide carmen

    show me normal
    me "Si ça te fait plaisir de te moquer, vas-y. Mais tu sais quoi, Carmen? Ce soir, je suis venue pour moi. Pas pour toi, ni pour qui que ce soit d'autre. Alors, amuse-toi bien avec tes piques. Moi, je vais juste être moi-même."
    hide me

    "Un silence pesa dans l'air. Les élèves autour, curieux de la confrontation, avaient cessé de parler. Carmen, décontenancée par la réponse posée de [player_name], fronça les sourcils."

    show carmen normal
    ca "Tss… Si tu veux. Je suppose que tout le monde a besoin de se donner de l'importance, même toi. Allez, les filles, on s'en va."
    hide carmen

    "Elle tourna les talons, mais son rire sonnait moins assuré qu'auparavant. Sa clique la suivit, bien que certaines d'entre elles échangèrent un regard avec [player_name], presque admiratif."
    "La bulle resta immobile un instant, respirant profondément. Elle pouvait encore sentir quelques regards, mais cette fois, ils semblaient moins jugeants. Certains élèves souriaient même, comme s'ils respectaient sa réponse."
    "Elle reprit son verre, un léger sourire aux lèvres. Ce n'était peut-être pas la soirée de rêve, mais elle avait gagné quelque chose de précieux: la capacité de ne plus se laisser atteindre par les remarques blessantes."

    jump endGame

label sasukeEnd:

    show bg hallRoom with dissolve

    show sasuke normal
    s "Même dans les ténèbres où je marche seul, il y a des éclats de lumière... Si je viens à ce bal, ce n'est pas pour la fête, mais pour comprendre ce que signifie vraiment le lien."
    hide sasuke

    jump endGame

label khyleEnd:

    show bg hallRoom with dissolve

    show khyle normal
    k "Ahhhhhh ma sportive préférée !!! Prête à t'envoyer en l'air ?"
    hide khyle

    jump endGame

label jeanEnd:

    show bg hallRoom with dissolve

    show jean normal
    j "Je suis content que tu ai accepter mon invitation, t'es prêtes à t'éclater?"
    hide jean

    jump endGame

label titusEnd:

    show bg hallRoom with dissolve

    show titus normal at top
    t "Par la terre plate creuse, je vais enfin pourvoir te surveiller, merci d'avoir accepté"
    hide titus

    jump endGame

label clementEnd:

    show bg hallRoom with dissolve

    show clement normal
    cl "Je me suis douché spécialement pour l'occasion."
    cl "Hâte de clutch cette soirée."
    hide clement

    jump endGame

label endGame:

    show bg end with dissolve

    "{size=+50}The End{/size}"