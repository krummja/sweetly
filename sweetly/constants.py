from __future__ import annotations
from beartype.typing import *
from typing import TypeAlias
if TYPE_CHECKING:
    pass

from sweetly.structs.tokens import Token


BEGIN = Token("Begin")
END = Token("End")

EMPTY = tuple()

