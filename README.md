# pydantic
# Pydantic – Why It Is Used

Pydantic is a Python library used for **data validation** and **type enforcement**.  
It ensures that the data entering your application is **correct, structured, and valid**.

---

# 1. Type Validation

Consider the following function:

```python
def insert_patient_data(name, age):
    print(name)
    print(age)
    print("Inserted in DB")

The function expects:

name → string

age → integer

However, someone could call the function like this:

insert_patient_data("bob", "thirty")

Using Type Hinting

We can add type hints to the function:

def insert_patient_data(name: str, age: int):
    print(name)
    print(age)
    print("Inserted in DB")


But type hints do not enforce types at runtime.

They only:

provide hints to developers

help static type checkers like mypy

So this will still work:

insert_patient_data("bob", "thirty")

Manual Type Checking

To enforce types manually, we can add checks:

def insert_patient_data(name, age):
    if type(name) == str and type(age) == int:
        print(name)
        print(age)
        print("Inserted in DB")
    else:
        raise TypeError("Incorrect data type")


This works, but it is not scalable.

If we add:

more fields

more functions like update_patient_data

we would have to rewrite validation logic again and again.


2. Data Validation

Sometimes validation involves more than just types.

Example: Age cannot be negative.


def insert_patient_data(name, age):
    if type(name) == str and type(age) == int:
        if age < 0:
            raise ValueError("Age can't be negative")
        else:
            print(name)
            print(age)
            print("Inserted in DB")
    else:
        raise TypeError("Incorrect data type")


Problems with this approach:

Validation logic is repeated

Hard to maintain

Not scalable when fields increase



How Pydantic Works
1. Define a Pydantic Model

Create a class that represents the ideal schema of the data.

It includes:

expected fields

their data types

validation constraints

Example constraints:

gt=0 → greater than 0

lt=100 → less than 100

2. Instantiate the Model with Raw Data

Provide raw input data (usually a dictionary or JSON-like structure).

3. Automatic Validation

Pydantic will automatically:

validate the data

convert it to the correct Python types if possible

4. Validation Errors

If the data does not meet the model requirements, Pydantic raises:

ValidationError

. Use the Validated Model

The validated model object can be passed throughout the application.

This ensures every part of the program works with:

clean data

type-safe data

logically valid data

Example Using Pydantic

from pydantic import BaseModel, Field

class Patient(BaseModel):
    name: str
    age: int = Field(gt=0)

def insert_patient_data(patient: Patient):
    print(patient.name)
    print(patient.age)
    print("Inserted in DB")

data = {
    "name": "Bob",
    "age": 30
}

patient = Patient(**data)

insert_patient_data(patient)


If invalid data is passed:

data = {
    "name": "Bob",
    "age": -5
}

Pydantic will raise a ValidationError.


