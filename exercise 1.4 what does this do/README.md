what does the function do?
    function x(arrayA, arrayB, n)
        if n == 0
            return a[0] * b[0]
        else
            return x(arrayA, arrayB, n-1) + a[n] * b[n]