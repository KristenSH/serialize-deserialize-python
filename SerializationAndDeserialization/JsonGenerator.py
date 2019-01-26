import json
import click # adding command line tool methods
import io

# define class person
class person:
    def __init__(self, id, name, address, phonenumber, email):
        self.id = id
        self.name = name
        self.address = address
        self.phonenumber = phonenumber
        self.email = email
        
# generates properties on the JSON file.
    def __repr__(self):
        return "%s(id=%r, name=%r, address=%r, phonenumber=%r, email=%r" % (
            self.__class__.__name__, self.id, self.name, self.address, self.phonenumber, self.email)

# input of person details and used the click module.
@click.command()
@click.option('--id', prompt='Your ID',
              help='The id of greet.')
@click.option('--name', prompt='Your name',
              help='The person to greet.')
@click.option('--address', prompt='Your address',
              help='The address of greet.')
@click.option('--phonenumber', prompt='Your phonenumber',
              help='The phonenumber of greet.')
@click.option('--email', prompt='Your email',
              help='The email of greet.')

def JsonGenerator(id, name, address, phonenumber, email):
    # Serialization and dumping instances of the person class
    with open('C:\\Users\\krist\\source\\repos\\SerializationAndDeserialization\\person.json', 'w') as outfile:
        JSONObj = json.dump(person(id, name, address, phonenumber, email).__dict__, outfile, indent=4)

    # Deserialization and loads from a json file
    with open("C:\\Users\\krist\\source\\repos\\SerializationAndDeserialization\\person.json", "r") as read_file:
        data = json.load(read_file)
        click.echo(data)

if __name__ == '__main__':
    JsonGenerator()