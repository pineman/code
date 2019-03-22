# __init__ file to make python treat this directory as a package

# this makes 'from module import *' statements work as it provides
# the list of modules to import.
__all__ = ['']

# this makes import module work. I can then access a submodule by 
# module.submodule, and a function by module.submodule.function()
from . import * 

