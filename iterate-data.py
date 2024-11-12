import os
import pandas as pd
import json
class IterateData:
    
    def CreateDataset(self, path):
        data = {
            "Patient ID": [],
            "Age": [],
            "Gender":[],
            "Location": [],
            "Recording Number": [],
            "Start (in ms)":[],
            "End (in ms)": [],
            "Type of Event":[]
        }
        
        for filename in os.listdir(path):
            if filename.__contains__(".json"):
                json_path = path + "/" + filename
                with open(json_path) as f:
                    info = json.load(f)
                    filename = filename.replace(".json", "")
                    patient_id, age, gender, location, recording_number = filename.split("_")
                    for i in info["event_annotation"]:
                        data["Patient ID"].append(patient_id)
                        data["Age"].append(age)
                        data["Gender"].append(gender)
                        data["Location"].append(location)
                        data["Recording Number"].append(recording_number)
                        data["Start (in ms)"].append(i["start"])
                        data["End (in ms)"].append(i["end"])
                        data["Type of Event"].append(i["type"])
                                       
        df = pd.DataFrame(data)
        return df
    

def main():
    iterator = IterateData()
    path = "/Users/harshgarg/Projects/HarshNikhil/RespiratoryEventDetection/SPRSound/Detection/train_detection_json"
    print(iterator.CreateDataset(path))
    
if __name__ == "__main__":
    main()
