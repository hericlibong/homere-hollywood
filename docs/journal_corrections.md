# Journal des corrections - Phase 5

Ce journal trace les corrections appliquées au corpus enrichi.

Fichier de référence conservé intact :

- `output/troy_true_or_false_all_scenes.json`

Fichier de travail enrichi :

- `output/troy_true_or_false_all_scenes_enriched.json`

Fichiers d'appui :

- `output/troy_true_or_false_all_scenes_tagged_draft.json`
- `output/audit_degre_fidelite.csv`
- `output/audit_corrections_phase5.csv`
- `docs/priorites_corrections_phase5.md`
- `docs/taxonomie_sources_et_fidelite.md`
- `docs/verification_motifs_majeurs.md`
- `docs/contradictions_majeures.md`

---

## Règles de correction

- Ne jamais écraser le JSON de référence.
- Conserver tous les champs existants.
- Ajouter ou modifier seulement les champs justifiés par les audits.
- Tracer chaque correction éditoriale significative.
- Distinguer les corrections structurelles des corrections d'analyse littéraire.

---

## Lot 5.1 - Enrichissement structurel

Date : 2026-04-29.

Statut : appliqué.

Fichier modifié : `output/troy_true_or_false_all_scenes_enriched.json`.

Type : ajout de champ.

Champ ajouté : `degre_fidelite`.

Source de la correction : `output/troy_true_or_false_all_scenes_tagged_draft.json`, généré en Phase 4 à partir de la taxonomie documentée.

Ancienne situation :

- Le fichier de référence contenait 7 champs.
- L'origine du matériau et le rapport du film aux sources étaient mélangés dans `source_principale`.

Nouvelle situation :

- Le fichier enrichi conserve les champs existants.
- Chaque scène possède maintenant un champ `degre_fidelite`.
- Les valeurs autorisées sont `1`, `2`, `3`, `4`.

Validation :

- Nombre de scènes : 202.
- Valeurs invalides de `degre_fidelite` : 0.
- Traçabilité détaillée : `output/audit_corrections_phase5.csv`.

Répartition provisoire :

| Degré | Libellé | Nombre de scènes |
|---|---:|---:|
| 1 | Reprise fidèle | 43 |
| 2 | Déplacement | 24 |
| 3 | Invention sur fond emprunté | 83 |
| 4 | Invention contradictoire | 52 |

Remarque :

Ce lot ne valide pas définitivement les 202 décisions. Il matérialise le brouillon contrôlable. Les scènes marquées `a_relire = True` dans `output/audit_degre_fidelite.csv` restent à arbitrer.

### Traçabilité du lot 5.1

Le fichier `output/audit_corrections_phase5.csv` décrit chaque ajout de `degre_fidelite` avec les colonnes suivantes :

| Colonne | Rôle |
|---|---|
| `scene` | numéro de scène concerné |
| `champ_modifie` | champ ajouté ou modifié |
| `ancienne_valeur` | valeur précédente, ou champ absent |
| `nouvelle_valeur` | nouvelle valeur appliquée |
| `justification` | raison éditoriale ou méthodologique |
| `source_documentaire` | document ou audit qui justifie la correction |

---

## Lots éditoriaux à venir

## Lot 5.2 - Arbitrage des anomalies Phase 6

Date : 2026-04-29.

Statut : appliqué.

Fichier modifié : `output/troy_true_or_false_all_scenes_enriched.json`.

Corrections tracées dans : `output/audit_corrections_phase5.csv`.

| Scène | Champ modifié | Ancienne valeur | Nouvelle valeur | Justification |
|---:|---|---|---|---|
| 104 | `reference_iliade` | `Chant VII` | valeur vide | La source principale reste `Héritage Gréco-Romain`. Le Chant VII est conservé dans l'explication littéraire comme contexte et nuance, non comme référence principale. |
| 113 | `reference_iliade` | valeur vide | `Formule épique homérique` | Convention éditoriale : les formules homériques sans scène précise restent classées `L'Iliade`, mais avec une référence non-numérique plutôt qu'un chant. |

Fichiers de contrôle remis en cohérence :

- `output/audit_degre_fidelite.csv`
- `output/quality_report.md`
- `output/statistiques_taxonomie.json`

---

## Lot 5.3 - Révision des contradictions classées `Adaptation Cinéma`

Date : 2026-04-29.

Statut : appliqué.

Objectif : revoir toutes les scènes où `degre_fidelite = 4` et `source_principale = Adaptation Cinéma`.

Fichier de revue : `output/audit_source_principale_phase5.csv`.

Résultat :

- 26 scènes revues.
- 7 scènes changent de `source_principale`.
- 3 scènes reçoivent aussi une `reference_iliade`.
- Les autres scènes restent `Adaptation Cinéma`, avec justification dans l'audit.

Corrections appliquées :

