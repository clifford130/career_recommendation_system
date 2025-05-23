from experta import KnowledgeEngine, Rule, Fact, Field

class UserProfile(Fact):
    skills = Field(list, default=[])
    education = Field(str, default="")
    interests = Field(list, default=[])

class CareerEngine(KnowledgeEngine):
    @Rule(UserProfile(skills=lambda skills: 'Python' in skills,
                      education='Bachelor in Computer Science',
                      interests=lambda interests: 'Data Analysis' in interests))
    def recommend_data_science(self):
        self.declare(Fact(recommendation="Data Scientist"))
    
    @Rule(UserProfile(skills=lambda skills: 'Java' in skills,
                      education='Bachelor in Computer Science',
                      interests=lambda interests: 'Software Development' in interests))
    def recommend_software_dev(self):
        self.declare(Fact(recommendation="Software Developer"))


    @Rule(UserProfile(skills=lambda skills: 'Diagnosis' in skills,
                      education='Bachelor in Medicine',
                      interests=lambda interests: 'pediatrics or surgery or medical diagnosis' in interests))
    def recommend_software_dev(self):
        self.declare(Fact(recommendation="Doctor"))


    @Rule(UserProfile(skills=lambda skills: 'interface design' in skills,
                      education='Bachelor in Human-Computer Interaction',
                      interests=lambda interests: 'designing system prototypes' in interests))
    def recommend_software_dev(self):
        self.declare(Fact(recommendation="UX Designer"))


    @Rule(UserProfile(skills=lambda skills: 'Network Security' in skills,
                      education='Bachelor in Cybersecurity',
                      interests=lambda interests: 'monitoring networks and systems from attacks' in interests))
    def recommend_software_dev(self):
        self.declare(Fact(recommendation="Cybersecurity Analyst"))


    @Rule(UserProfile(skills=lambda skills: 'Subject Knowledge' in skills,
                      education='Bachelor in Education',
                      interests=lambda interests: 'teaching students' in interests))
    def recommend_software_dev(self):
        self.declare(Fact(recommendation="Teacher"))

def get_recommendation(profile_data):
    engine = CareerEngine()
    engine.reset()
    engine.declare(UserProfile(**profile_data))
    engine.run()
    for fact in engine.facts.values():
        if isinstance(fact, Fact) and fact.get("recommendation"):
            return fact["recommendation"]
    return "No clear recommendation"
