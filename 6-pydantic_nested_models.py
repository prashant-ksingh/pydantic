from pydantic import BaseModel

# here address is itself collection of different fields

# Better organisation of related data(e.g. vitals. address, insurance)
# Reusability: Use Vitals in multiple models(e.g. Patient, MedicalRecord)
# Readability: Easier for developers and API consumer to understand
# Validation: Nested models are validated automatically, no extra work needed

class Address(BaseModel):
    city: str
    state: str
    pin: str

class Patient(BaseModel):
    name: str
    gender: str
    age: int
    address: Address


address_dict = {'city':'delhi', 'state': 'india', 'pin': '120001'}
address1 = Address(**address_dict)


patient_dict = {'name': 'Allen', 'gender': 'male', 'age': 35, 'address': address1}

patient1 = Patient(**patient_dict)

print(patient1)
print(patient1.address.pin)