| Scène | Champ | Ancienne valeur | Nouvelle valeur | Justification courte |
|---:|---|---|---|---|
| 94 | `source_principale` | `Adaptation Cinéma` | `L'Iliade` | inversion directe du duel Paris/Ménélas et de la rupture du pacte |
| 94 | `reference_iliade` | valeur vide | `Chant III, Chant IV` | chants concernés par le duel et la reprise du combat |
| 98 | `source_principale` | `Adaptation Cinéma` | `L'Iliade` | Ajax et Hector comme matériau iliadique majeur |
| 98 | `reference_iliade` | valeur vide | `Chant VII, Chant XVII` | duel Ajax/Hector et rôle d'Ajax dans le poème |
| 181 | `source_principale` | `Adaptation Cinéma` | `Le Cycle Troyen` | Achille actif pendant le sac, contradiction de chronologie cyclique |
| 189 | `source_principale` | `Adaptation Cinéma` | `Le Cycle Troyen` | Achille actif pendant le sac |
| 195 | `source_principale` | `Adaptation Cinéma` | `Le Cycle Troyen` | Achille actif dans le palais pendant le sac |
| 198 | `source_principale` | `Adaptation Cinéma` | `Héritage Gréco-Romain` | mort d'Agamemnon déplacée depuis la tradition du retour |
| 199 | `source_principale` | `Adaptation Cinéma` | `Le Cycle Troyen` | mort d'Achille par Pâris, tradition post-homérique |
| 202 | `source_principale` | `Adaptation Cinéma` | `Héritage Gréco-Romain` | Énée, survivance troyenne et traditions postérieures |

Fichiers remis en cohérence :

- `output/troy_true_or_false_all_scenes_enriched.json`
- `output/audit_degre_fidelite.csv`
- `output/audit_corrections_phase5.csv`
- `output/statistiques_taxonomie.json`

---

### Révision ultérieure de la scène 94

Date : 2026-04-30.

Statut : appliqué.

Après relecture éditoriale, la scène 94 est finalement ramenée à `Adaptation Cinéma`.

Justification : même si le duel Pâris/Ménélas et la rupture du pacte renvoient aux Chants III et IV de l'Iliade, la scène enchaîne trop d'inventions scénaristiques pour que `L'Iliade` reste la source principale : Pâris aux pieds d'Hector, Hector tuant Ménélas, Agamemnon exploitant immédiatement la rupture, l'Épée de Troie et la fuite vers les murs. Les chants iliadiques restent donc dans `explication_litteraire` comme contexte comparatif.

Corrections appliquées :

| Scène | Champ | Ancienne valeur | Nouvelle valeur |
|---:|---|---|---|
| 94 | `source_principale` | `L'Iliade` | `Adaptation Cinéma` |
| 94 | `reference_iliade` | `Chant III, Chant IV` | valeur vide |

Fichiers remis en cohérence :

- `output/troy_true_or_false_all_scenes_enriched.json`
- `output/audit_degre_fidelite.csv`
- `output/audit_references_iliade_phase5.csv`
- `output/audit_source_principale_phase5.csv`
- `output/audit_corrections_phase5.csv`
- `output/statistiques_taxonomie.json`

---

### Révision ultérieure de la scène 98

Date : 2026-04-30.

Statut : appliqué.

Après relecture éditoriale, la scène 98 est ramenée à `Adaptation Cinéma`.

Justification : Ajax et Hector sont bien des figures iliadiques, et les Chants VII et XVII restent utiles dans l'explication pour mesurer l'écart. Mais la scène met en place une mort d'Ajax par Hector, c'est-à-dire une invention filmique structurante qui contredit précisément la tradition. L'Iliade fonctionne donc comme contrepoint, non comme source principale de la scène.

Corrections appliquées :

| Scène | Champ | Ancienne valeur | Nouvelle valeur |
|---:|---|---|---|
| 98 | `source_principale` | `L'Iliade` | `Adaptation Cinéma` |
| 98 | `reference_iliade` | `Chant VII, Chant XVII` | valeur vide |

Fichiers remis en cohérence :

- `output/troy_true_or_false_all_scenes_enriched.json`
- `output/audit_degre_fidelite.csv`
- `output/audit_references_iliade_phase5.csv`
- `output/audit_source_principale_phase5.csv`
- `output/audit_corrections_phase5.csv`
- `output/statistiques_taxonomie.json`

---

### Révision ultérieure de la scène 118

Date : 2026-04-30.

Statut : appliqué.

La scène 118 a été corrigée après vérification du contenu réel du film.

Corrections appliquées :

| Scène | Champ | Ancienne valeur | Nouvelle valeur |
|---:|---|---|---|
| 118 | `scene_heading` | `INT. ACHILLES' WARSHIP - DAY` | `INT. ACHILLES' TENT - DAY` |
| 118 | `action_film` | scène située dans la cabine du navire, avec prophétie explicitement évoquée et bruits de guerre | scène située dans la tente d'Achille, dans son lit, où Briséis demande s'il pourrait renoncer à la guerre |
| 118 | `degre_fidelite` | `4` | `2` |
| 118 | `explication_litteraire` | prophétie présentée comme explicitement formulée dans la scène | prophétie du Chant IX présentée comme sous-texte littéraire |

