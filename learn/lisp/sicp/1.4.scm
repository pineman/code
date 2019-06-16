; 1.4
(define (a-plus-abs-b a b)
  ((if (> b 0) + -) a b))

; Lisp's model of evaluation allows operators themselves to be compound
; expressions whose value can be primitive operators. As such, its possible
; to "decide" which operator to use in an expression dynamically, as is the
; case in this example, using the if special form.
