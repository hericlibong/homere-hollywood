# Verification des motifs majeurs

Ce document rassemble les controles de Phase 2. Il ne modifie pas le JSON de reference. Il confirme, nuance ou signale les points a reprendre avant le futur tagging `degre_fidelite`.

Fichiers lies :

- `output/troy_true_or_false_all_scenes.json`
- `output/audit_motifs.csv`
- `output/audit_motifs_synthese.csv`
- `output/audit_references_prioritaires.csv`

---

## Lot A - Iliade, scenes centrales

Source locale principale :

- `sources/homere/Liliade.pdf`

Sources de controle en ligne :

- Perseus, *Iliad* : https://www.perseus.tufts.edu/hopper/text?doc=Hom.+Il.
- Scaife Viewer, *Iliad* : https://atlas.perseus.tufts.edu/library/urn:cts:greekLit:tlg0012.tlg001.perseus-eng4/

### Synthese

Les grands motifs iliadiques du corpus sont globalement bien identifies. Les ancrages suivants sont valides :

- Chant I : querelle Achille / Agamemnon, Chryseis, Briseis, retrait d'Achille.
- Chant III : duel Paris / Menelas et observation depuis les murs.
- Chant VI : Hector, Andromaque et Astyanax.
- Chant IX : choix d'Achille entre retour sans gloire durable et mort glorieuse devant Troie.
- Chant XVI : Patrocle part au combat avec les armes d'Achille et meurt sous Hector, apres intervention divine.
- Chant XVIII : annonce de la mort de Patrocle et deuil d'Achille.
- Chant XXII : duel Achille / Hector, mort d'Hector et outrage au corps.
- Chant XXIV : Priam chez Achille et restitution du corps d'Hector.

Le point principal a retenir : les references de fond sont bonnes, mais plusieurs motifs sont disperses dans le film et l'audit par mots-cles reste volontairement large. Certaines scenes candidates ne sont donc pas des reprises directes, mais des resonances, anticipations ou consequences narratives.

---

## Verifications par motif

| Motif | Reference verifiee | Verdict | Probleme ou nuance |
|---|---|---|---|
| Querelle Achille / Agamemnon | *Iliade*, Chant I, v. 1-7, 54-187, 318-348 | Confirme | L'audit est large : toutes les scenes candidates ne relevent pas directement de la querelle. |
| Briseis et Chryseis | *Iliade*, Chant I, v. 8-32, 111-120, 180-187, 318-348 | Confirme avec nuance | Briseis est homerique comme captive d'Achille, mais sa genealogie troyenne filmique reste une invention a signaler. |
| Duel Paris / Menelas | *Iliade*, Chant III, v. 15-120, 245-302, 340-382, 383-447 | Confirme | Menelas ne meurt pas dans l'Iliade ; toute mort filmique de Menelas est contradictoire avec le cadre homerique. |
| Hector / Andromaque / Astyanax | *Iliade*, Chant VI, v. 369-502 | Confirme | Le film deplace souvent le motif : chez Homere, la rencontre se fait pres des portes Scees, non dans la chambre. |
| Choix d'Achille entre vie longue et gloire | *Iliade*, Chant IX, v. 307-429, surtout v. 410-416 | Confirme | Le film diffuse ce motif dans plusieurs dialogues, parfois hors du contexte strict de l'ambassade homerique. |
| Patrocle portant les armes d'Achille | *Iliade*, Chant XVI, v. 1-100, 130-154, 818-863 | Confirme avec correction a prevoir | Le film ne simplifie pas seulement : il inverse deux points majeurs. Dans l'Iliade, Achille autorise Patrocle a porter ses armes et lui ordonne de revenir apres avoir repousse les Troyens des nefs. Hector sait qu'il tue Patrocle ; la mort suit l'intervention d'Apollon, la blessure d'Euphorbe puis le coup final d'Hector. Dans le film, Patrocle prend l'armure sans autorisation et Hector croit affronter Achille. |
| Deuil d'Achille | *Iliade*, Chant XVIII, v. 1-64, 95-147 ; Chant XXIII pour les funerailles | Confirme | Distinguer le deuil du Chant XVIII et les rites/funerailles du Chant XXIII. |
| Duel Achille / Hector | *Iliade*, Chant XXII, v. 131-213, 247-305, 306-366, 395-404 | Confirme | L'audit est tres large ; le noyau direct du duel correspond surtout aux scenes autour de 130-152. |
| Priam chez Achille et restitution du corps | *Iliade*, Chant XXIV, v. 334-467, 477-506, 507-676 | Confirme | Le film conserve le noyau de supplication mais supprime Hermes et simplifie le role de Pelee. |

