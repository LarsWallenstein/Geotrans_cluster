#GeoTrans_cluster

Name of the module stands for geographical transactions clustering.
This module is an implementation of the method, developed for the third course project
in HSE University. It takes dataframe with clients transactions history of the
specified format and returns list of clusters.

For the record, it was intended to be for public usage in this form, as it is a research project seeking to find a way to deal with the described problem

## Installation

Run the following to install:

'''python
pip install geotrans_cluster
'''

## Usage

Before using make sure, that your dataset corresponds with requirements. Csv file must contain the following columns in order to work correctly

user_id   :   string type, example: "423156821"
event_dt  :   string type, example: "20190312"
event_time:   string type, example: "2019-03-12 06:24:00.279"
lattitude :   float  type, example: 49.862621
longtitude:   see lattitude

'''python

import pandas as pd
import numpy  as np
import markov_clustering as mc
import matplotlib.pyplot as plt
import math
import pytz
import folium
import os.path
import networkx as nx


from haversine       import haversine, Unit
from collections     import Counter
from datetime        import datetime
from timezonefinder  import TimezoneFinder
from IPython.display import clear_output

import geotrans_cluster

path = [path to file with data]
data, names = data_load(path)


%matplotlib notebook
base = [path to the folder, where to store libs with information about clients]

archivate = True
libs= True
graph_f = True
cluster_f = True


if(archivate):
    archivate_maps(data, names, levels=4)

if(libs):
    lib = graph_preparation(data, names, base) # создание ориентировочной библиотеки знакомств
    prob_lib = znakomstvo_by_lib(lib,data) # расчёт вероятностей для библиотеки


lib, prob_lib = load_libs(base = base)
print("Libs loaded")
if(graph_f):
    graph = graph_forming(lib, prob_lib, treshold=0.9)
print("Graph formed")
    
if(cluster_f):
    result = mc.run_mcl(graph,pruning_threshold=0.7, inflation=2,expansion=2) 
    print("Clustered")
    clusters = mc.get_clusters(result)

    clust_0 = clusters_to_ids(lib=lib, prob_lib=prob_lib, clusters = clusters, number = 0)
    maps = get_cluster_maps(data = data, clust = clust_0)
    print("Number of clusters", len(clusters))

    plt.figure(figsize=(10,10))
    mc.drawing.draw_graph(result, clusters, edge_color="red",node_size=15,width = 1, with_labels=True, font_size = 8)
