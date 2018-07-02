# TomTom
Przemyślenia co stworzyć dla gry
1. Stworzyć sprawdzenie czy plik istniej gdy czytamy z pliku,
2. Stworzyć klasę, która będzie przechowywała mapę
    1. W mapie musi być informację o pokojach.
        - analizuje czy podana konfiguracja pomieszczeń jest możliwa
        - w sytuacji gdy konfiguracja jest niemożliwa wyrzucić info o błędzie
            w pliku wskazać gdzie jest błąd
    2. Powinno mieć też funkcje drukuj pokoje
3. Stworzyć klasę pokój 
    1. Pokój zawiera atrybuty:
        - nazwę;
        - w których kierunkach może się poruszać;
        - po przejściu każdego z kierunków w którym pokoju się znajdziemy
        - lokalizacja pokoju
4. Stworzyć klasę ruch
    - Ruch pobiera informacje – mapa
    - pobiera informacje gdzie chcemy iść i analizuje czy jest możliwy
    - jeśli nie jest wyrzuca błąd, jeśli jest wykonuje ruch
5. Main 
    pobiera informacje gdzie jest plik z mapą
    tworzy obiekt mapa
    układa gracza w pierwszym pokoju na liście
    pyta gdzie się ruszyć
    zamyka program






Przemyślenia co przetestować:
1.	Ruchy w każdy kierunku - zrobione
2.	Ruch w niemożliwym kierunku - zrobione
3.	Ruch z nieistniejącego pokoju - zrobione
4.	Błąd w mapie
    a.	zła nazwa pokoju - zrobione
    b.	zła nazwa kierunku - zrobione
    c.	nie istniejący kierunek - zrobione
    d.	plik z powtarzającymi się pokojami - zrobione
    e.	jakiś bełkot - zrobione
5.	Błędy w uruchomieniu maina - zrobione
6.	Automatyczne uruchomienie maina - zrobione
