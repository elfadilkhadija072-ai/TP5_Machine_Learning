# data_generation.py
# Génération de données hospitalières synthétiques

import pandas as pd
import numpy as np


def generate_hospital_data(n: int) -> pd.DataFrame:
    """
    Génère n enregistrements patients synthétiques avec des distributions réalistes.

    Paramètres
    ----------
    n : int
        Nombre de patients à générer.

    Retourne
    --------
    pd.DataFrame avec colonnes :
        patient_id, sex, age, severity, blood_pressure, readmissions
    """
    np.random.seed(42)  # Reproductibilité garantie

    # 1. ID unique séquentiel
    patient_id = np.arange(1, n + 1)

    # 2. Sexe : Bernoulli(0.5) → 0=Femme, 1=Homme
    sex = np.random.binomial(1, 0.5, size=n)

    # 3. Âge : Uniform(20, 80), arrondi à 1 décimale
    age = np.random.uniform(20, 80, size=n).round(1)

    # 4. Gravité : Multinomial([Low=0.5, Medium=0.3, High=0.2])
    severity_probs  = [0.5, 0.3, 0.2]
    severity_levels = ['Low', 'Medium', 'High']
    severity_indices = np.random.choice(len(severity_levels), size=n, p=severity_probs)
    severity = [severity_levels[i] for i in severity_indices]

    # 5. Pression artérielle : Normal(μ=120, σ=15), arrondie à 1 décimale
    blood_pressure = np.random.normal(loc=120, scale=15, size=n).round(1)

    # 6. Réadmissions : Poisson(λ=2)
    readmissions = np.random.poisson(lam=2, size=n)

    df = pd.DataFrame({
        'patient_id':     patient_id,
        'sex':            sex,
        'age':            age,
        'severity':       severity,
        'blood_pressure': blood_pressure,
        'readmissions':   readmissions,
    })

    return df