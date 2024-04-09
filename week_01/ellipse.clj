(println "Dieses Programm berechnet die Fläche einer Ellipse")

(println "Länge der ersten Achse:")
(def a (read-line))

(println "Länge der zweiten Achse:")
(def b (read-line))

(def result (* Math/PI (* (/ (read-string a) 2) (/ (read-string b) 2))))

(println (str "Die Fläche ist: " result))