from marshmallow import Schema, fields, pprint, post_load

class Person(object):
    def __init__(self, name, age):
        self.name = name
        self.age = age
    
    def __repr__(self):
        return '{} is {} years old'.format(self.name, self.age)

# schema is a description of the data that goes into the object
# needs description because marshmallow needs to know how to convert input data
class PersonSchema(Schema):
    # desribe the data that is inputed
    name = fields.String()
    age = fields.Integer()

    @post_load
    def create_person(self, data):
        return Person(**data)

input_dict = {}

input_dict['name'] = input('What is your name?')
input_dict['age'] = input('How old are you?')

#person = Person(name=input_dict['name'], age=input_dict['age'])

schema = PersonSchema()

#serialize complicated python object -> simple data structure
#result = schema.dump(person)

# serialize simple data structure -> complicated python object
result = schema.load(input_dict)

pprint(result.data)


