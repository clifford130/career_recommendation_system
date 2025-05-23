class CareerFrame:
    def __init__(self, title, required_skills, education, description):
        self.title = title
        self.required_skills = required_skills
        self.education = education
        self.description = description

# Define 20 careers
software_developer = CareerFrame(
    title="Software Developer",
    required_skills=["Programming", "Problem Solving", "Algorithms", "Data Structures", "Software Design", "Version Control", "Debugging", "Testing", "Collaboration", "Communication", "Agile Methodologies", "Cloud Computing", "Database Management"],
    education=["Bachelor in Computer Science", "Bachelor in Software Engineering", "Bachelor in Information Technology", "Bachelor in Computer Engineering", "Bachelor in Mathematics (with programming focus)", "Associate Degree in Computer Science (with experience)", "Relevant Coding Bootcamp Certification"],
    description="Software Developers design, develop, test, and maintain software applications that power everything from mobile apps to enterprise systems. They collaborate with teams to translate user needs into functional code, working in dynamic environments like tech startups or large corporations. This career offers paths to specialize in web development, mobile apps, or AI."
)

data_scientist = CareerFrame(
    title="Data Scientist",
    required_skills=["Python", "Data Analysis", "Machine Learning", "Statistics", "Data Visualization", "SQL", "Big Data Technologies", "Communication", "Problem Solving", "Domain Knowledge"],
    education=["Bachelor in Computer Science", "Bachelor in Statistics", "Bachelor in Mathematics", "Bachelor in Data Science", "Master in Data Science", "PhD in related field"],
    description="Data Scientists extract insights from complex datasets using statistical methods and machine learning, working in industries like finance or healthcare. They interpret data and communicate findings to stakeholders, with career paths leading to roles like Chief Data Officer."
)

doctor = CareerFrame(
    title="Doctor",
    required_skills=["Anatomy", "Patient Care", "Medical Research", "CPR", "Diagnosis", "Treatment Planning", "Communication", "Empathy", "Critical Thinking", "Teamwork"],
    education=["Bachelor in Medicine", "Doctor of Medicine (MD)", "Residency Program", "Specialization Certification"],
    description="Doctors diagnose and treat medical conditions in hospitals or clinics, specializing in areas like pediatrics or surgery. This career requires extensive training and offers the chance to impact lives significantly."
)

ux_designer = CareerFrame(
    title="UX Designer",
    required_skills=["User Experience", "Design", "Prototyping", "Wireframing", "User Research", "Usability Testing", "Visual Design", "Interaction Design", "Collaboration", "Communication", "interface design"],
    education=["Bachelor in Design", "Bachelor in Human-Computer Interaction", "Bachelor in Graphic Design", "Bachelor in Psychology", "Relevant Design Certification"],
    description="UX Designers create user-friendly interfaces for digital products, conducting research and designing prototypes. They work with developers and product managers, with opportunities to specialize in interaction design."
)

cybersecurity_analyst = CareerFrame(
    title="Cybersecurity Analyst",
    required_skills=["Cybersecurity", "Python", "Network Security", "Threat Analysis", "Incident Response", "Firewalls", "Encryption", "Risk Management", "Communication", "Problem Solving"],
    education=["Bachelor in Computer Science", "Bachelor in Cybersecurity", "Bachelor in Information Technology", "Relevant Certifications (e.g., CISSP, CEH)"],
    description="Cybersecurity Analysts protect organizations from cyber threats by monitoring networks and implementing security measures, working in industries like finance or government."
)

marketing_manager = CareerFrame(
    title="Marketing Manager",
    required_skills=["Digital Marketing", "SEO", "Content Strategy", "Market Research", "Analytics", "Communication", "Creativity", "Project Management", "Leadership", "Budgeting"],
    education=["Bachelor in Marketing", "Bachelor in Business Administration", "Bachelor in Communications", "Master in Marketing", "Relevant Certifications (e.g., Google Analytics)"],
    description="Marketing Managers develop strategies to promote products, overseeing campaigns and teams in diverse industries. Leadership and creativity drive success in this field."
)

