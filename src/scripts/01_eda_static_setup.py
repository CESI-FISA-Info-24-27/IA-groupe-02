"""
setup.py
--------
Script d'initialisation du projet.

Toutes les variables de configuration sont exposées dans le namespace
du notebook appelant après exécution.
"""

import json
import os

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import seaborn as sns

# On charge la configuration depuis le fichier JSON
_CONFIG_PATH = os.path.join(os.path.dirname(os.path.abspath(__file__)), "config.json")

with open(_CONFIG_PATH, "r", encoding="utf-8") as _f:
    _cfg = json.load(_f)

# On expose les chemins

RAW_DATA_DIR = _cfg["paths"]["raw_data"]
PRE_PROCESSED_DATA_DIR = _cfg["paths"]["pre_processed_data"]
CORRESPONDING_TABLE_DIR = _cfg["paths"]["corresponding_table"]
PROCESSED_DATA_DIR = _cfg["paths"]["processed_data"]

# On expose la clé de jointure
JOIN_KEY = _cfg["join_key"]

# On expose les colonnes à supprimer
COL_TO_DELETE = _cfg["columns_to_delete"]

# On expose les mappings catégoriels
DEPARTMENT_MAP = _cfg["mappings"]["department"]
EDUCATION_FIELD_MAP = _cfg["mappings"]["education_field"]
JOB_ROLE_MAP = _cfg["mappings"]["job_role"]

# On expose les mappings numériques vers catégoriels
NUM_CAT_HAS_LEFT = _cfg["numeric_mappings"]["has_left"]
NUM_CAT_BUSINESS_TRAVEL = _cfg["numeric_mappings"]["business_travel"]
NUM_CAT_EDUCATION = _cfg["numeric_mappings"]["education"]
NUM_CAT_JOB_INVOLVEMENT = _cfg["numeric_mappings"]["job_involvement"]
NUM_CAT_PERFORMANCE_RATING = _cfg["numeric_mappings"]["performance_rating"]
NUM_CAT_ENVIRONMENT_SATISFACTION = _cfg["numeric_mappings"]["environment_satisfaction"]
NUM_CAT_WORK_LIFE_BALANCE = _cfg["numeric_mappings"]["work_life_balance"]

# On expose les colonnes à renommer
COL_CORR = _cfg["column_rename"]

# On affiche un résumé de la configuration pour l'utilisateur
print(f"Le répertoire de données est :\n- Raw : {os.path.abspath(RAW_DATA_DIR)}\n- Pre-processed : {os.path.abspath(PRE_PROCESSED_DATA_DIR)}\n- Processed : {os.path.abspath(PROCESSED_DATA_DIR)}\n- Table de Correspondance : {os.path.abspath(CORRESPONDING_TABLE_DIR)}")
print()

print(f"La clé de jointure pour les DataFrames est : {JOIN_KEY}")
print()

print("La configuration a été chargée.")
