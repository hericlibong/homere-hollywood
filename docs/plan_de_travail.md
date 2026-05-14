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

- [x] Créer `docs/corpus_sources.md`.
- [x] Définir les catégories de sources :
  - [x] Homère.
  - [x] Cycle Troyen.
  - [x] Héritage gréco-romain.
  - [x] Mythographes et sources tardives.
  - [x] Géographie et noms propres.
- [x] Identifier les sources primaires à utiliser en priorité :
  - [x] Homère, *Iliade*.
  - [x] Homère, *Odyssée*.
  - [x] Résumés du Cycle Troyen attribués à Proclus.
  - [x] Virgile, *Énéide*, surtout livre II.
  - [x] Eschyle, *Agamemnon*.
  - [x] Sophocle, *Ajax*.
  - [x] Euripide, *Troyennes*, *Hécube*, *Andromaque*.
  - [x] Ovide, *Héroïdes* et passages pertinents des *Métamorphoses*.
  - [x] Stace, *Achilléide*.
  - [x] Apollodore, *Bibliothèque*.
  - [x] Hygin, *Fables*.
  - [x] Strabon, passages utiles pour les noms propres et lieux.
- [ ] Pour chaque source, renseigner :
  - [x] auteur ;
  - [x] oeuvre ;
  - [ ] date approximative ;
  - [x] statut : conservée, fragmentaire, perdue, tardive ;
  - [x] niveau de fiabilité éditoriale ;
  - [x] lien ou fichier local disponible ;
  - [x] motifs du film concernés.
- [ ] Créer une liste courte des sources réellement mobilisables pour la première passe.

Livrables :

- [x] `docs/corpus_sources.md`
- [x] `docs/table_sources_antiques.md`

---

## Phase 1 - Construire un index des motifs au lieu de relire scène par scène

But : organiser les 202 scènes par problèmes littéraires, pour travailler efficacement.

Critère de sortie : chaque grande question du film pointe vers un groupe de scènes candidates.

- [x] Créer `docs/index_motifs_troy.md`.
- [x] Extraire depuis le JSON consolidé les scènes contenant les personnages majeurs :
  - [x] Achille.
  - [x] Hector.
  - [x] Agamemnon.
  - [x] Ménélas.
  - [x] Pâris.
  - [x] Hélène.
  - [x] Briséis.
  - [x] Patrocle.
  - [x] Priam.
  - [x] Ajax.
  - [x] Ulysse.
  - [x] Énée.
  - [x] Andromaque.
- [x] Créer des groupes de motifs :
  - [x] querelle Achille / Agamemnon ;
  - [x] Briséis ;
  - [x] Pâris, Hélène et Sparte ;
  - [x] duel Pâris / Ménélas ;
  - [x] Hector et Andromaque ;
  - [x] Patrocle et les armes d'Achille ;
  - [x] mort d'Ajax ;
  - [x] duel Achille / Hector ;
  - [x] Priam chez Achille ;
  - [x] cheval de Troie ;
  - [x] sac de Troie ;
  - [x] mort d'Agamemnon ;
  - [x] survie de Pâris ;
  - [x] fuite d'Énée ;
  - [x] inventions géographiques ou politiques du film.
- [x] Pour chaque motif, lister :
  - [x] scènes concernées ;
  - [x] source antique attendue ;
  - [x] statut probable : reprise, déplacement, invention sur fond, contradiction ;
  - [x] priorité de vérification.

Livrables :

- [x] `docs/index_motifs_troy.md`
- [x] `output/audit_motifs.csv`

---

## Phase 2 - Vérifier d'abord les motifs à fort enjeu

But : contrôler les endroits où une erreur changerait fortement l'interprétation du film.

Critère de sortie : les grands écarts du film sont confirmés, corrigés ou nuancés avant tout tagging global.

### Lot A - Iliade, scènes centrales

- [x] Vérifier la querelle Achille / Agamemnon avec le Chant I.
- [x] Vérifier Briséis et Chryséis avec le Chant I.
- [x] Vérifier le duel Pâris / Ménélas avec le Chant III.
- [x] Vérifier Hector / Andromaque / Astyanax avec le Chant VI.
- [x] Vérifier le choix d'Achille entre vie longue et gloire avec le Chant IX.
- [x] Vérifier Patrocle avec le Chant XVI.
- [x] Vérifier le deuil d'Achille avec le Chant XVIII.
- [x] Vérifier le duel Achille / Hector avec le Chant XXII.
- [x] Vérifier Priam chez Achille avec le Chant XXIV.

### Lot B - Cycle Troyen

