(println "Dieses Programm berechnet die Fläche einer Ellipse")

;; ADD CODE HERE 

(require '[clojure.math :as math])

(println "Länge der ersten Achse:")

(def x (read-line))

(println "Länge der zweiten Achse:")

(def y (read-line))

(def result (* math/PI (/ (read-string x) 2) (/ (read-string y) 2)))

(println (str "Die Fläche ist: " result))