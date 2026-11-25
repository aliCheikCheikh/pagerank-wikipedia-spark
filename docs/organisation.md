# Organisation du groupe

## Répartition du travail

Chacun est responsable de ses fichiers, pour éviter les conflits Git.
Tout le monde doit comprendre l'ensemble du projet (questions à l'examen) :
chacun relit les pull requests des deux autres.

### Personne A : données et cluster
- Mettre le fichier Wikipédia dans un bucket GCS.
- `src/prepare_data.py` : conversion en Parquet, échantillon de 10 %.
- `scripts/` : création et suppression des clusters de 2, 4 et 6 nœuds, soumission des jobs.
- Mesurer les temps (préparation et temps par itération) et remplir le tableau du README.

### Personne B : algorithme
- `src/pagerank.py` : PageRank et PPR depuis Nantes, en DataFrame.
- Gestion des pages sans lien sortant (D) et vérification que la somme vaut 1.
- `tests/test_small_graph.py` : comparaison avec networkx sur un petit graphe.
- Rapport PPR / PR et choix du seuil.

### Personne C : performance et preuve
- `src/partitioning.py` : co-partitionnement des liens et des rangs.
- Coupure de la lignée, effet de l'AQE.
- Preuve avec `explain()` : un seul Exchange par itération.
- Rédaction des parties « Plan d'exécution » et « Commentaire des résultats » du README.

## Ordre de travail

1. B écrit le PageRank sur un mini-graphe, en local (gratuit). A prépare les données en parallèle.
2. C reprend le code de B pour le co-partitionnement et la lignée.
3. Essai sur 10 % des données, sur un petit cluster.
4. Expériences finales sur 2, 4 et 6 nœuds.
5. README final.

## Règles Git

- Ne jamais travailler directement sur `main`.
- Une branche par tâche : `feature/prepare-data`, `feature/pagerank`, `feature/co-partitioning`, etc.
- Ouvrir une pull request vers `main`, relue par au moins une autre personne avant la fusion.
- Faire de petits commits, qui font une seule chose.

### Messages de commit

Format : `type: description courte au présent`.

| Type | Usage | Exemple |
|---|---|---|
| `feat` | nouvelle fonctionnalité | `feat: add personalized PageRank from Nantes` |
| `fix` | correction de bug | `fix: redistribute dangling mass in each iteration` |
| `test` | tests | `test: compare small graph with networkx` |
| `docs` | documentation, README | `docs: add execution times for 4 nodes` |
| `perf` | optimisation | `perf: co-partition links and ranks by src` |
| `chore` | configuration, scripts | `chore: add Dataproc cluster script` |

## Budget GCP

- Chacun a son crédit de 50 $. On développe et on teste en local ou dans Cloud Shell (gratuit).
- Les clusters ne servent qu'aux essais sur 10 % et aux expériences finales.
- Toujours `--max-idle`, toujours supprimer le cluster à la fin.
- On répartit les expériences finales sur les trois crédits.
