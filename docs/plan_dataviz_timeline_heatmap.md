# Plan dataviz - Timeline heatmap interactive

Objectif : construire la première visualisation interactive de *Homère & Hollywood* à partir du corpus enrichi de *Troy*.

Référence d'inspiration : *Based on a True True Story?* d'Information is Beautiful. Le modèle inspire le principe général : une frise scène par scène, colorée, interactive, avec détail au survol ou au clic. L'objectif n'est pas de reproduire l'interface à l'identique.

---

## 1. Intention éditoriale

La visualisation doit répondre à une question simple :

> À quel moment *Troy* reprend-il la tradition antique, la déplace-t-il, brode-t-il sur elle ou la contredit-il ?

La timeline doit permettre de voir d'un coup :

- les zones du film proches de l'Iliade ;
- les zones inventées par le scénario ;
- les ruptures mythiques majeures ;
- le basculement du film vers le Cycle Troyen et la chute de Troie.

---

## 2. Adaptation à notre schéma de données

Le modèle Information is Beautiful classe les scènes selon un niveau de vérité : `TRUE`, `TRUE-ISH`, `FALSE-ISH`, `FALSE`, `UNKNOWN`.

Notre corpus ne mesure pas le vrai/faux historique. Il mesure deux axes :

### Axe principal d'affichage : `degre_fidelite`

La couleur principale de la timeline doit venir de `degre_fidelite` :

| Degré | Libellé | Sens dans la dataviz |
|---:|---|---|
| 1 | Reprise fidèle | Le film reprend un motif ou passage identifiable |
| 2 | Déplacement | Le film conserve le matériau mais change contexte, moment ou fonction |
| 3 | Invention sur fond emprunté | Le film invente, mais à partir de motifs ou codes antiques |
| 4 | Invention contradictoire | Le film contredit une donnée majeure de la tradition |

Pourquoi ce choix :

- c'est le meilleur axe pour raconter la liberté du film ;
- il permet de repérer immédiatement les ruptures ;
- il évite de réduire la dataviz à une simple classification par source.

### Axe secondaire : `source_principale`

`source_principale` doit rester visible, mais comme information secondaire :

- dans le panneau de détail ;
- en filtre ;
- éventuellement en bordure, motif ou petit indicateur dans chaque segment ;
- dans une vue complémentaire de matrice.

Valeurs :

- `L'Iliade`
- `Le Cycle Troyen`
- `Héritage Gréco-Romain`
- `Adaptation Cinéma`

---

## 3. Données utilisées

Fichier principal :

`output/viz_timeline_degre_fidelite.json`

Champs utilisés :

| Champ | Usage |
|---|---|
| `scene_number` | Ordre de la timeline |
| `scene_heading` | Titre court au survol ou clic |
| `characters` | Filtres personnages et panneau de détail |
| `source_principale` | Filtre et contexte littéraire |
| `reference_iliade` | Mention précise quand disponible |
| `degre_fidelite` | Couleur principale |
| `libelle_degre` | Libellé public |
| `color_key` / `color` | Palette initiale |
| `action_film` | Colonne "Film" ou résumé |
| `explication_litteraire` | Colonne "Source / analyse" |

Fichiers complémentaires :

- `output/viz_matrix_source_fidelite.json` pour la heatmap source x fidélité.
- `docs/ruptures_mythiques_troy.md` pour les annotations éditoriales.
- `docs/index_personnages_troy.md` pour les filtres personnages.

---

## 4. Forme visuelle attendue

### Vue principale

Une frise horizontale compacte :

- 201 segments, un par scène ;
- largeur proportionnelle égale au départ, car nous n'avons pas encore de durée fiable par scène ;
- ordre strict par `scene_number` ;
- couleur selon `degre_fidelite` ;
- segment actif agrandi ou surligné au survol.

Note : si des timecodes fiables sont ajoutés plus tard, la largeur pourra devenir proportionnelle à la durée.

### Panneau de détail

Au survol :

- affichage léger : numéro de scène, titre, degré, source principale.

Au clic :

- panneau de détail fixe avec :
  - scène ;
  - source principale ;
  - degré de fidélité ;
  - référence iliadique si présente ;
  - personnages ;
  - résumé film ;
  - explication littéraire.

### Images

Pour l'instant, aucun visuel de scène n'est disponible.

Prévoir un emplacement image facultatif :

- si `image_src` existe plus tard, afficher l'image ;
- sinon afficher un bloc sobre avec le titre de scène ou une texture neutre.

Le schéma de données pourra être enrichi plus tard avec :

```json
{
  "image_src": "assets/stills/troy/scene_141.jpg",
  "image_alt": "Achille et Hector avant le duel"
}
```

---

## 5. Interactions prioritaires

### Version 1 obligatoire

- Survol d'un segment : tooltip lisible.
- Clic sur un segment : panneau de détail.
- Légende des 4 degrés.
- Boutons de filtre par degré.
- Boutons précédent / suivant pour naviguer scène par scène.