Justification : la scène conserve le sous-texte du choix d'Achille au Chant IX, mais elle le déplace dans une scène intime avec Briséis. Elle ne contredit pas frontalement la source ; elle relève donc plutôt du déplacement.

Fichiers remis en cohérence :

- `output/troy_true_or_false_all_scenes_enriched.json`
- `output/audit_degre_fidelite.csv`
- `output/audit_references_iliade_phase5.csv`
- `output/audit_corrections_phase5.csv`
- `output/statistiques_taxonomie.json`

---

### Révision ultérieure de la scène 121

Date : 2026-04-30.

Statut : appliqué.

La scène 121 a été corrigée sur deux points : le détail filmique de la reconnaissance de Patrocle et la précision philologique du Chant XVI.

Corrections appliquées :

| Scène | Champ | Correction |
|---:|---|---|
| 121 | `action_film` | suppression du collier de coquillages ; Hector reconnaît Patrocle en retirant le casque |
| 121 | `explication_litteraire` | suppression du collier comme révélateur ; ajout de l'autorisation d'Achille, de sa recommandation de ne pas poursuivre jusqu'aux murs de Troie, et du rôle d'Apollon puis d'Euphorbe avant le coup final d'Hector |

Justification : la scène reste structurée par le Chant XVI et conserve `degre_fidelite = 4`, mais l'explication devait mieux faire apparaître l'inversion filmique : dans l'Iliade, Achille autorise Patrocle à porter son armure et Hector sait qu'il tue Patrocle ; le film transforme ces deux points.

Fichiers remis en cohérence :

- `output/troy_true_or_false_all_scenes_enriched.json`
- `output/audit_degre_fidelite.csv`
- `output/audit_references_iliade_phase5.csv`
- `output/audit_corrections_phase5.csv`

---

### Révision ultérieure de la scène 122

Date : 2026-04-30.

Statut : appliqué.

La scène 122 a été corrigée pour ne pas attribuer au film des éléments qui relèvent du modèle homérique.

Corrections appliquées :

| Scène | Champ | Correction |
|---:|---|---|
| 122 | `action_film` | retrait de la cendre, de la marche dans la mer et du combat contre les vagues |
| 122 | `explication_litteraire` | les cendres et la plainte sont désormais présentées comme éléments du Chant XVIII, non comme action filmique |

Justification : dans l'Iliade, Achille se couvre de cendre, se couche dans la poussière et pousse une plainte entendue par Thétis. Le film conserve l'annonce de la mort de Patrocle mais la transforme en choc violent autour d'Eudore et Briséis. La référence `Chant XVIII` reste correcte.

Fichiers remis en cohérence :

- `output/troy_true_or_false_all_scenes_enriched.json`
- `output/audit_degre_fidelite.csv`
- `output/audit_references_iliade_phase5.csv`
- `output/audit_corrections_phase5.csv`

---

## Lot 5.4 - Références iliadiques trop vagues ou multiples

Date : 2026-04-30.

Statut : traité.

Objectif : examiner les scènes classées `L'Iliade` dont `reference_iliade` était multiple, spéciale, ou associée à un `degre_fidelite = 4`.

Fichier de revue : `output/audit_references_iliade_phase5.csv`.

Décisions :

| Scènes | Décision |
|---|---|
| 29, 70, 72, 76, 82, 103, 107, 113, 115, 140, 148 | garder tel quel |
| 94, 98 | changer de convention : retour à `Adaptation Cinéma`, `reference_iliade` vide |
| 118 | corriger `action_film`, `explication_litteraire`, et passer `degre_fidelite` de `4` à `2` |
| 121, 122 | corriger `action_film` et `explication_litteraire`, référence conservée |
| 125 | reste à traiter dans le lot "incertitudes / rites funéraires", car le problème principal n'est pas la référence mais l'attribution d'éléments rituels au film ou au commentaire littéraire |

Conclusion : les références iliadiques trop vagues ou multiples ont été arbitrées. Les références conservées le sont parce que le ou les chants indiqués correspondent au motif structurant de la scène, tandis que les nuances secondaires sont portées par `explication_litteraire`.

---

## Lot 5.5 - Audit des incertitudes explicites

Date : 2026-04-30.

Statut : audit effectué, corrections à appliquer par sous-lots.

Objectif : traiter les formulations explicites d'incertitude dans `explication_litteraire` sans relire manuellement toutes les scènes.

Fichiers créés :

- `output/audit_incertitudes_explicit_phase5.csv`
- `docs/audit_incertitudes_explicit_phase5.md`

Résultat :

