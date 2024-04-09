(println "Dieses Programm berechnet die Flaeche einer Ellipse")

;; ADD CODE HERE 

(println "Laenge der ersten Achse:")
(def axis_a (read-line))
(println "Laenge der zweiten Achse:")
(def axis_b (read-line))

(def res (* Math/PI (/ (read-string axis_a) 2) (/ (read-string axis_b) 2)))

(println "Die Flaeche ist: " res)