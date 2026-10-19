
from career_engine import evaluate_assessment

profiles = [
    {
        "name": "Software Developer Profile",
        "interests": [
            "Programming and building applications",
            "Research and problem-solving"
        ],
        "skills": ["Python", "JavaScript", "Problem-solving"],
        "skillLevel": "Intermediate"
    },
    {
        "name": "Data Analyst Profile",
        "interests": [
            "Data analysis and mathematics",
            "Research and problem-solving"
        ],
        "skills": ["SQL", "Data analysis"],
        "skillLevel": "Beginner"
    },
    {
        "name": "Cybersecurity Profile",
        "interests": [
            "Cybersecurity and ethical security practices"
        ],
        "skills": ["Networking", "Linux", "Python"],
        "skillLevel": "Advanced"
    }
]

for profile in profiles:
    print("\n", profile["name"])

    recommendations = evaluate_assessment(profile)

    for career in recommendations:
        print(
            career["career"]["title"],
            "-", career["match"], "%"
        )
        print("Reason:", "; ".join(career["reasons"]))
        print("Skills to learn:", career["missing_skills"])
