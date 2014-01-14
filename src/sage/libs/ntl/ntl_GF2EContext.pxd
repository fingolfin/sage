include "decl.pxi"
include "sage/ext/cdefs.pxi"

from ntl_GF2X cimport ntl_GF2X

cdef class ntl_GF2EContext_class:
    cdef GF2EContext_c x
    cdef ntl_GF2X m
    cdef void restore_c(self)
    cdef object __weakref__
