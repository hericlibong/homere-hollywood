# Liens littéraires à intégrer

Ce fichier sert de registre de travail pendant la révision scène par scène de la dataviz.

Objectif : noter les liens, extraits ou références à intégrer plus tard dans le JSON enrichi, sans modifier tout de suite la structure du corpus.

Champ cible envisagé dans le JSON :

```json
"liens_litteraires": [
  {
    "texte_ancre": "",
    "source": "",
    "passage": "",
    "traduction": "",
    "url": "",
    "extrait": "",
    "note": ""
  }
]
```

Règle de travail :

- utiliser un lien public quand il est précis, stable et lisible ;
- privilégier un extrait traduit du corpus local quand il est plus utile au lecteur ;
- ne pas multiplier les liens : 1 ou 2 liens bien choisis par scène suffisent ;
- intégrer au JSON seulement après validation d'un lot cohérent.

---

## Scène 1 - EXT. THESSALIAN VALLEY - DAY

Texte d'ancrage envisagé :

`Catalogue des vaisseaux au Chant II de l'Iliade`

Source :

Homère, *Iliade*.

Passage :

Chant II, Catalogue des vaisseaux, passage des Épéens.

Traduction :

Leconte de Lisle, 1866.

Extrait à afficher ou utiliser en bulle :

> Et ceux qui habitaient Bouprasios et la divine Élis, et la terre qui renferme Hyrininè et la ville frontière de Myrsinè, et la roche Olénienne et Aleisios, étaient venus sous quatre chefs, et chaque chef conduisait dix nefs rapides où étaient de nombreux Épéiens.

Lien externe possible :

https://www.perseus.tufts.edu/hopper/text?doc=Perseus%3Atext%3A1999.01.0134%3Abook%3D2%3Acard%3D615

Note :

Le lien Perseus est stable mais en anglais/grec. Pour l'interface française, privilégier l'extrait du PDF local dans une bulle ou un bloc source, avec le lien externe en complément éventuel.

---

## Scène 4 - INT. ACHILLES' TENT - CONTINUOUS

Texte d'ancrage envisagé :

`sa relation à Agamemnon est déjà conflictuelle au Chant I`

Source :

Homère, *Iliade*.

Passage :

Chant I, querelle d'Achille et Agamemnon.

Traduction :

Leconte de Lisle, 1866.

Extrait principal à afficher ou utiliser en bulle :

> Et le divin Akhilleus lui répondit : — Certes, je mériterais d’être nommé lâche et vil si, à chacune de tes paroles, je te complaisais en toute chose. Commande aux autres, mais non à moi, car ne pense point que je t’obéisse jamais plus désormais.

Contexte possible :

Ce point de rupture fait suite à la menace directe d'Agamemnôn de s'emparer de la part d'honneur d'Achille pour affirmer sa supériorité :

> [...] moi-même j’irai sous ta tente et j’en entraînerai Breisèis aux belles joues, qui fut ton partage, afin que tu comprennes que je suis plus puissant que toi, et que chacun redoute de se dire mon égal en face.

Extrait alternatif :

> Lourd de vin, œil de chien, cœur de cerf ! jamais tu n’as osé, dans ton âme, t’armer pour le combat avec les hommes, ni tendre des embuscades avec les princes des Akhaiens.

Lien externe possible :

https://www.perseus.tufts.edu/hopper/text?doc=Perseus%3Atext%3A1999.01.0134%3Abook%3D1%3Acard%3D122

Note :

Pour l'interface, privilégier l'extrait principal : il correspond directement à l'indépendance d'Achille face au commandement d'Agamemnon. L'extrait insultant est plus spectaculaire mais pourra être réservé à une scène plus directement centrée sur la querelle.

---

## Scène 5 - EXT. MYCENAEAN CAMP

### Lien 1

Texte d'ancrage envisagé :

`Thétis`

Source :

Index interne à prévoir.

Passage :

Fiche personnage/source `Thétis`.

Traduction :

Sans objet.

Extrait :

Sans objet.

Lien externe possible :

À définir plus tard si une fiche interne n'est pas disponible.

Note :

Lien à faire pointer de préférence vers un index interne des personnages ou figures mythologiques. Thétis n'apparaît pas comme personnage du film, mais elle est essentielle pour comprendre la filiation divine d'Achille, son destin mortel et les traditions tardives sur le Styx.

