import dash
import visdcc
import pandas as pd
from dash import dcc
from dash import  html
from dash.dependencies import Input, Output, State
from raw_data import chapters
from generator import connector

app = dash.Dash()

df = pd.read_csv('data.csv')
node_list = list(set(df['source'].unique().tolist() + \
                     df['target'].unique().tolist())
                     )


nodes = [{'id': node_name, 'label': node_name, 'shape': 'dot', 'size': 7}
         for i, node_name in enumerate(node_list)]

edges = []

for node in connector(chapters) :
    source, target = node[0], node[1]
    edges.append({
        'id': chapters[source] + '__' + chapters[target],
        'from': source,
        'to': target,
        'width': 2,})