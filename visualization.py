# visualization.py
# Visualisation du tableau de bord + matrices de confusion + diagramme de Kiviat

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


def visualize_hospital_data(df: pd.DataFrame) -> None:
    """
    Affiche un tableau de bord 3×2 des distributions des variables hospitalières.

    Paramètre
    ---------
    df : pd.DataFrame contenant les données hospitalières.
    """
    sns.set_style("whitegrid")
    fig, axes = plt.subplots(3, 2, figsize=(14, 12))
    axes = axes.flatten()

    # 1. Répartition par sexe
    sns.countplot(x='sex', data=df, ax=axes[0], palette="Set2")
    axes[0].set_title('Sex Distribution (0=Female, 1=Male)')
    axes[0].set_xlabel('Sexe')
    axes[0].set_ylabel('Nombre de patients')

    # 2. Distribution d'âge avec ligne de moyenne
    sns.histplot(df['age'], bins=20, kde=True, ax=axes[1], color='skyblue')
    axes[1].axvline(df['age'].mean(), color='red', linestyle='--',
                    label=f"Mean: {df['age'].mean():.2f}")
    axes[1].legend()
    axes[1].set_title('Age Distribution')

    # 3. Niveaux de gravité (ordre fixe)
    order = ['Low', 'Medium', 'High']
    sns.countplot(x='severity', data=df, ax=axes[2], palette="pastel", order=order)
    axes[2].set_title('Severity Levels')

    # 4. Pression artérielle avec courbe KDE
    sns.histplot(df['blood_pressure'], bins=20, kde=True, ax=axes[3], color='orange')
    axes[3].axvline(df['blood_pressure'].mean(), color='red', linestyle='--',
                    label=f"Mean: {df['blood_pressure'].mean():.2f}")
    axes[3].legend()
    axes[3].set_title('Blood Pressure Distribution')

    # 5. Réadmissions (histogramme discret)
    sns.histplot(df['readmissions'], bins=10, kde=False, ax=axes[4], color='lightgreen')
    axes[4].axvline(df['readmissions'].mean(), color='red', linestyle='--',
                    label=f"Mean: {df['readmissions'].mean():.2f}")
    axes[4].legend()
    axes[4].set_title('Readmissions Distribution')

    # 6. Sous-graphe vide
    fig.delaxes(axes[5])

    plt.suptitle('Tableau de bord — Données Hospitalières Synthétiques', fontsize=14, y=1.01)
    plt.tight_layout()
    plt.show()


def plot_confusion_heatmaps(results: dict, class_names: list) -> None:
    """
    Affiche les matrices de confusion de chaque modèle sous forme de heatmap (grille 2×2).

    Paramètres
    ----------
    results     : dict retourné par train_and_evaluate_models()
    class_names : liste des noms de classes (ex: ['Low', 'Medium', 'High'])
    """
    fig, axes = plt.subplots(2, 2, figsize=(12, 10))
    axes = axes.flatten()

    for i, (name, result) in enumerate(results.items()):
        sns.heatmap(
            result['conf_matrix'],
            annot=True, fmt='d',
            cmap='Blues',
            ax=axes[i],
            xticklabels=class_names,
            yticklabels=class_names,
        )
        axes[i].set_title(f"{name} — Confusion Matrix")
        axes[i].set_xlabel('Predicted')
        axes[i].set_ylabel('Actual')

    plt.tight_layout()
    plt.show()


def plot_kiviat(results: dict, metric: str = 'f1-score') -> None:
    """
    Affiche un diagramme de Kiviat (radar chart) des F1-scores par classe et par modèle.

    Paramètres
    ----------
    results : dict retourné par train_and_evaluate_models()
    metric  : métrique à visualiser ('f1-score', 'precision', 'recall')
    """
    labels = ['Low', 'Medium', 'High']
    num_vars = len(labels)
    angles = np.linspace(0, 2 * np.pi, num_vars, endpoint=False).tolist()
    angles += angles[:1]  # Fermeture du polygone

    fig = plt.figure(figsize=(8, 6))
    ax  = plt.subplot(111, polar=True)

    colors = ['blue', 'orange', 'green', 'red']

    for (model_name, result), color in zip(results.items(), colors):
        stats = [result['report'][str(i)][metric] for i in range(num_vars)]
        stats += stats[:1]  # Fermeture
        ax.plot(angles, stats, label=model_name, color=color)
        ax.fill(angles, stats, alpha=0.1, color=color)

    ax.set_thetagrids(np.degrees(angles[:-1]), labels)
    plt.title(f"Radar Plot : {metric}", pad=15)
    plt.legend(loc='upper right', bbox_to_anchor=(1.2, 1.1))
    plt.tight_layout()
    plt.show()