<h1 style="text-align: center; font-family: 'Roboto', sans-serif; font-weight:bold; font-size:40px; margin: 40px 0">Projet HumanForYou</h1><img style="margin: 40px 0" src="./src/resources/StartImage.jpg"/><p style="text-align: center; font-style: italic; margin-top: 10px; font-size:15px">Rédigé par le <b>Groupe 2 </b></p><p style="text-align: right; font-size: 0.9em;">
BEROUD Dylan, SERRE Loïc, REPELLIN Benjamin</p>

---

# Contexte

HumanForYou est une entreprise pharmaceutique indienne d'environ 4 000 employés, confrontée à un taux d'attrition annuel de 15 %, soit près de 600 départs par an. Ce phénomène génère des coûts opérationnels significatifs : retards de projets nuisant à la réputation client, pression sur le service RH pour le recrutement continu, et délais d'intégration des nouveaux collaborateurs.

Pour comprendre et enrayer ce phénomène, la direction a mandaté une analyse approfondie des données internes. Le jeu de données disponible est riche et multidimensionnel :

- Pofils démographiques et contractuels des employés,
- Évaluations managériales,
- Résultats d'une enquête de satisfaction,
- Données de badgeuse couvrant l'intégralité de l'année 2015.

L'année de référence étant 2015 car précédant les départs observés en 2016.

<h2 style="font-family: 'Roboto', sans-serif; font-weight:bold; color:red; margin:30 0 10 0px">Problématique</h2>

<p style="text-align:center; font-size:15px">Quels sont les facteurs individuels, organisationnels et comportementaux qui influencent le plus le risque de départ d'un employé chez HumanForYou, et dans quelle mesure un modèle prédictif peut-il permettre d'identifier les profils à risque pour orienter les actions de rétention dans un contexte éthique ?</p>
<p style="margin:100px"/>

# Organisation

## Prérequis

| Élément        | Version           |
| ---------------- | ----------------- |
| **Python** | > 3.10            |
| **pip**    | dernière version |

## Installation

```bash
git clone <url-du-repo>
cd IA-groupe-02
pip install -r requirements.txt
```

## Arborescence du projet

```
IA-groupe-02/
├── src/
│   ├── data/
│   │   ├── raw/                   # Données brutes
│   │   ├── pre-processed/         # Premier traitement des données
│   │   ├── corresponding-tables/  # Tables de correspondance
│   │   └── processed/             # Données prêtes pour modélisation
│   ├── notebooks/                 # Notebooks Jupyter (EDA, modélisation)
│   ├── resources/                 # Images & Vidéos
│   └── scripts/                   # Scripts Python
├── lessons/                       # Mini-Projets & Ressources pédagogiques
├── .github/                       # CI/CD et Templates GitHub
├── requirements.txt
└── README.md
```

<p style="margin:100px"/>

# Stratégie Git

Nous adoptons une stratégie **GitHub Flow** simplifiée et adaptée au travail collaboratif :

## Convention de nommage des branches

```
<type>/<description>
```

**Types autorisés :**

- `feat/` : nouvelles fonctionnalités
- `fix/` : corrections de bugs
- `doc/` : modifications de documentation

## Workflow Git

1. **Créer une branche** depuis `main` :

   ```bash
   git checkout -b feat/nom-feature
   ```
2. **Commiter régulièrement** avec des messages clairs :

   ```bash
   git commit -m "feat/Descriptif court et explicite #3"
   ```
3. **Pousser la branche** :

   ```bash
   git push origin feat/nom-feature
   ```
4. **Créer une Pull Request** sur GitHub avec une description détaillée.
5. **Reviewer** : au moins 1 approbation requise avant merge.
6. **Merge** sur `main` et suppression de la branche.

## Règles de Merge

- Squash or Rebase pour maintenir un historique propre.
- Toutes les branches doivent être à jour avec `main` avant merge.
- Les notebooks Jupyter doivent être exécutés et testés avant merge.
- Force push sur `main` ou `dev` interdit.

<p style="margin:100px"/>

# Équipe

| Membre                      | Responsabilités                                           |
| --------------------------- | ---------------------------------------------------------- |
| **BEROUD Dylan**      | Modélisation, Documentation Éthique, Analyse Prédictive |
| **SERRE Loïc**       | Modélisation, Déploiement CI/CD                          |
| **REPELLIN Benjamin** | Analyse Prédictive                                        |
