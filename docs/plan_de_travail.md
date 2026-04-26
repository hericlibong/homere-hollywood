# Plan de travail - Consolidation critique de *Troy*

Ce plan part du principe que le fichier de référence actuel est :

`output/troy_true_or_false_all_scenes.json`

Le rapport méthodologique sert de cadre général :

`docs/rapport_methodologique.md`

Objectif : transformer la base existante en corpus critique fiable, vérifiable, enrichi et exploitable, sans refaire une analyse scène par scène depuis zéro.

---

## Principes de travail

- Ne pas régénérer les 202 scènes.
- Travailler par lots thématiques et par motifs, pas scène par scène.
- Séparer clairement :
  - l'origine du matériau : `source_principale`
  - le rapport du film aux sources : `degre_fidelite`
  - le niveau de certitude documentaire : à définir après vérification.
- Distinguer les sources primaires conservées, les sources perdues connues par résumé, les traditions tardives et les hypothèses.
- Toute correction du JSON doit être justifiée par une source ou par une règle éditoriale explicite.

---

## Phase 0 - Préparer l'environnement documentaire

But : créer une base de vérité avant d'ajouter de nouveaux tags au corpus.

Critère de sortie : les sources antiques utiles au projet sont identifiées, classées et reliées aux grands motifs du film.

- [ ] Créer `docs/corpus_sources.md`.
- [ ] Définir les catégories de sources :
  - [ ] Homère.
  - [ ] Cycle Troyen.
  - [ ] Héritage gréco-romain.
  - [ ] Mythographes et sources tardives.
  - [ ] Géographie et noms propres.
- [ ] Identifier les sources primaires à utiliser en priorité :
  - [ ] Homère, *Iliade*.
  - [ ] Homère, *Odyssée*.
  - [ ] Résumés du Cycle Troyen attribués à Proclus.
  - [ ] Virgile, *Énéide*, surtout livre II.
  - [ ] Eschyle, *Agamemnon*.
  - [ ] Sophocle, *Ajax*.
  - [ ] Euripide, *Troyennes*, *Hécube*, *Andromaque*.
  - [ ] Ovide, *Héroïdes* et passages pertinents des *Métamorphoses*.
  - [ ] Stace, *Achilléide*.
  - [ ] Apollodore, *Bibliothèque*.
  - [ ] Hygin, *Fables*.
  - [ ] Strabon, passages utiles pour les noms propres et lieux.
- [ ] Pour chaque source, renseigner :
  - [ ] auteur ;
  - [ ] oeuvre ;
  - [ ] date approximative ;
  - [ ] statut : conservée, fragmentaire, perdue, tardive ;
  - [ ] niveau de fiabilité éditoriale ;
  - [ ] lien ou fichier local disponible ;
  - [ ] motifs du film concernés.
- [ ] Créer une liste courte des sources réellement mobilisables pour la première passe.

Livrables :

- [ ] `docs/corpus_sources.md`
- [ ] `docs/table_sources_antiques.md`

---

## Phase 1 - Construire un index des motifs au lieu de relire scène par scène

But : organiser les 202 scènes par problèmes littéraires, pour travailler efficacement.

Critère de sortie : chaque grande question du film pointe vers un groupe de scènes candidates.

- [ ] Créer `docs/index_motifs_troy.md`.
- [ ] Extraire depuis le JSON consolidé les scènes contenant les personnages majeurs :
  - [ ] Achille.
  - [ ] Hector.
  - [ ] Agamemnon.
  - [ ] Ménélas.
  - [ ] Pâris.
  - [ ] Hélène.
  - [ ] Briséis.
  - [ ] Patrocle.
  - [ ] Priam.
  - [ ] Ajax.
  - [ ] Ulysse.
  - [ ] Énée.
  - [ ] Andromaque.
- [ ] Créer des groupes de motifs :
  - [ ] querelle Achille / Agamemnon ;
  - [ ] Briséis ;
  - [ ] Pâris, Hélène et Sparte ;
  - [ ] duel Pâris / Ménélas ;
  - [ ] Hector et Andromaque ;
  - [ ] Patrocle et les armes d'Achille ;
  - [ ] mort d'Ajax ;
  - [ ] duel Achille / Hector ;
  - [ ] Priam chez Achille ;
  - [ ] cheval de Troie ;
  - [ ] sac de Troie ;
  - [ ] mort d'Agamemnon ;
  - [ ] survie de Pâris ;
  - [ ] fuite d'Énée ;
  - [ ] inventions géographiques ou politiques du film.
- [ ] Pour chaque motif, lister :
  - [ ] scènes concernées ;
  - [ ] source antique attendue ;
  - [ ] statut probable : reprise, déplacement, invention sur fond, contradiction ;
  - [ ] priorité de vérification.

Livrables :

- [ ] `docs/index_motifs_troy.md`
- [ ] `output/audit_motifs.csv`

---

## Phase 2 - Vérifier d'abord les motifs à fort enjeu

But : contrôler les endroits où une erreur changerait fortement l'interprétation du film.

Critère de sortie : les grands écarts du film sont confirmés, corrigés ou nuancés avant tout tagging global.

