from __future__ import annotations
from beartype.typing import *
from typing import TypeAlias
from collections.abc import Hashable

if TYPE_CHECKING:
    pass

from sweetly.structs.tokens import Token


GraphData: TypeAlias = dict[Hashable, Any]

Edges: TypeAlias = dict[Token, set[Any]]
