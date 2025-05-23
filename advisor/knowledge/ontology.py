from rdflib import Graph, Namespace

def load_career_ontology(ontology_path='career.owl'):
    g = Graph()
    try:
        g.parse(ontology_path, format="xml")
    except Exception as e:
        print("Error loading ontology:", e)
    return g

def query_career_requirements(g, career_name):
    CAREER = Namespace("http://example.org/career#")
    query = f"""
    SELECT ?skill WHERE {{
        ?career a CAREER:{career_name} .
        ?career CAREER:requires ?skill .
    }}
    """
    try:
        qres = g.query(query, initNs={"CAREER": CAREER})
        return [str(row.skill) for row in qres]
    except Exception:
        return []
