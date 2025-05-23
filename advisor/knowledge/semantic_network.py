import networkx as nx

def build_semantic_network():
    G = nx.Graph()
    # Add nodes: skills and career roles
    G.add_node("Python")
    G.add_node("Data Analysis")
    G.add_node("Software Developer")
    G.add_node("Data Scientist")
    G.add_node("Doctor")
    G.add_node("UX Designer")
    G.add_node("Cybersecurity Analyst")
    G.add_node("Teacher")
    
    # Add edges: relationships between skills and careers
    G.add_edge("Python", "Software Developer")
    G.add_edge("Python", "Data Scientist")
    G.add_edge("Data Analysis", "Data Scientist")
    G.add_edge("Java", "Software Developer")
    G.add_edge("Diagnosis", "Doctor")
    G.add_edge("interface design", "UX Designer")
    G.add_edge("Network Security", "Cybersecurity Analyst")
    G.add_edge("Subject Knowledge", "Teacher")
    return G

def find_related_careers(skill):
    G = build_semantic_network()
    try:
        return list(G.neighbors(skill))
    except Exception:
        return []
