from flask import Flask
from flask import request
app = Flask(__name__)

class Developer:

    def __init__(self, first_name, last_name, programming_language):
        self.first_name = first_name
        self.last_name = last_name
        self.programming_language = programming_language

    def __str__(self):
        return f'{self.first_name} {self.last_name} - {self.programming_language}'

dev1 = Developer('Harry', 'Potter', 'python')
dev2 = Developer('Hermione', 'Granger', 'ruby')
dev3 = Developer('Filius', 'Flitwick', 'java')

developers = [dev1, dev2, dev3]


@app.route('/developer_controller')
def developer_controller():
    """
    In order to create developer and add to the list the controller should be called
    with parameters:
    fn - set first name
    ln - set last name
    pl - programming language
    Example: http://[host]:[port]/developer_controller?fn=[first_name]&ln=[last_name]&pl=[language]
    Otherwise if controller will be called without parameters empty developer instance will
    be created
    :return: created developer
    """
    first_name = request.args.get('fn')
    last_name = request.args.get('ln')
    programming_language = request.args.get('pl')
    dev = Developer(first_name, last_name, programming_language)
    developers.append(dev)
    return str(dev)


@app.route('/remove_developer')
def remove_developer():
    if len(developers) == 0:
        return 'There is no developers in the list'
    developers.pop()
    return str(list(map(lambda dev: str(dev), developers)))
