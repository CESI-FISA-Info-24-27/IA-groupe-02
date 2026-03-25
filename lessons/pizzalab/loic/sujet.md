# Mini-projet IA - SliceLab

## Contexte et Objectif

SliceLab est une startup française qui propose une plateforme d'analyse et de conseil aux pizzerias indépendantes et aux petites chaînes. Grâce à son réseau de partenaires, elle collecte des données opérationnelles sur les établissements afin de leur fournir des recommandations personnalisées : ajustement de la carte, optimisation des délais, positionnement tarifaire.

Afin de mieux adapter ses recommandations, SliceLab souhaite segmenter automatiquement ses pizzerias partenaires en groupes homogènes. Plutôt que de traiter tous les établissements de la même façon, l'idée est d'identifier des profils distincts - par exemple des pizzerias artisanales premium d'un côté et des enseignes à fort volume de l'autre - pour personnaliser les conseils fournis.

## Solution envisagée

L'équipe data de SliceLab envisage d'utiliser un algorithme de clustering non supervisé pour découvrir ces profils sans avoir à les définir à l'avance. L'algorithme K-Means a été retenu pour une première expérimentation avec **k = 2** groupes.

Avant d'appliquer cet algorithme, il est nécessaire de consolider et préparer soigneusement les données : les exports régionaux ont été produits par des équipes différentes, à des moments différents, et ne suivent pas tous le même format.

## Description du jeu de données

Les données sont réparties dans **5 fichiers** issus d'exports régionaux. Une fois consolidés, ils représentent environ **600 établissements** répartis sur le territoire français.

Le jeu de données final attendu doit contenir les colonnes suivantes :

- **latitude** : latitude géographique de la pizzeria (varie de 43,2 à 51,1).
- **longitude** : longitude géographique de la pizzeria (varie de -4,8 à 8,2).
- **type_etablissement** : catégorie de l'établissement. Valeurs possibles : `Artisanale`, `Chaîne`, `Snack`, `Restaurant italien`.
- **nb_pizzas_carte** : nombre de pizzas différentes proposées au menu (varie de 2 à 60).
- **prix_moyen** : prix moyen d'une pizza en euros (varie de 6 à 28).
- **note_moyenne** : note moyenne attribuée par les clients sur 5 étoiles (varie de 1,0 à 5,0). Certains établissements récemment intégrés n'ont pas encore reçu d'avis.
- **nb_avis** : nombre total d'avis clients enregistrés sur la plateforme (varie de 0 à 4 200).
- **temps_preparation_moyen** : temps moyen de préparation d'une commande en **minutes** (varie de 5 à 45).
- **annee_ouverture** : année d'ouverture de l'établissement (varie de 1980 à 2024).
- **ca_mensuel_k** : chiffre d'affaires mensuel estimé en **milliers d'euros** (varie de 5 à 120).

### Les fichiers sources

**`donnees_nord_ouest.csv`** - Export de la région Nord-Ouest (Bretagne, Normandie, Pays de la Loire). Environ 120 établissements.

**`donnees_sud_est.tsv`** - Export de la région Sud-Est (Occitanie, PACA, Auvergne-Rhône-Alpes). Environ 130 enregistrements.

**`donnees_idf.csv`** - Export de la région Île-de-France. Environ 120 établissements.

**`donnees_grand_est.csv`** - Export de la région Grand-Est et Bourgogne. Environ 120 établissements.

**`export_toutes_regions.csv`** - Export consolidé produit par une équipe externe, couvrant l'ensemble du territoire. Environ 120 enregistrements supplémentaires.

## Travail attendu

À partir de ces cinq fichiers, vous devez produire un notebook Jupyter qui :

1. **Charge et consolide** les données en un seul DataFrame propre, prêt pour l'analyse.
2. **Explore** le jeu de données consolidé pour en comprendre la structure et la distribution.
3. **Visualise** les données à travers au moins quatre représentations graphiques pertinentes, dont une carte géographique.
4. **Prépare** les données pour le machine learning.
5. **Applique un clustering K-Means avec k = 2** et interprète les segments obtenus.
