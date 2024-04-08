(ns ellipse)

(println "Dieses Programm berechnet die Fläche einer Ellipse")

(defn ellipse_area [a b] (* Math/PI (/ a 2) (/ b 2)))

(println "Länge der ersten Achse:")
(def a_axis (read-line))

(println "Länge der zweiten Achse:")
(def b_axis (read-line ))

(println "Die Fläche ist " (ellipse_area (read-string a_axis) (read-string b_axis)))

