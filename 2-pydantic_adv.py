from pydantic import BaseModel
from typing import List, Dict,Optional

# Type Vaidation

# All the fields are by default required by pydantic model(to make optional field -- allergies: Optional[List[str]] = None -- none is deafult value and this is required in case of optional field)
class Patient(BaseModel):
    name: str
    age: int
    weight: float
    married: bool = False                                     # default value for a field
    allergies: Optional[List[str]] = None                     # List[str] -- because we have to valide the data in the list is str(two level validation)
    contact_details: Dict[str, str]

 
def insert_patient_data(patient: Patient):
        print(patient.name)
        print(patient.age)
        print("Inserted in DB")

def update_patient_data(patient: Patient):
        print(patient.name)
        print(patient.age)
        print("Updated in DB")


patient_info = {'name': 'Susy', 'age': 30 , 'weight': 55.5, 'married': True, 'allergies':['pollen','dust'], 'contact_details': {'email': 'susy@gmail.com', 'phone':'24238653'}}



patient1 = Patient(**patient_info)

insert_patient_data(patient1)
update_patient_data(patient1)

# pydentic is smart enough to convert the type of your data from '30'(str) to 30(int)


# Data validation in python 
# -- pydantic give you soe custo data type apart from python (for e.g. for validation for email -- EmailStr)


from pydantic import BaseModel, EmailStr, AnyUrl

class PatientOne(BaseModel):
    name: str
    age: int
    email: EmailStr
    linkedin_url : AnyUrl
    weight: float
    married: bool = False                                     # default value for a field
    allergies: Optional[List[str]] = None                     # List[str] -- because we have to valide the data in the list is str(two level validation)
    contact_details: Dict[str, str]

patientOne_info = {'name': 'Susy', 'age': 30, 'email': 'susy@gmail.com', 'linkedin_url': 'http://linkedin.com/1234', 'weight': 55.5, 'married': True, 'allergies':['pollen','dust'], 'contact_details': {'phone':'24238653'}}


def insert_patientOne_data(patient: PatientOne):
        print(patient.name)
        print(patient.age)
        print("Patient One Inserted in DB")

patient2 = PatientOne(**patientOne_info)
insert_patientOne_data(patient2)



# Some time you can require your custom data validation like 0< age <= 60
# Field function is also used to attach meta data


from pydantic import BaseModel, EmailStr, AnyUrl, Field
from typing import List, Dict,Optional, Annotated

# meta data can be attached with the combination of Field and Annotated
# can also set default value in - married and allergies field
# pydantic is smart enough to understand the integer value in string format as integer(Type coersion), but can work against you -- weight field -- using strict parameter


class PatientTwo(BaseModel):
#     name: str = Field(max_length=50)
    name: Annotated[str, Field(max_length=50, title='Name of the patient', description='the name should be less than 50 character', example=['Bob', 'peter'])]
    age: int
    email: EmailStr
    linkedin_url : AnyUrl
#     weight: float = Field(gt=0, le = 60)
    weight: float = Annotated[float, Field(gt=0, le = 60, strict=True)]
    married: Annotated[bool, Field(default=None, description='Is ptient married or not')]                                   
    allergies: Annotated[Optional[List[str]], Field(default=None, max_length=5)]                     # List[str] -- because we have to valide the data in the list is str(two level validation)
    contact_details: Dict[str, str]






