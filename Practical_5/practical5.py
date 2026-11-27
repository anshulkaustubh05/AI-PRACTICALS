# Practical 5: Rule based expert system for disease diagnosis (forward chaining)
# Name: Anshul Kaustubh
# Enrollment No: 92400118122

print("Name: Anshul Kaustubh | Enrollment No: 92400118122")
print("Practical 5 - Rule Based Expert System (Medical Diagnosis)")
print("-" * 55)

# rules : (list of conditions, conclusion)
rules = [
    (["fever", "cough"], "respiratory infection"),
    (["respiratory infection", "body pain"], "Flu"),
    (["sneezing", "runny nose"], "Common Cold"),
    (["fever", "headache", "joint pain"], "Dengue"),
    (["Flu"], "Advice: take rest, drink fluids and take paracetamol"),
    (["Common Cold"], "Advice: take steam and warm water"),
    (["Dengue"], "Advice: get a blood test and see a doctor quickly"),
]


def forward_chaining(symptoms):
    facts = list(symptoms)
    changed = True
    while changed:
        changed = False
        for conditions, result in rules:
            ok = True
            for c in conditions:
                if c not in facts:
                    ok = False
            if ok and result not in facts:
                facts.append(result)
                print("   Rule fired:", " AND ".join(conditions), "=>", result)
                changed = True
    return facts


patients = {
    "Patient 1": ["fever", "cough", "body pain"],
    "Patient 2": ["sneezing", "runny nose"],
    "Patient 3": ["fever", "headache", "joint pain"],
    "Patient 4": ["headache"],
}

for name, symptoms in patients.items():
    print(name, "symptoms:", symptoms)
    facts = forward_chaining(symptoms)
    diagnosis = [f for f in facts if f in ["Flu", "Common Cold", "Dengue"]]
    if diagnosis:
        print("   Diagnosis:", diagnosis[0])
    else:
        print("   Diagnosis: not enough information, consult a doctor")
    print()
