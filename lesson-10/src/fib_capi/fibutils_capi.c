#include <Python.h>

int fib_rec_c(int n)
{
    if (n <= 2)
        return 1;

    return fib_rec_c(n - 1) + fib_rec_c(n - 2);
}


int fib_iter_c(int n)
{
    int a = 0, b = 1;
    for (int i = 0; i < n; ++i)
    {
        int tmp = b;
        b = a + b;
        a = tmp;
    }
    return a;
}


PyObject *fibutils_rec_c_api(PyObject* self, PyObject* args)
{
    int n;
    if (!PyArg_ParseTuple(args, "i", &n))
        return NULL;

    int res = fib_rec_c(n);
    return PyLong_FromLong(res);
}


PyObject *fibutils_iter_c_api(PyObject* self, PyObject* args)
{
    int n;
    if (!PyArg_ParseTuple(args, "i", &n))
        return NULL;

    int res = fib_iter_c(n);
    return PyLong_FromLong(res);
}


static PyMethodDef methods[] = {
    {"fib_rec_c_api", fibutils_rec_c_api, METH_VARARGS, "recursive fib calculation with C-api"},
    {"fib_iter_c_api", fibutils_iter_c_api, METH_VARARGS, "iterative fib calculation with C-api"},
    {NULL, NULL, 0, NULL},
};


static struct PyModuleDef module_fibutils_c_api = {
    PyModuleDef_HEAD_INIT, "fibutils_c_api", NULL, -1, methods
};


PyMODINIT_FUNC PyInit_fibutils_c_api()
{
    return PyModule_Create( &module_fibutils_c_api );
}
