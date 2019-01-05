# begin by extracting Twitter handles from the TAGS spreadsheet
# note: assumes you have downloaded the TAGS spreadsheet from Google Drive and saved archives sheet as a .csv
# you could also programmatically obtain TAGS spreadsheet data via the Sheets API but I wanted to keep it simple

# import modules
import csv
import networkx as nx
from operator import itemgetter
import community

# define function to extract twitter handles from TAGS archive spreadsheet
def extract_handles(file):
    # open and read the files, create Header Row for export .csv
    text = open(file)
    entry = csv.reader(text)

    export_file_name = file[:-4] + "_edge_list.csv"
    handles = open(export_file_name, 'a+')
    handles.write('source,target\n')

    # import entities_str column
    for line in entry:
        # extract the initial tweeter handle from column B
        from_user = line[1]
        
        # extract the entities_str (full tweet) text from column Q
        entities_str = line[16]

        # split entities_str into a list whose first item is misc. characters and subsequent items start with a twitter handle
        entities_str = entities_str.split('"screen_name":"')
        
        # remove the first item of misc. characters
        entities_str.pop(0)
        
        # isolate just the twitter handles from subsequent items
        for item in entities_str:
            item = item.split('"')
            item = item[0]
            
            # write initial tweeter handle and entities_str twitter handles to file in network edge format
            handles.write(from_user + ',' + item + '\n')
    
    # close files
    text.close()
    handles.close()
    
# define the function to create and analyze the network

def create_network(file):
    with open(file, 'r') as edgecsv:
        edgereader = csv.reader(edgecsv)
        edges = [tuple(e) for e in edgereader][1:] 
        nodes = []
        for e in edges:
            n1 = e[0]
            n2 = e[1]
            if (n1 in nodes) and (n2 in nodes):
                continue
            elif (n1 in nodes) and (n2 != ""):
                nodes.append(n2)
            elif (n1 != ""):
                nodes.append(n1)
            #print(nodes)
                    
    G = nx.Graph()
    G.add_nodes_from(nodes)
    #print(G.nodes())
    G.add_edges_from(edges)
    return G
    
def analyze_network(N):
    print(nx.info(N))
    density = nx.density(N)
    print("Network density: ", density)
    
    if (nx.is_connected(N)):
        diameter = nx.diameter(N)
        print("Network is connected, with diameter: ", diameter)
    else:
        components = nx.connected_components(N)
        largest_component =  max(components, key=len)
        subN = N.subgraph(largest_component)
        diameter = nx.diameter(subN)
        print("Network is disconnected and its largest connected component has diameter: ", diameter)

    triadic_closure = nx.transitivity(N)
    print("Triadic closure: ", triadic_closure)
    
    degree_dict = dict(N.degree(N.nodes()))
    nx.set_node_attributes(N, degree_dict, 'degree')
    sorted_degree = sorted(degree_dict.items(), key=itemgetter(1), reverse=True)
    print("Top 10 nodes by degree: ")
    for d in sorted_degree[:10]:
        print(d)
        
    betweenness_dict = nx.betweenness_centrality(N)
    nx.set_node_attributes(N, betweenness_dict, 'betweenness')
    sorted_betweenness = sorted(betweenness_dict.items(), key=itemgetter(1), reverse=True)
    print("Top 10 nodes by betweenness centrality: ")
    for d in sorted_betweenness[:10]:
        print(d)    
    
    eigenvector_dict = nx.eigenvector_centrality(N)
    nx.set_node_attributes(N, eigenvector_dict, 'eigenvector')
    sorted_eigenvector = sorted(eigenvector_dict.items(), key=itemgetter(1), reverse=True)
    print("Top 10 nodes by eigenvector centrality: ")
    for d in sorted_eigenvector[:10]:
        print(d)    
    
# begin program
# get name of archive spreadsheet file from user and generate name of edge list file
file_name = input('What is the exact name of your csv file (include the .csv) ')
edge_file_name = file_name[:-4] + "_edge_list.csv"

# extract twitter handles, create network graph, and analyze network
extract_handles(file_name)
network = create_network(edge_file_name)
analyze_network(network)


# end program