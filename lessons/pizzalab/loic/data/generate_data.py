"""
Génère les fichiers de données volontairement imparfaits pour le workshop SliceLab.
Chaque fichier représente une région et contient des problèmes différents.
"""

import random
import csv
import os
import json

random.seed(42)

DATA_DIR = os.path.dirname(os.path.abspath(__file__))

TYPES_FR = ["Artisanale", "Chaîne", "Snack", "Restaurant italien"]
TYPES_EN = ["Artisan", "Chain", "Snack", "Italian restaurant"]
TYPES_TYPOS = ["ARTISANALE", "chaine", "Snack", "restaurant ITALIEN", "Artisannale", "chaîne", "SNACK", "Resto italien"]

def rand_float(lo, hi, decimals=4):
    return round(random.uniform(lo, hi), decimals)

def rand_int(lo, hi):
    return random.randint(lo, hi)

def rand_type(pool):
    return random.choice(pool)

# ── helpers par région ──────────────────────────────────────────────────────

def nord_ouest_row(i):
    """Problèmes : séparateur ;, décimale virgule, € dans les prix,
    lignes de métadonnées en tête, valeurs manquantes encodées 'N/A'/'non renseigné'."""
    lat = rand_float(47.0, 51.0, 4)
    lon = rand_float(-4.8, 1.6, 4)
    typ = rand_type(TYPES_FR)
    nb_p = rand_int(4, 45)
    prix = rand_float(7.0, 20.0, 2)
    # décimale virgule + symbole €
    prix_str = f'"{str(prix).replace(".", ",")} €"'
    note = rand_float(2.5, 5.0, 1) if random.random() > 0.18 else random.choice(["", "N/A", "non renseigné"])
    if isinstance(note, float):
        note = str(note).replace(".", ",")
    nb_avis = rand_int(0, 1800)
    prep = rand_int(8, 40) if random.random() > 0.15 else ""
    annee = rand_int(1985, 2024)
    ca = rand_int(8, 95)
    # remplacer . par , dans lat/lon aussi
    lat_s = str(lat).replace(".", ",")
    lon_s = str(lon).replace(".", ",")
    return f"{lat_s};{lon_s};{typ};{nb_p};{prix_str};{note};{nb_avis};{prep};{annee};{ca}"

def sud_est_row(i):
    """Problèmes : séparateur tabulation, types en anglais, date complète pour annee_ouverture,
    note au format 'X/5', ca_mensuel_k parfois en euros entiers, doublons."""
    lat = rand_float(43.1, 46.5, 4)
    lon = rand_float(2.0, 8.2, 4)
    typ = rand_type(TYPES_EN)
    nb_p = rand_int(4, 50)
    prix = rand_float(8.0, 22.0, 2)
    # note format "X/5" ou vide
    note_val = rand_float(2.5, 5.0, 1) if random.random() > 0.12 else ""
    note_str = f"{note_val}/5" if note_val != "" else ""
    nb_avis = rand_int(0, 3000)
    prep = rand_int(8, 40) if random.random() > 0.10 else ""
    # annee comme date complète
    annee = rand_int(1985, 2024)
    date_str = f"01/01/{annee}"
    # CA parfois en euros au lieu de k€
    ca_val = rand_int(8, 100)
    ca = ca_val * 1000 if random.random() < 0.20 else ca_val
    return f"{lat}\t{lon}\t{typ}\t{nb_p}\t{prix}\t{note_str}\t{nb_avis}\t{prep}\t{date_str}\t{ca}"