### Lien 2

Texte d'ancrage envisagé :

`Stace dans l'Achilléide`

Source :

Stace, *Achilléide*.

Passage :

Livre I, lignes 242-274 environ ; passage où Thétis conduit Achille à Scyros et évoque la protection incomplète par les eaux du Styx.

Traduction :

J. H. Mozley, 1928, traduction anglaise.

Extrait court possible :

> if at thy birth I fortified thee with the stern waters of Styx — ay, would I had wholly!

Résumé pour bulle française :

Dans l'*Achilléide*, Thétis rappelle qu'elle a fortifié Achille à sa naissance avec les eaux du Styx, tout en regrettant de ne pas l'avoir fait entièrement. C'est l'un des appuis littéraires tardifs du motif de l'invulnérabilité imparfaite d'Achille.

Lien externe :

https://www.theoi.com/Text/StatiusAchilleid1A.html

Note :

Le passage exact se trouve dans la section `Achilleid Book 1`, autour des lignes 242-274. Pour une interface française, utiliser plutôt le résumé ci-dessus ou rechercher plus tard une traduction française librement exploitable de l'*Achilléide*.

---

## Scène 6 - EXT. THESSALIAN VALLEY

### Lien 1

Texte d'ancrage envisagé :

`Nestor`

Source :

Index interne.

Passage :

`docs/index_personnages_troy.md`, entrée `Nestor`.

Traduction :

Sans objet.

Extrait :

Sans objet.

Lien interne cible :

`docs/index_personnages_troy.md`

Note :

Lien à faire pointer vers une fiche ou entrée interne. Dans cette scène, Nestor est utile comme médiateur : son rôle de conseiller correspond à sa fonction homérique, notamment dans le Chant I.

### Lien 2

Texte d'ancrage envisagé :

`Myrmidons`

Source principale pour la scène :

Homère, *Iliade*.

Passage :

Chant II, Catalogue des vaisseaux, contingent d'Achille.

Traduction :

Leconte de Lisle, 1866.

Extrait à afficher ou utiliser en bulle :

> Et je nommerai aussi ceux qui habitaient Argos Pélasgique, et Alos et Alopè, et ceux qui habitaient Trakinè et la Phthiè, et la Hellas aux belles femmes. Et ils se nommaient Myrmidones, ou Hellènes, ou Akhaiens, et Akhilleus commandait leurs cinquante nefs.

Lien externe possible :

https://mediterranees.net/mythes/troie/iliade/chant2.html

Note :

Pour la scène 6, ce passage homérique suffit à documenter les Myrmidons comme peuple associé à Achille, à la Phthie et au contingent qu'il commande. En revanche, l'origine mythologique du nom des Myrmidons, liée aux fourmis et à Éaque, ne se trouve pas dans l'Iliade : elle relève notamment d'Ovide, *Métamorphoses*, livre VII.

Source complémentaire si l'on veut expliquer l'origine du nom :

Ovide, *Métamorphoses*, livre VII.

Extrait résumé pour bulle :

Dans les *Métamorphoses*, Éaque raconte que Zeus repeuple Égine en transformant des fourmis en hommes. Il les nomme Myrmidons afin de conserver le souvenir de leur origine.

Lien externe complémentaire :

https://mediterranees.net/litterature/ovide/metamorphoses/livre7.html

### Lien 3

Texte d'ancrage envisagé :

`Le refus du sceptre préfigure le Chant I, où Achille jette le sceptre royal à terre en signe de rupture avec Agamemnon`

Source :

Homère, *Iliade*.

Passage :

Chant I, querelle d'Achille et Agamemnon, serment sur le sceptre puis jet du sceptre.

Traduction :

Leconte de Lisle, 1866.

Extrait à afficher ou utiliser en bulle :

> Mais je te le dis, et j'en jure un grand serment : par ce sceptre qui ne produit ni feuilles, ni rameaux, et qui ne reverdira plus [...] certes, bientôt le regret d'Akhilleus envahira tous les fils des Akhaiens [...]
>
> Ainsi parla le Pèléide, et il jeta contre terre le sceptre aux clous d'or, et il s'assit.

Lien externe possible :

https://mediterranees.net/mythes/troie/iliade/chant1.html

Note :

