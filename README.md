# 🏥 TP5 — Tableau de Bord : Données Hospitalières Synthétiques

> **Projet Python** — Génération, traitement, export et visualisation de données hospitalières synthétiques sous forme de tableau de bord interactif.

---

## 📌 Objectif du Projet

Ce TP a pour but de :
- **Générer** des données hospitalières fictives mais réalistes avec Python
- **Exporter** ces données dans plusieurs formats (CSV, JSON, PDF, XLSX)
- **Visualiser** les indicateurs clés sous forme de graphiques statistiques
- **Analyser** des distributions médicales : âge, sexe, sévérité, pression artérielle, réadmissions

---

## 📁 Structure du Projet

```
tp5/
│
├── 📄 data_generation.py          # Script de génération des données synthétiques
├── 📄 data_export.py              # Script d'export multi-format
│
├── 📊 hospital_data.csv           # Données au format CSV
├── 📊 hospital_data.json          # Données au format JSON
├── 📊 hospital_data.pdf           # Données au format PDF
├── 📊 hospital_data.xlsx          # Données au format Excel
│
├── 🖼️ screen_shots/
│   └── resultats tp5/
│       ├── GRAPHE1.png            # Sex Distribution + Age Distribution
│       ├── GRAPHE2.png            # Severity Levels
│       ├── GRAPHE3.png            # Blood Pressure + Readmission
│       ├── RESULT TERIMAL1.png    # Résultat terminal 1
│       ├── RESULTTERMINAL2.png    # Résultat terminal 2
│       ├── TERMINAL3.png          # Résultat terminal 3
│       └── TERMINAL4.png          # Résultat terminal 4
│
├── 📂 venv_tp5/                   # Environnement virtuel (non versionné)
├── 📂 venv_tp6/                   # Environnement virtuel TP6 (non versionné)
├── 📄 .gitignore
└── 📄 README.md
```

---

## 📈 Tableau de Bord — Visualisations

### 🔵 Graphique 1 — Sex Distribution & Age Distribution

![Sex Distribution et Age Distribution](screen_shots/resultats%20tp5/GRAPHE1.png)

| Indicateur | Détail |
|---|---|
| Sex Distribution | Répartition Femmes (0) vs Hommes (1) |
| Age Distribution | Histogramme des âges — **Moyenne : 50.65 ans** |

---

### 🟠 Graphique 2 — Severity Levels

![Severity Levels](screen_shots/resultats%20tp5/GRAPHE2.png)

| Niveau | Description |
|---|---|
| **Low** | Cas peu sévères — majorité des patients |
| **Medium** | Cas modérés |
| **High** | Cas critiques nécessitant une attention urgente |

---

### 🟡 Graphique 3 — Blood Pressure & Readmission Distribution

![Blood Pressure et Readmission Distribution](screen_shots/resultats%20tp5/GRAPHE3.png)

| Indicateur | Valeur |
|---|---|
| Pression artérielle moyenne | **121.12 mmHg** |
| Nombre moyen de réadmissions | **2.03** |
| Plage pression | 80 à 160 mmHg |
| Plage réadmissions | 0 à 6 |

---

## 🖥️ Résultats Terminal

### Terminal 1 — Exécution `data_generation.py`

![Résultat Terminal 1](screen_shots/resultats%20tp5/RESULT%20TERIMAL1.png)

---

### Terminal 2 — Exécution `data_export.py`

![Résultat Terminal 2](screen_shots/resultats%20tp5/RESULTTERMINAL2.png)

---

### Terminal 3

![Terminal 3](screen_shots/resultats%20tp5/TERMINAL3.png)

---

### Terminal 4

![Terminal 4](screen_shots/resultats%20tp5/TERMINAL4.png)

---

## ⚙️ Technologies Utilisées

| Technologie | Rôle |
|---|---|
| `Python 3.x` | Langage principal |
| `pandas` | Manipulation des données |
| `matplotlib` | Visualisation / graphiques |
| `numpy` | Calculs numériques |
| `openpyxl` | Export Excel (.xlsx) |
| `reportlab` | Export PDF |
| `json` | Export JSON |

---


