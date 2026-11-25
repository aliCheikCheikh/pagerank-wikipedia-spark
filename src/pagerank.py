"""PageRank et PageRank personnalisé en PySpark DataFrame (responsable : personne B).

Formule de l'énoncé, pour chaque page p et à chaque itération :
    r(p) <- (1 - d) * v(p) + d * (somme sur u->p de r(u) / deg(u) + v(p) * D)
avec d = 0,85 et D = somme des rangs des pages sans lien sortant.

- PageRank : v(p) = 1/N pour toutes les pages.
- PPR depuis Nantes : v(67453) = 1, v(p) = 0 sinon.
On part de r = v, 20 itérations, la somme des rangs doit rester égale à 1.
"""