Passage directement pertinent pour la scène 6 : le film transforme le sceptre en objet politique visible dès le prologue, alors que dans l'Iliade le geste du sceptre marque la rupture publique entre Achille et Agamemnon.

---

## Scène 8 - INT. PALACE OF SPARTA - RECEPTION HALL - CONTINUOUS

### Lien 1

Texte d'ancrage envisagé :

`La visite de Pâris à Sparte et l'hospitalité de Ménélas proviennent des Chants Cypriens`

Source :

*Chants Cypriens*, Cycle Troyen.

Passage :

Résumé de Proclus : arrivée d'Alexandre/Pâris à Lacédémone, accueil par Ménélas à Sparte, dons à Hélène, départ de Ménélas en Crète, puis fuite de Pâris avec Hélène.

Traduction :

Traduction de travail à partir du résumé anglais H. G. Evelyn-White, 1914.

Résumé pour bulle :

Dans les *Chants Cypriens*, Pâris arrive à Lacédémone et est reçu par Ménélas à Sparte. Il offre des présents à Hélène ; Ménélas part ensuite en Crète, et Pâris quitte Sparte avec Hélène.

Lien externe possible :

https://www.theoi.com/Text/EpicCycle.html

Note :

Cette source établit la situation narrative de la scène : Pâris à Sparte, accueilli par Ménélas. Elle ne donne pas un portrait moral détaillé de Ménélas.

### Lien 2

Texte d'ancrage envisagé :

`Le portrait de Ménélas en mari grossier et aviné diverge fortement d'Homère, où Ménélas est « irréprochable »`

Source :

Homère, *Iliade*.

Passage :

Chant III, regrets d'Hélène et jugement porté sur Ménélas face à Pâris.

Traduction :

Leconte de Lisle, 1866.

Extrait 1 à afficher ou utiliser en bulle :

> Et la déesse, ayant ainsi parlé, jeta dans son cœur un doux souvenir de son premier mari, et de son pays, et de ses parents. Et Hélénè, s'étant couverte aussitôt de voiles blancs, sortit de la chambre nuptiale en pleurant. [...] Que n'ai-je subi la noire mort quand j'ai suivi ton fils, abandonnant ma chambre nuptiale et ma fille née en mon pays lointain, et mes frères, et les chères compagnes de ma jeunesse ! Mais telle n'a point été ma destinée, et c'est pour cela que je me consume en pleurant.

Extrait 2 à afficher ou utiliser en bulle :

> Te voici revenu du combat. Que n'y restais-tu, mort et dompté par l'homme brave qui fut mon premier mari ! ne te vantais-tu pas de l'emporter sur Ménélaos cher à Arès, par ton courage, par ta force et par ta lance ?

Lien externe possible :

https://mediterranees.net/mythes/troie/iliade/chant3.html

Note :

Ces deux passages suffisent pour l'interface : l'Iliade ne présente pas Ménélas comme un mari odieux, mais comme le premier mari regretté par Hélène et comme un guerrier dont elle reconnaît la valeur face à Pâris. Cela appuie directement le contraste avec le Ménélas grossier et aviné du film.

---

## Scène 9 - INT. HELEN'S CHAMBER - NIGHT

Texte d'ancrage envisagé :

`le duel du Chant III`

Source :

Homère, *Iliade*.

Passage :

Chant III, regrets d'Hélène et jugement porté sur Ménélas face à Pâris après le duel.

Traduction :

Leconte de Lisle, 1866.

Extrait à afficher ou utiliser en bulle :

> Te voici revenu du combat. Que n'y restais-tu, mort et dompté par l'homme brave qui fut mon premier mari ! ne te vantais-tu pas de l'emporter sur Ménélaos cher à Arès, par ton courage, par ta force et par ta lance ?

Lien externe possible :

https://mediterranees.net/mythes/troie/iliade/chant3.html

Note :

Lien réutilisé depuis la scène 8. Il appuie le contraste entre la liaison consentie et romantisée par le film, et l'Hélène homérique du Chant III, déjà à Troie, lucide, hostile à Pâris et encore capable de reconnaître la valeur de Ménélas.

---

## Scène 11 - INT. HELEN'S CHAMBER - NIGHT (LATER)

Texte d'ancrage envisagé :

`Propontide`

Source :

Index interne.

Passage :

