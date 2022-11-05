from __future__ import annotations
from beartype.typing import *
from typing import TypeAlias
from collections.abc import Hashable

if TYPE_CHECKING:
    from sweetly._types import GraphData, Edges
    from sweetly.structs.tokens import Token

from sweetly.constants import BEGIN


__all__ = ["Graph"]


class Graph:
    """
    Core structure representing a directed graph of nodes.
    """

    def __init__(self, *chain) -> None:
        self.edges: Edges = {BEGIN: set()}
        self.named = {}
        self.nodes = {}
        
        if len(chain) > 0:
            self.add_chain(*chain)

    def __getitem__(self, key: str):
        return self.nodes[key]

    def __enter__(self):
        pass
    
    def __exit__(self, exc_type, exc_val, exc_tb):
        return None

    def get_cursor(self, ref=BEGIN):
        pass

    def orphan(self):
        pass

    def index_of(self, mixed):
        pass

    def indices_of(self, *things, _type=set):
        pass
    
    def outputs_of(self, idx_or_node, create: bool = False):
        pass

    def add_node(self, new_node, *, name: str | None = None) -> None:
        pass

    def add_chain(
            self, 
            *nodes,
            input: Token = BEGIN, 
            output_resolver = None,
            name: str | None = None, 
            use_existing_nodes: bool = False
        ) -> None:
        pass