def idf_row(i):
    """Problèmes : lat/lon inversées, colonnes supplémentaires, noms de colonnes différents,
    nb_pizzas_carte parfois en toutes lettres, outliers extrêmes."""
    # Vraie lat IDF ~48.5-49.0, vrai lon ~1.5-3.0 → ici INVERSÉES dans le fichier
    true_lat = rand_float(48.2, 49.1, 4)
    true_lon = rand_float(1.5, 3.2, 4)
    typ = rand_type(TYPES_FR)
    # nb_pizzas parfois texte
    nb_p_val = rand_int(4, 45)
    nombres_texte = {4:"quatre",5:"cinq",6:"six",7:"sept",8:"huit",9:"neuf",10:"dix",
                     11:"onze",12:"douze",15:"quinze",20:"vingt",30:"trente"}
    nb_p = nombres_texte.get(nb_p_val, str(nb_p_val)) if random.random() < 0.12 else nb_p_val
    prix = 999 if random.random() < 0.04 else rand_float(8.0, 22.0, 2)
    note = rand_float(2.5, 5.0, 1) if random.random() > 0.10 else ""
    nb_avis = rand_int(0, 3500)
    prep = rand_int(8, 40) if random.random() > 0.08 else ""
    annee = rand_int(1985, 2024)
    ca = -50 if random.random() < 0.03 else rand_int(10, 115)
    email = f"contact{i}@pizza-{'idf' if random.random()>0.5 else 'paris'}.fr"
    phone = f"01 {rand_int(10,99)} {rand_int(10,99)} {rand_int(10,99)} {rand_int(10,99)}"
    # colonnes : lat, lon INVERSÉES, puis type, nb_pizzas, prix, note, avis, prep_time, opened, ca, email, telephone
    return f"{true_lon},{true_lat},{typ},{nb_p},{prix},{note},{nb_avis},{prep},{annee},{ca},{email},{phone}"

def grand_est_row(i):
    """Problèmes : pas d'en-tête, ordre des colonnes différent, temps_preparation en secondes,
    types avec casse/typos incohérentes, note_moyenne = 0 pour manquant."""
    lat = rand_float(46.5, 50.5, 4)
    lon = rand_float(3.5, 8.2, 4)
    typ = rand_type(TYPES_TYPOS)
    nb_p = rand_int(4, 50)
    prix = rand_float(7.5, 19.0, 2)
    # note: 0 pour manquant, sinon valeur normale
    note = 0 if random.random() < 0.15 else rand_float(2.5, 5.0, 1)
    nb_avis = rand_int(0, 2500)
    # temps en SECONDES au lieu de minutes
    prep_min = rand_int(8, 40)
    prep = prep_min * 60
    annee = rand_int(1980, 2024)
    ca = rand_int(6, 110)
    # Ordre : ca, annee, prep(sec), nb_avis, note, prix, nb_pizzas, type, lat, lon
    return f"{ca},{annee},{prep},{nb_avis},{note},{prix},{nb_p},{typ},{lat},{lon}"

def export_mixte_row(i, region_label=None):
    """Problèmes : lignes de séparation de région, coordonnées en DMS,
    ca_mensuel_k mélange k€ et €, décimales mélangées . et ,."""
    lat_dec = rand_float(43.0, 51.0, 4)
    lon_dec = rand_float(-4.5, 8.0, 4)

    # convertir lat en DMS
    lat_d = int(lat_dec)
    lat_m = int((lat_dec - lat_d) * 60)
    lat_s_val = round(((lat_dec - lat_d) * 60 - lat_m) * 60, 1)
    lat_dms = f"{lat_d}°{lat_m}'{lat_s_val}\"N"

    lon_abs = abs(lon_dec)
    lon_d = int(lon_abs)
    lon_m = int((lon_abs - lon_d) * 60)
    lon_s_val = round(((lon_abs - lon_d) * 60 - lon_m) * 60, 1)
    dir_lon = "O" if lon_dec < 0 else "E"
    lon_dms = f"{lon_d}°{lon_m}'{lon_s_val}\"{dir_lon}"

    typ = rand_type(TYPES_FR)
    nb_p = rand_int(4, 50)
    prix = rand_float(8.0, 22.0, 2)
    # mélanger . et , pour le prix
    if random.random() < 0.4:
        prix = str(prix).replace(".", ",")
    note = rand_float(2.5, 5.0, 1) if random.random() > 0.12 else ""
    nb_avis = rand_int(0, 2800)
    prep = rand_int(8, 40) if random.random() > 0.10 else ""
    annee = rand_int(1985, 2024)
    # CA mélangé : parfois en € entiers (x1000)
    ca_val = rand_int(8, 110)
    ca = ca_val * 1000 if random.random() < 0.25 else ca_val

    return f"{lat_dms},{lon_dms},{typ},{nb_p},{prix},{note},{nb_avis},{prep},{annee},{ca}"

# ── Génération des fichiers ─────────────────────────────────────────────────

N = 120  # lignes de données par fichier

