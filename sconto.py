# sconto.py
def main():
    prezzi = []
    animale = []
    riga = input("Passami il prezzo pieno e Y/N se animale: ")
    while riga != "-1":
        dati = riga.split(" ")
        prezzi.append(float(dati[0]))
        animale.append(dati[1] == 'Y')
        riga = input("Passami il prezzo pieno e Y/N se animale: ")
    sconto = calcola_sconto(prezzi, animale, len(prezzi))
    print(f"Sconto applicato: € {sconto:.2f}")

def calcola_sconto(prices, isPet, nr_articoli):
    nr_animali = sum(isPet)
    nr_non_animali = nr_articoli - nr_animali

    if nr_animali >= 1 and nr_non_animali >= 5:
        sconto = 0
        for i in range(nr_articoli):
            if not isPet[i]:
                sconto += prices[i] * 0.2
        return sconto
    else:
        return 0

main()