---

## Problemes identifies

### 1. Scene 113 a arbitrer plus tard

La scene 113 est classee `L'Iliade`, mais `reference_iliade` est vide et son explication dit qu'elle ne reprend pas un passage precis de l'Iliade. Elle ne bloque pas le Lot A, mais devra etre reprise en Phase 5.

### 2. Audits volontairement larges

Les motifs `duel_achille_hector`, `querelle_achille_agamemnon` et `priam_achille_corps_hector` capturent beaucoup de scenes ou les personnages sont mentionnes sans que la scene soit une reprise directe. Il faudra distinguer :

- reprise directe ;
- resonance thematique ;
- anticipation ;
- consequence narrative ;
- invention filmique appuyee sur un motif homerique.

### 3. Plusieurs chants iliadiques restent hors Lot A

Le Lot A valide les motifs centraux, mais d'autres references du JSON devront etre controlees plus tard :

- Chant VII : Ajax / Hector, treve funeraire.
- Chant XII : mur ou defenses.
- Chant XIX : retour d'Achille au combat.
- Chant XXIII : funerailles de Patrocle.

---

## Conclusion Lot A

Le Lot A est valide comme socle homerique prioritaire. Les motifs majeurs attribues a l'Iliade sont correctement localises dans les chants attendus. Les corrections futures ne porteront probablement pas sur le fait que ces motifs existent dans l'Iliade, mais sur :

- la precision des vers ;
- la distinction reprise directe / deplacement / resonance ;
- la formulation des inventions filmiques autour de Briseis, Patrocle, Menelas et Hector ;
- la reduction des faux positifs dans les audits de motifs.

Correction a reporter en Phase 5 : les scenes du groupe `patrocle_armes_achille` devront expliciter que le film transforme le Chant XVI sur deux points structurants : autorisation d'Achille remplacee par un emprunt secret, et reconnaissance de Patrocle par Hector remplacee par une erreur d'identification.

---

## Lot B - Cycle Troyen

Sources de controle principales :

- Theoi, *Epic Cycle Fragments* : https://www.theoi.com/Text/EpicCycle.html
- CHS, *Epic Cycle* : https://chs.harvard.edu/primary-source/epic-cycle-sb/

Sources locales de recoupement :

- Virgile, *Eneide* : `sources/virgil/eneide.pdf`
- Euripide, *Troyennes* : `sources/euripide/troyen.pdf`
- Homere, *Iliade* : `sources/homere/Liliade.pdf`, pour confirmer ce que l'Iliade ne raconte pas.

### Synthese

Le Lot B confirme que plusieurs blocs narratifs du film ne relevent pas de l'Iliade mais de la tradition cyclique :

- Paris a Sparte, l'hospitalite de Menelas, l'union avec Helene et le depart nocturne relevent des *Chants Cypriens*, connus par le resume de Proclus.
- La mort d'Achille apres Hector mais avant la prise de Troie releve de l'*Ethiopide* ; le film deplace fortement cette chronologie.
- Le cheval de Troie releve de la *Petite Iliade* et du *Sac d'Ilion*, avec un fort recoupement chez Virgile, *Eneide* II.
- La prise de Troie, Sinon, Laocoon, Priam, Cassandre, Astyanax, Andromaque et Enee relevent du *Sac d'Ilion* et de traditions posterieures conservees.