| Catégorie | Action | Nombre |
|---|---|---:|
| `sources_perdues_fragmentaires` | conserver la prudence formulée | 32 |
| `noms_secondaires` | transférer au lot noms propres | 15 |
| `incertitude_generale` | revue ciblée | 7 |
| `geographie_litteraire` | vérifier par table des sources ou transférer | 2 |

Conclusion : le chantier ne nécessite pas 56 relectures manuelles. Les règles déjà construites réduisent l'effort immédiat à 7 scènes de revue ciblée, plus le lot séparé des noms propres secondaires.

### Sous-lot `incertitude_generale`

Date : 2026-04-30.

Statut : appliqué.

Scènes traitées : 5, 67, 112, 142, 148, 152, 171.

Corrections appliquées :

| Scène | Action |
|---:|---|
| 5 | suppression de `référence à confirmer` ; l'invulnérabilité d'Achille est formulée comme tradition post-homérique développée par Stace |
| 67 | remplacement de `semble défier` par une formulation interprétative assumée |
| 112 | remplacement de `semble pouvoir tuer` par une formulation plus nette |
| 171 | suppression de `point à vérifier` ; la divergence Poséidon / Athéna / Ulysse / Sinon est formulée comme variation de traditions |
| 142, 148, 152 | aucune correction nécessaire dans le JSON actuel |

Fichiers remis en cohérence :

- `output/troy_true_or_false_all_scenes_enriched.json`
- `output/audit_incertitudes_explicit_phase5.csv`
- `output/audit_incertitudes_signalees_phase5.csv`
- `output/audit_degre_fidelite.csv`
- `output/audit_corrections_phase5.csv`

### Sous-lot noms et lieux secondaires

Date : 2026-04-30.

Statut : appliqué.

Règle utilisée : quand un nom ou lieu secondaire ne change ni `source_principale`, ni `degre_fidelite`, ni l'interprétation de la scène, on ne relance pas une recherche. On formule sobrement et on clôt.

Scènes corrigées : 1, 6, 8, 10, 12, 40, 44, 59, 61, 98, 103, 108, 116, 132, 168, 193, 202.

Exemples de décisions :

- Boagrius : nom grec à résonance géographique, mais pas champion homérique ; le personnage et le duel sont filmiques.
- Triopas : nom mythologique attesté, mais le roi du prologue appartient au dispositif scénaristique.
- Tecton, Eudore, Lysander, Archeptolemus, Selepius : noms secondaires ou graphies de script, non structurants.
- Larissa, Scamandre, Ida : repères géographiques utiles mais non bloquants pour la taxonomie.

Résultat : 17 formulations `à vérifier` ou équivalentes ont été retirées ou stabilisées. Les `à vérifier` restants concernent surtout des sources perdues ou fragmentaires, où la prudence est normale.

Fichiers remis en cohérence :

- `output/troy_true_or_false_all_scenes_enriched.json`
- `output/audit_corrections_phase5.csv`
- `output/audit_incertitudes_explicit_phase5.csv`
- `output/audit_incertitudes_signalees_phase5.csv`
- `output/audit_a_verifier_restants_phase5.csv`

### Suppressions éditoriales pour la dataviz

Date : 2026-05-02.

Statut : appliqué.

| Scène | Action | Justification |
|---:|---|---|
| 0 | supprimée du corpus enrichi | ouverture/titre de scénario sans contenu narratif antique |
| 2 | supprimée du corpus enrichi | micro-transition sans enjeu littéraire propre |
| 3 | supprimée du corpus enrichi | prolongement de la transition du messager, sans scène littéraire autonome |
| 7 | supprimée du corpus enrichi | transition maritime vers Sparte ; les enjeux Pâris/Hélène/Sparte sont traités dans les scènes suivantes |
| 13 | supprimée du corpus enrichi | transition maritime vers Troie ; le départ d'Hélène avec Pâris est traité dans les scènes adjacentes |
| 16 | supprimée du corpus enrichi | plan court de constat de disparition d'Hélène, redondant avec l'arc Pâris/Hélène/Sparte |
| 19 | supprimée du corpus enrichi | arrivée de Ménélas à Mycènes, liaison avant la décision de guerre |
| 24 | supprimée du corpus enrichi | transition visuelle vers Thétis ; le motif des deux destins est traité dans la scène suivante |
| 27 | supprimée du corpus enrichi | plan de navire d'Achille, redondant avec le départ vers Troie |
| 43 | supprimée du corpus enrichi | micro-transition de Tecton vers l'armurerie, sans enjeu littéraire autonome |
| 53 | supprimée du corpus enrichi | déplacement militaire vers la plage, sans motif autonome |
| 106 | supprimée du corpus enrichi | transition atmosphérique du camp grec après la défaite |
| 111 | supprimée du corpus enrichi | transition nocturne avant Achille et Briséis |
| 119 | supprimée du corpus enrichi | alerte de camp préparant l'attaque troyenne |
| 134 | supprimée du corpus enrichi | approche d'Achille vers Troie avant le duel, redondante avec les scènes du duel |
| 154 | supprimée du corpus enrichi | calme nocturne préparant la visite de Priam |
| 156 | supprimée du corpus enrichi | isolement visuel de Briséis sur la plage, sans scène littéraire autonome |
| 159 | supprimée du corpus enrichi | attente de Priam, transition interne à la restitution du corps |
| 175 | supprimée du corpus enrichi | neutralisation tactique de gardes, micro-liaison pendant l'infiltration grecque |
| 177 | supprimée du corpus enrichi | Briséis observe un signe visuel de la chute, redondant avec l'arc du sac |
| 180 | supprimée du corpus enrichi | destruction de l'armurerie, détail tactique sans motif antique autonome |
| 197 | supprimée du corpus enrichi | transition vers la résolution Achille / Agamemnon / Briséis |

