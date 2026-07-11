import pickle

try:
    with open("model.pkl", "rb") as f:
        model = pickle.load(f)
    with open("vectorizer.pkl", "rb") as f:
        vectorizer = pickle.load(f)
except FileNotFoundError:
    print("Greska: Model nije pronadjen. Prvo pokrenite train_model.py!")
    exit()
print("--- Interaktivno testiranje modela ---")
print("Unesite naslov proizvoda (ili izlaz za kraj):")

while True:
    user_input = input("\nNaslov proizvoda: ")
    if user_input.lower() == "izlaz":
        break

    input_tfidf = vectorizer.transform([user_input.lower()])
    prediction = model.predict(input_tfidf)[0]

    print(f"Predvidjena kategorija: {prediction}")