Point methodologique central : les poemes du Cycle Troyen sont perdus ou fragmentaires. Les references doivent donc rester prudentes : "selon le resume attribue a Proclus", "tradition cyclique", "fragment transmis par...". Il ne faut pas les presenter comme des textes conserves comparables a l'Iliade.

---

## Verifications par motif cyclique

| Motif | Reference verifiee | Verdict | Probleme ou nuance |
|---|---|---|---|
| Paris a Sparte et origine de la guerre | *Chants Cypriens*, resume de Proclus | Confirme avec prudence | Le sejour de Paris a Sparte, l'hospitalite de Menelas, l'union avec Helene et le depart nocturne sont attestes par le resume. La presence d'Hector dans l'ambassade reste une invention filmique a signaler. |
| Episodes lies a la mort d'Achille | *Ethiopide*, resume de Proclus | Confirme avec contradiction filmique | Dans l'*Ethiopide*, Achille meurt apres Hector et avant la prise de Troie, tue par Paris et Apollon. Le film le maintient actif pendant le sac et deplace sa mort dans la chute finale. |
| Cheval de Troie | *Petite Iliade* et *Sac d'Ilion*, resumes de Proclus | Confirme | La construction par Epeios, les guerriers caches, le faux depart vers Tenedos et l'entree du cheval appartiennent a la tradition cyclique ; Virgile amplifie ensuite Sinon et Laocoon dans l'*Eneide* II. |
| Episodes de la chute de Troie | *Sac d'Ilion*, resume de Proclus | Confirme avec ecarts majeurs | Le *Sac d'Ilion* confirme cheval, Sinon, prise de la ville, Priam, Cassandre, Astyanax, Andromaque et Enee. Le film modifie fortement plusieurs destins, notamment Agamemnon, Briseis, Paris, Helene et Achille. |
| Statut documentaire du Cycle Troyen | Proclus, fragments, traditions indirectes | Statut confirme | Les poemes cycliques sont perdus ou fragmentaires : les references doivent etre formulees comme resume de Proclus, fragment ou tradition cyclique, jamais comme citation directe d'une oeuvre conservee. |

---

## Problemes identifies

### 1. Hector a Sparte

Les *Chants Cypriens* confirment le cadre Paris / Helene / Menelas a Sparte, mais ne justifient pas la presence d'Hector dans cette ambassade. Ce point reste une invention du scenario et devra etre marque comme tel dans les corrections futures.

### 1 bis. Retour de Sparte sur le navire troyen

Les scenes 13 a 16 prolongent le noyau cyclique du depart de Paris avec Helene, mais le traitement filmique doit etre signale comme fortement invente. La revelation d'Helene cachee dans la cabine ou la cale du navire devant Hector n'est pas attestee comme telle dans les sources conservees ou indirectes du Cycle. Elle transforme la fuite ou l'enlevement d'Helene en scene de crise fraternelle et politique.

Le dialogue entre Hector et Paris suppose aussi une intimite fraternelle moderne, avec souvenirs d'enfance partages. Cette construction doit etre nuancee au regard de la tradition de l'exposition de Paris apres la prophetie annoncant la ruine de Troie : selon cette tradition, Paris grandit a l'ecart avant d'etre reconnu. Les scenes du bateau devront donc etre traitees comme un noyau cyclique authentique (`source_principale = "Le Cycle Troyen"`) fortement transforme, avec `degre_fidelite` probable `4`.

### 2. Achille pendant le sac de Troie

Le Cycle Troyen place la mort d'Achille avant la prise de Troie. Sa presence active pendant la chute finale du film est donc une contradiction avec la chronologie cyclique dominante.

### 3. Ajax

La *Petite Iliade* confirme une tradition ou Ajax devient fou apres le jugement des armes d'Achille et se suicide. Le film qui fait tuer Ajax par Hector modifie donc fortement cette tradition. Le point sera aussi recoupe avec Sophocle dans le Lot C.

### 4. Paris survivant