- [x] Vérifier Pâris à Sparte et l'origine de la guerre avec les *Chants Cypriens*.
- [x] Vérifier les épisodes liés à la mort d'Achille avec l'*Éthiopide*.
- [x] Vérifier le cheval de Troie avec la *Petite Iliade* et le *Sac d'Ilion*.
- [x] Vérifier les épisodes de la chute de Troie avec le *Sac d'Ilion*.
- [x] Noter explicitement que ces sources sont perdues et connues par résumés ou fragments.

### Lot C - Héritage gréco-romain

- [x] Vérifier le cheval de Troie, Priam et Énée avec Virgile, *Énéide* II.
- [x] Vérifier Ajax avec Sophocle, *Ajax*.
- [x] Vérifier Agamemnon avec Eschyle, *Agamemnon*.
- [x] Vérifier le sort des femmes troyennes avec Euripide.
- [x] Vérifier les traditions tardives sur Achille avec Stace, *Achilléide*.
- [x] Vérifier les synthèses mythographiques avec Apollodore et Hygin, en les marquant comme tardives.

Livrables :

- [x] `docs/verification_motifs_majeurs.md`
- [x] `output/audit_references_prioritaires.csv`

---

## Phase 3 - Définir et documenter la taxonomie à deux axes

But : intégrer la suggestion de double taxonomie sans mélanger origine et fidélité.

Critère de sortie : les règles de classification sont écrites avant modification du JSON.

- [x] Créer `docs/taxonomie_sources_et_fidelite.md`.
- [x] Conserver `source_principale` comme axe d'origine du matériau :
  - [x] `L'Iliade`
  - [x] `Le Cycle Troyen`
  - [x] `Héritage Gréco-Romain`
  - [x] `Adaptation Cinéma`
- [x] Ajouter le futur champ `degre_fidelite` :
  - [x] `1` : reprise fidèle.
  - [x] `2` : déplacement.
  - [x] `3` : invention sur fond emprunté.
  - [x] `4` : invention contradictoire.
- [x] Écrire les critères d'arbitrage :
  - [x] quand choisir `1` plutôt que `2` ;
  - [x] quand choisir `3` plutôt que `4` ;
  - [x] comment traiter une scène avec matériau antique et contradiction filmique ;
  - [x] comment traiter les scènes composites.
- [x] Ajouter des exemples obligatoires :
  - [x] scène 6, Boagrius : `Adaptation Cinéma` + degré `3`.
  - [x] scène 8, banquet de Sparte : `Le Cycle Troyen` + degré `4` si Hector à Sparte est confirmé comme invention contradictoire.
  - [x] scène 98, Ajax : matériau iliadique ou grec majeur + degré `4` si mort par Hector.
  - [x] scène 141, Achille / Hector : `L'Iliade` + degré `1` ou `2` selon l'écart exact.

Livrables :

- [x] `docs/taxonomie_sources_et_fidelite.md`

---

## Phase 4 - Tagging assisté semi-manuel, option B

But : ajouter `degre_fidelite` rapidement, mais en gardant le contrôle éditorial.

Critère de sortie : un fichier tagué provisoire existe, avec les contradictions majeures isolées.

- [x] Créer un script ou traitement local pour générer un brouillon :
  - [x] lire `output/troy_true_or_false_all_scenes.json` ;
  - [x] ajouter `degre_fidelite` ;
  - [x] préserver tous les champs existants ;
  - [x] écrire un nouveau fichier sans écraser la référence.
- [x] Appliquer les règles de départ :
  - [x] `source_principale = "L'Iliade"` et `reference_iliade` non vide : degré `1` par défaut.
  - [x] `source_principale = "Adaptation Cinéma"` : degré `3` par défaut.
  - [x] `source_principale = "Le Cycle Troyen"` : degré `1`, `2` ou `3` selon motif.
  - [x] `source_principale = "Héritage Gréco-Romain"` : degré `1`, `2` ou `3` selon motif.
- [x] Appliquer une liste explicite de contradictions majeures en degré `4` :
  - [x] Hector à Sparte.
  - [x] Briséis princesse troyenne, cousine d'Hector ou prêtresse d'Apollon.
  - [x] mort de Ménélas par Hector.
  - [x] mort d'Ajax par Hector.
  - [x] Agamemnon tué à Troie.
  - [x] Achille vivant ou actif pendant le sac de Troie.
  - [ ] Achille lié au cheval de Troie.
  - [x] Pâris survivant jusqu'à la fuite finale.
  - [x] Hélène fuyant avec les Troyens.
  - [x] Énée adolescent recevant l'Épée de Troie.
  - [x] l'Épée de Troie comme objet central du scénario.
- [x] Produire un audit des scènes en degré `4`.
- [ ] Relire uniquement les scènes ambiguës, pas les 202 scènes.

Livrables :

- [x] `output/troy_true_or_false_all_scenes_tagged_draft.json`
- [x] `output/audit_degre_fidelite.csv`
- [x] `docs/contradictions_majeures.md`

