from pydantic import BaseModel, Field, StrictInt


class anabel(BaseModel):

    x : StrictInt = Field(...,description="this is x")
    y : str = Field(...,description="this is y")


pyd_input = anabel(**{"x": 10,"y": "Anabel"})

def main(para1:anabel):

    print("Hello Anabel")


main(pyd_input)