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

## 🛠️ Installation & Exécution

### 1. Cloner le projet

```bash
git clone https://github.com/TON_USERNAME/tp5-donnees-hospitalieres.git
cd tp5-donnees-hospitalieres
```

### 2. Créer et activer l'environnement virtuel

```bash
# Créer l'environnement
python -m venv venv_tp5

# Activer (Windows)
venv_tp5\Scripts\activate

# Activer (Linux / Mac)
source venv_tp5/bin/activate
```

### 3. Installer les dépendances

```bash
pip install pandas matplotlib numpy openpyxl reportlab
```

### 4. Lancer la génération des données

```bash
python data_generation.py
```

### 5. Lancer l'export des données

```bash
python data_export.py
```

---

## 🚀 Publier sur GitHub depuis VS Code

### 🔧 Configuration initiale (une seule fois)

```bash
# 1. Initialiser Git
git init

# 2. Créer le .gitignore
echo "venv_tp5/" >> .gitignore
echo "venv_tp6/" >> .gitignore
echo "__pycache__/" >> .gitignore
echo "*.pyc" >> .gitignore

# 3. Ajouter TOUS les fichiers (scripts + données + photos)
git add .

# 4. Vérifier que les images sont bien trackées
git status

# 5. Premier commit
git commit -m "feat: TP5 - Tableau de bord données hospitalières synthétiques"

# 6. Lier au dépôt GitHub (remplacer TON_USERNAME)
git remote add origin https://github.com/TON_USERNAME/tp5-donnees-hospitalieres.git

# 7. Envoyer sur GitHub
git branch -M main
git push -u origin main
```

---

### 📸 Tracker uniquement les photos

```bash
# Ajouter tout le dossier screenshots
git add "screen_shots/resultats tp5/"

# Ou photo par photo
git add "screen_shots/resultats tp5/GRAPHE1.png"
git add "screen_shots/resultats tp5/GRAPHE2.png"
git add "screen_shots/resultats tp5/GRAPHE3.png"
git add "screen_shots/resultats tp5/RESULT TERIMAL1.png"
git add "screen_shots/resultats tp5/RESULTTERMINAL2.png"
git add "screen_shots/resultats tp5/TERMINAL3.png"
git add "screen_shots/resultats tp5/TERMINAL4.png"

git commit -m "feat: ajout screenshots tableau de bord TP5"
git push
```

> ⚠️ **Important** : Les noms de dossiers/fichiers avec des **espaces** doivent être entre guillemets dans le terminal.

---

### 🔄 Mettre à jour après modification

```bash
git status
git add .
git commit -m "update: description de ce qui a changé"
git push
```

---

### 🖥️ Via l'interface VS Code (sans terminal)

| Étape | Action |
|---|---|
| 1 | Ouvrir **Source Control** : `Ctrl + Shift + G` |
| 2 | Cliquer **`+`** sur chaque fichier pour le stager |
| 3 | Écrire le message de commit |
| 4 | Cliquer **✓ Commit** |
| 5 | Cliquer **Sync Changes / Push** |

---

## 📋 Commandes Git — Référence Rapide

```bash
git init                    # Initialiser un dépôt Git
git status                  # Voir l'état des fichiers
git add .                   # Stager tous les fichiers
git add "nom fichier"       # Stager un fichier (avec guillemets si espace)
git commit -m "message"     # Créer un commit
git push                    # Envoyer sur GitHub
git pull                    # Récupérer les modifications distantes
git log --oneline           # Voir l'historique des commits
git ls-files                # Lister tous les fichiers trackés
git remote -v               # Voir les dépôts distants configurés
git diff                    # Voir les modifications non commitées
```

---

## 📊 Statistiques Clés du Dataset

| Indicateur | Valeur |
|---|---|
| Âge moyen | **50.65 ans** |
| Pression artérielle moyenne | **121.12 mmHg** |
| Réadmissions moyennes | **2.03** |
| Niveaux de sévérité | Low / Medium / High |
| Formats d'export | CSV, JSON, PDF, XLSX |
| Graphiques générés | 5 |

---

## 📝 Remarques

- Données **100% synthétiques** — aucune donnée patient réelle utilisée
- Les `venv_tp5/` et `venv_tp6/` sont ignorés via `.gitignore`
- Les images s'affichent automatiquement sur GitHub grâce aux chemins relatifs avec `%20` pour les espaces

---

## 👤 Auteur

Projet réalisé dans le cadre du cours **TP5 — Traitement et Visualisation de Données**

---

## 📄 Licence

Usage académique uniquement — tous droits réservés.