Future entrée géographique `Propontide`.

Traduction :

Sans objet.

Extrait :

Sans objet.

Lien interne cible :

`docs/index_sources_antiques_troy.md` ou futur index géographique dédié.

Note :

Lien à faire pointer vers une fiche courte : mer située entre l'Égée et le Pont-Euxin. Dans la scène 11, le collier venu de Propontide sert surtout à donner une couleur grecque au cadeau ; ce n'est pas un motif homérique identifiable.

---

## Scène 12 - INT. PALACE - COURTYARD - LATER

### Lien 1

Texte d'ancrage envisagé :

`Tecton`

Source :

Homère, *Iliade*.

Passage :

Chant V, mort de Phéréclos, fils du charpentier Harmôn, constructeur des navires de Pâris.

Traduction :

Leconte de Lisle, 1866.

Extrait à afficher ou utiliser en bulle :

> Et Mèrionès tua Phéréklos, fils du charpentier Harmôn, qui fabriquait adroitement toute chose de ses mains et que Pallas Athènè aimait beaucoup. Et c'était lui qui avait construit pour Alexandros ces nefs égales qui devaient causer tant de maux aux troiens et à lui-même ; car il ignorait les oracles des dieux.

Lien externe possible :

https://mediterranees.net/mythes/troie/iliade/chant5.html

Note :

Le Tecton du film reste un personnage scénaristique, mais son nom active une résonance homérique pertinente : dans l'Iliade, le constructeur lié aux navires de Pâris est associé indirectement au malheur troyen.

### Lien 2

Texte d'ancrage envisagé :

`Poséidon`

Source :

Index interne.

Passage :

Future entrée `Poséidon`.

Traduction :

Sans objet.

Extrait :

Sans objet.

Lien interne cible :

`docs/index_sources_antiques_troy.md` ou futur index des figures divines.

Note :

Lien à faire pointer vers une fiche courte. Dans cette scène, l'offrande à Poséidon convient au départ en mer, mais ne correspond pas à une scène homérique précise.

---

## Scène 14 - EXT. SHIP'S DECK - DAY

Texte d'ancrage envisagé :

`une tradition importante, attestée notamment chez Apollodore et Hygin`

Source :

Pseudo-Apollodore, *Bibliothèque*, III, 12, 5 ; Hygin, *Fables*, 91.

Passage :

Rêve d'Hécube, prophétie annonçant la ruine de Troie, exposition de Pâris sur le mont Ida et enfance à l'écart.

Traduction :

Traduction de travail française à partir de J. G. Frazer pour Apollodore et de Roger Macfarlane pour Hygin.

Résumé pour bulle :

Avant la naissance de Pâris, Hécube rêve qu'elle enfante un brandon enflammé qui embrase Troie. L'enfant est interprété comme la future ruine de la cité : Priam le fait exposer sur le mont Ida, où il est recueilli et élevé loin de la famille royale avant d'être reconnu.

Extrait à afficher ou utiliser en bulle :

> Hécube rêva qu'elle avait mis au monde un brandon enflammé, et que le feu se répandait dans toute la ville et la brûlait. Aesacos interpréta ce songe : l'enfant devait causer la ruine de sa patrie. Priam fit donc exposer le nouveau-né sur l'Ida ; mais l'enfant fut recueilli et élevé à l'écart, puis reçut le nom de Pâris.

Liens externes possibles :

- https://www.theoi.com/Text/Apollodorus3.html
- https://ogcma.byu.edu/TrojanWarFallANCIENT_Hyginus.htm

Note :

Ce lien sert à expliquer pourquoi le dialogue intime entre Hector et Pâris sur leur enfance partagée est problématique. Le film transforme un motif de destin et d'exposition en souvenir familial continu. Les liens externes sont conservés seulement pour approfondissement ; l'interface doit privilégier l'extrait français ci-dessus.

---

## Scène 18 - EXT. TROJAN SHIP

Texte d'ancrage envisagé :

`Au Chant III de l'Iliade, Hector blâme Pâris`

Source :

Homère, *Iliade*.

Passage :

Chant III, reproche d'Hector à Pâris après son recul devant Ménélas.

Traduction :

Leconte de Lisle, 1866.

Extrait à afficher ou utiliser en bulle :