La *Petite Iliade* indique que Philoctete tue Alexandros/Paris avant la chute de Troie. La survie de Paris jusqu'a la fuite finale du film est donc une invention contradictoire par rapport a cette tradition.

### 5. Enee

Le *Sac d'Ilion* mentionne le retrait des compagnons d'Enee vers l'Ida apres le prodige de Laocoon. Virgile developpe ensuite Enee comme survivant porteur d'un avenir troyen. Le film reutilise cette fonction, mais l'objet de l'Epee de Troie et la modalite exacte de transmission sont filmiques.

---

## Conclusion Lot B

Le Lot B confirme que la fin de *Troy* quitte nettement le terrain de l'Iliade. Le film entre dans la matiere du Cycle Troyen, puis la recompose avec Virgile, Euripide et des inventions propres au scenario.

Les points les plus importants pour le futur storytelling sont :

- le cheval de Troie n'est pas dans l'Iliade ;
- la chute de Troie appartient a la tradition cyclique et a ses prolongements greco-romains ;
- Achille ne devrait pas etre vivant pendant le sac dans la chronologie cyclique dominante ;
- Paris ne devrait pas survivre jusqu'a la fuite finale ;
- les scenes du bateau apres Sparte utilisent un noyau cyclique mais inventent la decouverte d'Helene par Hector et une dynamique fraternelle problematique ;
- Ajax ne meurt pas par Hector dans la tradition cyclique ;
- les references au Cycle doivent toujours signaler leur statut indirect.

---

## Lot C - Heritage greco-romain

Sources locales de controle :

- Virgile, *Eneide* : `sources/virgil/eneide.pdf`
- Euripide, *Troyennes* : `sources/euripide/troyen.pdf`

Sources de controle en ligne :

- Eschyle, *Agamemnon* : https://www.theoi.com/Text/AeschylusAgamemnon.html
- Sophocle, *Ajax* : https://www.theoi.com/Text/SophoclesAjax.html
- Euripide, *Troyennes* : https://www.theoi.com/Text/EuripidesTrojanWomen.html
- Stace, *Achilleide* : https://www.theoi.com/Text/StatiusAchilleid1A.html
- Pseudo-Apollodore, *Bibliotheque/Epitome* : https://www.theoi.com/Text/ApollodorusE.html

### Synthese

Le Lot C confirme que `Heritage Greco-Romain` doit designer des oeuvres litteraires precises, pas un contexte culturel vague. Les sources les plus utiles pour *Troy* sont :

- Virgile, *Eneide* II : cheval de Troie, Sinon, Laocoon, mort de Priam, incendie de Troie, fuite d'Enee.
- Sophocle, *Ajax* : tradition tragique de la folie et du suicide d'Ajax.
- Eschyle, *Agamemnon* : retour d'Agamemnon et meurtre par Clytemnestre.
- Euripide, *Troyennes* : captives troyennes, Hecube, Cassandre, Andromaque, Astyanax.
- Stace, *Achilleide* : traditions tardives sur Achille, a utiliser avec prudence.
- Apollodore et Hygin : syntheses mythographiques tardives, utiles pour verifier des variantes.

---

## Verifications par motif greco-romain

