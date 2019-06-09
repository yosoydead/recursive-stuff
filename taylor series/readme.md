* Link: https://en.wikipedia.org/wiki/Taylor_series
* An example would be: c^x =  1 + x/1 + x^2/2! + x^3/3! + x^4/4! + .... + n terms
* There are three operations done:
    - sum of terms -> can be written as **sum(n-1) + n**
        - the actual addition using recursion is done at return time (when the function enters the base case and starts returning all the previous calls)
    - x is raised to powers -> can be written as **fact(n-1) * x**
    - the denominator represents a factorial number -> can be written as **pow(x,n-1) * x**
* Some considerations:
    - it would be very costly and time consuming to calculate the power of **x** and the factorial of **n** for every division
    - i should use some static/global variables to calculate both power and factorial 