(loop [n 999
       sum 0]
  (if (= n 1)
    (println sum) #! 233168
    (recur 
      (dec n)
      (if (or (zero? (mod n 3)) (zero? (mod n 5)))
        (+ sum n)
        sum))))

