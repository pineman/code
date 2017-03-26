# __init__ file to make python treat this directory as a package/module thing.

# this makes 'from module import *' statements work as it provides
# the list of modules to import.
__all__ = ['']

# this makes 'import module' work. A submodule can then be accessed by 
# module.submodule, and a function by module.submodule.function()
from . import *
