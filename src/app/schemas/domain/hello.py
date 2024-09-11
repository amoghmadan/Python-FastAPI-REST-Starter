import pydantic


class World(pydantic.BaseModel):
    """Hello: World"""

    hello: str
