; 1.3
(define (sum-of-squares a b) (+ (* a a) (* b b)))

(define (two-largest-sum-of-squares x y z)
  (cond (and (> x y) (> y z)) (sum-of-squares x y)
		(and (> x z) (> z y)) (sum-of-squares x z)
		(and (> y x) (> z x)) (sum-of-squares y z)))

(two-largest-sum-of-squares 1 1 1)
