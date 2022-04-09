from dataclasses import field
import imp
import requests
import json
import os

from properties import Properties
from page import Page
from database import Database


token = os.environ["NOTION_TOKEN_PUT_EXPERIMENT"]

database_id = 'd08f239718194d1f990c7ed7c67a6653'

headers = {
    "Accept": "application/json",
    "Notion-Version": "2022-02-22",
    "Content-Type": "application/json",
    "Authorization": "Bearer " + token
}

PROPERTY = Properties()

def main():

    fields_key, data_extract = json_reader()
    
    column_type = read_database(fields_key)

    write_database(column_type,fields_key,data_extract)
 
def json_reader():
    
    data_extract =[]

    json_file = open('data.json')
    json_dict = json.load(json_file)

    data_extract.append(json_dict["entries"][0]["_id"])
    
    fields_key=list(json_dict["entries"][0]["fields"])
    fields_data=list(map(lambda l:json_dict["entries"][0]["fields"][l],json_dict["entries"][0]["fields"]))

    data_extract.append(fields_data)
    data_extract.append(json_dict["entries"][0]["body"])
    
    json_file.close()

    return fields_key,data_extract

def read_database(fields_key):

    D = Database(integrations_token=token)
    D.retrieve_database(database_id=database_id,fields_key=fields_key)

    return D.properties_list

def write_database(column_type,fields_key,data_extract):

    set_property('title','id',data_extract[0])

    for type, key, data in zip(column_type,fields_key,data_extract[1]):
        set_property(type,key,data)
    
    P = Page(integrations_token=token)
    P.create_page(database_id=database_id, properties=PROPERTY)

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