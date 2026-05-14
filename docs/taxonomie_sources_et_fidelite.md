# Taxonomie sources et fidelite

Ce document definit la taxonomie a deux axes qui sera utilisee pour enrichir le corpus *Troy*.

Il ne modifie pas encore le JSON de reference :

`output/troy_true_or_false_all_scenes.json`

Il sert a fixer les regles avant le tagging semi-manuel de Phase 4.

---

## 1. Objet du document

Le champ actuel `source_principale` indique l'origine dominante du materiau litteraire d'une scene. Il ne suffit pas toujours a decrire la maniere dont le film traite cette source.

Deux scenes peuvent avoir une meme origine antique mais des rapports tres differents a la tradition :

- reprise assez fidele ;
- deplacement de lieu, de moment ou de personnage ;
- invention inspiree par un motif antique ;
- contradiction avec une donnee majeure de la tradition.

La nouvelle taxonomie separe donc deux questions :

1. D'ou vient le materiau ?
2. Que fait le film avec ce materiau ?

---

## 2. Axe 1 - `source_principale`

Le champ `source_principale` est conserve. Il reste l'axe d'origine du materiau.

Valeurs autorisees :

- `L'Iliade`
- `Le Cycle Troyen`
- `Heritage Greco-Romain`
- `Adaptation Cinema`

### 2.1 `L'Iliade`

Utiliser cette valeur quand la scene reprend principalement un passage, un motif, une structure narrative ou une formule directement rattachee a l'Iliade.

Exemples :

- querelle Achille / Agamemnon ;
- Briseis et Chryseis ;
- duel Paris / Menelas ;
- Hector / Andromaque / Astyanax ;
- Patrocle et les armes d'Achille ;
- duel Achille / Hector ;
- Priam chez Achille.

Attention :

