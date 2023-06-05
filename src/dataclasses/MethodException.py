from dataclasses import dataclass


@dataclass(frozen=True)
class MethodException:
    """Represent the exceptions that a method can throw
    """
    
    exception: str
    """The name of the exception
    """
    
    description: str
    """The description of the exception
    """
