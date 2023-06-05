from dataclasses import dataclass


@dataclass(frozen=True)
class MainClass:
    """Represent the main class that is parsed
    """

    name: str
    """The name of the main class
    """
    
    short_description: str
    """The short description that we will use inside of the metadata
    """
    
    long_description: str
    """The long description of the class
    """
