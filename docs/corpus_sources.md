# Corpus de sources antiques pour l'analyse de *Troy*

Ce document definit le corpus documentaire utilise pour verifier les `explication_litteraire` du fichier de reference :

`output/troy_true_or_false_all_scenes.json`

Il ne sert pas a reclasser immediatement les scenes. Il sert d'abord a verifier les affirmations litteraires : source, oeuvre, auteur, passage, niveau de certitude.

---

## 1. Perimetre du projet

Le projet releve de la litterature comparee. Les scenes du film sont analysees sous l'angle de leur genealogie litteraire : textes grecs, latins, tardifs ou mythographiques qui transmettent, transforment ou prolongent la matiere troyenne.

Les categories du champ `source_principale` doivent donc etre comprises ainsi :

- `L'Iliade` : passages, formules, personnages ou structures narratives directement rattaches a l'epopee homerique.
- `Le Cycle Troyen` : episodes issus des poemes cycliques perdus ou fragmentaires, connus par resumes, fragments et traditions indirectes.
- `Heritage Greco-Romain` : oeuvres litteraires antiques ou tardo-antiques qui prolongent la matiere troyenne : Virgile, tragiques grecs, Ovide, Stace, Apollodore, Hygin, etc.
- `Adaptation Cinema` : materiau principalement invente par le scenario moderne, meme s'il peut contenir des resonances antiques a verifier dans l'explication.

Les pratiques historiques, rituelles, archeologiques ou anthropologiques ne constituent pas en elles-memes des sources de classification. Elles ne doivent pas piloter `source_principale`. Si une explication mentionne un rite ou une coutume, la verification doit demander : existe-t-il une source litteraire antique precise qui justifie cette affirmation ?

---

## 2. Methode de verification

La verification se fait affirmation par affirmation dans `explication_litteraire`.

Pour chaque affirmation, relever :

- scene concernee ;
- affirmation a verifier ;
- source proposee dans le JSON ;
- oeuvre et auteur de controle ;
- livre, chant ou vers si possible ;
- statut : confirme, a nuancer, non confirme, hors corpus ;
- consequence eventuelle : conserver, reformuler, sourcer, retirer.

Cette phase ne modifie pas encore le JSON de reference. Elle produit d'abord des audits.

---

## 3. Portes d'entree dans l'audit

Les motifs listes dans ce document sont indicatifs et non exhaustifs. Ils ne doivent jamais limiter l'enquete.

Une scene entre dans l'audit d'une source si au moins un de ces criteres est present :

- `source_principale` nomme cette source ou cette famille de sources ;
- `reference_iliade` est renseigne ;
- `explication_litteraire` mentionne explicitement une oeuvre, un auteur, un chant, un vers, une formule ou une tradition ;
- la scene contient un personnage ou un episode dont l'explication affirme une origine antique ;
- la scene est classee `Adaptation Cinema`, mais son explication invoque une source antique secondaire.

Exemple : une scene classee `Adaptation Cinema` mais dont l'explication cite le Chant I de l'Iliade doit entrer dans l'audit homerique.

---

## 4. Niveaux de fiabilite documentaire

### Niveau A - Sources litteraires conservees

Textes conserves, directement consultables. Ce sont les sources les plus fortes pour confirmer ou corriger une affirmation.

Exemples :

- Homere, *Iliade* ;
- Homere, *Odyssee* ;
- Virgile, *Eneide* ;
- Eschyle, *Agamemnon* ;
- Sophocle, *Ajax* ;
- Euripide, *Troyennes*, *Hecube*, *Andromaque* ;
- Ovide, *Heroides*, *Metamorphoses* ;
- Stace, *Achilleide*.

### Niveau B - Sources perdues, fragmentaires ou indirectes

Textes dont l'etat de conservation impose la prudence. Ils peuvent etre utilises, mais leur statut doit etre signale.

Exemples :

- *Chants Cypriens* ;
- *Ethiopide* ;
- *Petite Iliade* ;
- *Sac d'Ilion* ;
- *Retours* ;
- *Telegonie* ;
- resumes attribues a Proclus ;
- fragments transmis par scholies ou auteurs posterieurs.

