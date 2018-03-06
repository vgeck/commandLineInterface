"""Two-three sentences about what your project does
Examples:
>>> import myproject as mp
>>> print mp.variableC
42
List of modules
"""

import cli.base_objects as baseObjects
import cli.menu as menu
import cli.menu_entry as menuEntry


from cli.base_objects import *
from cli.menu import *
from cli.menu_entry import *

__all__ = [baseObjects.__all__,
           menu.__all__,
           menuEntry.__all__
          ]


if __name__ == "__main__":
    
    import doctest
    doctest.testmod()