# ── Fichier 1 : Nord-Ouest (déjà créé manuellement, on l'écrase proprement) ──
path1 = os.path.join(DATA_DIR, "donnees_nord_ouest.csv")
with open(path1, "w", encoding="utf-8") as f:
    f.write("# Export SliceLab - Région Nord-Ouest - 15/03/2024\n")
    f.write("# Fichier généré automatiquement - ne pas modifier\n")
    f.write("Latitude;Longitude;Type;nb_pizzas_carte;prix_moyen;note_moyenne;nb_avis;temps_preparation_moyen;annee_ouverture;ca_mensuel_k\n")
    for i in range(N):
        f.write(nord_ouest_row(i) + "\n")
print(f"[OK] {path1} ({N} lignes)")

# ── Fichier 2 : Sud-Est (TSV, anglais, dates, doublons) ─────────────────────
path2 = os.path.join(DATA_DIR, "donnees_sud_est.tsv")
header2 = "latitude\tlongitude\testablishment_type\tnb_pizzas\tavg_price\tavg_rating\tnb_reviews\tprep_time_min\topening_date\tmonthly_revenue_k"
rows2 = [sud_est_row(i) for i in range(N)]
# injecter ~10 doublons
for _ in range(10):
    rows2.append(random.choice(rows2[:80]))
random.shuffle(rows2)
with open(path2, "w", encoding="utf-8") as f:
    f.write(header2 + "\n")
    for r in rows2:
        f.write(r + "\n")
print(f"[OK] {path2} ({len(rows2)} lignes dont ~10 doublons)")

# ── Fichier 3 : Île-de-France (lat/lon inversées, colonnes extras) ───────────
path3 = os.path.join(DATA_DIR, "donnees_idf.csv")
header3 = "lat,lon,type,nb_pizzas,prix,note,avis,prep_time,opened,ca,email_contact,telephone"
with open(path3, "w", encoding="utf-8") as f:
    f.write(header3 + "\n")
    for i in range(N):
        f.write(idf_row(i) + "\n")
print(f"[OK] {path3} ({N} lignes, lat/lon inversées)")

# ── Fichier 4 : Grand-Est (pas d'en-tête, ordre différent, temps en sec) ────
path4 = os.path.join(DATA_DIR, "donnees_grand_est.csv")
with open(path4, "w", encoding="utf-8") as f:
    # PAS d'en-tête
    for i in range(N):
        f.write(grand_est_row(i) + "\n")
print(f"[OK] {path4} ({N} lignes, sans en-tête, ordre: ca,annee,prep_sec,nb_avis,note,prix,nb_pizzas,type,lat,lon)")

# ── Fichier 5 : Export mixte (DMS coords, lignes marqueurs, CA mélangé) ─────
path5 = os.path.join(DATA_DIR, "export_toutes_regions.csv")
regions = ["BRETAGNE", "NORMANDIE", "OCCITANIE", "ALSACE", "ILE-DE-FRANCE"]
with open(path5, "w", encoding="utf-8") as f:
    f.write("latitude,longitude,type_etablissement,nb_pizzas_carte,prix_moyen,note_moyenne,nb_avis,temps_preparation_moyen,annee_ouverture,ca_mensuel_k\n")
    idx = 0
    for reg in regions:
        f.write(f"=== REGION {reg} ===\n")
        for _ in range(N // len(regions)):
            f.write(export_mixte_row(idx, reg) + "\n")
            idx += 1
print(f"[OK] {path5} ({N} lignes + {len(regions)} lignes marqueurs, coordonnées DMS)")

print("\nTous les fichiers générés dans :", DATA_DIR)
print("\nRécapitulatif des problèmes :")
print("  donnees_nord_ouest.csv  → séparateur ;, décimale virgule, '€' dans prix, 2 lignes entête, N/A/'non renseigné'")
print("  donnees_sud_est.tsv     → séparateur TAB, types en anglais, date complète, note 'X/5', CA parfois en €, doublons")
print("  donnees_idf.csv         → lat/lon inversées, noms de colonnes différents, nb_pizzas en lettres, outliers prix/CA")
print("  donnees_grand_est.csv   → pas d'en-tête, ordre colonnes différent, prep en SECONDES, typos dans types")
print("  export_toutes_regions.csv → lignes marqueurs '=== REGION ===', coordonnées DMS, mélange . et , et k€/€")
