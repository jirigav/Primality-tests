# Primality tests

## Trial division

* trial_division.py
* The simplest primality test improved by trying to divide only by numbers of format 6k ± 1 less than √n.
* Inefficient for large numbers. 


## Fermat primality test

* fermat.py
* The simplest probabilistic primality test
* Takes number of loops as a second argument. 

## Miller–Rabin primality test

* miller_rabin.py
* Probabilistic test
* Takes number of loops as a second argument. 

## Solovay–Strassen primality test

* solovay_strassen.py
* needs utils/jacobi.py to work
* Probabilistic test
* Takes number of loops as a second argument. 

## Lucas primality test

* lucas.py
* needs SymPy to work `pip install sympy`
* Probabilistic test
* Takes number of loops as a second argument. 