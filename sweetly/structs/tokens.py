
class Token:
    
    def __init__(self, name: str) -> None:
        self.__name__ = name
        
    def __repr__(self) -> str:
        return f"<{self.__name__}>"
    
    
class Flag(Token):
    must_be_first = False
    must_be_last = False
    allows_data = True
