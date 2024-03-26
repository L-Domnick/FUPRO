# 24SS FuPr Übungen

Hier finden sich die Hausaufgaben zur Vorlesung FuPr (siehe https://ki.inf.th-bingen.de/lectures/24ss-fupr/).

Jede Hausaufgabe bekommt einen eigenen Folder. Ihr reicht die Hausaufgaben als Merge Requests ein.

## Ablauf

- Holt euch den aktuellen Stand des Repositories
    - Indem ihr das Repo initial auscheckt
        - `git clone git@gitlab.rlp.net:f.dahms/24ss-fupr-uebungen.git`
    - Indem ihr das Repo updated
        - `git checkout main`
        - `git pull`
- Erzeugt einen neuen Branch (`git checkout -b neuer_branch`)
- Editiert die Dateien im entsprechenden Folder und löst die entsprechende Aufgabe
- Commited eure Änderungen
    - `git add .`
    - `git commit`
- Die Änderungen nach GitLab pushen
    - `git push --set-upstream origin neuer_branch`
- Erstellt einen Merge Request in der gitlab UI
