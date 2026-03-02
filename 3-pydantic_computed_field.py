from pydantic import BaseModel, EmailStr, computed_field
from typing import List, Dict,Optional

# Computed Field -- for this field value is not provided by th user, instead you calculate the field from available fields
#  For e.g.-- For BMI we can use weight and height

class Patient(BaseModel):
    name: str
    email: EmailStr
    age: int
    weight: float
    height: float
    married: bool = False                                     # default value for a field
    allergies: Optional[List[str]] = None                     # List[str] -- because we have to valide the data in the list is str(two level validation)
    contact_details: Dict[str, str]


    @computed_field
    @property
    def calculate_bmi(self) -> float:
        bmi = round(self.weight/(self.height**2),2)
        return bmi
    

def insert_patient_data(patient: Patient):
        print(patient.name)
        print(patient.age)
        print(patient.allergies)
        print(patient.married)
        print('BMI',patient.calculate_bmi)
        print("Inserted in DB")

patient_info = {'name': 'Susy', 'email': 'susy@hdfc.com', 'age': 62 , 'weight': 82, 'height': 176, 'married': True, 'allergies':['pollen','dust'], 'contact_details': {'phone':'24238653', 'emergency':'9876543321'}}

patient1 = Patient(**patient_info)      # in this step these are the step performed - VAlidatio, typer coresion

insert_patient_data(patient1)