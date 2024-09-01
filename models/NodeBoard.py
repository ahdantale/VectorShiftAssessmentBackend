from pydantic import BaseModel

class NodeBoard(BaseModel):
    nodes : list
    edges : list
