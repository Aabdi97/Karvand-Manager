import os
import json
class Karvand:
    def __init__(self,fullname,email,city,Educational_Qualification,Field_of_study,skill_name,skill_point):
        self.id = karvands.index(self) + 1 if self in karvands else len(karvands) + 1
        self.fullname = fullname
        self.email = email
        self.city =city
        self.Educational_Qualification = Educational_Qualification
        self.Field_of_study = Field_of_study
        self.skill_name = skill_name
        self.skill_point = skill_point


karvands = []

def get_karvand():
    path = "data\\karvands.json"
    if not os.path.exists("data"):
        os.makedirs("data")
    if os.path.exists(path):
        with open(path, "r") as f:
            try:
                 karvands_data =[]
                 data =json.load(f)
                 for item in data:
                    karvand = Karvand(
                        item["fullname"],
                        item["email"],
                        item["city"],
                        item["Educational_Qualification"],
                        item["Field_of_study"],
                        item["skill_name"],
                        item["skill_point"]
                    )

                    karvand.id = item["id"]
                    karvands_data.append(karvand)
                 return karvands_data
            except:
                print("Error getting Karvands")
                return []
    else:
        with open(path, "w") as f:
            try:
                return json.dump(karvands, f)
            except:
                print("Error getting Karvands")
                return json.dump([], f)

def save_karvand():
    with open("data\\karvands.json", "w") as f:
        json.dump([vars(k) for k in karvands], f, indent=2)

def save_report(report):
    if not os.path.exists("data"):
        os.makedirs("data")
    with open("data\\report.json", "w") as f:
        json.dump(report, f)

def get_karvand_input():
    data =  Karvand(    
        fullname=input("Full name: "),
        email=input("Email: "),
        city=input("City: "),
        Educational_Qualification=input("Educational qualification: "),
        Field_of_study=input("Field of study: "),
        skill_name=input("Skill name: "),
        skill_point=None
    )
    skill_point = input("Skill point: ")
    if skill_point.isnumeric():
        skill_point = int(skill_point)
        if 0 < skill_point < 100:
            data.skill_point = skill_point
        else:
            data.skill_point = None
            print("Skill point is not valid")
            data.skill_point = int(input("Skill point: "))
    else:
        data.skill_point = None
        print("Skill point is not valid")
        skill_point = input("Skill point: ")
        data.skill_point = int(skill_point)
    return data
def get_karvand_input_update(karvand):
    data = Karvand(
        fullname=input(f"Full name (current: {karvand.fullname}): "),
        email=input(f"Email (current: {karvand.email}): "),
        city=input(f"City (current: {karvand.city}): "),
        Educational_Qualification=input(f"Educational qualification (current: {karvand.Educational_Qualification}): "),
        Field_of_study=input(f"Field of study (current: {karvand.Field_of_study}): "),
        skill_name=input(f"Skill name (current: {karvand.skill_name}): "),
        skill_point=None
    )
    skill_point = input("Skill point: ")
    if skill_point.isnumeric():
        skill_point = int(skill_point)
        if 0 < skill_point < 100:
            data.skill_point = skill_point
        else:
            data.skill_point = None
            print("Skill point is not valid")
            data.skill_point = int(input("Skill point: "))
    else:
            data.skill_point = None
            print("Skill point is not valid")
            skill_point = input("Skill point: ")
            data.skill_point = int(skill_point)
    return data

def search_karvand_by_id(skill):
    results = [k for k in karvands if k.skill_name.lower() == skill.lower()]
    for k in results:
        print(f"{k.fullname} - {k.skill_name} ({k.skill_point})")
    if not results:
        print("No matches")
    
while True:
    karvands =get_karvand()
    menu = int(input("""
1 - Add Karvand
2 - Show all Karvands
3 - Search Karvand by ID
4 - Search Karvand by skill
5 - Update Karvand
6 - Delete Karvand
7 - Total report
8 - Exit
Choose: """))
    match menu:
        case 1:
            karvands.append(get_karvand_input())
            save_karvand()
            print("Added!")

        case 2:
            if not karvands:
                print("No Karvands")
                continue
            for i, k in enumerate(karvands):
                print(f"({k.id}: {k.fullname} - {k.email} - {k.city} - {k.Educational_Qualification}  - {k.skill_name})")
        case 3:
            try:
                idx = int(input("Enter ID to search: "))
                for i in range(len(karvands)):
                    if idx == karvands[i].id:
                        k = karvands[i]
                        print(f"{k.fullname} - {k.skill_name} ({k.skill_point})")
                else:
                    print("Not found wit this id")
            except ValueError:
                print("Invalid input")
                continue
        case 4:
            skill = input("Skill to search: ")
            results = [k for k in karvands if k.skill_name.lower() == skill.lower()]
            for k in results:
                print(f"{k.fullname} - {k.skill_name} ({k.skill_point})")
            if not results:
                print("No matches")
        case 5:
            try:
                idx = int(input("Enter ID to update: "))
                for i in range(len(karvands)):
                    if idx == karvands[i].id:
                        karvands[i] = get_karvand_input_update(karvands[i])
                        save_karvand()
                        print("Updated!")
                    else:
                        print("Not found")
            except ValueError:
                print("Invalid input")
                continue
        case 6:
            try:
                idx = int(input("Enter ID to delete: "))
                for i in range(len(karvands)):
                    if idx == karvands[i].id:
                        karvands.pop(i)
                        save_karvand()
                        print("Deleted!")
                    else:
                        print("Not found")
            except ValueError:
                print("Invalid input")
                continue
        case 7:
            total_karvands = len(karvands)
            print(f"Total: {total_karvands}")
            total_skills_count = len(set(k.skill_name for k in karvands))
            print(f"Total skills: {total_skills_count}")
            skill_points_mean = sum(k.skill_point for k in karvands) / total_karvands
            print(f"Average skill point: {skill_points_mean:.1f}")
            city_list = list(dict.fromkeys(k.city for k in karvands))
            print(f"Cities: {city_list}")
            all_skills = list(dict.fromkeys(k.skill_name for k in karvands))
            save_report({
                "total_karvands": total_karvands,
                "total_skills_count": total_skills_count,
                "skill_points_mean": skill_points_mean,
                "city_list": city_list,
                "all_skills": all_skills
            })
        case 8:
            break

        
    
    
    
    
    
    
    
    
    
    
    
    
    
    