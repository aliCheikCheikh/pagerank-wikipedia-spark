"""Préparation des données (responsable : personne A).

À faire :
- lire enwiki.wikilink_graph.2018-03-01.csv.gz (TSV avec en-tête) depuis le bucket GCS ;
- ne garder que les colonnes utiles (page_id_from, page_id_to) ;
- écrire une seule fois le résultat en Parquet (un .gz ne peut pas être découpé) ;
- produire aussi un échantillon de 10 % pour les essais.
"""