### Niveau C - Mythographes et compilations tardives

Sources utiles pour cartographier des traditions, mais plus tardives et souvent synthetiques.

Exemples :

- Apollodore, *Bibliotheque* ;
- Hygin, *Fables* ;
- Servius, commentaires a Virgile, si necessaire.

### Niveau D - Sources auxiliaires

Sources utiles pour noms propres, lieux, genealogies, geographie litteraire ou traditions locales.

Exemples :

- Strabon, *Geographie* ;
- Pausanias, *Description de la Grece* ;
- scholies antiques, si elles sont explicitement identifiees.

---

## 5. Corpus principal

### 5.1 Homere, *Iliade*

- Auteur : Homere, attribution traditionnelle.
- Langue : grec ancien.
- Statut : source litteraire conservee.
- Niveau de fiabilite : A.
- Usage dans le projet : verifier toutes les scenes marquees `L'Iliade`, toutes les references a un chant, et toutes les allusions homeriques presentes dans les explications.
- Source locale : `sources/Liliade.pdf`.
- Sources de controle :
  - Perseus / Scaife Viewer : https://atlas.perseus.tufts.edu/library/urn:cts:greekLit:tlg0012.tlg001.perseus-eng4/
  - Perseus Hopper, texte grec/anglais par chant : https://www.perseus.tufts.edu/

Points d'attention :

- L'Iliade ne raconte pas toute la guerre de Troie. Elle couvre un episode limite de la colere d'Achille.
- Les episodes posterieurs a la mort d'Hector ne doivent pas etre attribues a l'Iliade.
- Une scene peut contenir un personnage iliadique sans reprendre un passage de l'Iliade.
- Une formule homerique ou une resonance stylistique ne suffit pas toujours a remplir `reference_iliade`.

Portes d'entree dans l'audit homerique :

- `source_principale = "L'Iliade"` ;
- `reference_iliade` non vide ;
- mentions de "Iliade", "Homere", "homerique", "Chant", "vers" ;
- references aux formules ou episodes homeriques dans `explication_litteraire`.

### 5.2 Homere, *Odyssee*

- Auteur : Homere, attribution traditionnelle.
- Langue : grec ancien.
- Statut : source litteraire conservee.
- Niveau de fiabilite : A.
- Usage dans le projet : verifier les traditions de retour, Menelas et Helene apres la guerre, le souvenir du cheval de Troie, les morts evoques dans l'au-dela.
- Source de controle :
  - Perseus Hopper : https://www.perseus.tufts.edu/hopper/text?doc=Perseus:text:1999.01.0135

Passages a surveiller :

- Chant IV : Menelas et Helene a Sparte apres la guerre.
- Chant VIII : chant de Demodocos sur le cheval de Troie.
- Chant XI : nekuia, morts et memoire des heros.
- Chant XXIV : ombres des pretendants, memoire d'Achille et Agamemnon.

---

## 6. Cycle Troyen

Le Cycle Troyen designe un ensemble de poemes epiques entourant l'Iliade et l'Odyssee. La plupart sont perdus. Ils sont connus par fragments, resumes et traditions indirectes, notamment le resume attribue a Proclus.

La mention d'une source cyclique doit toujours indiquer son statut : source perdue, connue par resume ou fragments.

Sources de controle :

- Center for Hellenic Studies, *Epic Cycle* : https://chs.harvard.edu/primary-source/epic-cycle-sb/
- Theoi, *Epic Cycle Fragments* : https://www.theoi.com/Text/EpicCycle.html

### 6.1 *Chants Cypriens*

- Statut : poeme perdu, connu par resume et fragments.
- Niveau de fiabilite : B.
- Usage dans le projet : verifier les episodes precedant l'Iliade.
- Questions typiques :
  - jugement de Paris ;
  - depart ou sejour de Paris a Sparte ;
  - enlevement ou fuite d'Helene ;
  - rassemblement des Acheens ;
  - debuts de la guerre.

### 6.2 *Ethiopide*

- Statut : poeme perdu, connu par resume et fragments.
- Niveau de fiabilite : B.
- Usage dans le projet : verifier les episodes posterieurs a l'Iliade autour d'Achille.
- Questions typiques :
  - Penthesilee ;
  - Memnon ;
  - mort d'Achille par Paris et Apollon.

