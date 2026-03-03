from pydantic import BaseModel, EmailStr, AnyUrl, Field, model_validator
from typing import List, Dict,Optional, Annotated

# What if the data validation depends on more than one field - e.g.- if patient ag is more than 60 the it should have a emergancy contact number - if not we will not create patient -- model validator is used


class Patient(BaseModel):
    name: str
    email: EmailStr
    age: int
    weight: float
    married: bool = False                                     # default value for a field
    allergies: Optional[List[str]] = None                     # List[str] -- because we have to valide the data in the list is str(two level validation)
    contact_details: Dict[str, str]


    @model_validator(mode='after')                        #no need of field as this works on whole model 
    def validate_emergency_contact(cls, model):
        if model.age > 60 and 'emergency' not in model.contact_details:
            raise ValueError('Patient older than 60 must have an emergency contact')
        return model
    
def insert_patient_data(patient: Patient):
        print(patient.name)
        print(patient.age)
        print("Inserted in DB")

patient_info = {'name': 'Susy', 'email': 'susy@hdfc.com', 'age': 62 , 'weight': 55.5, 'married': True, 'allergies':['pollen','dust'], 'contact_details': {'phone':'24238653', 'emergency':'9876543321'}}

patient1 = Patient(**patient_info)      # in this step these are the step performed - VAlidatio, typer coresion

insert_patient_data(patient1)



