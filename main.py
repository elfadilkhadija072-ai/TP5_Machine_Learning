# main.py
# Point d'entrée principal du pipeline TP5 — Apprentissage Automatique

from data_generation import generate_hospital_data
from visualization   import visualize_hospital_data, plot_confusion_heatmaps, plot_kiviat
from data_export     import save_hospital_data
from ml_pipeline     import prepare_data_for_classification, train_and_evaluate_models


def main():
    print("=" * 55)
    print("  TP5 — Pipeline ML : Données Hospitalières Synthétiques")
    print("=" * 55)

    # ── 1. Génération des données ──────────────────────────────
    print("\n[1/5] Génération des données...")
    df = generate_hospital_data(300)
    print(df.head())
    print(f"\nShape : {df.shape}")
    print(df.describe())

    # ── 2. Visualisation ──────────────────────────────────────
    print("\n[2/5] Visualisation des données...")
    visualize_hospital_data(df)

    # ── 3. Export dans plusieurs formats ──────────────────────
    print("\n[3/5] Export des données...")
    save_hospital_data(df, 'csv',   'hospital_data')
    save_hospital_data(df, 'excel', 'hospital_data')
    save_hospital_data(df, 'json',  'hospital_data')
    save_hospital_data(df, 'xml',   'hospital_data')
    save_hospital_data(df, 'pdf',   'hospital_data')

    # ── 4. Préparation pour le ML ──────────────────────────────
    print("\n[4/5] Préparation des données pour la classification...")
    X_train, X_val, X_test, y_train, y_val, y_test, encoders = \
        prepare_data_for_classification(df, target_col='severity')

    # ── 5. Entraînement + Évaluation des modèles ──────────────
    print("\n[5/5] Entraînement et évaluation des modèles...")
    results = train_and_evaluate_models(X_train, X_val, y_train, y_val)

    # ── 6. Visualisation des résultats ────────────────────────
    print("\n[6/6] Visualisation des résultats...")
    class_names = ['Low', 'Medium', 'High']
    plot_confusion_heatmaps(results, class_names)
    plot_kiviat(results, metric='f1-score')

    print("\n✅ Pipeline terminé avec succès !")


if __name__ == "__main__":
    main()