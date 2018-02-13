; 1.5
(define (p) (p))

(define (test x y)
  (if (= x 0)
  	0
  	y))

(test 0 (p))

; - Applicative order:
;   - Evaluate the body of the procedure (value of the combination's operator)
;     with each formal parameter replaced by the correspoding arguments
;     (value of the combination's operands).
;
; - Normal order:
;   - Fully expand the combination's operators until only primitive operators
;     are involved, and only then evaluate the remaining combinations.
;
; With applicative order, the interpreter will get stuck evaluating the second
; operand to test, as p evaluates to itself.
; With normal order, the second operand to test is never evaluated, as the if
; special form's predicate is evaluated to #t and so the form's value is 0.
