import pandas as pd
import json as js

#check what are you doing in here 

class data:
    
    def __init__(self, json_file):
        self.json_file = json_file
        
    
    def create_user(self, username, password):
        self.json_file[username] = {"password":password}
        js.dump(self.json_file, open(r'The_program\csv\users_manifest.json', 'w'), indent=4)
        
        return self.json_file
    
    def check_passwords(self, username, password):
        
        if username and password in self.json_file.items():
            return True
        else:
            return False
    