Résultat : le corpus enrichi contient désormais 179 scènes exploitables pour la dataviz.

### Révision scène par scène - scène 8

Date : 2026-05-02.

Statut : appliqué.

| Scène | Champ | Correction |
|---:|---|---|
| 8 | `action_film` | suppression de la mention des servantes menées par Polydora ; ajout de `roi de Sparte` pour Ménélas ; simplification de la mention d'Achille sans détail sur Pélée l'Argonaute |
| 8 | `explication_litteraire` | suppression du développement sur Pélée l'Argonaute et Polydora ; conservation des *Chants Cypriens* pour l'épisode et recentrage du contraste moral sur l'*Iliade* III, où Hélène garde le souvenir de Ménélas et reconnaît sa valeur face à Pâris |

Justification : ces détails surchargeaient l'explication et n'étaient pas assez perceptibles ou utiles pour la lecture littéraire de la scène. Le point fort à conserver est le contraste entre le Ménélas filmique, grossier et aviné, et le Ménélas de l'*Iliade* III : premier mari regretté par Hélène et guerrier reconnu face à Pâris.

### Révision scène par scène - scène 9

Date : 2026-05-02.

Statut : lien littéraire noté, JSON inchangé.

| Scène | Champ | Correction |
|---:|---|---|
| 9 | `liens_litteraires` futur | ajout d'un lien à prévoir sur `le duel du Chant III`, réutilisant l'extrait du Chant III où Hélène oppose Pâris à Ménélas après le duel |

Justification : l'explication existante est conservée. Le lien enrichira la lecture sans modifier l'analyse.

### Révision scène par scène - scène 10

Date : 2026-05-02.

Statut : appliqué.

| Scène | Champ | Correction |
|---:|---|---|
| 10 | `action_film` | remplacement de `Polydora` par `une servante` |
| 10 | `explication_litteraire` | suppression de la phrase sur Polydora comme nom homérique porté par une fille de Pélée |

Justification : dans le film, la servante n'est pas nommée de manière utile pour la lecture. La précision sur Polydora ajoutait un bruit philologique sans enjeu narratif.

### Révision scène par scène - scène 11

Date : 2026-05-02.

Statut : appliqué.

| Scène | Champ | Correction |
|---:|---|---|
| 11 | `degre_fidelite` | passage de `2` à `3` |
| 11 | `explication_litteraire` | réécriture pour clarifier le fil : motif cyclique du départ d'Hélène avec Pâris, scène intime inventée, Hélène homérique déjà à Troie au Chant III |
| 11 | `liens_litteraires` futur | ajout d'un lien interne à prévoir sur `Propontide` |

Justification : la scène ne déplace pas une scène antique précise ; elle invente une scène amoureuse privée sur le fond cyclique du départ d'Hélène avec Pâris. Elle relève donc mieux de l'invention sur fond emprunté.

### Révision scène par scène - scène 12

Date : 2026-05-02.

Statut : liens littéraires notés, JSON inchangé.

| Scène | Champ | Correction |
|---:|---|---|
| 12 | `liens_litteraires` futur | ajout d'un lien à prévoir sur `Tecton`, avec extrait de l'*Iliade* V sur Phéréclos fils du charpentier Harmôn |
| 12 | `liens_litteraires` futur | ajout d'un lien interne à prévoir sur `Poséidon` |

Justification : le texte de la scène 12 est conservé. Les liens renforceront l'appui documentaire sans alourdir l'explication.

### Révision scène par scène - scène 14

Date : 2026-05-02.

Statut : appliqué.

| Scène | Champ | Correction |
|---:|---|---|
| 14 | `degre_fidelite` | passage de `3` à `4` |
| 14 | `explication_litteraire` | suppression du développement secondaire sur le lion sculpté ; recentrage sur Hector absent du voyage de Sparte et sur le dialogue fraternel incompatible avec la tradition de l'exposition de Pâris |
| 14 | `liens_litteraires` futur | ajout d'un lien à prévoir vers Apollodore et Hygin sur la prophétie de ruine, l'exposition de Pâris et son enfance à l'écart |