> Misérable Pâris, qui n'as que ta beauté, trompeur et efféminé, plût aux Dieux que tu ne fusses point né, ou que tu fusses mort avant tes dernières noces ! Certes, cela eût mieux valu de beaucoup, plutôt que d'être l'opprobre et la risée de tous ! [...] Pourquoi, étant un lâche, as-tu traversé la mer sur tes nefs rapides, avec tes meilleurs compagnons, et, mêlé à des étrangers, as-tu enlevé une très belle jeune femme du pays d'Apy, parente d'hommes belliqueux ? Immense malheur pour ton père, pour ta ville et pour tout le peuple ; joie pour nos ennemis et honte pour toi-même !

Lien externe possible :

https://mediterranees.net/mythes/troie/iliade/chant3.html

Note :

L'extrait appuie le contraste Hector/Pâris que le film transpose sur le navire. Chez Homère, le reproche intervient pendant la guerre, après le recul de Pâris devant Ménélas, et non au moment du retour de Sparte.

---

## Scène 22 - EXT. ITHACA - DAY

### Lien 1

Texte d'ancrage envisagé :

`Argos renvoie à l'Odyssée, Chant XVII`

Source :

Homère, *Odyssée*.

Passage :

Chant XVII, reconnaissance d'Ulysse par son chien Argos à Ithaque.

Traduction :

Leconte de Lisle, 1867.

Extrait à afficher ou utiliser en bulle :

> Et un chien, qui était couché là, leva la tête et dressa les oreilles. C'était Argos, le chien du malheureux Odysseus qui l'avait nourri lui-même autrefois [...] Et, aussitôt, il reconnut Odysseus qui approchait, et il remua la queue et dressa les oreilles ; mais il ne put pas aller au-devant de son maître.

Lien externe possible :

https://mediterranees.net/mythes/ulysse/odyssee/chant17.html

Note :

Le film place Argos au moment du départ vers Troie, alors que l'Odyssée le montre au moment du retour. Ce déplacement est très utile pour la dataviz : un nom suffit à faire sentir l'arrachement d'Ulysse à Ithaque et la longueur du retour à venir.

### Lien 2

Texte d'ancrage envisagé :

`il tente d'éviter l'expédition en feignant la folie`

Source :

*Chants Cypriens*, résumé de Proclus ; Pseudo-Apollodore, *Épitomé*, III, 7.

Passage :

Recrutement d'Ulysse avant la guerre de Troie ; fausse folie ; démasquage par Palamède au moyen de Télémaque.

Traduction :

Traduction de travail française à partir de H. G. Evelyn-White pour Proclus et de J. G. Frazer pour Apollodore.

Extrait à afficher ou utiliser en bulle :

> Ulysse ne voulait pas partir pour la guerre et feignit la folie. Palamède comprit que cette folie était jouée : il arracha Télémaque des bras de Pénélope et tira son épée comme s'il allait tuer l'enfant. Par crainte pour son fils, Ulysse avoua sa ruse et dut rejoindre l'expédition.

Liens externes possibles :

- https://www.theoi.com/Text/EpicCycle.html
- https://www.perseus.tufts.edu/hopper/text?doc=Perseus%3Atext%3A1999.01.0022%3Atext%3DEpitome%3Abook%3DE%3Achapter%3D3%3Asection%3D7

Note :

Ce motif explique pourquoi la scène du film est un faux positif : elle paraît légère et inventée, mais elle remplace un épisode antique important où Ulysse tente réellement d'échapper à Troie. Les liens externes sont conservés pour contrôle ; l'interface doit privilégier l'extrait français ci-dessus.

---

## Scène 23 - EXT. SEASIDE CLIFF - LATE AFTERNOON

Texte d'ancrage envisagé :

`le recrutement d'Achille pour l'expédition grecque`

Source :

Stace, *Achilléide*.

Passage :

Livre I, découverte d'Achille à Scyros par Ulysse et appel à rejoindre la flotte grecque.

Traduction :

Traduction de travail française à partir de J. H. Mozley, 1928.

Extrait à afficher ou utiliser en bulle :

> Ulysse s'approcha d'Achille et lui dit à voix basse : « Pourquoi hésites-tu ? Nous te connaissons : tu es l'élève de Chiron, le descendant du ciel et de la mer. La flotte dorienne t'attend, ta Grèce t'appelle, et les murs mêmes de Pergame semblent déjà trembler pour que tu les renverses. Debout, ne tarde plus. »