### Lot A - Iliade, scènes centrales

- [ ] Vérifier la querelle Achille / Agamemnon avec le Chant I.
- [ ] Vérifier Briséis et Chryséis avec le Chant I.
- [ ] Vérifier le duel Pâris / Ménélas avec le Chant III.
- [ ] Vérifier Hector / Andromaque / Astyanax avec le Chant VI.
- [ ] Vérifier le choix d'Achille entre vie longue et gloire avec le Chant IX.
- [ ] Vérifier Patrocle avec le Chant XVI.
- [ ] Vérifier le deuil d'Achille avec le Chant XVIII.
- [ ] Vérifier le duel Achille / Hector avec le Chant XXII.
- [ ] Vérifier Priam chez Achille avec le Chant XXIV.

### Lot B - Cycle Troyen

- [ ] Vérifier Pâris à Sparte et l'origine de la guerre avec les *Chants Cypriens*.
- [ ] Vérifier les épisodes liés à la mort d'Achille avec l'*Éthiopide*.
- [ ] Vérifier le cheval de Troie avec la *Petite Iliade* et le *Sac d'Ilion*.
- [ ] Vérifier les épisodes de la chute de Troie avec le *Sac d'Ilion*.
- [ ] Noter explicitement que ces sources sont perdues et connues par résumés ou fragments.

### Lot C - Héritage gréco-romain

- [ ] Vérifier le cheval de Troie, Priam et Énée avec Virgile, *Énéide* II.
- [ ] Vérifier Ajax avec Sophocle, *Ajax*.
- [ ] Vérifier Agamemnon avec Eschyle, *Agamemnon*.
- [ ] Vérifier le sort des femmes troyennes avec Euripide.
- [ ] Vérifier les traditions tardives sur Achille avec Stace, *Achilléide*.
- [ ] Vérifier les synthèses mythographiques avec Apollodore et Hygin, en les marquant comme tardives.

Livrables :

- [ ] `docs/verification_motifs_majeurs.md`
- [ ] `output/audit_references_prioritaires.csv`

---

## Phase 3 - Définir et documenter la taxonomie à deux axes

But : intégrer la suggestion de double taxonomie sans mélanger origine et fidélité.

Critère de sortie : les règles de classification sont écrites avant modification du JSON.

- [ ] Créer `docs/taxonomie_sources_et_fidelite.md`.
- [ ] Conserver `source_principale` comme axe d'origine du matériau :
  - [ ] `L'Iliade`
  - [ ] `Le Cycle Troyen`
  - [ ] `Héritage Gréco-Romain`
  - [ ] `Adaptation Cinéma`
- [ ] Ajouter le futur champ `degre_fidelite` :
  - [ ] `1` : reprise fidèle.
  - [ ] `2` : déplacement.
  - [ ] `3` : invention sur fond emprunté.
  - [ ] `4` : invention contradictoire.
- [ ] Écrire les critères d'arbitrage :
  - [ ] quand choisir `1` plutôt que `2` ;
  - [ ] quand choisir `3` plutôt que `4` ;
  - [ ] comment traiter une scène avec matériau antique et contradiction filmique ;
  - [ ] comment traiter les scènes composites.
- [ ] Ajouter des exemples obligatoires :
  - [ ] scène 6, Boagrius : `Adaptation Cinéma` + degré `3`.
  - [ ] scène 8, banquet de Sparte : `Le Cycle Troyen` + degré `4` si Hector à Sparte est confirmé comme invention contradictoire.
  - [ ] scène 98, Ajax : matériau iliadique ou grec majeur + degré `4` si mort par Hector.
  - [ ] scène 141, Achille / Hector : `L'Iliade` + degré `1` ou `2` selon l'écart exact.

Livrables :

- [ ] `docs/taxonomie_sources_et_fidelite.md`

---

## Phase 4 - Tagging assisté semi-manuel, option B

But : ajouter `degre_fidelite` rapidement, mais en gardant le contrôle éditorial.

Critère de sortie : un fichier tagué provisoire existe, avec les contradictions majeures isolées.

- [ ] Créer un script ou traitement local pour générer un brouillon :
  - [ ] lire `output/troy_true_or_false_all_scenes.json` ;
  - [ ] ajouter `degre_fidelite` ;
  - [ ] préserver tous les champs existants ;
  - [ ] écrire un nouveau fichier sans écraser la référence.
- [ ] Appliquer les règles de départ :
  - [ ] `source_principale = "L'Iliade"` et `reference_iliade` non vide : degré `1` par défaut.
  - [ ] `source_principale = "Adaptation Cinéma"` : degré `3` par défaut.
  - [ ] `source_principale = "Le Cycle Troyen"` : degré `1`, `2` ou `3` selon motif.
  - [ ] `source_principale = "Héritage Gréco-Romain"` : degré `1`, `2` ou `3` selon motif.
