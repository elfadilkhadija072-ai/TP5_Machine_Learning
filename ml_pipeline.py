# ml_pipeline.py
# Préparation des données + entraînement + évaluation des modèles ML

import pandas as pd
from sklearn.model_selection     import train_test_split
from sklearn.preprocessing       import StandardScaler, LabelEncoder
from sklearn.neighbors           import KNeighborsClassifier
from sklearn.linear_model        import Perceptron
from sklearn.naive_bayes         import GaussianNB
from sklearn.neural_network      import MLPClassifier
from sklearn.metrics             import classification_report, confusion_matrix


def prepare_data_for_classification(df: pd.DataFrame, target_col: str):
    """
    Prépare le DataFrame pour la classification :
    - Encode les variables catégorielles (LabelEncoder)
    - Normalise les features numériques (StandardScaler)
    - Divise en train (60%) / validation (20%) / test (20%)
    - Exclut patient_id des features (anti-surapprentissage)

    Retourne
    --------
    X_train, X_val, X_test, y_train, y_val, y_test, label_encoders
    """
    df_encoded    = df.copy()
    label_encoders = {}

    # Encodage de toutes les colonnes catégorielles (type object)
    for col in df.select_dtypes(include=['object']).columns:
        le = LabelEncoder()
        df_encoded[col] = le.fit_transform(df[col])
        label_encoders[col] = le

    # Séparation features / cible (on exclut patient_id)
    X = df_encoded.drop(columns=[target_col, 'patient_id'])
    y = df_encoded[target_col]

    # Normalisation (importante pour KNN et MLP)
    scaler   = StandardScaler()
    X_scaled = scaler.fit_transform(X)

    # Split : 60% train, 40% temp
    X_train, X_temp, y_train, y_temp = train_test_split(
        X_scaled, y, test_size=0.4, random_state=42
    )
    # Split temp → 50% val, 50% test → chacun = 20% du total
    X_val, X_test, y_val, y_test = train_test_split(
        X_temp, y_temp, test_size=0.5, random_state=42
    )

    print(f"📊 Train : {len(X_train)} | Validation : {len(X_val)} | Test : {len(X_test)}")
    return X_train, X_val, X_test, y_train, y_val, y_test, label_encoders


def train_and_evaluate_models(X_train, X_val, y_train, y_val) -> dict:
    """
    Entraîne et évalue 4 algorithmes de classification sur les données de validation.

    Algorithmes :
        - KNN          (k=3)
        - Perceptron   (max_iter=1000)
        - Naive Bayes  (Gaussien)
        - MLP          (couche cachée 50 neurones, max_iter=1000)

    Retourne
    --------
    dict : { nom_modèle: { 'model', 'report', 'conf_matrix' } }
    """
    models = {
        'KNN':        KNeighborsClassifier(n_neighbors=3),
        'Perceptron': Perceptron(max_iter=1000, random_state=42),
        'NaiveBayes': GaussianNB(),
        'NeuralNet':  MLPClassifier(hidden_layer_sizes=(50,), max_iter=1000, random_state=42),
    }

    results = {}
    for name, model in models.items():
        model.fit(X_train, y_train)
        y_pred = model.predict(X_val)

        report   = classification_report(y_val, y_pred, output_dict=True)
        conf_mat = confusion_matrix(y_val, y_pred)

        results[name] = {
            'model':       model,
            'report':      report,
            'conf_matrix': conf_mat,
        }

        # Affichage console
        print(f"\n{'='*45}")
        print(f"  Modèle : {name}")
        print(f"{'='*45}")
        print(classification_report(y_val, y_pred, target_names=['Low', 'Medium', 'High']))

    return results