
import optparse
import json

from console import print_error,print_status

from children import Children
from properties import Properties
from page import Page
from database import Database
from parse import Parser
from notion_api import GetToken

#token = os.environ["NOTION_TOKEN_PUT_EXPERIMENT"]

#database_id = 'd08f239718194d1f990c7ed7c67a6653'

CHILDREN = Children()
PROPERTY = Properties()
PARSER = Parser()
GETTOKEN = GetToken()
DATABASE = Database(integrations_token=GETTOKEN.token)
PAGE = Page(integrations_token=GETTOKEN.token)

def main():

    parser = optparse.OptionParser()  
    PARSER.get_option(parser=parser)

    datas = json_reader()

    page_ids = retrive_page_id(datas[0][1][1])

    for index,(fields_key,data_extract)in enumerate(datas):

        column_type = read_database(fields_key)

        if page_ids:
            update_database(column_type,fields_key,data_extract,page_ids[index])
        elif not page_ids:
            write_database(column_type,fields_key,data_extract)

def json_reader():

    datas = []

    try: 
        json_file = open(PARSER.options.json_input)
        json_dict = json.load(json_file)

    except FileNotFoundError:
        print_error(f"The '{PARSER.options.json_input}' file cannot be found ")
        exit(1)

    try:
        for i in range(len(json_dict["entries"])): 
            fields_key=list(json_dict["entries"][i]["fields"])
            fields_data=list(map(lambda l:json_dict["entries"][i]["fields"][l],json_dict["entries"][0]["fields"]))

            body_data=[json_dict["entries"][i]["body"]["type"],json_dict["entries"][i]["body"]["content"]]

            data_extract=[json_dict["entries"][i]["_id"],json_dict["entries"][i]["type"], fields_data, body_data]

            datas.append([fields_key,data_extract])

        json_file.close()

    except KeyError:
        print_error("The json file is badly formatted")
        exit(1)

    return datas

def read_database(fields_key):

    DATABASE.retrive_column_type(database_id=PARSER.options.notion_db_id,fields_key=fields_key)

    return DATABASE.type_list

def retrive_page_id(content_type):

    page_ids = []

    DATABASE.query_database_filter(database_id=PARSER.options.notion_db_id, column_name="Type", content=content_type)

    for result in DATABASE.result["results"]:
            page_ids.append(result["id"])
    
    return page_ids

def write_database(column_type,fields_key,data_extract):

    set_property('title','id',data_extract[0])
    set_property('select','Type',data_extract[1])

    for type, key, data in zip(column_type,fields_key,data_extract[2]):
        set_property(type,key,data)

    set_children(data_extract[3][0],data_extract[3][1])

    PAGE.create_page(database_id=PARSER.options.notion_db_id, properties=PROPERTY,children=CHILDREN)

    print_status("Success","Data added to the database ")  #Not yet reliable 

    PROPERTY.clear()
    CHILDREN.clear()

def update_database(column_type,fields_key,data_extract,page_id):

    set_property('title','id',data_extract[0])
    set_property('select','Type',data_extract[1])

    for type, key, data in zip(column_type,fields_key,data_extract[2]):
        set_property(type,key,data)
    
    set_children(data_extract[3][0],data_extract[3][1])
    
    PAGE.update_page(page_id=page_id,properties=PROPERTY,children=CHILDREN)

    print_status("Success","Updated database")  #Not yet reliable 

    PROPERTY.clear()
    CHILDREN.clear()

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
        case 'multi_select':
            PROPERTY.set_multi_select(key, data)     #Not sure if it works, this option requires an input table
        case 'checkbox':
            PROPERTY.set_checkbox(key, data)
        case 'url':
            PROPERTY.set_checkbox(key, data)
        case 'email':
            PROPERTY.set_email(key, data)
        case 'phone_number':
            PROPERTY.set_phone_number(key, data)

def set_children(type,data):

    match type:
        case 'embed':
            CHILDREN.set_embed(data)
    

if __name__ == '__main__':
    main()