class Parser:
    def __init__(self):
        self.options = object

    def get_option(self,parser):
        # create OptionParser object
        
        # add options
        parser.add_option('-d','--notion-db-id',
                        dest = 'notion_db_id',
                        type = 'string',
                        help = 'specify the id of the database notion')
        parser.add_option('-f', '--json-file',
                        dest = 'json_input',
                        type = 'string',
                        help = 'specify the input json file')
        
        (options, args) = parser.parse_args()
        self.options = options
        if (options.notion_db_id == None):
            print("exit")
            exit(0)
        elif (options.json_input == None):
            print("exit")
            exit(0)