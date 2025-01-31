# Copyright (c) 2018-2022 Patricio Cubillos.
# bibmanager is open-source software under the MIT license (see LICENSE).

from .utils import *
from .utils import __all__

# Clean up top-level namespace--delete everything that isn't in __all__
# or is a magic attribute, and that isn't a submodule of this package
for varname in dir():
    if not ((varname.startswith('__') and varname.endswith('__')) or
            varname in __all__):
        del locals()[varname]
del(varname)