### 6.3 *Petite Iliade*

- Statut : poeme perdu, connu par resume et fragments.
- Niveau de fiabilite : B.
- Usage dans le projet : verifier les episodes qui menent a la chute de Troie.
- Questions typiques :
  - jugement des armes d'Achille ;
  - folie et mort d'Ajax selon la tradition cyclique ;
  - Philoctete ;
  - mort de Paris ;
  - construction ou ruse du cheval selon les traditions transmises.

### 6.4 *Sac d'Ilion*

- Statut : poeme perdu, connu par resume et fragments.
- Niveau de fiabilite : B.
- Usage dans le projet : verifier la prise de Troie.
- Questions typiques :
  - cheval de Troie ;
  - Laocoon ;
  - Sinon ;
  - mort de Priam ;
  - sort de Cassandre ;
  - fuite ou retrait d'Enee selon la tradition.

### 6.5 *Retours*

- Statut : poeme perdu, connu par resume et fragments.
- Niveau de fiabilite : B.
- Usage dans le projet : verifier les retours des heros grecs.
- Questions typiques :
  - retour de Menelas ;
  - retour d'Agamemnon ;
  - tempetes et errances ;
  - destin des chefs acheens apres Troie.

### 6.6 *Telegonie*

- Statut : poeme perdu, connu par resume et fragments.
- Niveau de fiabilite : B.
- Usage dans le projet : faible pour *Troy*, utile seulement si une explication mentionne les traditions tardives autour d'Ulysse apres l'Odyssee.

---

## 7. Heritage greco-romain litteraire

Cette categorie designe des oeuvres litteraires antiques ou tardo-antiques qui reprennent, prolongent ou transforment la matiere troyenne. Elle ne designe pas une ambiance culturelle generale.

### 7.1 Virgile, *Eneide*

- Auteur : Virgile.
- Langue : latin.
- Statut : source litteraire conservee.
- Niveau de fiabilite : A.
- Usage dans le projet : verifier les traditions latines sur la chute de Troie, le cheval, Laocoon, Sinon, Priam et Enee.
- Source de controle :
  - Perseus Hopper : https://www.perseus.tufts.edu/hopper/text?doc=urn:cts:latinLit:phi0690.phi003.perseus-eng2
  - Theoi, *Aeneid* II : https://www.theoi.com/Text/VirgilAeneid2.html

Passage central :

- Livre II : recit d'Enee sur la chute de Troie.

### 7.2 Eschyle, *Agamemnon*

- Auteur : Eschyle.
- Langue : grec ancien.
- Statut : source litteraire conservee.
- Niveau de fiabilite : A.
- Usage dans le projet : verifier le retour et la mort d'Agamemnon, quand le film invente ou deplace son destin.
- Source de controle :
  - Theoi : https://www.theoi.com/Text/AeschylusAgamemnon.html

### 7.3 Sophocle, *Ajax*

- Auteur : Sophocle.
- Langue : grec ancien.
- Statut : source litteraire conservee.
- Niveau de fiabilite : A.
- Usage dans le projet : verifier la tradition de la mort d'Ajax, surtout si le film le fait mourir autrement.
- Source de controle :
  - Theoi : https://www.theoi.com/Text/SophoclesAjax.html

### 7.4 Euripide, *Troyennes*, *Hecube*, *Andromaque*

- Auteur : Euripide.
- Langue : grec ancien.
- Statut : sources litteraires conservees.
- Niveau de fiabilite : A.
- Usage dans le projet : verifier les traditions tragiques sur les femmes troyennes, le sort des captives, Andromaque, Hecube, Cassandre et Astyanax.
- Sources de controle :
  - *Troyennes* : https://www.theoi.com/Text/EuripidesTrojanWomen.html
  - *Hecube* : https://www.theoi.com/Text/EuripidesHecuba.html
  - *Andromaque* : https://www.theoi.com/Text/EuripidesAndromache.html

### 7.5 Ovide, *Heroides* et *Metamorphoses*

