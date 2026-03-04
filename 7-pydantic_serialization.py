from pydantic import BaseModel

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

temp = patient1.model_dump()

print(temp)
print(type(temp))

temp_json = patient1.model_dump_json()

print(temp_json)
print(type(temp_json))

temp_json_name = patient1.model_dump_json(include=['name'])

print(temp_json_name)

rem_json_name = patient1.model_dump_json(exclude=['name'])
rem_json_state = patient1.model_dump_json(exclude={'address': ['state']})


# Suppose in models gender has default value and while making a models obj male field is not given
json_field = patient1.model_dump(exclude_unset=True)

# after exclude_unset = True is set the fields whic are not being passed while creationaof object will not be exported