### Version 1.1 utile

- Filtre par `source_principale`.
- Filtre par personnage principal.
- Bouton "réinitialiser".
- Indication du nombre de scènes visibles après filtre.

### Version ultérieure

- Recherche texte.
- Annotations des grandes ruptures mythiques.
- Passage vers la matrice source x fidélité.
- Comparaison avec d'autres films quand le corpus sera élargi.

---

## 6. Palette proposée

La palette doit être lisible et éviter de copier celle du modèle.

Palette de départ par `degre_fidelite` :

| Degré | Couleur | Usage |
|---:|---|---|
| 1 | `#D6A84F` | reprise fidèle |
| 2 | `#C7743A` | déplacement |
| 3 | `#6E7F80` | invention sur fond emprunté |
| 4 | `#B33A3A` | invention contradictoire |

À vérifier visuellement sur fond clair et fond sombre. La première version peut commencer sur fond clair pour la lisibilité des textes, puis évoluer vers une identité plus sombre si cela sert mieux le projet.

---

## 7. Structure technique proposée

Objectif : app statique simple, facile à versionner.

Structure minimale :

```text
webapp/
  index.html
  styles.css
  app.js
  data/
    viz_timeline_degre_fidelite.json
    viz_matrix_source_fidelite.json
```

Option alternative : garder les données dans `output/` et les charger depuis là pendant le développement. Pour une publication statique, copier les datasets dans `webapp/data/`.

Librairie :

- D3.js pour le rendu de la timeline.
- JavaScript natif pour les filtres et le panneau de détail.

Pas besoin de framework au départ.

---

## 8. Plan de mise en place

### Étape 1 - Préparer le dossier webapp

- [x] Créer `webapp/index.html`.
- [x] Créer `webapp/styles.css`.
- [x] Créer `webapp/app.js`.
- [x] Créer `webapp/data/`.
- [x] Copier `output/viz_timeline_degre_fidelite.json` dans `webapp/data/`.

Critère de sortie :

- la page charge dans le navigateur ;
- le JSON est lisible par le script.

### Étape 2 - Afficher la timeline brute

- [x] Charger les 201 scènes.
- [x] Créer un conteneur horizontal.
- [x] Dessiner un segment par scène.
- [x] Colorer chaque segment par `degre_fidelite`.
- [x] Ajouter une légende.

Critère de sortie :

- la frise complète est visible ;
- les couleurs correspondent aux 4 degrés.

### Étape 3 - Ajouter le survol

- [x] Afficher un tooltip au survol.
- [x] Montrer : scène, heading, source, degré.
- [x] Surligner le segment survolé.
- [x] Gérer le survol clavier si possible.

Critère de sortie :

- l'utilisateur comprend chaque segment sans cliquer.

### Étape 4 - Ajouter le panneau de détail

- [x] Au clic, fixer la scène active.
- [x] Afficher le résumé film.
- [x] Afficher l'explication littéraire.
- [x] Afficher les personnages.
- [x] Ajouter boutons précédent / suivant.

Critère de sortie :

- la timeline devient navigable comme un lecteur scène par scène.

### Étape 5 - Ajouter les filtres

- [x] Filtres par degré.
- [x] Filtres par source principale.
- [x] Réinitialisation.
- [x] Compteur de scènes visibles.

Critère de sortie :

- l'utilisateur peut isoler les contradictions, les reprises fidèles ou les sources.

### Étape 6 - Préparer l'emplacement image

- [x] Ajouter un bloc média dans le panneau de détail.
- [x] Afficher une image si `image_src` existe.
- [x] Afficher un placeholder éditorial sinon.

Critère de sortie :

- les images pourront être ajoutées plus tard sans casser le layout.

### Étape 7 - Vérification

- [ ] Tester desktop.
- [ ] Tester mobile.
- [ ] Vérifier que les textes longs ne débordent pas.
- [ ] Vérifier que les couleurs restent lisibles.
- [x] Vérifier que le JSON se charge correctement depuis un serveur local.

Critère de sortie :

- première version utilisable et montrable.

---

## 9. Ce qu'on ne fait pas en version 1

- Pas de comparaison multi-films.
- Pas de carte complète du Cycle Troyen.
- Pas de galerie d'images tant que les visuels ne sont pas disponibles.
- Pas d'animation complexe.
- Pas de back-end.

La version 1 doit prouver l'expérience centrale : explorer *Troy* scène par scène par degré de fidélité.

---

## 10. Décision recommandée

Commencer par une app statique D3 avec la timeline degré de fidélité comme première vue.

La matrice source x fidélité pourra être ajoutée ensuite comme vue secondaire, mais la première expérience doit rester la frise interactive : c'est la plus proche du film, la plus pédagogique et la plus conforme à l'inspiration envoyée.

