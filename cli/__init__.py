"""Two-three sentences about what your project does
Examples:
>>> import myproject as mp
>>> print mp.variableC
42
List of modules
"""

import baseObjects
import menu
import menuEntry


from baseObjects import *
from menu import *
from menuEntry import *

__all__ = [ baseObjects.__all__,
            menu.__all__,
            menuEntry.__all__
          ]


if __name__ == "__main__":
    
    import doctest
    doctest.testmod()
