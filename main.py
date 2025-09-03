import os
import time

def czytelny_czas(sekundy):
    """Zamienia czas w sekundach na czytelną formę."""
    minuty, sekundy = divmod(int(sekundy), 60)
    godziny, minuty = divmod(minuty, 60)
    if godziny > 0:
        return f"{godziny} godz. {minuty} min {sekundy} sek"
    elif minuty > 0:
        return f"{minuty} minut i {sekundy} sekund"
    else:
        return f"{sekundy} sekund"

def przeszukaj_katalog(start_path, rozszerzenie, fraza):
    znalezione = []
    for root, dirs, files in os.walk(start_path):
        print(f"[KATALOG] {root}")
        for file in files:
            if file.endswith(rozszerzenie):
                sciezka = os.path.join(root, file)
                print(f"  [PLIK] Czytam: {sciezka}")
                try:
                    with open(sciezka, 'r', encoding='utf-8', errors='ignore') as f:
                        for nr_linii, linia in enumerate(f, start=1):
                            if fraza in linia:
                                print(f"    >>> ZNALEZIONO frazę '{fraza}' w pliku {sciezka} w linii {nr_linii}")
                                znalezione.append((sciezka, nr_linii, linia.strip()))
                except Exception as e:
                    print(f"    [BŁĄD] Nie można odczytać pliku: {sciezka} ({e})")
    return znalezione

def main():
    print("=== Wyszukiwarka fraz w plikach ===")
    start_path = input("Podaj ścieżkę początkową (np. C:\\Users\\Twoj_User\\Documents): ").strip()
    rozszerzenie = input("Podaj rozszerzenie pliku (np. .txt): ").strip()
    fraza = input("Podaj frazę do wyszukania: ").strip()

    start_time = time.time()
    wyniki = przeszukaj_katalog(start_path, rozszerzenie, fraza)
    end_time = time.time()

    print("\n" + "="*60)
    print("PODSUMOWANIE WYNIKÓW:")
    if wyniki:
        for sciezka, nr_linii, tresc in wyniki:
            print(f"{sciezka} (linia {nr_linii}): {tresc}")
    else:
        print("Nie znaleziono żadnych wyników.")
    print("="*60)
    print(f"Czas wyszukiwania: {czytelny_czas(end_time - start_time)}")

    input("\nNaciśnij Enter, aby zakończyć...")

if __name__ == "__main__":
    main()
