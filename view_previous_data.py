import json

with open("data.json", "r") as File:
    Saved_Data = json.load(File)

print(Saved_Data[-1])