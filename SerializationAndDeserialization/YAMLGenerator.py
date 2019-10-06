import yaml
import click # adding command line tool commands
import io

# define class person
class person:
    def __init__(self, id, name, address, phonenumber, email):
        self.id = id
        self.name = name
        self.address = address
        self.phonenumber = phonenumber
        self.email = email

# generates properties on the YAML file.
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
              help='The email.')

def YAMLGenerator(id, name, address, phonenumber, email):
    # Serialize YAML file
    with io.open('C:\\Users\\krist\\source\\repos\\SerializationAndDeserialization\\contacts.yaml', 'w', encoding='utf8') as outfile:
        YamlObj = yaml.dump(person(id, name, address, phonenumber, email).__dict__, outfile, default_flow_style=False, allow_unicode=True)

    # Deserialize YAML file
    with open("C:\\Users\\krist\\source\\repos\\SerializationAndDeserialization\\contacts.yaml", 'r') as stream:
        try:
            click.echo(yaml.load(stream))
        except yaml.YAMLError as exc:
            click.echo(exc)

if __name__ == '__main__':
    YAMLGenerator()