---

## Phase 5 - Correction ciblée du JSON de référence

But : corriger le corpus à partir des audits, sans réécriture massive.

Critère de sortie : une version consolidée enrichie existe et les corrections sont traçables.

- [x] Créer un fichier de suivi des corrections :
  - [x] `docs/journal_corrections.md`
- [x] Pour chaque correction, noter :
  - [x] scène ;
  - [x] champ modifié ;
  - [x] ancienne valeur ;
  - [x] nouvelle valeur ;
  - [x] justification ;
  - [x] source documentaire.
- [x] Corriger en priorité :
  - [x] arbitrer les anomalies Phase 6 : scènes 104 et 113 ;
  - [x] mauvaises attributions à `source_principale` ;
  - [x] références iliadiques trop vagues ;
  - [x] contradictions classées comme simples adaptations ;
  - [x] révision des incertitudes explicites dans `explication_litteraire` ;
    - [x] auditer et classer les 56 scènes concernées ;
    - [x] appliquer les corrections du sous-lot `incertitude_generale` ;
    - [x] traiter les cas de noms et lieux secondaires sans recherche supplémentaire ;
    - [x] nettoyer les formulations restantes `à vérifier` / `à confirmer` par simplification ou suppression des détails non vérifiables ;
  - [x] recherche ciblée d'incertitudes non signalées restantes ;
  - [x] noms propres secondaires douteux.
- [x] Créer une version de sortie enrichie :
  - [x] conserver le fichier original ;
  - [x] produire une nouvelle version nommée explicitement.

Livrables :

- [x] `output/troy_true_or_false_all_scenes_enriched.json`
- [x] `output/audit_corrections_phase5.csv`
- [x] `output/audit_source_principale_phase5.csv`
- [x] `output/audit_references_iliade_phase5.csv`
- [x] `output/audit_incertitudes_explicit_phase5.csv`
- [x] `output/audit_a_verifier_restants_phase5.csv`
- [x] `docs/audit_incertitudes_explicit_phase5.md`
- [x] `docs/priorites_corrections_phase5.md`
- [x] `docs/journal_corrections.md`

---

## Phase 6 - Contrôles qualité

But : s'assurer que le corpus reste exploitable techniquement et éditorialement.

Critère de sortie : le corpus enrichi est valide, cohérent et prêt pour visualisation ou publication.

- [x] Vérifier que le JSON est valide.
- [x] Vérifier que chaque scène possède les champs attendus.
- [x] Vérifier que `source_principale` ne contient que les 4 valeurs autorisées.
- [x] Vérifier que `degre_fidelite` ne contient que `1`, `2`, `3`, `4`.
- [x] Vérifier les doublons de `scene_number`.
- [x] Vérifier les scènes manquantes.
- [x] Vérifier les longueurs extrêmes de `action_film`.
- [x] Vérifier les champs `reference_iliade` :
  - [x] vide quand la scène ne reprend pas vraiment l'Iliade ;
  - [x] précis quand la scène reprend un passage identifiable.
- [x] Produire un résumé statistique :
  - [x] nombre de scènes par `source_principale` ;
  - [x] nombre de scènes par `degre_fidelite` ;
  - [x] matrice `source_principale` x `degre_fidelite` ;
  - [x] liste des scènes degré `4`.

Livrables :

- [x] `output/quality_report.md`
- [x] `output/statistiques_taxonomie.json`

---

## Phase 7 - Préparer les usages finaux

But : transformer le corpus en support lisible, pédagogique et visualisable.

Critère de sortie : les données peuvent servir à une visualisation, un article, une formation ou une édition critique.

- [x] Préparer une matrice visuelle `source_principale` x `degre_fidelite`.
- [x] Préparer une timeline du film colorée par degré de fidélité.
- [x] Préparer une liste narrative des grandes ruptures mythiques du film.
- [x] Préparer un index des personnages.
- [x] Préparer un index des sources antiques.
- [x] Préparer une bibliographie de contrôle.
- [x] Préparer une note méthodologique courte pour accompagner le corpus.

Livrables :

- [x] `docs/synthese_editoriale.md`
- [x] `docs/bibliographie_controle.md`
- [x] `docs/note_methodologique_courte.md`
- [x] fichiers de données pour visualisation à définir.

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

- [x] Créer `docs/corpus_sources.md`.
- [x] Créer `docs/table_sources_antiques.md`.
- [x] Créer `docs/index_motifs_troy.md`.
- [x] Générer `output/audit_motifs.csv`.
- [ ] Identifier les 20 à 40 scènes prioritaires à vérifier.
- [ ] Valider la liste des contradictions majeures.
- [ ] Seulement ensuite, lancer le tagging `degre_fidelite`.

