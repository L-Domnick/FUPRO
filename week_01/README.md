# Woche 1

In dieser Woche solltest du deine Entwicklungsumgebung aufsetzen und in der Lage sein, ein simples Clojure Programm zum Laufen zu bekommen.
Fange mit der Übung am besten früh an. Wenn etwas nicht funktioniert, dann kannst du im Teams nach Hilfe fragen (am besten mit Screenshot vom Fehler).

## Entwicklungsumgebung

Installiere

- Java
    - Windows: https://www.java.com/en/download/help/windows_manual_download.html
    - OS X: z.B.: `brew install java`
    - Linux: z.B.: `apt-get install default-jdk`
- Clojure: https://clojure.org/guides/install_clojure
- Leiningen: https://leiningen.org/#install
- einen Editor deines Vertrauens (z.B. VS Code: https://code.visualstudio.com/)

## Einen eigenen Branch machen

Erstelle einen eigenen Git Branch für deine Lösung (der Branch Name sollte nicht mit denen von anderen kollidieren):

    git checkout -b meine_loesung_fuer_woche_1

## Clojure Basics

Als nächstes erweitere das Programm in `ellipse.clj`.
Es soll die Fläche einer Ellipse berechnen. Diese berechnet sich als $\pi \frac{a}{2} \frac{b}{2}$ wobei $a$ und $b$ die Längen der beiden Achsen sind.

Ein Beispiel Lauf des Programs (mit `clojure ellipse.clj`) könnte so aussehen.:

    Dieses Programm berechnet die Fläche einer Ellipse
    Länge der ersten Achse:
    8
    Länge der zweiten Achse:
    3
    Die Fläche ist: 18.849539999999998


Das Programm verwendet 3 Funktionen, die wir in der Vorlesung nicht hatten:

- println: Druckt die Parameter auf der Konsole in einer eigenen Zeile aus.
- read-line: Wartet auf Input vom Nutzer.
- read-string: Konvertiert einen String in eine Clojure Datenstruktur.

Anmerkung: Hier verwenden wir read-string um einen String mit möglichst wenig Aufwand zu einer Zahl zu parsen.
Allgemein ist read-string nicht sicher um beliebigen Input zu parsen. Später bekommen wir Alternativen dafür.

## Ergebnis einchecken und Merge Request erstellen

Stelle sicher, dass du alle deine Änderungen commited hast:

    git add ellipse.clj
    git commit

Dann pushe den ganzen Branch nach Gitlab:

    git push --set-upstream origin meine_loesung_fuer_woche_1

Nun erstelle noch einen Merge Request in Gitlab für diesen neuen Branch.
