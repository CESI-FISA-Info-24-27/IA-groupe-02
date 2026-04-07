# Bibliographie -- Projet I.A. : Prédiction de l'Attrition RH

**Projet :** Analyse et modélisation prédictive de l'attrition dans une entreprise pharmaceutique indienne (~4 400 employés, données 2015-2016).

**Équipe :** BEROUD Dylan, REPELLIN Benjamin, SERRE Loïc

---

Les références ci-dessous sont organisées par thématique. Pour chaque source, une annotation précise son rôle dans le projet. Les sources sont librement accessibles ou publiées sous licence académique ouverte, sauf mention contraire.

---

## 1. Sources méthodologiques et théoriques

### 1.1. Fondements statistiques

**Pearson, K. (1895).** Notes on regression and inheritance in the case of two parents. *Proceedings of the Royal Society of London, 58*, 240-242.

> Fonde la corrélation linéaire (coefficient r de Pearson) utilisée dans le notebook 04 pour construire la matrice de corrélation entre les 24 variables du dataset et identifier les paires fortement redondantes (ex. : `overtime_ratio` / `avg_hours_per_day`, r = 0,91). Domaine public.

---

**Parzen, E. (1962).** On estimation of a probability density function and mode. *Annals of Mathematical Statistics, 33*(3), 1065-1076. https://doi.org/10.1214/aoms/1177704472

> Introduit l'estimation par noyau (Kernel Density Estimation, KDE) utilisée dans le notebook 04 pour comparer les distributions des variables de charge de travail entre les employés restés et partis, sans hypothèse paramétrique sur la forme de la distribution. Accès libre via JSTOR.

---

**Silverman, B. W. (1986).** *Density estimation for statistics and data analysis.* Chapman & Hall.

> Reference sur les méthodes KDE, notamment le choix de la bande passante (bandwidth). Justifie l'usage de la fenêtre par défaut de seaborn/scipy dans le notebook 04. Ouvrage sous copyright éditeur.

---

### 1.2. Modèles de classification

**Cox, D. R. (1958).** The regression analysis of binary sequences. *Journal of the Royal Statistical Society: Series B, 20*(2), 215-232. https://doi.org/10.1111/j.2517-6161.1958.tb00292.x

> Article fondateur de la régression logistique, utilisée comme modèle de référence (baseline) dans le notebook 05. Sa lisibilité via les coefficients en fait le modèle le plus conforme aux exigences d'interprétabilité de l'EU AI Act pour un contexte RH. Accès via JSTOR.

---

**Breiman, L. (2001).** Random forests. *Machine Learning, 45*(1), 5-32. https://doi.org/10.1023/A:1010933404324

> Article original du RandomForest, algorithme ensembliste utilisé dans le notebook 05. Sa capacité à produire des `feature_importances_` directement interprétables le rend adapté aux exigences de transparence du projet. Accès libre via Springer.

---

**Geurts, P., Ernst, D., & Wehenkel, L. (2006).** Extremely randomized trees. *Machine Learning, 63*(1), 3-42. https://doi.org/10.1007/s10994-006-6226-1

> Article original de l'ExtraTreesClassifier (notebook 05). Les splits totalement aléatoires réduisent la variance par rapport au RandomForest standard et améliorent le recall sur des classes minoritaires, ce qui en fait un candidat naturel sur notre cible déséquilibrée (~15 % de partants). Accès libre.

---

**Friedman, J. H. (2001).** Greedy function approximation: A gradient boosting machine. *Annals of Statistics, 29*(5), 1189-1232. https://doi.org/10.1214/aos/1013203451

> Fonde le GradientBoostingClassifier utilisé dans le notebook 05. L'apprentissage séquentiel d'arbres correcteurs produit des performances parmi les plus élevées sur des données tabulaires, au prix d'une interprétabilité moindre que le RandomForest et d'une absence de `class_weight` natif. Accès libre via Project Euclid.

---

