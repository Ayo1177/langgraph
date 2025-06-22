#dictionary  = {
#    "name": "Langraph Agents",
#    "description": "A collection of agents that can be used to interact with Langraph.",
#    "version": "0.1.0",}



###typed dictionary:
from typing import TypedDict
#typed dictionary: insures type safety 
class Movie(TypedDict):
    name: str
    year: int

movie = Movie(name="Langraph Agents",year=2023)



###Union
from typing import Union
#union allows a variable to be one of several types
def square(x: Union[int, float]) -> float:
    return x*x



###optional
from typing import Optional
#optional allows a variable to be None or of a specified type but cannot be anything else
def nice_message(name: Optional[str]) -> None:
    if name is None:
        print("Hello, stranger!")
    else:
        print(f"Hello, {name}!")



### Any
from typing import Any
#any allows a variable to be of any type
def print_value(x: Any):
    print(x)


###Lambda function
nums = [1, 2, 3, 4, 5]
squares = list(map(lambda x: x * x, nums))
# Output: 100