Lien externe possible :

https://www.theoi.com/Text/StatiusAchilleid1B.html

Note :

Le film ne reprend pas la scène de Scyros : Achille n'est pas caché parmi les filles de Lycomède et Ulysse ne le démasque pas par les armes. Mais la fonction narrative est la même : Ulysse vient chercher Achille et utilise sa parole pour le ramener vers la guerre et la gloire. Le lien externe sert au contrôle ; l'interface doit privilégier l'extrait français ci-dessus.

---

## Scène 25 - EXT. SEASHORE - SUNSET

Texte d'ancrage envisagé :

`Achille rapporte que sa mère Thétis lui a annoncé deux sorts`

Source :

Homère, *Iliade*.

Passage :

Chant IX, v. 410-416 environ ; Achille expose à l'ambassade menée par Ulysse les deux destinées annoncées par Thétis.

Traduction :

Leconte de Lisle, 1866.

Extrait à afficher ou utiliser en bulle :

> Ma mère Thétis aux pieds d'argent m'a dit que deux destinées me conduisent à la mort. Si je reste ici à combattre autour de la ville des Troiens, mon retour est perdu, mais ma gloire sera impérissable ; si je retourne dans ma chère patrie, ma noble gloire est perdue, mais ma vie sera longue, et la mort ne m'atteindra pas de longtemps.

Lien externe possible :

https://mediterranees.net/mythes/troie/iliade/chant9.html

Note :

Dans l'Iliade, Thétis ne prononce pas directement cette prophétie dans la scène : Achille la rapporte. Le film déplace donc une parole rapportée du Chant IX avant le départ et la fait dire directement par Thétis. L'analyse littéraire actuelle peut rester telle quelle ; ce lien servira surtout à rendre visible le noyau homérique de la scène.

---

## Scène 26 - EXT. AEGEAN SEA - DAY

Texte d'ancrage envisagé :

`les Chants Cypriens plaçaient avant le vrai départ plusieurs péripéties majeures`

Source :

*Chants Cypriens*, résumé de Proclus.

Passage :

Résumé du départ grec : Aulis, erreur vers la Mysie, tempête, second rassemblement à Aulis, colère d'Artémis et sacrifice manqué d'Iphigénie.

Traduction :

Traduction de travail française à partir de H. G. Evelyn-White.

Extrait à afficher ou utiliser en bulle :

> Les chefs se rassemblent à Aulis et sacrifient. Ils prennent ensuite la mer, mais atteignent la Teuthranie en la prenant pour Ilion. Quand ils repartent de Mysie, une tempête les disperse. Réunis une seconde fois à Aulis, ils sont retenus par Artémis, irritée contre Agamemnon ; Calchas demande alors le sacrifice d'Iphigénie. Artémis l'enlève cependant et place une biche sur l'autel.

Lien externe possible :

https://www.theoi.com/Text/EpicCycle.html

Note :

La scène du film devient un faux positif intéressant : elle paraît seulement montrer une transition maritime, mais elle efface en réalité tout un bloc du Cycle Troyen. L'interface peut utiliser ce lien pour signaler que le départ vers Troie n'est pas, dans la tradition antique, un trajet simple et immédiat.

---

## Scène 28 - EXT. TROY - DAY

### Lien 1

Texte d'ancrage envisagé :

`L'arrivée d'Hélène à Troie appartient aux événements antérieurs à l'Iliade`

Source :

*Chants Cypriens*, résumé de Proclus.

Passage :

Arrivée de Pâris et Hélène à Troie après le départ de Sparte.

Traduction :

Traduction de travail française à partir de H. G. Evelyn-White.

Extrait à afficher ou utiliser en bulle :

> Héra soulève une tempête contre eux, et ils sont entraînés vers Sidon, que Pâris prend. De là, il navigue vers Troie et y célèbre son mariage avec Hélène.

Lien externe possible :

https://www.theoi.com/Text/EpicCycle.html

Note :

Le résumé des *Chants Cypriens* confirme le cadre général : l'arrivée d'Hélène à Troie précède l'Iliade. Le film transforme cependant cette arrivée en entrée publique et triomphale dans la cité, avec Hector comme témoin, ce qui relève de la dramatisation cinématographique.

