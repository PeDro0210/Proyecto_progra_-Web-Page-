import pandas as pd


#check what are you doing in here 

class data:
    
    def __init__(self, json_file):
        self.json_file = json_file
        
    def read_json(self):
        return pd.read_json(self.json_file)
    
    def create_user(self, username, password):
        df = self.read_json()
        df = df.append({'username': username, 'password': password}, ignore_index=True)
        df.to_json(self.json_file)
    
    def check_passwords(self, username, password):
        df = self.read_json()
        if username and password in df.values:
            return True
        else:
            return False
    
         