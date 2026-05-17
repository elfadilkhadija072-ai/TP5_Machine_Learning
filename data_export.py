# data_export.py
# Export des données dans plusieurs formats (CSV, Excel, JSON, XML, PDF)

import pandas as pd
from fpdf import FPDF


def save_hospital_data(df: pd.DataFrame, format: str, filename: str) -> None:
    """
    Sauvegarde le DataFrame dans le format demandé.

    Paramètres
    ----------
    df       : pd.DataFrame à sauvegarder.
    format   : 'csv' | 'excel' | 'json' | 'xml' | 'pdf'  (insensible à la casse)
    filename : nom de fichier sans extension.
    """
    format = format.lower()
    supported = ['csv', 'excel', 'json', 'xml', 'pdf']

    if format not in supported:
        raise ValueError(f"Format '{format}' non supporté. Choisissez parmi : {supported}")

    if format == 'csv':
        df.to_csv(f"{filename}.csv", index=False)
        print(f"✅ Fichier sauvegardé : {filename}.csv")

    elif format == 'excel':
        df.to_excel(f"{filename}.xlsx", index=False)
        print(f"✅ Fichier sauvegardé : {filename}.xlsx")

    elif format == 'json':
        df.to_json(f"{filename}.json", orient='records', indent=4)
        print(f"✅ Fichier sauvegardé : {filename}.json")

    elif format == 'xml':
        df.to_xml(f"{filename}.xml", index=False)
        print(f"✅ Fichier sauvegardé : {filename}.xml")

    elif format == 'pdf':
        _export_pdf(df, filename)
        print(f"✅ Fichier sauvegardé : {filename}.pdf")


def _export_pdf(df: pd.DataFrame, filename: str) -> None:
    """Génère un PDF tabulaire (limité aux 30 premières lignes)."""
    pdf = FPDF()
    pdf.add_page()
    pdf.set_font("Arial", size=9)

    col_width  = pdf.w / (len(df.columns) + 1)
    row_height = 8
    spacing    = 1.2

    # En-tête
    pdf.set_fill_color(200, 220, 255)
    for col in df.columns:
        pdf.cell(col_width, row_height * spacing, str(col), border=1, fill=True)
    pdf.ln(row_height * spacing)

    # Données (max 30 lignes)
    for _, row in df.head(30).iterrows():
        for item in row:
            pdf.cell(col_width, row_height * spacing, str(item), border=1)
        pdf.ln(row_height * spacing)

    pdf.output(f"{filename}.pdf")