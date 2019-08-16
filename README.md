# grafy
Zadanie grafy do badania Ś

W każdym trialu pojawiają się obok siebie dwie macierze 3x3 na których wyświetlana są grafy, czyli kółka-wierzchołki 
oraz strzałki między nimi. Strzałki mogą być dwustronne. 

Na grafie wzorcowym po lewej stronie dwa kółka oznaczone zostają poprzez jeden z dwóch kolorów (np. niebieski i żółty), 
pozostałe kółka są czarne. Do każdego z kolorów przypisany jest na stałe (w całym zadaniu) określony przycisk myszki - 
lewy bądź prawy. 

Na grafie po prawej stronie należy kliknąć określonym przyciskiem myszki na odpowiednie wierzchołki. Wszystkie 
wierzchołki w tym grafie są czarne. Kliknięcie na wierzchołek danym przyciskiem powinno skutkować krótkotrwałym 
(np. 0.5 sek) oznaczeniem tego wierzchołka odpowiednim kolorem.

Trial kończy się po użyciu każdego z  przycisków myszy na dwóch różnych wierzchołkach, po użyciu tego samego przycisku 
myszy na dwóch różnych wierzchołkach (odpowiedź niepoprawna) lub po upływie czasu.

Triale sczytywane są z pliku. Jeśli dany trial ma parametr FEED ustawiony na 1 (co może wystąpić również dla trialu 
poza treningiem), to po udzieleniu odpowiedzi zostaje wyświetlony feedback - właściwe wierzchołki w prawym grafie 
zostają wypełnione odpowiednimi kolorami.

W pliku wynikowych zostaje m.in. zapisana informacja o:
* numerach wierzchołków (pól macierzy), które zostały zaznaczone lewym oraz prawym przyciskiem (lub “-” jeśli przycisk 
nie został wykorzystany)
* poprawności (1/0) dla lewego oraz prawego przycisku z osobna
* poprawności (1/0) w trialu (odpowiedź jest poprawna gdy oba kliknięcia są poprawne)

Odpowiedzi udzielane są myszką.

Trening z feedbackiem “w trialu” - znaczy to, że item nie znika po udzieleniu odpowiedzi, a informacja czy odpowiedź 
była poprawna czy nie, wyświetlana jest u dołu ekranu pod itemem. Oprócz tej informacji, poprawne rozwiązanie zostaje 
oznaczona na itemie. Feedback znika po kliknięciu myszką (a może jakiś inny sposób?)

Trening jest warunkowy - warunkiem przejścia jest osiągnięcie określonej poprawności w treningu (parametr do ustawienia 
w configu). Jeśli wymagana poprawność nie zostaje osiągnięta, pojawia się odpowiednia informacja i trening rozpoczyna 
się ponownie - aż do skutku.

Tak jak ostatnio, istnieje ograniczenie czasowe na trial, a na określoną ilość czasu przed jego osiągnięciem wyświetlona
zostaje ikonka zegarka.
