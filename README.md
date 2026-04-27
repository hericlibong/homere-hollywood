# Homère & Hollywood 

*Relecture des épopées homériques à travers le cinéma et les séries.*

---

## Le projet en bref

**Homère & Hollywood** est un projet de data storytelling qui compare les adaptations cinématographiques et télévisuelles des épopées homériques avec leurs textes sources. L'objectif n'est pas de juger les choix des réalisateurs, mais de cartographier précisément ce qui vient d'Homère, du Cycle Troyen, de la tradition antique élargie (Virgile, Ovide, tragiques grecs) ou de l'invention pure du film.

Le projet s'inscrit dans l'actualité de la sortie de *The Odyssey* de Christopher Nolan, prévue le 17 juillet 2026.

L'angle est celui d'une **généalogie littéraire** : pour chaque scène d'un film, on retrace son origine dans le corpus antique. Le résultat n'est ni une critique de cinéma, ni une étude académique, mais une lecture transversale qui rend visible ce que ces films doivent — ou non — aux textes anciens.

---

## État d'avancement

| Étape | Statut |
|---|---|
| Concept et corpus | ✅ Validé |
| Schéma de données | ✅ Finalisé (7 champs) |
| Prompt système d'analyse | ✅ Calibré pour la phase 2 |
| Dataset *Troy* (Petersen, 2004) | ✅ Première version, 202 scènes |
| Rapport méthodologique | ✅ Disponible |
| Validation philologique fine | 🔲 Phase 2 à venir |
| Autres films du corpus | 🔲 À traiter |
| Stack technique de la web app | 🔲 À choisir |
| Visualisations interactives | 🔲 À développer |
| Déploiement | 🔲 À venir |

---

## Le corpus

### Films et séries analysés

- *Troy* — Wolfgang Petersen, 2004
- *Ulysses* — Mario Camerini, 1954 (avec Kirk Douglas)
- *Troy: Fall of a City* — série BBC/Netflix, 2018
- *The Odyssey* — Christopher Nolan, 2026 (à venir)

### Textes sources

**Sources primaires**
- *Iliade* et *Odyssée* d'Homère — domaine public

**Cycle épique troyen**
Six épopées aujourd'hui perdues, connues par fragments et par le résumé de Proclus :
- *Chants Cypriens*
- *Éthiopide*
- *Petite Iliade*
- *Sac d'Ilion*
- *Les Retours*
- *Télégonie*

**Tradition antique élargie**
- Virgile, *Énéide*
- Ovide, *Métamorphoses*, *Héroïdes*
- Tragiques grecs : Eschyle, Sophocle, Euripide
- Stace, *Achilléide*
- Apollonios de Rhodes, *Argonautiques*

---

## Méthodologie

L'unité de base de l'analyse est la **scène** ou la séquence dans le film. Chaque scène est analysée selon sept dimensions :

| Champ | Description |
|---|---|
| `scene_number` | Numéro de scène |
| `scene_heading` | Intitulé de la scène |
| `characters` | Personnages présents |
| `action_film` | Résumé condensé de la scène |
| `source_principale` | L'Iliade / Le Cycle Troyen / Héritage Gréco-Romain / Adaptation Cinéma |
| `reference_iliade` | Chant précis si applicable |
| `explication_litteraire` | Analyse de la généalogie littéraire |

Les sources sont classées en trois niveaux de fiabilité :

- **Niveau 1** — Homère : texte vérifiable, ton affirmatif
- **Niveau 2** — Tradition antique majeure (Virgile, Ovide, tragiques) : référence indicative fiable
- **Niveau 3** — Sources perdues, fragmentaires ou obscures : marquées "à vérifier" pour la phase 2

Le détail de la méthode est documenté dans [`rapport_methodologique.md`](rapport_methodologique.md).

---

## Visualisations prévues

Quatre visualisations sont envisagées pour la web app :

1. **Bandeau scène par scène** — frise horizontale par film, colorée selon la source, avec survol interactif. Visualisation principale.
2. **Carte du Cycle Troyen** — diagramme montrant quelle portion du cycle chaque film couvre.
3. **Fiches personnages** — comparaison Homère vs film pour 6 à 8 personnages clés (Achille, Hector, Hélène, Ulysse, etc.).
4. **Comparateur de films** — tableau ou radar sur quelques axes analytiques.

---

## Identité visuelle

- Palette sombre, codée par source : terracotta/ocre pour Homère, or pour le Cycle Troyen, ardoise bleue pour la tradition antique élargie, gris pour l'invention pure.
- Typographie : serif élégante pour les titres, sans-serif sobre pour les données.
- Ton : data essay. Texte court, visualisations au centre.

---

## Crédits et sources

- *Iliade* et *Odyssée* d'Homère : domaine public, traductions de référence consultables sur [Perseus Digital Library](http://www.perseus.tufts.edu/).
- Cycle Troyen et tradition antique : sources documentées dans le rapport méthodologique.
- Scripts des films : utilisés pour l'analyse, droits respectifs aux ayants droit.
- Le projet n'a pas de visée commerciale et s'inscrit dans une démarche éditoriale et pédagogique.

---

## À propos

Projet personnel à l'intersection du data-journalisme, de la culture antique et de la visualisation de données. Conçu pour rendre lisible la généalogie littéraire des grandes adaptations homériques au cinéma.