### Lien 2

Texte d'ancrage envisagé :

`Aphrodite est pertinente parce qu'elle protège Pâris et Hélène au Chant III`

Source :

Homère, *Iliade*.

Passage :

Chant III ; Aphrodite sauve Pâris du duel contre Ménélas, le dépose dans sa chambre, puis contraint Hélène à le rejoindre.

Traduction :

Leconte de Lisle, 1866.

Extrait à afficher ou utiliser en bulle :

> Aphroditè, étant Déesse, enleva très facilement Alexandros en l'enveloppant d'une nuée épaisse, et elle le déposa dans sa chambre nuptiale, sur son lit parfumé. [...] Et la divine Aphroditè, pleine de colère, lui dit : « Malheureuse ! crains de m'irriter, de peur que je t'abandonne dans ma colère [...] »

Lien externe possible :

https://mediterranees.net/mythes/troie/iliade/chant3.html

Note :

Ce lien justifie la présence visuelle d'Aphrodite dans le décor de Troie : la statue n'est pas une preuve textuelle en soi, mais elle renvoie à une fonction littéraire très claire de la déesse dans le Chant III.

---

## Scène 29 - EXT. PALACE OF TROY

### Liens d'index internes

Texte d'ancrage envisagé :

`Andromaque`

Destination prévue :

Index personnage interne : Andromaque.

Note :

Lien à utiliser dès la première apparition forte d'Andromaque dans la timeline. L'index devra rappeler son rôle homérique d'épouse d'Hector, mère d'Astyanax/Scamandrios, et figure centrale des adieux du Chant VI.

Texte d'ancrage envisagé :

`Briséis`

Destination prévue :

Index personnage interne : Briséis.

Note :

Lien à utiliser parce que la scène introduit la grande invention contradictoire du film : Briséis comme cousine de Priam et servante d'Apollon, alors que l'Iliade la présente comme captive d'Achille et enjeu de la querelle du Chant I.

---

## Scène 30 - INT. PRIAM'S MEETING HALL - DAY

### Lien 1

Texte d'ancrage envisagé :

`Priam y apparaît souvent digne et pieux, surtout au Chant XXIV`

Source :

Homère, *Iliade*.

Passage :

Chant XXIV ; Priam reçoit le conseil d'Hécube, accomplit une libation et prie Zeus avant de partir racheter le corps d'Hector.

Traduction :

Leconte de Lisle, 1866.

Extrait à afficher ou utiliser en bulle :

> O femme, je ne repousserai point ton conseil. Il est bon d'élever ses mains vers Zeus, afin qu'il ait pitié de nous. [...] Priamos, s'étant lavé les mains, reçut la coupe de Hékabè ; et, priant, debout au milieu de la cour, il répandit le vin, regardant l'Ouranos.

Lien externe possible :

https://mediterranees.net/mythes/troie/iliade/chant24.html

Note :

Ce lien appuie précisément la formule de l'analyse : Priam n'est pas seulement roi affligé, il agit selon un registre rituel et pieux avant d'aller vers Achille. La scène 30 invente le débat politique, mais conserve ce profil religieux du personnage.

### Lien 2

Texte d'ancrage envisagé :

`Apollon protège les Troyens, soutient Hector et intervient contre les Achéens, notamment dès le Chant I`

Source :

Homère, *Iliade*.

Passage :

Chant I ; Apollon, irrité par l'affront fait à son prêtre Chrysès, envoie la peste dans le camp achéen.

Traduction :

Leconte de Lisle, 1866.

Extrait à afficher ou utiliser en bulle :

> Irrité contre le Roi, il suscita dans l'armée un mal mortel, et les peuples périssaient, parce que l'Atréide avait couvert d'opprobre Khrysès le sacrificateur. [...] Assis à l'écart, loin des nefs, il lança une flèche [...] ensuite, il perça les hommes eux-mêmes du trait qui tue. Et sans cesse les bûchers brûlaient, lourds de cadavres.

Lien externe possible :

https://mediterranees.net/mythes/troie/iliade/chant1.html

Note :

Ce lien documente la référence au Chant I dans l'analyse. La scène 30 invente la confiance personnelle de Priam en Apollon, mais elle s'appuie sur un fait homérique solide : Apollon intervient activement contre les Achéens.

---