| Motif | Reference verifiee | Verdict | Probleme ou nuance |
|---|---|---|---|
| Cheval de Troie, Priam et Enee chez Virgile | Virgile, *Eneide* II, avec antecedent homerique d'Enee en *Iliade* XX | Confirme avec nuance | Virgile conserve et amplifie la chute de Troie : cheval, Sinon, Laocoon, Priam, incendie, fuite d'Enee. Mais l'importance d'Enee ne commence pas avec Virgile : dans l'Iliade, il est deja un heros dardanien majeur, fils d'Anchise et d'Aphrodite, promis a survivre avec sa descendance. Le film reduit fortement cette stature en faisant d'Enee un jeune survivant presque anonyme et en deplacant la charge symbolique vers l'Epee de Troie, objet filmique. |
| Ajax chez Sophocle | Sophocle, *Ajax* | Confirme avec contradiction filmique | Sophocle confirme une tradition tragique de la folie et du suicide d'Ajax apres l'attribution des armes d'Achille. Le film qui fait tuer Ajax par Hector modifie radicalement ce destin. |
| Agamemnon chez Eschyle | Eschyle, *Agamemnon* | Confirme avec contradiction filmique | Eschyle place la mort d'Agamemnon a Argos, apres son retour de Troie, par Clytemnestre avec Egisthe en arriere-plan. Le film le tue a Troie par Briseis : invention contradictoire majeure. |
| Femmes troyennes chez Euripide | Euripide, *Troyennes*, *Hecube*, *Andromaque* | Confirme | Les *Troyennes* confirment un imaginaire tragique des captives, Hecube, Cassandre, Andromaque et Astyanax apres la chute. Le film reprend ce climat mais adoucit ou transforme plusieurs destins, notamment Andromaque et Helene. |
| Traditions tardives sur Achille chez Stace | Stace, *Achilleide* | Confirme avec usage limite | Stace est utile pour traditions tardives autour de l'enfance d'Achille, Thetis, Chiron, Scyros et une allusion a l'immersion inachevee dans le Styx. Il ne doit pas servir a verifier les grands episodes iliadiques du film. |
| Syntheses mythographiques Apollodore / Hygin | Pseudo-Apollodore, *Bibliotheque/Epitome* ; Hygin, *Fables* | Confirme comme sources de controle tardives | Apollodore et Hygin sont utiles pour controler variantes et sequences, mais doivent etre marques comme sources tardives ou compilatoires, non comme sources premieres. |

---

## Problemes identifies

### 1. Virgile et le Cycle Troyen se recoupent

Pour le cheval et la chute de Troie, Virgile ne remplace pas le Cycle Troyen. Il en conserve et amplifie une tradition. Les explications devront distinguer :

- source cyclique perdue ;
- reprise ou amplification virgilienne conservee ;
- invention propre au film.

Pour Enee, il faut aussi distinguer l'antecedent homerique et l'elaboration virgilienne. L'Iliade presente deja Enee comme heros dardanien important, fils d'Anchise et d'Aphrodite, promis a survivre avec sa descendance. Virgile transforme cette survivance en destin romain. Le film conserve la fonction de survivant, mais la reduit et la deplace vers l'Epee de Troie.

### 2. Ajax demande un double controle

Ajax est un heros iliadique et cyclique, mais Sophocle est indispensable pour la tradition tragique du suicide. Le film, qui le fait mourir par Hector, doit etre marque comme ecart majeur.

### 3. Agamemnon ne meurt pas a Troie dans la tradition majeure

Eschyle confirme que le meurtre d'Agamemnon appartient au retour, pas a la prise de Troie. Le meurtre par Briseis dans le film est donc une invention contradictoire.

### 4. Euripide confirme le climat tragique, pas toutes les solutions filmiques

Les *Troyennes* confirment le sort des captives et l'imaginaire de la ville detruite. Mais le film transforme fortement certains destins, notamment la fuite d'Andromaque et d'Helene.

### 5. Stace et les mythographes sont secondaires

Stace, Apollodore et Hygin sont utiles pour des variantes et traditions tardives, mais ils ne doivent pas etre mis au meme niveau que l'Iliade, Virgile ou les tragediens conserves.

---

## Conclusion Lot C

Le Lot C valide l'utilite de la categorie `Heritage Greco-Romain`, a condition de la definir strictement comme corpus litteraire. Elle sert surtout a verifier :

- la chute de Troie chez Virgile ;
- Ajax chez Sophocle ;
- Agamemnon chez Eschyle ;
- les captives et femmes troyennes chez Euripide ;
- les variantes tardives chez Stace, Apollodore et Hygin.

Les corrections futures devront eviter de classer comme `Heritage Greco-Romain` un simple detail rituel ou culturel non rattache a une oeuvre litteraire precise.
