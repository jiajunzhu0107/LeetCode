from mimetypes import init
import requests
import json
from portApi import db
from model import Port
# from schema import port_schema

def getPortData(url):
    response = requests.get(url)
    data = response.json()
    return data

def insertIntoDb(data):
    # data = schema.load(data)
    for port_code, port_data in data.items():
        new_port = Port(portId = port_code, name = port_data['name'], country = port_data['country'], data=str(port_data))
        db.session.add(new_port)
    db.session.commit()

        # data = json.load()
    # print(data)

    # open("test.json", "wb").write(response.content)
    # print(data)

def main():
    url = "https://raw.githubusercontent.com/marchah/sea-ports/master/lib/ports.json"
    data = getPortData(url)
    insertIntoDb(data)

if __name__ == "__main__":
    url = "https://raw.githubusercontent.com/marchah/sea-ports/master/lib/ports.json"
    res = getPortData(url)
    from initdb import init_db
    init_db()
    insertIntoDb(res)
    data = Port.query.get('AEAJM')
    print(data)