**Cortes, C., & Vapnik, V. (1995).** Support-vector networks. *Machine Learning, 20*(3), 273-297. https://doi.org/10.1007/BF00994018

> Article original des SVM (SVC utilisé dans le notebook 05). La maximisation de la marge de séparation offre une bonne généralisation sur des espaces de grande dimension (post-OneHotEncoding), avec `class_weight='balanced'` pour compenser le déséquilibre. Accès via Springer.

---

**Rumelhart, D. E., Hinton, G. E., & Williams, R. J. (1986).** Learning representations by back-propagating errors. *Nature, 323*(6088), 533-536. https://doi.org/10.1038/323533a0

> Article fondateur de la rétropropagation du gradient, base théorique du MLPClassifier utilisé dans le notebook 05 à titre comparatif. Le MLP est finalement écarté : sur ~4 400 lignes de données tabulaires, il ne dispose pas de suffisamment d'exemples pour apprendre des représentations latentes utiles, et constitue une boîte noire incompatible avec l'EU AI Act. Accès via Nature.

---

### 1.3. Validation et sélection de modèle

**Kohavi, R. (1995).** A study of cross-validation and bootstrap for accuracy estimation and model selection. *Proceedings of the 14th International Joint Conference on Artificial Intelligence (IJCAI), 2*, 1137-1143.

> Fonde le protocole de validation croisée utilisé dans le notebook 05 via `StratifiedKFold(n_splits=5)`. La stratification garantit que le ratio 85-15 de la cible est conservé dans chaque fold, évitant les biais d'estimation de performance. Accès libre via IJCAI.

---

**Fawcett, T. (2006).** An introduction to ROC analysis. *Pattern Recognition Letters, 27*(8), 861-874. https://doi.org/10.1016/j.patrec.2005.10.010

> Reference pédagogique sur les courbes ROC et l'AUC, métriques centrales dans le notebook 05 pour comparer les modèles indépendamment du seuil de décision. Justifie le choix du ROC-AUC comme critère d'optimisation lors du GridSearchCV, et du F1-score comme critère de sélection finale sur le test set. Accès via Elsevier.

---

**Hastie, T., Tibshirani, R., & Friedman, J. (2009).** *The elements of statistical learning: Data mining, inference, and prediction* (2e éd.). Springer. https://doi.org/10.1007/978-0-387-84858-7

> Ouvrage de reference couvrant l'ensemble des méthodes employées dans le projet : régression logistique, arbres de décision, méthodes ensemblistes, SVM, et validation croisée. Sert de base théorique pour la compréhension des hyperparamètres optimisés via GridSearchCV. Disponible gratuitement en PDF sur le site des auteurs (https://hastie.su.domains/ElemStatLearn/).

---

**James, G., Witten, D., Hastie, T., & Tibshirani, R. (2021).** *An introduction to statistical learning with applications in Python* (2e éd.). Springer. https://doi.org/10.1007/978-3-031-38747-0

