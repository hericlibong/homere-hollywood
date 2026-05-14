# Priorités de correction - Phase 5

Ce document sépare les corrections déjà tracées des arbitrages éditoriaux encore ouverts.

Le fichier enrichi existe et il est valide. La Phase 5 n'est toutefois pas terminée sur le fond : les corrections ci-dessous doivent être traitées par lots.

---

## 1. Mauvaises attributions possibles à `source_principale`

Statut : traité pour le lot prioritaire `degre_fidelite = 4` + `source_principale = Adaptation Cinéma`.

| Priorité | Scènes | Problème | Action proposée |
|---|---|---|---|
| Haute | 104 | `source_principale = Héritage Gréco-Romain`, mais `reference_iliade = Chant VII` | traité : conservation de `Héritage Gréco-Romain`, suppression de `reference_iliade` |
| Haute | 113 | `source_principale = L'Iliade`, mais pas de chant précis | traité : convention `reference_iliade = Formule épique homérique` |
| Moyenne | 98-107 | mort d'Ajax souvent classée `Adaptation Cinéma` | traité pour la scène 98 ; scènes de conséquence maintenues si transition filmique |
| Moyenne | 168, 176, 179, 187, 202 | Énée réduit et Épée de Troie | traité pour la scène 202 ; les autres scènes restent documentées dans l'audit degré 4 |

---

## 2. Références iliadiques trop vagues ou incohérentes

Statut : à arbitrer.

| Priorité | Scènes | Problème | Action proposée |
|---|---|---|---|
| Haute | 113 | `reference_iliade` vide malgré `source_principale = L'Iliade` | traité : `Formule épique homérique` |
| Haute | 104 | `reference_iliade = Chant VII` avec `source_principale = Héritage Gréco-Romain` | traité : `reference_iliade` vidée, Chant VII maintenu dans l'explication |
| Moyenne | scènes avec plusieurs chants | certaines références combinent plusieurs motifs | vérifier si la référence doit rester multiple ou être hiérarchisée |

---

## 3. Contradictions encore classées avec `source_principale = Adaptation Cinéma`

Statut : traité pour le premier lot prioritaire.

Avec la taxonomie à deux axes, ce n'est pas automatiquement une erreur : une scène peut avoir une origine filmique et un `degre_fidelite = 4` si elle contredit une donnée antique majeure. Mais ces scènes doivent être revues parce que certaines contiennent peut-être un matériau antique identifiable.

Familles concernées :

- mort de Ménélas par Hector ;
- mort d'Ajax par Hector ;
- Briséis princesse troyenne ou cousine d'Hector ;
- Patrocle, armure d'Achille et erreur d'identification ;
- Achille vivant pendant le sac de Troie ;
- Agamemnon tué à Troie par Briséis ;
- Pâris survivant jusqu'à la fuite finale.

Fichier de contrôle : `output/audit_degre_fidelite.csv`.

Fichier de revue : `output/audit_source_principale_phase5.csv`.

---

## 4. Incertitudes signalées dans les explications

Statut : à traiter progressivement.

Plusieurs explications utilisent explicitement des formules de prudence comme "à vérifier". Elles ne sont donc pas invisibles, mais elles doivent être résolues avant publication.

Exemples de motifs à reprendre :

- Boagrius et Triopas ;
- Polydora ;
- Tecton ;
- Eudore ;
- traditions des *Chants Cypriens* connues par Proclus ;
- traditions sur la mort d'Achille ;
- offrande du cheval à Athéna ou Poséidon selon les versions.

---

## 5. Noms propres secondaires douteux

Statut : à traiter après les grandes contradictions.

Priorité éditoriale plus basse, car ces noms ne changent pas la lecture globale du film, mais ils peuvent affaiblir la précision du corpus.

Noms à vérifier :

- Boagrius ;
- Triopas ;
- Polydora ;
- Tecton ;
- Eudore ;
- Lysander / `LSYANDER` ;
- Glaucus / Glaucos.

---

## Ordre recommandé

1. Résoudre les mentions "à vérifier" qui touchent le Cycle Troyen.
2. Traiter les noms propres secondaires.

Cet ordre évite de disperser l'effort : on commence par ce qui peut modifier la visualisation et le storytelling.
