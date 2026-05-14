# Note méthodologique courte

Cette note accompagne le corpus enrichi de *Troy* :

`output/troy_true_or_false_all_scenes_enriched.json`

Elle résume les principes de lecture du fichier sans remplacer le rapport complet :

`docs/rapport_methodologique.md`

---

## Objet du corpus

Le corpus découpe *Troy* en scènes et décrit, pour chacune, son rapport aux sources antiques. L'objectif n'est pas de juger le film, mais de rendre visible sa généalogie littéraire : ce qui vient de l'Iliade, du Cycle Troyen, de la tradition gréco-romaine ou de l'invention scénaristique.

Le corpus est conçu pour servir à une mini web app de data storytelling : timeline, heatmap, fiches personnages, index des sources et parcours sur les grandes ruptures mythiques.

---

## Deux axes de lecture

### 1. `source_principale`

Ce champ indique l'origine dominante du matériau :

| Valeur | Sens |
|---|---|
| `L'Iliade` | Passage, motif, personnage ou structure directement rattaché à l'épopée homérique |
| `Le Cycle Troyen` | Épisodes antérieurs ou postérieurs à l'Iliade, connus par poèmes perdus, résumés ou fragments |
| `Héritage Gréco-Romain` | Prolongements littéraires conservés ou tardifs : Virgile, tragiques, Ovide, Stace, mythographes |
| `Adaptation Cinéma` | Invention principalement scénaristique, même si elle peut utiliser des résonances antiques |

### 2. `degre_fidelite`

Ce champ indique comment le film traite ce matériau :

| Degré | Sens |
|---:|---|
| 1 | Reprise fidèle |
| 2 | Déplacement |
| 3 | Invention sur fond emprunté |
| 4 | Invention contradictoire |

Ces deux axes doivent être lus ensemble. Une scène peut venir de l'Iliade et être contradictoire, ou être inventée par le film tout en brodant sur un motif antique.

---

## Périmètre documentaire

Le corpus repose sur des sources littéraires antiques. Les pratiques historiques, rituelles ou archéologiques ne servent pas à classer une scène, sauf si elles sont rattachées à un texte du corpus.

Sources principales utilisées :

- Homère, *Iliade* et *Odyssée* ;
- Cycle Troyen, surtout les résumés attribués à Proclus ;
- Virgile, *Énéide* ;
- Eschyle, Sophocle, Euripide ;
- Stace, Ovide, Apollodore, Hygin, selon les besoins.

Les sources perdues du Cycle Troyen sont utilisées avec prudence : elles ne sont pas traitées comme des textes conservés, mais comme des traditions indirectement documentées.

---

## Limites assumées

Le corpus n'est pas une édition critique exhaustive. Il vise une lecture claire, vérifiable et visualisable.

Certaines scènes sont composites : elles mélangent un motif antique solide, un déplacement narratif et une invention propre au film. Dans ces cas, `source_principale` indique la matrice dominante, tandis que `explication_litteraire` détaille les nuances.

Le fichier enrichi conserve une vocation éditoriale : il sert à raconter comment *Troy* transforme la matière antique, pas seulement à produire des statistiques.

---

## Fichiers associés

- `docs/taxonomie_sources_et_fidelite.md` : définition complète des deux axes.
- `docs/ruptures_mythiques_troy.md` : synthèse narrative des grandes ruptures.
- `docs/index_personnages_troy.md` : personnages et enjeux mythiques.
- `docs/index_sources_antiques_troy.md` : sources mobilisées.
- `docs/bibliographie_controle.md` : sources de contrôle.
- `output/viz_matrix_source_fidelite.json` : matrice préparée pour visualisation.
- `output/viz_timeline_degre_fidelite.json` : timeline préparée pour visualisation.