Justification : la scène paraît d'abord seulement familiale, mais elle efface un point central du destin de Troie : dans une tradition importante, Pâris n'a pas grandi normalement auprès d'Hector après la prophétie annonçant la ruine de la cité. Elle relève donc de l'invention contradictoire.

### Révision scène par scène - scène 15

Date : 2026-05-02.

Statut : appliqué.

| Scène | Champ | Correction |
|---:|---|---|
| 15 | `explication_litteraire` | réécriture resserrée pour éviter la répétition avec la scène 14 : maintien du noyau cyclique, invention du témoin Hector, transformation du départ d'Hélène en crise familiale et politique |

Justification : la classification reste inchangée (`Le Cycle Troyen` + degré 4). La scène doit rester compréhensible seule dans la dataviz, tout en évitant de répéter l'analyse de l'enfance de Pâris déjà portée par la scène 14.

### Révision scène par scène - scène 17

Date : 2026-05-03.

Statut : appliqué.

| Scène | Champ | Correction |
|---:|---|---|
| 17 | `characters` | suppression de `POLYDORA` et `HIPPASUS` ; conservation de `MENELAUS` et `FISHERMAN` |
| 17 | `action_film` | remplacement de Polydora par `une servante` et suppression d'Hippasus |
| 17 | `explication_litteraire` | suppression des développements sur Polydora et Hippasus |

Justification : ces noms ajoutaient un bruit inutile dans la scène et dans l'analyse. Le coeur de la scène reste la réaction inventée de Ménélas à partir du départ cyclique d'Hélène avec Pâris.

### Révision scène par scène - scène 18

Date : 2026-05-03.

Statut : appliqué.

| Scène | Champ | Correction |
|---:|---|---|
| 18 | `degre_fidelite` | passage de `3` à `4` |
| 18 | `explication_litteraire` | recentrage sur l'invention du retour de Sparte avec Hector ; suppression du renvoi au Chant VI ; maintien du contraste Hector/Pâris au Chant III et de la responsabilité tragique donnée à Hector |
| 18 | `liens_litteraires` futur | ajout d'un lien à prévoir sur le reproche d'Hector à Pâris dans l'*Iliade*, Chant III |

Justification : la scène prolonge l'invention contradictoire de l'arc du bateau. Le matériau homérique utile est le reproche d'Hector à Pâris, mais ce reproche se situe pendant la guerre, non lors du retour de Sparte.

### Révision scène par scène - scène 22

Date : 2026-05-03.

Statut : appliqué.

| Scène | Champ | Correction |
|---:|---|---|
| 22 | `degre_fidelite` | passage de `2` à `3` |
| 22 | `explication_litteraire` | réécriture pour faire apparaître le motif d'Ulysse qui tente d'éviter Troie, la fausse folie démasquée par Palamède, et le déplacement d'Argos du retour vers le départ |
| 22 | `liens_litteraires` futur | ajout de deux liens à prévoir : Argos dans l'*Odyssée* XVII ; fausse folie d'Ulysse dans les *Chants Cypriens* et chez Apollodore |

Justification : la scène n'est pas un simple déplacement. Elle invente une version douce et cinématographique d'un motif antique important : Ulysse ne veut pas partir pour Troie et tente d'échapper à l'expédition.

### Révision scène par scène - scène 23

Date : 2026-05-03.

Statut : appliqué.

| Scène | Champ | Correction |
|---:|---|---|
| 23 | `explication_litteraire` | réécriture pour recentrer la scène sur Ulysse comme recruteur d'Achille avant Troie, plutôt que sur l'ambassade iliadique du Chant IX |
| 23 | `liens_litteraires` futur | ajout d'un lien à prévoir vers Stace, *Achilléide*, sur le recrutement d'Achille à Scyros par Ulysse |

Justification : la scène n'appartient pas à l'Iliade. Elle invente une version libre du recrutement d'Achille, avec Ulysse comme émissaire rusé qui touche le désir de gloire du héros.

### Sous-lot `Ethiopide` et mort d'Achille

Date : 2026-05-01.

Statut : appliqué.

Règle utilisée : pour l'*Ethiopide*, le texte complet est perdu, mais le résumé de Proclus constitue une référence documentaire exploitable. Les formulations `à vérifier` sont donc supprimées quand elles concernent le point confirmé par ce résumé : Achille meurt après Hector et avant le sac de Troie, tué par Pâris avec l'aide d'Apollon.

Scènes corrigées : 57, 126, 184, 189, 195, 200.

Source documentaire utilisée :

- Proclus, résumé de l'*Ethiopide*, transmis dans la tradition du Cycle épique ; version de contrôle : Theoi Classical Texts Library, `Epic Cycle Fragments`, section `The Aethiopis`.

