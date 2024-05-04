# Snake Game

Prosta gra węża napisana w Pythonie z wykorzystaniem modułu Turtle.

## Jak grać

1. Uruchom plik `snake_game.py`.
2. Steruj wężem za pomocą klawiszy WSAD.
3. Zbieraj czerwone kwadraty (jedzenie), aby zwiększać wynik.
4. Unikaj zderzeń z krawędziami planszy oraz z samym sobą.

## Elementy gry

### Wąż

- Wąż reprezentowany jest przez linię kwadratów.
- Zaczyna grę z trzema segmentami.
- Kiedy zje jedzenie, wydłuża się o jeden segment.

### Jedzenie

- Jedzenie reprezentowane jest przez czerwony kwadrat.
- Po zjedzeniu przez węża, pojawia się w losowym miejscu na planszy.

### Wynik

- Aktualny wynik wyświetlany jest na górze planszy.
- Zwiększa się za każdym razem, gdy wąż zje jedzenie.
- Najlepszy wynik jest przechowywany

## Struktura plików

- `snake_game.py`: Główny plik zawierający logikę gry.
- `snake.py`: Klasa reprezentująca węża i jego zachowanie.
- `food.py`: Klasa reprezentująca jedzenie.
- `scoreboard.py`: Klasa reprezentująca wynik i jego wyświetlanie.

## Rozszerzalność

- Gra została napisana z myślą o łatwej rozszerzalności.
- Możesz modyfikować wygląd węża, jedzenia i planszy zmieniając kolory i kształty.
- Możesz również dostosować trudność gry poprzez zmianę prędkości węża lub szybkości pojawiania się jedzenia.


