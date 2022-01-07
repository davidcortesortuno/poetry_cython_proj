
cdef extern from "example.h":
    void C_fun(double * a, double * b, int n)

# Adds the elements of *a into *b
def my_function(double [:] a, double [:] b, int n):
    C_fun(&a[0], &b[0], n)
