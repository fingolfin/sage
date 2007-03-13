import sage.rings.padics.padic_field_extension_generic
import sage.rings.padics.eisenstein_extension_generic
import sage.rings.padics.padic_lazy_generic
import sage.rings.infinity

infinity = sage.rings.infinity.infinity
pAdicFieldExtensionGeneric = sage.rings.padics.padic_field_extension_generic.pAdicFieldExtensionGeneric
EisensteinExtensionGeneric = sage.rings.padics.eisenstein_extension_generic.EisensteinExtensionGeneric
pAdicLazyGeneric = sage.rings.padics.padic_lazy_generic.pAdicLazyGeneric

class EisensteinFieldExtensionLazy(EisensteinExtensionGeneric, pAdicFieldExtensionGeneric, pAdicLazyGeneric):
    r"""
    Eisenstein Extension of a lazy p-adic field

    You should not create this class directly unless you know what you're doing.  Use ExtensionFactory.
    """

    def __init__(self, base, poly, names, prec, halt, print_mode):
        EisensteinExtensionGeneric.__init__(self, poly, names, prec, print_mode)
        pAdicLazyGeneric.__init__(self, poly.base_ring().prime(), prec, print_mode, names, halt)

    def __call__(self, x, absprec = infinity, relprec = infinity):
        return EisensteinExtensionLazyElement(self, x, absprec, relprec)

    def gen(self, n = 0):
        if n == 0:
            try:
                return self._gen
            except AttributeError:
                self._gen = EisensteinExtensionLazyElement(self, self.polynomial_ring().gen(), check = False, construct = True)
                return self._gen
