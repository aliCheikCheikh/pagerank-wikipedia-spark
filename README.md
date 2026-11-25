# PageRank et PageRank personnalisé sur Wikipédia avec PySpark (DataFrame)

Projet du cours *Large Scale Data Management* (Pascal Molli, Nantes Université), 2026-2027.

**Membres du groupe :** NOM Prénom, NOM Prénom, NOM Prénom

## Objectif

Calculer, sur le graphe des liens de Wikipédia anglais (WikiLinkGraphs, 1er mars 2018) :
- le **PageRank** classique : quelle est l'entité au centre de Wikipédia ?
- le **PageRank personnalisé (PPR)** depuis l'article *Nantes* (id 67453) : à quoi ressemble Wikipédia vu depuis Nantes ?

Contraintes : PySpark **DataFrame** uniquement (ni RDD, ni GraphFrames), d = 0,85, 20 itérations, somme des rangs = 1.

## Organisation du dépôt

| Dossier | Contenu |
|---|---|
| `src/` | Code PySpark (préparation des données, PageRank, PPR) |
| `tests/` | Tests sur un petit graphe, comparaison avec `networkx.pagerank` |
| `scripts/` | Scripts Dataproc (création / suppression des clusters, soumission des jobs) |
| `results/` | Résultats bruts des expériences (top 20, temps, plans d'exécution) |
| `docs/` | Organisation du groupe et règles de travail |

## Résultats

### Top 20 du PageRank
*À compléter.*

### Top 20 du PPR depuis Nantes
*À compléter.*

### Top 20 du rapport PPR / PR
*À compléter (seuil choisi et justification).*

### Commentaire des différences
*À compléter.*

## Temps d'exécution

| Nœuds | Préparation (s) | PR : temps par itération (s) | PPR : temps par itération (s) |
|---|---|---|---|
| 2 | | | |
| 4 | | | |
| 6 | | | |

*Configuration des machines : à compléter (même type de machine pour tous les nœuds).*

## Plan d'exécution d'une itération

*À compléter : sortie de `explain()` montrant un seul `Exchange` par itération (regroupement des contributions par page de destination), et aucun shuffle sur la jointure liens / rangs.*

### Co-partitionnement
*À compléter : méthode utilisée.*

### Coupure de la lignée
*À compléter : méthode utilisée et vérification que le partitionnement est conservé (AQE).*

## Reproduire les expériences

*À compléter : commandes pour préparer les données, lancer un cluster, soumettre le job, supprimer le cluster.*

## Bonus : instantané 2008

*Optionnel.*

## Références

- S. Brin, L. Page. *The Anatomy of a Large-Scale Hypertextual Web Search Engine*, 1998.
- M. Zaharia et al. *Resilient Distributed Datasets*, NSDI 2012.
- M. Armbrust et al. *Spark SQL*, SIGMOD 2015.
- C. Consonni, D. Laniado, A. Montresor. *WikiLinkGraphs*, ICWSM 2019.
