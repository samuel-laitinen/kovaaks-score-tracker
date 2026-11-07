# read and print scores from C:\Program Files (x86)\Steam\steamapps\common\FPSAimTrainer\FPSAimTrainer\stats
import os 

folder =  r"C:\Program Files (x86)\Steam\steamapps\common\FPSAimTrainer\FPSAimTrainer\stats"

def readscores(filename):
    score = None
    scenario = None
    try:
        with open(filename) as source:
            for line in source:
                parts = line.split(",")
                if line.startswith("Score:"):
                    score = float(parts[1])
                elif line.startswith("Scenario:"):
                    scenario = parts[1].strip()
    except IOError:
        print("IOError")
    return score, scenario


best = {}

best_date = {}

for name in os.listdir(folder):
    if name.endswith(".csv"):
        parts = name.split(" - ")
        date = parts[-1].split("-")[0]
        path = os.path.join(folder, name)
        score, scenario = readscores(path)
        if scenario not in best or score > best[scenario]:
            best[scenario] = score
            best_date[scenario] = date

for scenario, score in best.items():
    print(f"{scenario}: {score} - {best_date[scenario]}")

