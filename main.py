import json
from fastapi import FastAPI, Form
from fastapi.middleware.cors import CORSMiddleware
from models import NodeBoard
from utils.graph import is_graph_dag

origins = [
    "http://localhost:3000",
    "http://localhost:3001",
]

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get('/')
def read_root():
    return {'Ping': 'Pong'}

@app.get('/pipelines/parse/{nodes_param}/{edges_param}')
def parse_pipeline(nodes_param : str, edges_param : str):
    nodes, edges = json.loads(nodes_param), json.loads(edges_param)
    num_nodes = len(nodes)
    num_edges = len(edges)
    is_dag = is_graph_dag(nodes,edges)
    return {
        "num_nodes" : num_nodes,
        "num_edges" : num_edges,
        "is_dag" : is_dag
    }
    