Résultat : les mentions flottantes du type `Ethiopide, à vérifier` ou `référence à confirmer dans l'Ethiopide` sont remplacées par `d'après le résumé de Proclus de l'Ethiopide`.

### Sous-lot `Chants Cypriens` et scène absente

Date : 2026-05-01.

Statut : appliqué.

Décisions appliquées :

| Scène | Action |
|---:|---|
| 9 | simplification de l'explication : la relation de Pâris et Hélène à Sparte est rattachée directement aux *Chants Cypriens*, sans formule `à vérifier` |
| 165 | suppression de la scène du corpus enrichi, car elle ne fait pas partie du film |

Résultat : l'audit des incertitudes explicites passe à 23 scènes restantes.

### Sous-lot final `à vérifier`

Date : 2026-05-01.

Statut : appliqué.

Règle utilisée : ne pas relire les scènes une par une. Scanner les formulations restantes, vérifier le cadre documentaire quand il est disponible, puis :

- supprimer `à vérifier` quand la source générale est établie ;
- reformuler comme invention ou dramatisation filmique quand le détail précis n'est pas attesté ;
- retirer les précisions inutiles quand elles créent plus de bruit que d'information.

Familles traitées :

| Famille | Scènes | Traitement |
|---|---|---|
| *Chants Cypriens* : Pâris, Hélène, rassemblement grec, départ vers Troie | 11, 13, 15, 16, 19, 20, 21, 22, 26, 28, 32, 34, 39 | suppression des `à vérifier`, maintien du cadre cyclique, détails filmiques nommés comme inventions |
| Cheval et chute de Troie : *Petite Iliade*, *Sac d'Ilion*, *Odyssée* VIII, *Énéide* II | 162, 167, 169, 170, 173, 175, 176, 185, 190, 192 | suppression des `à vérifier`, distinction entre motif antique général et tactique cinématographique |
| Marqueur faible sans enjeu littéraire | 44 | remplacement de `probablement` par une convention éditoriale stable sur la coquille `LSYANDER` |

Source documentaire utilisée :

- Proclus, résumés du Cycle épique, via Theoi Classical Texts Library, `Epic Cycle Fragments`.
- Homère, *Odyssée*, Chant VIII pour la mention du cheval.
- Virgile, *Énéide*, livre II pour le récit développé de la chute de Troie.

Résultat : plus aucune formulation `à vérifier`, `à confirmer` ou équivalente ne reste dans `explication_litteraire`. Les marqueurs faibles restants ont aussi été contrôlés.

---

### Lot 5.6 - Contradictions confirmées

Objectif : stabiliser les scènes où le degré 4 est solidement confirmé par la Phase 2.

Familles candidates :

- mort de Ménélas par Hector ;
- mort d'Ajax par Hector ;
- Patrocle, armure d'Achille et erreur d'identification ;
- Agamemnon tué à Troie ;
- Achille vivant pendant le sac de Troie ;
- Pâris survivant jusqu'à la fuite finale.

### Lot 5.7 - Scènes composites

Objectif : traiter les scènes où plusieurs couches coexistent.

Scènes candidates :

- scène 104 : trêve funéraire, morts contradictoires, détail des pièces ;
- scène 122 : deuil de Patrocle, Briséis, violence filmique ;
- scène 200 : Briséis, Achille, Pâris, sac de Troie.

### Lot 5.8 - Références littéraires à préciser

Objectif : corriger uniquement les explications qui citent une tradition sans oeuvre ou auteur suffisamment identifié.

Points candidats :

- pièces sur les yeux / obole de Charon ;
- Énée : statut homérique puis amplification virgilienne ;
- traditions cycliques connues par résumés et fragments.

### Lot 5.9 - Attributions à ne pas modifier sans arbitrage

Objectif : garder de côté les cas où la correction serait interprétative.

Scènes candidates :

- scène 104 : `source_principale` actuellement `Héritage Gréco-Romain` avec `reference_iliade = Chant VII`.
- scène 113 : `source_principale = L'Iliade`, mais `reference_iliade` vide, car il s'agit d'une formule épique et non d'un passage précis.

Statut après Phase 6 :

| Scène | Problème constaté | Statut |
|---:|---|---|
| 104 | `source_principale = Héritage Gréco-Romain` avec `reference_iliade = Chant VII` | arbitré : référence supprimée, nuance gardée dans l'explication |
| 113 | `source_principale = L'Iliade` mais `reference_iliade` vide | arbitré : `reference_iliade = Formule épique homérique` |

Ces deux cas sont notés comme anomalies éditoriales dans `output/quality_report.md` et `output/statistiques_taxonomie.json`.

---

### Révision scène par scène - scène 25

Date : 2026-05-03.

Statut : lien littéraire noté, JSON inchangé.