mechanical_engineer = CareerFrame(
    title="Mechanical Engineer",
    required_skills=["Mechanical Design", "CAD", "Thermodynamics", "Fluid Mechanics", "Materials Science", "Problem Solving", "Project Management", "Communication", "Teamwork", "Innovation"],
    education=["Bachelor in Mechanical Engineering", "Master in Mechanical Engineering", "Relevant Certifications (e.g., PE License)"],
    description="Mechanical Engineers design and test mechanical systems, working in industries like automotive or aerospace with opportunities to innovate in robotics."
)

financial_analyst = CareerFrame(
    title="Financial Analyst",
    required_skills=["Financial Modeling", "Data Analysis", "Excel", "Accounting", "Economics", "Communication", "Attention to Detail", "Problem Solving", "Forecasting", "Investment Analysis"],
    education=["Bachelor in Finance", "Bachelor in Accounting", "Bachelor in Economics", "Master in Finance", "CFA Certification"],
    description="Financial Analysts guide investment decisions by analyzing financial data, working in banks or corporate finance with paths to roles like CFO."
)

teacher = CareerFrame(
    title="Teacher",
    required_skills=["Subject Knowledge", "Communication", "Patience", "Classroom Management", "Lesson Planning", "Assessment", "Empathy", "Adaptability", "Technology Integration", "Collaboration"],
    education=["Bachelor in Education", "Teaching Certification", "Subject-Specific Degree", "Master in Education"],
    description="Teachers educate students, fostering development in schools or online, with opportunities to advance to roles like Principal."
)

graphic_designer = CareerFrame(
    title="Graphic Designer",
    required_skills=["Graphic Design", "Creativity", "Adobe Creative Suite", "Typography", "Color Theory", "Communication", "Time Management", "Attention to Detail", "Collaboration", "Problem Solving"],
    education=["Bachelor in Graphic Design", "Bachelor in Fine Arts", "Associate Degree in Graphic Design", "Relevant Design Certification"],
    description="Graphic Designers create visual content for media, working in agencies or as freelancers with paths to roles like Creative Director."
)

nurse = CareerFrame(
    title="Nurse",
    required_skills=["Patient Care", "Medical Knowledge", "Communication", "Empathy", "Critical Thinking", "Time Management", "Teamwork", "Attention to Detail", "Stress Management", "Technical Skills"],
    education=["Bachelor of Science in Nursing (BSN)", "Associate Degree in Nursing (ADN)", "Nursing Diploma", "Registered Nurse (RN) License", "Specialization Certification"],
    description="Nurses provide care in healthcare settings, specializing in areas like emergency nursing with opportunities for leadership roles."
)

civil_engineer = CareerFrame(
    title="Civil Engineer",
    required_skills=["Civil Engineering", "AutoCAD", "Structural Analysis", "Project Management", "Communication", "Problem Solving", "Teamwork", "Attention to Detail", "Sustainability", "Budgeting"],
    education=["Bachelor in Civil Engineering", "Master in Civil Engineering", "Professional Engineer (PE) License"],
    description="Civil Engineers design infrastructure like roads and bridges, working for government or firms to impact communities."
)

psychologist = CareerFrame(
    title="Psychologist",
    required_skills=["Psychology", "Counseling", "Research", "Communication", "Empathy", "Critical Thinking", "Ethics", "Data Analysis", "Problem Solving", "Patience"],
    education=["Bachelor in Psychology", "Master in Psychology", "Doctorate in Psychology (PhD or PsyD)", "Licensure"],
    description="Psychologists study behavior and provide therapy, working in practices or schools with a focus on mental health."
)

