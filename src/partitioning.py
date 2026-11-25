"""Co-partitionnement et coupure de la lignée (responsable : personne C).

À faire :
- co-partitionner la table des liens et la table des rangs sur la même clé,
  pour que leur jointure ne provoque pas de shuffle ;
- couper la lignée à chaque itération (localCheckpoint ou checkpoint)
  en vérifiant que le partitionnement est conservé ;
- vérifier l'effet de l'AQE sur le plan ;
- fournir la preuve avec explain() : un seul Exchange par itération.
"""
