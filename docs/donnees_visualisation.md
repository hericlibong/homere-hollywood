# Données de visualisation

Ce document liste les fichiers déjà préparés pour la future mini web app et précise leur usage.

---

## Fichiers de données disponibles

| Fichier | Format | Usage prévu |
|---|---|---|
| `output/troy_true_or_false_all_scenes_enriched.json` | JSON | Corpus enrichi complet, source principale des vues |
| `output/viz_matrix_source_fidelite.json` | JSON | Heatmap ou matrice `source_principale x degre_fidelite` |
| `output/viz_matrix_source_fidelite.csv` | CSV | Lecture rapide de la matrice |
| `output/viz_timeline_degre_fidelite.json` | JSON | Timeline scène par scène colorée par degré de fidélité |
| `output/viz_timeline_degre_fidelite.csv` | CSV | Lecture rapide de la timeline |
| `output/statistiques_taxonomie.json` | JSON | Statistiques globales, répartition par source et par degré |

---

## Documents éditoriaux exploitables

| Fichier | Usage prévu |
|---|---|
| `docs/ruptures_mythiques_troy.md` | Cartes ou section sur les grandes libertés du film |
| `docs/index_personnages_troy.md` | Fiches personnages et filtres |
| `docs/index_sources_antiques_troy.md` | Section sources antiques |
| `docs/bibliographie_controle.md` | Page ou note de sources |
| `docs/note_methodologique_courte.md` | Encadré méthodologique |
| `docs/synthese_editoriale.md` | Fil narratif général de la web app |

---

## Vues prioritaires

### 1. Matrice source x fidélité

Fichier : `output/viz_matrix_source_fidelite.json`.

Objectif :

- montrer la structure globale du film ;
- faire apparaître les zones d'invention et de contradiction ;
- permettre un clic sur une case pour afficher les scènes correspondantes.

### 2. Timeline par degré de fidélité

Fichier : `output/viz_timeline_degre_fidelite.json`.

Objectif :

- afficher les scènes dans l'ordre du film ;
- colorer chaque scène selon `degre_fidelite` ;
- ouvrir un panneau de détail avec résumé, source, degré et explication littéraire.

### 3. Parcours des ruptures mythiques

Fichier éditorial : `docs/ruptures_mythiques_troy.md`.

Objectif :

- regrouper les scènes en grands thèmes narratifs ;
- éviter une lecture scène par scène trop lourde ;
- servir de support à des cartes éditoriales.

---

## Données à produire plus tard si nécessaire

Ces fichiers ne sont pas indispensables pour commencer la web app, mais pourront être utiles :

- `output/viz_personnages_troy.json` : index machine des personnages et scènes associées.
- `output/viz_sources_antiques_troy.json` : index machine des sources et scènes associées.
- `output/viz_ruptures_mythiques_troy.json` : version structurée des ruptures mythiques.

Pour l'instant, les documents Markdown suffisent pour cadrer le storytelling ; les deux datasets prioritaires sont déjà prêts : matrice et timeline.