- La presence d'Achille, Hector ou Troie ne suffit pas a classer une scene dans `L'Iliade`.
- Une simple resonance homerique ne suffit pas toujours a remplir `reference_iliade`.
- Les episodes posterieurs a la mort d'Hector ne sont pas racontes par l'Iliade.

### 2.2 `Le Cycle Troyen`

Utiliser cette valeur quand la scene releve principalement d'un episode transmis par les poemes cycliques perdus ou fragmentaires.

Exemples :

- Paris a Sparte ;
- enlevement ou fuite d'Helene ;
- rassemblement des Acheens ;
- mort d'Achille ;
- cheval de Troie ;
- prise de Troie.

Attention :

- Les oeuvres du Cycle Troyen sont perdues ou fragmentaires.
- Les references doivent etre formulees prudemment : resume de Proclus, fragment, tradition cyclique.
- Ne pas presenter les *Chants Cypriens*, l'*Ethiopide*, la *Petite Iliade* ou le *Sac d'Ilion* comme des textes conserves comparables a l'Iliade.

### 2.3 `Heritage Greco-Romain`

Utiliser cette valeur quand la scene est principalement eclairee par une oeuvre litteraire antique ou tardo-antique conservee ou identifiable.

Exemples :

- Virgile, *Eneide* ;
- Eschyle, *Agamemnon* ;
- Sophocle, *Ajax* ;
- Euripide, *Troyennes*, *Hecube*, *Andromaque* ;
- Ovide, *Heroides*, *Metamorphoses* ;
- Stace, *Achilleide* ;
- Apollodore, *Bibliotheque* ;
- Hygin, *Fables*.

Attention :

- `Heritage Greco-Romain` designe un corpus litteraire, pas un contexte culturel general.
- Une pratique rituelle, historique ou archeologique ne suffit pas a classer une scene dans cette categorie.
- La source doit etre une oeuvre ou une tradition litteraire identifiable.

### 2.4 `Adaptation Cinema`

Utiliser cette valeur quand le materiau principal de la scene est une invention du scenario moderne.

Exemples :

- duel Achille / Boagrius ;
- Briseis princesse troyenne et cousine d'Hector ;
- Hector a Sparte ;
- mort de Menelas par Hector ;
- mort d'Ajax par Hector ;
- Agamemnon tue a Troie ;
- Epee de Troie ;
- tunnel d'evacuation.

Attention :

- Une scene classee `Adaptation Cinema` peut contenir des resonances antiques.
- Ces resonances doivent etre expliquees dans `explication_litteraire`, mais elles ne changent pas forcement la source principale.

---

## 3. Axe 2 - `degre_fidelite`

Le champ `degre_fidelite` sera ajoute en Phase 4. Il mesure le rapport du film a la source ou a la tradition.

Valeurs autorisees :

- `1` : reprise fidele ;
- `2` : deplacement ;
- `3` : invention sur fond emprunte ;
- `4` : invention contradictoire.

### 3.1 Degre 1 - Reprise fidele

La scene reprend un passage ou un motif identifiable des sources, parfois condense ou modernise, sans en inverser le sens.

Une reprise fidele peut contenir des simplifications. Elle reste degre 1 si le noyau dramatique, les rapports de personnages et le sens general sont conserves.

Exemples :

- Priam vient supplier Achille pour recuperer le corps d'Hector.
- Duel Achille / Hector, si la scene conserve le noyau du Chant XXII.
- Duel Paris / Menelas, si la scene conserve le principe du combat singulier et son enjeu.

### 3.2 Degre 2 - Deplacement

La scene utilise un element reel des sources, mais le transpose :

- autre lieu ;
- autre moment ;
- autre personnage ;
- autre enchainement narratif ;
- condensation de plusieurs passages.

Le sens general reste compatible avec la tradition, mais la mise en scene deplace le materiau.

Exemples :

- adieux d'Hector et Andromaque deplaces dans une chambre au lieu des portes Scees ;
- motif iliadique diffuse dans plusieurs dialogues au lieu d'apparaitre dans son contexte d'origine ;
- scene composite qui condense plusieurs moments antiques.

### 3.3 Degre 3 - Invention sur fond emprunte

La scene est inventee par le film, mais elle s'appuie sur des motifs, codes ou structures antiques reconnaissables.

Elle ne contredit pas necessairement la tradition ; elle brode sur elle.

Exemples :

- duel Achille / Boagrius en Thessalie ;
- tunnel d'Andromaque comme invention qui joue sur le motif de la captivite future ;
- certaines scenes de strategie ou de camp qui traduisent visuellement une tension homerique sans reprendre un passage precis.

### 3.4 Degre 4 - Invention contradictoire

La scene contredit une donnee majeure des sources antiques ou de la tradition litteraire dominante.

Il peut s'agir :

- d'une mort inventee ;
- d'une survie impossible dans la chronologie antique dominante ;
- d'un personnage place dans un episode ou il n'apparait pas ;
- d'une genealogie transformee ;
- d'un role narratif contraire a la tradition.

Exemples :

- mort de Menelas par Hector ;
- mort d'Ajax par Hector ;
- Briseis princesse troyenne et cousine d'Hector ;
- Hector a Sparte ;
- Achille vivant pendant le sac de Troie ;
- Paris survivant jusqu'a la fuite finale ;
- Agamemnon tue a Troie par Briseis.

---

## 4. Criteres d'arbitrage

### 4.1 Choisir `1` plutot que `2`

Choisir `1` si :

- le passage source est clairement identifiable ;
- les personnages principaux conservent leur role ;
- l'enjeu dramatique est le meme ;
- les simplifications ne changent pas le sens du motif.

Choisir `2` si :

- le motif est deplace dans un autre lieu ou moment ;
- plusieurs passages sont condenses ;
- un personnage est remplace ou ajoute sans contradiction majeure ;
- le film conserve l'idee mais reorganise fortement la scene.

Exemple :

- Priam chez Achille peut etre `1` si l'on privilegie le noyau de supplication conserve.
- Hector / Andromaque peut etre `2` si l'on insiste sur le deplacement spatial et domestique.

### 4.2 Choisir `3` plutot que `4`

Choisir `3` si :

- la scene est inventee ;
- elle s'inspire de codes antiques ;
- elle ne contredit pas une donnee majeure ;
- elle pourrait exister comme broderie moderne autour du mythe.

Choisir `4` si :

- la scene invente une mort contraire a la tradition ;
- elle fait survivre un personnage qui devrait etre mort selon la tradition dominante ;
- elle attribue a un personnage une genealogie ou un role incompatible ;
- elle modifie une chronologie structurante.

Exemple :

- Boagrius tue par Achille : degre `3`.
- Ajax tue par Hector : degre `4`.

### 4.3 Scene avec materiau antique et contradiction filmique

Quand une scene utilise un materiau antique authentique pour produire une rupture avec la tradition, il ne faut pas ecraser les deux dimensions.

Regle :

- `source_principale` indique le materiau dominant ;
- `degre_fidelite` indique la rupture eventuelle.

Exemple :

- Une scene peut etre rattachee a l'Iliade, au Cycle Troyen ou a Sophocle, tout en ayant `degre_fidelite = 4`.

Ce cas est important pour le storytelling : il montre que le film ne part pas toujours de rien, mais transforme parfois une tradition forte en la contredisant.

### 4.4 Scenes composites

Une scene composite combine plusieurs couches :

- motif homerique ;
- episode cyclique ;
- amplification virgilienne ;
- invention filmique.

Regle :

1. Identifier le noyau narratif principal.
2. Conserver ce noyau dans `source_principale`.
3. Utiliser `explication_litteraire` pour decrire les couches secondaires.
4. Utiliser `degre_fidelite` pour mesurer l'ecart global du film.

Exemple :

- Une scene de funerailles peut rappeler l'Iliade, contenir un detail post-homerique et inclure des morts filmiques contradictoires. La classification ne doit pas forcement changer a cause d'un detail secondaire ; l'explication doit faire apparaitre les couches.

---

## 5. Exemples obligatoires

### 5.1 Scene 6 - Achille contre Boagrius

Proposition :

```json
{
  "source_principale": "Adaptation Cinema",
  "degre_fidelite": 3
}
```

Justification :

Le duel contre Boagrius est invente par le film. Il ne reprend pas un episode antique precis. Mais il utilise des codes heroiques homeriques : duel singulier, vitesse d'Achille, tension avec Agamemnon, mediation de Nestor, patronyme de Peleide. C'est une invention sur fond emprunte.

### 5.2 Scene 8 - Banquet de Sparte

Proposition :

```json
{
  "source_principale": "Le Cycle Troyen",
  "degre_fidelite": 4
}
```

Justification :

La visite de Paris a Sparte et le cadre Menelas / Helene relevent des *Chants Cypriens*, connus par le resume de Proclus. Mais la presence d'Hector dans cette ambassade n'est pas justifiee par la tradition antique dominante. Le film introduit donc une invention contradictoire ou fortement intrusive dans un cadre cyclique authentique.

### 5.3 Scene 98 - Ajax tue par Hector

Proposition :

```json
{
  "source_principale": "Heritage Greco-Romain",
  "degre_fidelite": 4
}
```

Justification :

Ajax est un heros majeur de la tradition grecque. Sa mort n'est pas une mort au combat contre Hector : la tradition cyclique et Sophocle associent son destin a la folie puis au suicide apres l'attribution des armes d'Achille. Le film invente donc une mort contradictoire.

Point a arbitrer en Phase 5 :

- Si la scene est interpretee surtout comme materiau iliadique de bataille, `source_principale` pourrait etre discute.
- Mais le `degre_fidelite = 4` doit rester stable.

### 5.4 Scenes 13-16 - Retour de Sparte sur le navire troyen

Proposition :

```json
{
  "source_principale": "Le Cycle Troyen",
  "degre_fidelite": 4
}
```

Justification :

Le noyau narratif vient des *Chants Cypriens* : Paris repart avec Helene et cet episode declenche la guerre. Mais le film invente fortement le traitement : Hector accompagne Paris, decouvre Helene cachee sur le navire, puis devient temoin direct du choix de son frere. Le dialogue fraternel suppose une enfance commune et une intimite continue, alors qu'une tradition importante fait de Paris un enfant expose a cause de la prophetie de ruine de Troie, puis eleve a l'ecart avant sa reconnaissance. C'est donc un cas de noyau cyclique authentique transforme en scene familiale moderne et contradictoire.

### 5.5 Scene 141 - Duel Achille / Hector

Proposition :

```json
{
  "source_principale": "L'Iliade",
  "degre_fidelite": 1
}
```

Justification :

Le duel Achille / Hector est le sommet du Chant XXII. Le film condense et simplifie, mais conserve le noyau dramatique : confrontation directe, mort d'Hector, lien avec Patrocle, outrage au corps. Si une scene precise de la sequence deplace fortement un detail, elle pourra etre notee `2`, mais le noyau du motif reste une reprise forte.

### 5.6 Scene 104 - Treve funeraire et morts contradictoires

Proposition provisoire :

```json
{
  "source_principale": "Heritage Greco-Romain",
  "degre_fidelite": 4
}
```

Justification :

La scene est composite. Elle rappelle la treve funeraire du Chant VII de l'Iliade, mais contient aussi des morts filmiques contradictoires, notamment Menelas et Ajax. Le detail des pieces sur les yeux ne doit pas piloter la classification s'il n'est pas rattache a une oeuvre litteraire precise. Cette scene devra etre arbitree en Phase 5, mais elle illustre clairement le cas "materiau antique + contradiction filmique".

---

## 6. Consequences pour le tagging

La Phase 4 devra produire un fichier enrichi sans ecraser le JSON de reference.

Fichier attendu :

`output/troy_true_or_false_all_scenes_tagged_draft.json`

Chaque scene recevra :

```json
{
  "degre_fidelite": 1
}
```

ou :

```json
{
  "degre_fidelite": 2
}
```

ou :

```json
{
  "degre_fidelite": 3
}
```

ou :

```json
{
  "degre_fidelite": 4
}
```

Le tagging initial suivra l'option B :

- heuristique automatique ;
- liste explicite de contradictions majeures ;
- relecture ciblee des scenes ambigues.

---

## 7. Points a ne pas faire

- Ne pas changer `source_principale` des scenes avant l'audit de Phase 5.
- Ne pas utiliser `Heritage Greco-Romain` pour un simple detail culturel ou rituel non rattache a une oeuvre.
- Ne pas confondre une resonance homerique avec une reprise directe.
- Ne pas classer toute invention comme contradiction.
- Ne pas traiter les sources du Cycle Troyen comme des textes conserves.
- Ne pas presenter Apollodore ou Hygin comme sources premieres.
- Ne pas masquer les scenes hybrides : elles sont souvent les plus interessantes pour le storytelling.
