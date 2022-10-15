from json2notion.console import print_error

class Parser:
    def __init__(self):
        """
        init
        """
        self.options = object

    def get_option(self,parser):
        """
        Create a page
        :param parser: Object of OptionParser()
        """
        parser.add_option('-i','--id',
                        dest = 'notion_db_id',
                        type = 'string',
                        help = 'Specify the id of the database notion')
        parser.add_option('-f', '--file',
                        dest = 'json_input',
                        type = 'string',
                        help = 'Specify the input json file')
        
        (options, args) = parser.parse_args()
        self.options = options
        
        if (options.notion_db_id == None):
            print_error("please enter a Notion database's id with -d option")
            exit(1)
        elif (options.json_input == None):
            print_error("please provide a json file with the -f option")
            exit(1)