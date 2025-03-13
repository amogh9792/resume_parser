import re

skill_set = {"Python", "Django", "Machine Learning", "Data Science", "React", "NLP", "SQL"}

def extract_skills(text):
    """Extract skills from text based on predefined skill set."""
    found_skills = set()
    
    for skill in skill_set:
        if re.search(rf'\b{re.escape(skill)}\b', text, re.IGNORECASE):
            found_skills.add(skill)
    
    return list(found_skills)

# Example usage:
text = "I have experience in Python, Django, and Machine Learning."
print(extract_skills(text))  # ['Python', 'Django', 'Machine Learning']
