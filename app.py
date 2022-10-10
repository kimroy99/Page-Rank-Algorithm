from cProfile import label
from math import ceil
import streamlit as st
import networkx as nx
import matplotlib.pyplot as plt
from matplotlib.pyplot import figure, text
from itertools import count
import pagerank as pg

st.markdown("<h1 style='text-align: center; color: black;'>Page Rank Algotithm</h1>", unsafe_allow_html=True)


edges=[]
n=st.number_input("Enter the number of nodes",min_value=1,max_value=10,value=1)
e=st.number_input("Enter the number of edges",min_value=1,value=1)
a=st.text_input("Enter all 1st edges").split()
b=st.text_input("Enter all 2nd edges").split()
st.markdown("<h1 style='text-align: center; color: black;'>Choose one</h1>", unsafe_allow_html=True)

def pagerank(G,alpha=0.85,personalization=None,max_iter=100, tol=1.0e-6, nstart=None, weight='weight',dangling=None):
    if len(G)==0: return {}
    if not G.is_directed(): D=G.to_directed()
    else: D=G

    W = nx.stochastic_graph(D, weight=weight)
    N = W.number_of_nodes()

if st.button("NX page rank"):
        for i in range(e):
            edges.append((int(a[i]),int(b[i])))
        G=nx.Graph()
        G.add_nodes_from([i for i in range(n)])
        G.add_edges_from(edges)
        npg=nx.pagerank(G,0.5)
        fig, ax = plt.subplots()
        pos = nx.spring_layout(npg)
        nx.draw(G, pos,node_size=[v * 10000 for v in npg.values()],
                                  node_color=[v * 10000 for v in npg.values()],
                                  labels={node: str(node)+"-"+str(round(npg[node],2))+"%" for node in npg.keys()}) 
        for i in range(len(npg)):
            text=ax.texts[i]
            text.set_size(50*list(npg.values())[i])
        st.pyplot(fig)
        st.write(npg)
        st.markdown("<h1 style='text-align: center; color: black;'>NetworkX Page Rank Algorithm</h1>", unsafe_allow_html=True)

if st.button("Page Rank"):
    for i in range(e):
        edges.append((int(a[i]),int(b[i])))
    G=nx.Graph()
    G.add_nodes_from([i for i in range(n)])
    G.add_edges_from(edges)
    npg=nx.pagerank(G,0.5)
    P=pg.PageRank(G,False)
    r=P.rank()
    fig, ax = plt.subplots()
    pos = nx.spring_layout(npg)
    nx.draw(G, pos,node_size=[v * 10000 for v in r.values()],
                                  node_color=[v * 10000 for v in r.values()],
                                  labels={node: str(node)+"-"+str(round(npg[node],2))+"%" for node in r.keys()}) 
    for i in range(len(r)):
        text=ax.texts[i]
        text.set_size(50*list(r.values())[i])
    st.pyplot(fig)
    st.write(r)
    st.markdown("<h1 style='text-align: center; color: black;'>Page Rank Algorithm from scratch</h1>", unsafe_allow_html=True)

    