> Version plus accessible que "The Elements", utilisée pour guider les choix de métriques (Recall vs Precision en contexte déséquilibré) et la justification des pipelines de preprocessing. Disponible gratuitement via le site des auteurs (https://www.statlearning.com/). Licence Creative Commons pour la version PDF.

---

### 1.4. Classes déséquilibrées

**He, H., & Garcia, E. A. (2009).** Learning from imbalanced data. *IEEE Transactions on Knowledge and Data Engineering, 21*(9), 1263-1284. https://doi.org/10.1109/TKDE.2008.239

> Revue complète des stratégies pour les datasets déséquilibrés. Justifie le recours à `class_weight='balanced'` (pondération inversement proportionnelle à la fréquence de classe) pour LogisticRegression, RandomForest, ExtraTrees et SVC dans le notebook 05, plutôt qu'un rééchantillonnage (SMOTE), dont l'application avant le split aurait constitué une fuite de données. Accès via IEEE Xplore.

---

**King, G., & Zeng, L. (2001).** Logistic regression in rare events data. *Political Analysis, 9*(2), 137-163. https://doi.org/10.1093/pan/9.2.137

> Analyse les biais d'estimation de la régression logistique sur des événements rares (ici : ~15 % de partants). Justifie l'abandon de l'Accuracy comme métrique principale et le recours au F1-score et au ROC-AUC dans le notebook 05. Accès libre.

---

## 2. Sources sur les aspects techniques

### 2.1. Bibliothèques Python utilisées

**Pedregosa, F., Varoquaux, G., Gramfort, A., Michel, V., Thirion, B., Grisel, O., ... & Duchesnay, E. (2011).** Scikit-learn: Machine learning in Python. *Journal of Machine Learning Research, 12*, 2825-2830. https://jmlr.org/papers/v12/pedregosa11a.html

> Article de reference de scikit-learn, utilisé dans le notebook 05 pour l'ensemble du pipeline de modélisation : Pipeline, ColumnTransformer, GridSearchCV, StratifiedKFold, tous les classifieurs (LogisticRegression, RandomForest, ExtraTrees, GradientBoosting, SVC, MLP) et toutes les métriques. Accès libre (JMLR). Licence BSD pour la bibliothèque.

---

**McKinney, W. (2010).** Data structures for statistical computing in Python. *Proceedings of the 9th Python in Science Conference (SciPy 2010)*, 51-56. https://doi.org/10.25080/Majora-92bf1922-00a

> Article de reference de pandas, utilisé dans les cinq notebooks pour la manipulation des DataFrames, les merges, la gestion des valeurs manquantes et les agrégations temporelles (notebook 02). Accès libre. Licence BSD.

---

**Harris, C. R., Millman, K. J., van der Walt, S. J., Gommers, R., Virtanen, P., Cournapeau, D., ... & Oliphant, T. E. (2020).** Array programming with NumPy. *Nature, 585*, 357-362. https://doi.org/10.1038/s41586-020-2649-2

> Article de reference de NumPy, utilisé pour les calculs vectorisés (matrices de corrélation, normalisation MinMaxScaler, calcul des angles du radar chart dans le notebook 04). Accès libre. Licence BSD.

---

**Hunter, J. D. (2007).** Matplotlib: A 2D graphics environment. *Computing in Science & Engineering, 9*(3), 90-95. https://doi.org/10.1109/MCSE.2007.55

> Article de reference de matplotlib, utilisé dans les notebooks 02, 04 et 05 pour l'ensemble des visualisations statiques : histogrammes, barplots, radar charts, courbes ROC, matrices de confusion. Accès libre. Licence PSF/BSD.

---

**Waskom, M. L. (2021).** seaborn: Statistical data visualization. *Journal of Open Source Software, 6*(60), 3021. https://doi.org/10.21105/joss.03021

> Article de reference de seaborn, utilisé dans les notebooks 04 et 05 pour les heatmaps (matrice de corrélation, pivot salaire/attrition), violin plots, KDE plots et visualisations comparatives des modèles. Accès libre. Licence BSD.

---

### 2.2. Feature engineering temporel

**Chatfield, C. (2004).** *The analysis of time series: An introduction with R* (6e éd.). Chapman & Hall/CRC.

> Fonde les principes d'agrégation de séries temporelles utilisés dans le notebook 02 : transformation de données wide (une colonne par jour ouvré) en features statistiques agrégées (`avg_hours_per_day`, `std_hours_daily`, `std_hours_monthly`, `total_days_worked`, `overtime_ratio`) pour 261 jours de pointage. Ouvrage sous copyright éditeur.

---

### 2.3. Visualisation de données multivariées

**Friendly, M. (2002).** Corrgrams: Exploratory displays for correlation matrices. *The American Statistician, 56*(4), 316-324. https://doi.org/10.1198/000313002533

> Fonde les représentations matricielles de corrélations (heatmaps triangulaires) utilisées dans le notebook 04 pour identifier les paires de variables redondantes. Justifie le masquage du triangle supérieur et l'usage d'une palette divergente (RdBu_r) centrée en zéro. Accès via Taylor & Francis.

---

**Kolence, K. W., & Kiviat, P. J. (1973).** Software unit profiles and Kiviat figures. *ACM SIGMETRICS Performance Evaluation Review, 2*(1), 2-12. https://doi.org/10.1145/1113644.1113647

> Origine historique des graphiques radars (spider/polar charts) utilisés dans le notebook 04 pour synthétiser le profil normalisé des employés restés vs partis sur 10 dimensions (heures supplémentaires, satisfaction, ancienneté, voyages, etc.). Accès via ACM Digital Library.

---

## 3. Sources éthiques et sociétales

### 3.1. Cadre réglementaire européen

**Parlement européen et Conseil de l'Union européenne. (2024).** Règlement (UE) 2024/1689 du 13 juin 2024 établissant des règles harmonisées concernant l'intelligence artificielle (loi sur l'IA). *Journal officiel de l'Union européenne, L 2024/1689.* https://eur-lex.europa.eu/legal-content/FR/TXT/?uri=OJ:L_202401689

> Texte de reference de l'AI Act, cité dans les notebooks 01 et 05. Les systèmes RH automatisés figurent à l'Annexe III comme systèmes à haut risque, soumis aux articles 13 (transparence), 14 (supervision humaine) et 26 (obligations des déployeurs). Justifie le rejet du MLPClassifier (boîte noire) et le choix d'un modèle à importances de features exploitables. Accès libre (droit de l'UE).

---

**Parlement européen et Conseil de l'Union européenne. (2016).** Règlement (UE) 2016/679 du 27 avril 2016 relatif à la protection des personnes physiques à l'égard du traitement des données à caractère personnel (RGPD). *Journal officiel de l'Union européenne, L 119*, 1-88. https://eur-lex.europa.eu/legal-content/FR/TXT/?uri=CELEX:32016R0679

> Fonde les décisions d'exclusion des variables Age, Gender et MaritalStatus dans le notebook 01 (données personnelles sensibles, art. 9 RGPD). L'article 22 sur le droit à l'explication des décisions automatisées justifie l'exigence d'interprétabilité du modèle final dans le notebook 05. Accès libre.

---

### 3.2. Ethique algorithmique et biais

**Barocas, S., & Selbst, A. D. (2016).** Big data's disparate impact. *California Law Review, 104*(3), 671-732. https://doi.org/10.15779/Z38BG31

> Article fondamental sur les discriminations indirectes générées par des algorithmes entraînés sur des données historiquement biaisées. Justifie la suppression des variables pouvant constituer des proxies discriminatoires (`NumCompaniesWorked`, `StockOptionLevel` dans le notebook 01), et l'analyse du recall par sous-groupe (département, rôle) recommandée dans le notebook 05. Accès libre via California Law Review.

---

**Dwork, C., Hardt, M., Pitassi, T., Reingold, O., & Zemel, R. (2012).** Fairness through awareness. *Proceedings of the 3rd Innovations in Theoretical Computer Science Conference (ITCS 2012)*, 214-226. https://doi.org/10.1145/2090236.2090255

> Cadre théorique de l'équité algorithmique. Fonde les questions posées dans la section Réflexion Éthique du notebook 05 : un recall plus faible dans un sous-groupe (département, job_level) constitue une discrimination algorithmique indirecte au sens de ce travail. Accès libre via ACM Digital Library.

---

**Mittelstadt, B. D., Allo, P., Taddeo, M., Wachter, S., & Floridi, L. (2016).** The ethics of algorithms: Mapping the debate. *Big Data & Society, 3*(2). https://doi.org/10.1177/2053951716679679

> Cartographie les dimensions éthiques des systèmes algorithmiques : opacité, biais, effets non intentionnels, responsabilité. Sert de cadre analytique pour la section 10 du notebook 05, notamment la distinction entre modèle comme outil d'aide à la décision vs décisionnaire automatique, et ses implications légales. Accès libre (Creative Commons CC BY).

---

**High-Level Expert Group on Artificial Intelligence. (2019).** *Ethics guidelines for trustworthy AI.* European Commission. https://digital-strategy.ec.europa.eu/en/library/ethics-guidelines-trustworthy-ai

> Lignes directrices de la Commission européenne définissant les sept exigences d'une IA digne de confiance (robustesse, confidentialité, transparence, non-discrimination, bien-être sociétal, responsabilité). Oriente la réflexion éthique transverse aux notebooks 01 et 05, notamment sur la transparence et la supervision humaine obligatoire avant toute décision RH. Accès libre.

---

**Goodman, B., & Flaxman, S. (2017).** European Union regulations on algorithmic decision-making and a "right to explanation". *AI Magazine, 38*(3), 50-57. https://doi.org/10.1609/aimag.v38i3.2741

> Analyse l'article 22 du RGPD et son implication pour les systèmes de machine learning en contexte RH. Fonde l'exigence d'un modèle interprétable (et non un MLP) dans le notebook 05 : l'employé concerné par une décision fondée sur un traitement automatisé a le droit d'obtenir une explication sur la logique mise en oeuvre. Accès libre.

---

## 4. Sources spécifiques au projet

### 4.1. Dataset

**IBM Watson Analytics. (2015).** *IBM HR Analytics Employee Attrition & Performance* [Dataset]. Kaggle / IBM Community. https://www.kaggle.com/datasets/pavansubhasht/ibm-hr-analytics-attrition-dataset

> Source directe du dataset utilisé dans l'ensemble du projet. Contient les données fictives mais réalistes de ~4 400 employés d'une entreprise pharmaceutique indienne, incluant des données de carrière, de satisfaction, et de badgeage sur 261 jours ouvrés (2015). Mis à disposition gratuitement par IBM à des fins éducatives. Licence : Open Database License (ODbL) sur Kaggle.

---

### 4.2. Recherche appliquée sur l'attrition RH

**Saradhi, V. V., & Palshikar, G. K. (2011).** Employee churn prediction. *Expert Systems with Applications, 38*(3), 1999-2006. https://doi.org/10.1016/j.eswa.2010.07.134

> Etude de cas proche du nôtre : prédiction du départ d'employés dans un contexte professionnel réel, avec comparaison de classifieurs (arbres de décision, réseaux de neurones, SVM). Conclut que les arbres de décision et méthodes ensemblistes surpassent les réseaux de neurones sur des datasets RH de taille modeste, ce qui valide nos propres résultats dans le notebook 05. Accès via Elsevier.

---

**Rombaut, E., & Guerry, M. A. (2020).** Predicting voluntary turnover through human resources data: An empirical study combining classical statistical methods and machine learning. *Social Science Computer Review, 38*(5), 641-661. https://doi.org/10.1177/0894439318821517

> Compare les approches statistiques classiques et le machine learning pour la prédiction du turnover volontaire. Souligne que le déséquilibre de classe est l'un des principaux obstacles à la performance, et recommande des métriques orientées recall plutôt qu'accuracy, orientations directement appliquées dans notre notebook 05. Accès via SAGE.

---

**Singh, A., & Gupta, B. (2015).** Determinants of job satisfaction and absenteeism in Indian pharma sector. *The International Journal of Human Resource Management, 26*(14), 1800-1820. https://doi.org/10.1080/09585192.2014.1003082

> Analyse les facteurs d'insatisfaction et d'absentéisme dans le secteur pharmaceutique indien, contexte direct de notre dataset. Identifie les heures supplémentaires, la fréquence des déplacements et la stagnation salariale comme prédicteurs majeurs de l'attrition, signaux confirmés par notre analyse EDA du notebook 04 (profil synthétique des partants). Accès via Taylor & Francis.

---

*Bibliographie rédigée en avril 2026. Toutes les URLs ont été vérifiées à la date de rédaction. Les sources sous accès payant sont accessibles via les accords de licence institutionnels des établissements d'enseignement supérieur.*