- Auteur : Ovide.
- Langue : latin.
- Statut : sources litteraires conservees.
- Niveau de fiabilite : A pour le texte, a manier comme tradition poetique tardive.
- Usage dans le projet : verifier les voix epistolaires ou transformations poetiques de personnages troyens, notamment Helene, Paris, Oenone, Briseis selon les textes mobilises.
- Source de controle a rattacher :
  - Perseus ou editions numeriques fiables a identifier selon les passages.

### 7.6 Stace, *Achilleide*

- Auteur : Stace.
- Langue : latin.
- Statut : source litteraire conservee mais incomplete.
- Niveau de fiabilite : A pour le texte, tradition tardive pour la matiere.
- Usage dans le projet : verifier les traditions tardives autour d'Achille, surtout enfance, travestissement a Skyros et motifs non homeriques.
- Source de controle :
  - Wikisource, traduction anglaise : https://en.wikisource.org/wiki/Achilleid_(Statius)

---

## 8. Mythographes et sources tardives

Ces sources servent a verifier l'existence d'une tradition, mais elles doivent etre distinguees des sources epiques ou tragiques plus anciennes.

### 8.1 Apollodore, *Bibliotheque*

- Auteur : pseudo-Apollodore.
- Langue : grec ancien.
- Statut : compilation mythographique conservee.
- Niveau de fiabilite : C.
- Usage dans le projet : verifier genealogies, sequences mythologiques, variantes et syntheses de la guerre de Troie.
- Source de controle :
  - Theoi : https://www.theoi.com/Text/ApollodorusE.html

### 8.2 Hygin, *Fables*

- Auteur : Hygin, attribution traditionnelle.
- Langue : latin.
- Statut : compilation mythographique tardive.
- Niveau de fiabilite : C.
- Usage dans le projet : verifier variantes tardives, listes de personnages, traditions secondaires.
- Source de controle a rattacher :
  - edition numerique fiable a identifier selon les passages.

---

## 9. Geographie et noms propres

Ces sources ne doivent pas remplacer les sources litteraires narratives, mais elles peuvent aider a verifier un nom, un lieu ou une tradition locale citee dans une explication.

### 9.1 Strabon, *Geographie*

- Auteur : Strabon.
- Langue : grec ancien.
- Statut : source conservee.
- Niveau de fiabilite : D pour le projet.
- Usage dans le projet : verifier lieux, fleuves, ethnonymes, noms propres geographiques.
- Source de controle :
  - Perseus Hopper : https://www.perseus.tufts.edu/

### 9.2 Pausanias, *Description de la Grece*

- Auteur : Pausanias.
- Langue : grec ancien.
- Statut : source conservee.
- Niveau de fiabilite : D pour le projet.
- Usage dans le projet : verifier traditions locales et cultuelles seulement si elles sont explicitement invoquees dans une explication.

---

## 10. Sources a localiser ou ajouter

- [x] Localiser et rattacher `Liliade.pdf` si le fichier doit etre utilise directement dans le depot : `sources/Liliade.pdf`.
- [ ] Localiser ou rattacher `troy.pdf` si le scenario source doit etre cite dans les audits.
- [ ] Identifier une edition numerique stable de l'Odyssee en francais ou anglais.
- [ ] Identifier une edition numerique stable d'Ovide, *Heroides*.
- [ ] Identifier une edition numerique stable d'Ovide, *Metamorphoses*.
- [ ] Identifier une edition numerique stable d'Hygin, *Fables*.
- [ ] Decider si Theoi, Perseus et CHS suffisent pour la premiere passe de verification.

---

## 11. Premiere application pratique

La premiere passe d'audit peut commencer par l'Iliade :

- toutes les scenes `source_principale = "L'Iliade"` ;
- toute scene avec `reference_iliade` renseigne ;
- toute scene dont `explication_litteraire` cite Homere, l'Iliade, un chant, un vers ou une formule homerique.

Sortie attendue :

`output/audit_iliade_candidates.csv`

Colonnes recommandees :

- `scene_number`
- `scene_heading`
- `source_principale`
- `reference_iliade`
- `affirmation_a_verifier`
- `source_attendue`
- `passage_a_controler`
- `statut_verification`
- `note`
