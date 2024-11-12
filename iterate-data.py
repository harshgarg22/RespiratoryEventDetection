import os
import pandas as pd

class IterateData:
    
    def CreateDataset(self, path):
        data = {
            "Patient ID": [],
            "Age": [],
            "Gender":[],
            "Location": [],
            "Recording Number": []
        }
        
        for filename in os.listdir(path):
            if filename.__contains__(".json"):
                filename = filename.replace(".json", "")
                patient_id, age, gender, location, recording_number = filename.split("_")
                data["Patient ID"].append(patient_id)
                data["Age"].append(age)
                data["Gender"].append(gender)
                data["Location"].append(location)
                data["Recording Number"].append(recording_number)
        
        df = pd.DataFrame(data)
        
        return df
    

def main():
    iterator = IterateData()
    path = "/Users/harshgarg/Projects/HarshNikhil/RespiratoryEventDetection/SPRSound/Detection/train_detection_json"
    print(iterator.CreateDataset(path))
    
if __name__ == "__main__":
    main()
