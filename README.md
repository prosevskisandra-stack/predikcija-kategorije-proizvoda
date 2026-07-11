# Predikcija kategorije proizvoda na osnovu naslova

Ovaj projekat koristi masinsko ucenje (Logisticku regresiju) za automatsku klasifikaciju proizvoda u odgovarajuce kategorije na osnovu tekstualnog naslova.

## Struktura projekta
* "products.csv" - Skup podataka koriscen za testiranje.
* "modelovanje.ipynb" - Jupyter sveska sa kompletnom analizom i razvojem resenja.
* "train_model.py" - Python skripta za automatsko treniranje modela.
* "predict_category.py" - Python skripta za interaktivn testiranje modela kroz terminal.
* "README.md" - Dokumentacija projekta.

## Uputstvo za pokretanje i testiranje

1. **Treniranje modela:**
    Pokrenite skriptu iz terminala kako bi se generisale binarne datoteke modela:
    ```bash
    python train_model.py