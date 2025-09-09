try:
    __WINDCRAFT_SETUP__ = True
except NameError:
    __WINDCRAFT_SETUP__ = False

if not __WINDCRAFT_SETUP__:
    __all__ = [
        "Arrow",
        "Colors",
        "Text",
        "Farm",
        "Fonts",
        "Logo",
        "Player",
        "Solver",
        "Turbine",
    ]
    from .arrow import Arrow
    from .colors import Colors
    from .farm import Farm
    from .fonts import Fonts
    from .logo import Logo
    from .player import Player
    from .solver import Solver
    from .text import Text
    from .turbine import Turbine
