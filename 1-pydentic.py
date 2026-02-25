from pydantic import BaseModel

class Patient(BaseModel):
    name: str
    age: int
    weight: float

def insert_patient_data(patient: Patient):
        print(patient.name)
        print(patient.age)
        print("Inserted in DB")

def insert_patient_data(patient: Patient):
        print(patient.name)
        print(patient.age)
        print("Updated in DB")


patient_info = {'name': 'Susy', 'age': 30 , 'weight': 55.5}

patient1 = Patient(**patient_info)

insert_patient_data(patient1)
insert_patient_data(patient1)

# pydentic is smart enoughto convert the type of your data from '30'(str) to 30(int)