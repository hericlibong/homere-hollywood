# Index des motifs - *Troy*

Ce document ouvre la Phase 1 du plan de travail. Il organise le fichier de reference `output/troy_true_or_false_all_scenes.json` par motifs litteraires afin d'eviter une reprise scene par scene.

Le fichier d'audit associe est :

`output/audit_motifs.csv`

La synthese par motif est :

`output/audit_motifs_synthese.csv`

---

## Role de l'index

L'index sert a constituer des lots de verification. Il ne corrige pas encore le JSON et ne tranche pas la classification finale.

Une scene peut appartenir a plusieurs motifs. C'est normal : une meme sequence peut mobiliser un motif homerique, un personnage tragique, une invention filmique et une reference au Cycle Troyen.

L'audit CSV est volontairement large. Il doit etre relu comme une liste de candidats, pas comme une verite definitive.

---

## Methode de generation

L'audit a ete genere a partir du fichier consolide en recherchant :

- les personnages majeurs ;
- les noms propres secondaires ;
- les expressions presentes dans `action_film` ;
- les references litteraires presentes dans `explication_litteraire` ;
- les scenes dont `source_principale` ou `reference_iliade` signalent une source antique.

Colonnes de `output/audit_motifs.csv` :

- `scene_number`
- `scene_heading`
- `motif_id`
- `motif`
- `source_principale`
- `reference_iliade`
- `source_attendue`
- `statut_probable`
- `priorite`
- `raison_entree_audit`

---

## Synthese des lots

| Motif | Scenes candidates | Priorite | Source attendue |
|---|---:|---|---|
| Duel Achille / Hector | 55 | haute | Iliade, Chant XXII |
| Sac et chute de Troie | 47 | haute | Cycle Troyen / Virgile, *Eneide* II / Euripide |
| Cheval de Troie | 37 | haute | Cycle Troyen / Virgile, *Eneide* II / Odyssee VIII |
| Noms propres secondaires a verifier | 36 | moyenne | Iliade / mythographes / geographie selon nom |
| Inventions geographiques ou politiques du film | 46 | moyenne | Iliade / Cycle Troyen / geographie litteraire / adaptation filmique |
| Querelle Achille / Agamemnon | 34 | haute | Iliade, Chant I |
| Paris, Helene et Sparte | 34 | haute | Cycle Troyen / Iliade / Odyssee selon contexte |
| Femmes troyennes et captives | 29 | moyenne | Euripide, *Troyennes*, *Hecube*, *Andromaque* |
| Patrocle et les armes d'Achille | 28 | haute | Iliade, Chant XVI |
| Priam chez Achille et restitution du corps | 26 | haute | Iliade, Chant XXIV |
| Mort ou destin d'Agamemnon | 23 | haute | Eschyle, *Agamemnon* / Odyssee / adaptation |
| Ajax | 18 | haute | Iliade / Sophocle, *Ajax* / Cycle Troyen |
| Hector, Andromaque, Astyanax | 14 | haute | Iliade, Chant VI / Euripide selon contexte |
| Briseis | 12 | haute | Iliade, Chant I / adaptation filmique a verifier |
| Duel Paris / Menelas | 12 | haute | Iliade, Chant III |
| Survie ou destin de Paris | 12 | moyenne | Cycle Troyen / adaptation |
| Enee et survivance troyenne | 7 | haute | Virgile, *Eneide* / Cycle Troyen |

---

## Lots prioritaires proposes

### Lot 1 - Iliade, noyau dur

Objectif : verifier les explications liees aux chants les plus cites et les plus structurants.

- Querelle Achille / Agamemnon : Chant I.
- Briseis : Chant I et ecarts filmiques.
- Duel Paris / Menelas : Chant III.
- Hector, Andromaque, Astyanax : Chant VI.
- Patrocle et les armes d'Achille : Chant XVI.
- Duel Achille / Hector : Chant XXII.
- Priam chez Achille : Chant XXIV.

Source locale principale :

- `sources/homere/Liliade.pdf`

### Lot 2 - Chute de Troie

Objectif : verifier tout ce qui ne releve pas de l'Iliade mais de la tradition de la prise de Troie.

- Cheval de Troie.
- Sac et chute de Troie.
- Priam pendant la chute.
- Enee et survivance troyenne.

Sources de controle :

- Cycle Troyen, *Petite Iliade* et *Sac d'Ilion*, via resumes/fragments.
- Virgile, *Eneide* II : `sources/virgil/eneide.pdf`.
- Odyssee VIII pour le souvenir du cheval.

### Lot 3 - Destins contradictoires ou deplaces

Objectif : isoler les endroits ou le film modifie fortement une tradition litteraire.

- Mort ou destin d'Agamemnon.
- Ajax.
- Survie ou destin de Paris.
- Briseis comme personnage filmique.
- Enee comme survivant porteur d'avenir.

Sources de controle :

- Sophocle, *Ajax*.
- Eschyle, *Agamemnon*.
- Cycle Troyen.
- Virgile, *Eneide*.

### Lot 4 - Femmes troyennes et captives

Objectif : verifier les traditions tragiques et post-iliadiques autour des femmes troyennes.

- Hecube.
- Cassandre.
- Andromaque.
- Astyanax.
- Captives troyennes.
- Helene dans les traditions post-homeriques.

Source locale principale :

- Euripide, *Troyennes* : `sources/euripide/troyen.pdf`.

### Lot 5 - Noms propres secondaires

Objectif : eviter les affirmations fragiles sur les noms secondaires et les traditions locales.

Noms signales par l'audit :

- Triopas.
- Boagrius.
- Tecton.
- Lysander.
- Archeptolemus.
- Velior.
- Eudorus.
- Aphaereus / Aphareus.
- Echepolus.
- Haemon.
- Polydora.
- Glaucus.

Sources de controle :

- Iliade si le nom est homerique.
- Mythographes si le nom releve d'une tradition secondaire.
- Strabon ou Pausanias seulement pour lieux, fleuves ou traditions locales explicitement invoques.

### Lot 6 - Inventions geographiques ou politiques

Objectif : reperer les elements ou le film reconstruit la carte politique ou geographique de la matiere troyenne.

Exemples de signaux :

- Thessalie, Phthie, Sparte, Mycenes.
- Agamemnon comme constructeur d'un empire grec unifie.
- Alliance ou soumission politique entre royaumes.
- Tunnel, passage secret, fuite organisee.
- Epee de Troie ou objet politique invente.

Sources de controle :

- Iliade pour les lieux et appartenances explicitement homeriques.
- Cycle Troyen si l'episode appartient a la tradition epique perdue.
- Virgile et les tragiques si l'element releve de la chute de Troie ou de la survivance troyenne.
- Strabon ou Pausanias seulement pour verifier un nom de lieu ou une tradition locale citee dans une explication.

---

## Premiere selection de verification

Pour demarrer sans se disperser, la premiere passe doit porter sur les lots suivants :

1. Iliade, noyau dur.
2. Chute de Troie.
3. Destins contradictoires.

La verification doit se faire affirmation par affirmation dans `explication_litteraire`, sans modifier immediatement `source_principale`.

---

## Limites de l'audit

- Les recherches par mots-cles produisent des faux positifs.
- Les scenes tres riches peuvent apparaitre dans plusieurs lots.
- Les scenes classees `Adaptation Cinema` peuvent tout de meme contenir des references antiques a verifier.
- Les chiffres de scenes candidates mesurent un perimetre de travail, pas une classification definitive.