architect = CareerFrame(
    title="Architect",
    required_skills=["Architectural Design", "AutoCAD", "SketchUp", "Creativity", "Communication", "Project Management", "Attention to Detail", "Problem Solving", "Sustainability", "Building Codes"],
    education=["Bachelor in Architecture", "Master in Architecture", "Architectural License"],
    description="Architects design buildings, balancing aesthetics and safety, working in firms or as consultants."
)

pharmacist = CareerFrame(
    title="Pharmacist",
    required_skills=["Pharmacy", "Medication Knowledge", "Patient Counseling", "Attention to Detail", "Communication", "Ethics", "Problem Solving", "Teamwork", "Time Management", "Regulatory Compliance"],
    education=["Doctor of Pharmacy (PharmD)", "Pharmacy License", "Residency"],
    description="Pharmacists dispense medications and advise on use, working in pharmacies or hospitals."
)

electrical_engineer = CareerFrame(
    title="Electrical Engineer",
    required_skills=["Electrical Engineering", "Circuit Design", "MATLAB", "Problem Solving", "Communication", "Teamwork", "Project Management", "Innovation", "Safety Standards", "Programming"],
    education=["Bachelor in Electrical Engineering", "Master in Electrical Engineering", "Professional Engineer (PE) License"],
    description="Electrical Engineers design electrical systems, working in energy or manufacturing."
)

lawyer = CareerFrame(
    title="Lawyer",
    required_skills=["Legal Knowledge", "Research", "Communication", "Negotiation", "Critical Thinking", "Ethics", "Attention to Detail", "Problem Solving", "Advocacy", "Time Management"],
    education=["Bachelor in Law (LLB)", "Juris Doctor (JD)", "Bar Admission"],
    description="Lawyers provide legal advice and representation, working in firms or government."
)

journalist = CareerFrame(
    title="Journalist",
    required_skills=["Writing", "Research", "Interviewing", "Ethics", "Communication", "Critical Thinking", "Time Management", "Multimedia Skills", "Adaptability", "Storytelling"],
    education=["Bachelor in Journalism", "Bachelor in Communications", "Bachelor in English", "Relevant Journalism Certification"],
    description="Journalists report news, working for media outlets with a focus on storytelling."
)

chef = CareerFrame(
    title="Chef",
    required_skills=["Culinary Arts", "Creativity", "Time Management", "Leadership", "Communication", "Attention to Detail", "Food Safety", "Menu Planning", "Budgeting", "Teamwork"],
    education=["Culinary Arts Degree", "Apprenticeship", "Relevant Culinary Certification"],
    description="Chefs prepare meals and manage kitchens, working in restaurants or catering."
)

environmental_scientist = CareerFrame(
    title="Environmental Scientist",
    required_skills=["Environmental Science", "Research", "Data Analysis", "Communication", "Problem Solving", "Fieldwork", "GIS", "Sustainability", "Policy Knowledge", "Teamwork"],
    education=["Bachelor in Environmental Science", "Bachelor in Biology", "Master in Environmental Science", "Relevant Certifications"],
    description="Environmental Scientists study and protect natural resources, working for agencies or non-profits."
)

career_frames = {
    "Software Developer": software_developer,
    "Data Scientist": data_scientist,
    "Doctor": doctor,
    "UX Designer": ux_designer,
    "Cybersecurity Analyst": cybersecurity_analyst,
    "Marketing Manager": marketing_manager,
    "Mechanical Engineer": mechanical_engineer,
    "Financial Analyst": financial_analyst,
    "Teacher": teacher,
    "Graphic Designer": graphic_designer,
    "Nurse": nurse,
    "Civil Engineer": civil_engineer,
    "Psychologist": psychologist,
    "Architect": architect,
    "Pharmacist": pharmacist,
    "Electrical Engineer": electrical_engineer,
    "Lawyer": lawyer,
    "Journalist": journalist,
    "Chef": chef,
    "Environmental Scientist": environmental_scientist,
}
