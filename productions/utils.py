from typing import Dict, List
import networkx as nx

def find_isomorphisms(G_main: nx.Graph, G_to_find: nx.Graph, filter_duplicates=True) -> List[Dict]:
	GM = nx.algorithms.isomorphism.GraphMatcher(G_main, G_to_find, node_match=lambda n1,n2: n1['label']==n2['label'])
	
	if not GM.subgraph_is_isomorphic():
		return []
	
	isomorphisms = list(GM.subgraph_isomorphisms_iter())
	
	if filter_duplicates and len(isomorphisms) > 1:
		isomorphisms_filtered = []
		for i in range(len(isomorphisms)):
			for j in range(i+1,len(isomorphisms)):
				if isomorphisms[i].keys() == isomorphisms[j].keys():
					isomorphisms_filtered.append(isomorphisms[i])
		
		isomorphisms = isomorphisms_filtered
		
	return isomorphisms