- [ ] Appliquer une liste explicite de contradictions majeures en degré `4` :
  - [ ] Hector à Sparte.
  - [ ] Briséis princesse troyenne, cousine d'Hector ou prêtresse d'Apollon.
  - [ ] mort de Ménélas par Hector.
  - [ ] mort d'Ajax par Hector.
  - [ ] Agamemnon tué à Troie.
  - [ ] Achille vivant ou actif pendant le sac de Troie.
  - [ ] Achille lié au cheval de Troie.
  - [ ] Pâris survivant jusqu'à la fuite finale.
  - [ ] Hélène fuyant avec les Troyens.
  - [ ] Énée adolescent recevant l'Épée de Troie.
  - [ ] l'Épée de Troie comme objet central du scénario.
- [ ] Produire un audit des scènes en degré `4`.
- [ ] Relire uniquement les scènes ambiguës, pas les 202 scènes.

Livrables :

- [ ] `output/troy_true_or_false_all_scenes_tagged_draft.json`
- [ ] `output/audit_degre_fidelite.csv`
- [ ] `docs/contradictions_majeures.md`

---

## Phase 5 - Correction ciblée du JSON de référence

But : corriger le corpus à partir des audits, sans réécriture massive.

Critère de sortie : une version consolidée enrichie existe et les corrections sont traçables.

- [ ] Créer un fichier de suivi des corrections :
  - [ ] `docs/journal_corrections.md`
- [ ] Pour chaque correction, noter :
  - [ ] scène ;
  - [ ] champ modifié ;
  - [ ] ancienne valeur ;
  - [ ] nouvelle valeur ;
  - [ ] justification ;
  - [ ] source documentaire.
- [ ] Corriger en priorité :
  - [ ] mauvaises attributions à `source_principale` ;
  - [ ] références iliadiques trop vagues ;
  - [ ] contradictions classées comme simples adaptations ;
  - [ ] incertitudes non signalées ;
  - [ ] noms propres secondaires douteux.
- [ ] Créer une version de sortie enrichie :
  - [ ] conserver le fichier original ;
  - [ ] produire une nouvelle version nommée explicitement.

Livrables :

- [ ] `output/troy_true_or_false_all_scenes_enriched.json`
- [ ] `docs/journal_corrections.md`

---

## Phase 6 - Contrôles qualité

But : s'assurer que le corpus reste exploitable techniquement et éditorialement.

Critère de sortie : le corpus enrichi est valide, cohérent et prêt pour visualisation ou publication.

- [ ] Vérifier que le JSON est valide.
- [ ] Vérifier que chaque scène possède les champs attendus.
- [ ] Vérifier que `source_principale` ne contient que les 4 valeurs autorisées.
- [ ] Vérifier que `degre_fidelite` ne contient que `1`, `2`, `3`, `4`.
- [ ] Vérifier les doublons de `scene_number`.
- [ ] Vérifier les scènes manquantes.
- [ ] Vérifier les longueurs extrêmes de `action_film`.
- [ ] Vérifier les champs `reference_iliade` :
  - [ ] vide quand la scène ne reprend pas vraiment l'Iliade ;
  - [ ] précis quand la scène reprend un passage identifiable.
- [ ] Produire un résumé statistique :
  - [ ] nombre de scènes par `source_principale` ;
  - [ ] nombre de scènes par `degre_fidelite` ;
  - [ ] matrice `source_principale` x `degre_fidelite` ;
  - [ ] liste des scènes degré `4`.

Livrables :

- [ ] `output/quality_report.md`
- [ ] `output/statistiques_taxonomie.json`

---

## Phase 7 - Préparer les usages finaux

But : transformer le corpus en support lisible, pédagogique et visualisable.

Critère de sortie : les données peuvent servir à une visualisation, un article, une formation ou une édition critique.

- [ ] Préparer une matrice visuelle `source_principale` x `degre_fidelite`.
- [ ] Préparer une timeline du film colorée par degré de fidélité.
- [ ] Préparer une liste narrative des grandes ruptures mythiques du film.
- [ ] Préparer un index des personnages.
- [ ] Préparer un index des sources antiques.
- [ ] Préparer une bibliographie de contrôle.
- [ ] Préparer une note méthodologique courte pour accompagner le corpus.

Livrables :

- [ ] `docs/synthese_editoriale.md`
- [ ] `docs/bibliographie_controle.md`
- [ ] fichiers de données pour visualisation à définir.

---

## Ordre d'exécution recommandé

1. Phase 0 : corpus documentaire.
2. Phase 1 : index des motifs.
3. Phase 2 : vérification des motifs à fort enjeu.
4. Phase 3 : taxonomie à deux axes.
5. Phase 4 : tagging assisté semi-manuel.
6. Phase 5 : correction ciblée.
7. Phase 6 : contrôles qualité.
8. Phase 7 : usages finaux.

---

## Première séquence de travail proposée

Cette première séquence doit produire une base solide sans toucher encore au JSON de référence.

- [ ] Créer `docs/corpus_sources.md`.
- [ ] Créer `docs/table_sources_antiques.md`.
- [ ] Créer `docs/index_motifs_troy.md`.
- [ ] Générer `output/audit_motifs.csv`.
- [ ] Identifier les 20 à 40 scènes prioritaires à vérifier.
- [ ] Valider la liste des contradictions majeures.
- [ ] Seulement ensuite, lancer le tagging `degre_fidelite`.