| Scène | Élément | Décision | Justification |
|---:|---|---|---|
| 25 | futur lien intégré | ajouter un lien sur `Achille rapporte que sa mère Thétis lui a annoncé deux sorts` | l'analyse littéraire est conservée ; le lien documente le passage central de l'Iliade, Chant IX, où Achille rapporte lui-même les deux destinées annoncées par Thétis |

Source documentaire :

- Homère, *Iliade*, Chant IX, v. 410-416 environ, traduction Leconte de Lisle, 1866.

Note éditoriale :

Dans l'Iliade, Thétis ne prononce pas directement cette prophétie dans la scène : Achille la rapporte. Le film transforme donc une parole rapportée en dialogue direct entre Achille et Thétis.

---

### Révision scène par scène - scène 26

Date : 2026-05-03.

Statut : correction appliquée.

| Scène | Champ | Ancienne valeur | Nouvelle valeur | Justification |
|---:|---|---|---|---|
| 26 | `degre_fidelite` | 2 | 3 | la scène ne déplace pas seulement un épisode précis : elle condense et invente une transition spectaculaire sur fond de matière cyclique |
| 26 | `explication_litteraire` | lecture centrée sur le départ collectif, le Catalogue des vaisseaux et la voile noire | lecture centrée sur la compression des péripéties pré-troyennes : Aulis, Mysie, tempête, second rassemblement, Artémis et Iphigénie | transformer une scène de transition en faux positif utile pour le storytelling |
| 26 | futur lien intégré | non renseigné | ajout d'un lien sur les péripéties des *Chants Cypriens* avant le vrai départ | permettre à l'interface d'expliquer ce que le film saute entre la décision de partir et l'armada en mer |

Source documentaire :

- *Chants Cypriens*, résumé de Proclus, via Theoi Classical Texts Library, *Epic Cycle Fragments*.

---

### Révision scène par scène - scène 28

Date : 2026-05-03.

Statut : liens littéraires notés, JSON inchangé.

| Scène | Élément | Décision | Justification |
|---:|---|---|---|
| 28 | futur lien intégré | ajouter un lien sur l'arrivée d'Hélène à Troie dans les *Chants Cypriens* | confirmer que cette arrivée relève du Cycle Troyen et non de l'Iliade |
| 28 | futur lien intégré | ajouter un lien sur Aphrodite protégeant Pâris et contraignant Hélène au Chant III de l'Iliade | justifier la pertinence littéraire d'Aphrodite dans le décor divin de Troie |

Sources documentaires :

- *Chants Cypriens*, résumé de Proclus, via Theoi Classical Texts Library, *Epic Cycle Fragments*.
- Homère, *Iliade*, Chant III, traduction Leconte de Lisle, 1866.

Note éditoriale :

La scène reste conservée : elle n'est pas homérique au sens strict, mais elle sert à visualiser un moment pré-iliadique important et à ouvrir vers les dieux protecteurs du conflit.

---

### Révision scène par scène - scène 29

Date : 2026-05-03.

Statut : liens d'index notés, JSON inchangé.

| Scène | Élément | Décision | Justification |
|---:|---|---|---|
| 29 | futur lien d'index interne | ajouter un lien sur `Andromaque` | première apparition importante du personnage ; renvoi utile vers son rôle homérique et les adieux du Chant VI |
| 29 | futur lien d'index interne | ajouter un lien sur `Briséis` | la scène introduit l'invention contradictoire majeure du film autour de Briséis |

Note éditoriale :

Classification et analyse conservées : la scène est correctement traitée comme matériau iliadique déplacé et recomposé avec une contradiction forte autour de Briséis.

---

### Révision scène par scène - scène 30

Date : 2026-05-03.

Statut : lien littéraire noté, JSON inchangé.

| Scène | Élément | Décision | Justification |
|---:|---|---|---|
| 30 | futur lien intégré | ajouter un lien sur `Priam y apparaît souvent digne et pieux, surtout au Chant XXIV` | la référence à un chant précis doit être accompagnée d'un extrait ; le passage de la libation et de la prière de Priam confirme le profil pieux du personnage |
| 30 | futur lien intégré | ajouter un lien sur `Apollon protège les Troyens, soutient Hector et intervient contre les Achéens, notamment dès le Chant I` | la seconde référence précise de l'analyse devait aussi être documentée ; le Chant I montre Apollon envoyant la peste dans le camp achéen |

Source documentaire :

- Homère, *Iliade*, Chant XXIV, traduction Leconte de Lisle, 1866.
- Homère, *Iliade*, Chant I, traduction Leconte de Lisle, 1866.

Note éditoriale :

Règle confirmée pour la suite : quand une explication cite un chant précis, soit on ajoute une pastille/lien avec extrait, soit on simplifie la phrase pour éviter une référence non documentée.

À prévoir après la révision scène par scène : passage global sur le corpus pour repérer toutes les mentions `Chant ...` dans `explication_litteraire` et vérifier qu'elles ont une référence textuelle ou qu'elles sont volontairement simplifiées.
