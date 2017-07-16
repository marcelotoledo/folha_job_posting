;; Source: http://hotsites.folha.com.br/2015/03/31/selecao/
;;
;; Sabe-se que por trás de cada cometa há um OVNI. Esses OVNIs
;; frequentemente buscam bons desenvolvedores aqui na Terra.
;; Infelizmente só têm espaço para levar um grupo de devs por vez. Para
;; a seleção, há um engenhoso esquema, da associação do nome do cometa
;; ao nome do grupo, que possibilita a cada grupo saber se será levado
;; ou não.

;; Os dois nomes, do grupo e do cometa, são convertidos em um número
;; que representa o produto das letras do nome, onde "A" é 1 e "Z" é
;; 26. Assim, o grupo "LARANJA" seria 12 * 1* 18 * 1 * 14 * 10 * 1 =
;; 30240. Se o resto da divisão do número do grupo por 45 for igual ao
;; resto da divisão do número do cometa por 45, então o grupo será
;; levado.

;; Para os cometas e grupos abaixo, qual grupo NÃO será levado?

;; [COMETA]  [GRUPO]
;;  HALLEY    AMARELO
;;  ENCKE     VERMELHO
;;  WOLF      PRETO
;;  KUSHIDA   AZUL
(ns folha-clojure.core
  (:gen-class))

(def translation-table {:A 1  :B 2  :C 3  :D 4  :E 5  :F 6
                        :G 7  :H 8  :I 9  :J 10 :K 11 :L 12
                        :M 13 :N 14 :O 15 :P 16 :Q 17 :R 18
                        :S 19 :T 20 :U 21 :V 22 :W 23 :X 24
                        :Y 25 :Z 26})

(def groups [{ :comet "HALLEY"  :group "AMARELO" }
             { :comet "ENCKE"   :group "VERMELHO" }
             { :comet "WOLF"    :group "PRETO" }
             { :comet "KUSHIDA" :group "AZUL" }])

(defn translate
  [string]
  (let [list (map str string)]
    (reduce * (map #(translation-table (keyword %)) list))))

(defn who-goes
  [sequence]
  (if (not-empty sequence)
    (let [item  (first sequence)]
      (println (format "Cometa: %10s (%d)\t (%d)\t Grupo %10s (%d)\t (%d)" (item :comet) (translate (item :comet)) (mod (translate (item :comet)) 45) (item :group) (translate (item :group)) (mod (translate (item :group)) 45)))
      (recur (rest sequence)))))

(defn -main
  [& args]
  (who-goes groups))
