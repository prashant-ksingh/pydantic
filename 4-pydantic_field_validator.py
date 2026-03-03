from pydantic import BaseModel, EmailStr, AnyUrl, Field, field_validator
from typing import List, Dict,Optional, Annotated

# Field Validators - Suppose the Hospital has a tieup models with a company - So the people from the caompany can get a specific discount -- you can identify from the email
# you can perform transformation - e.g. - patient name should be in capital letter
# field validator works in two mode -- Before and After mode  (default is after)

class Patient(BaseModel):
    name: str
    email: EmailStr
    age: int
    weight: float
    married: bool = False                                     # default value for a field
    allergies: Optional[List[str]] = None                     # List[str] -- because we have to valide the data in the list is str(two level validation)
    contact_details: Dict[str, str]

    @field_validator('email', mode='after')                #after means here we get value after the validation ans type coersion 
    @classmethod
    def email_validator(cls, value):
        valid_domains = ['hdfc.com', 'icici.com']
        # abc@gmail.com
        domain_name = value.split('@')[-1]

        if domain_name not in valid_domains:
            raise ValueError('Not a valid domain')

        return value 
    
    @field_validator('name')
    @classmethod
    def transform_name(cls, value):
         return value.upper()
    

    @field_validator('age', mode='before')         # her if you'll send age: '30' the this will give error - TypeError: '<' not supported between instances of 'int' and 'str'
    @classmethod
    def validate_age(cls, value):
        if 0 < value <= 100:
            return value
        else:
            raise ValueError("Age should be in between 0 and 100") 



def insert_patient_data(patient: Patient):
        print(patient.name)
        print(patient.age)
        print("Inserted in DB")



patient_info = {'name': 'Susy', 'email': 'susy@hdfc.com', 'age': '30' , 'weight': 55.5, 'married': True, 'allergies':['pollen','dust'], 'contact_details': {'phone':'24238653'}}

patient1 = Patient(**patient_info)      # in this step these are the step performed - VAlidatio, typer coresion

insert_patient_data(patient1)
