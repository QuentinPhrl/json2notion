import optparse
import json
import os

from properties import Properties
from page import Page
from database import Database
from parse import Parser
from notion_api import GetToken

#token = os.environ["NOTION_TOKEN_PUT_EXPERIMENT"]

#database_id = 'd08f239718194d1f990c7ed7c67a6653'

PROPERTY = Properties()
PARSER = Parser()
GETTOKEN = GetToken()

def main():

    parser = optparse.OptionParser()  
    PARSER.get_option(parser=parser)

    datas = json_reader()

    for data in datas:

        fields_key = data[0]
        data_extract = data[1]

        column_type = read_database(fields_key)

        write_database(column_type,fields_key,data_extract)

 
def json_reader():
    datas = []
    data_extract = []

    json_file = open(PARSER.options.json_input)
    json_dict = json.load(json_file)
    
    for i in range(len(json_dict["entries"])):
        
        fields_key=list(json_dict["entries"][i]["fields"])
        fields_data=list(map(lambda l:json_dict["entries"][i]["fields"][l],json_dict["entries"][0]["fields"]))

        data_extract=[json_dict["entries"][i]["_id"], fields_data, json_dict["entries"][i]["body"]]

        datas.append([fields_key,data_extract])

    json_file.close()

    return datas


def read_database(fields_key):

    D = Database(integrations_token=GETTOKEN.token)
    D.retrieve_database(database_id=PARSER.options.notion_db_id,fields_key=fields_key)

    return D.properties_list


def write_database(column_type,fields_key,data_extract):

    set_property('title','id',data_extract[0])

    for type, key, data in zip(column_type,fields_key,data_extract[1]):
        set_property(type,key,data)
    
    P = Page(integrations_token=GETTOKEN.token)
    P.create_page(database_id=PARSER.options.notion_db_id, properties=PROPERTY)
    

def set_property(type,key,data):

    match type:
        case 'title':
            PROPERTY.set_title(key, data)
        case 'rich_text':
            PROPERTY.set_rich_text(key, data)
        case 'number':
            PROPERTY.set_number(key, data)
        case 'select':
            PROPERTY.set_select(key, data)
        case 'select':
            PROPERTY.set_multi_select(key, data)
        case 'checkbox':
            PROPERTY.set_checkbox(key, data)
        case 'url':
            PROPERTY.set_checkbox(key, data)
        case 'email':
            PROPERTY.set_email(key, data)
        case 'phone_number':
            PROPERTY.set_phone_number(key, data)
    print(PROPERTY.result)


if __name__ == '__main__':
    main()