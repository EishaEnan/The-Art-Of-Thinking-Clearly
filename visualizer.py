from pyvis.network import Network
from raw_data import chapters
from generator import connector

data_net = Network(height="800px", width="100%", bgcolor="#222222", font_color="white", notebook=False, select_menu=True)
# set the physics layout of the network
data_net.force_atlas_2based()
label = {}

for i, chapter in enumerate(chapters):
    label[i] = chapter[0]

for i in range(99):
    data_net.add_node(i,label[i])

for edge in connector(chapters) :
    data_net.add_edge(edge[0], edge[1])
               

#For customizing physics, nodes, edges, layouts
#data_net.show_buttons(filter_=['physics'])



data_net.show("TheArtOfThinkingClearly.html")