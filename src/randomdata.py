
import random
import pandas as pd

class RandomFrame:
    
    def __init__(self, min_number, max_number, n_columns, n_rows):
        
        self.min_number = min_number
        self.max_number = max_number
        self.n_columns = n_columns
        self.n_rows = n_rows
    
    def generate_frame(self):
        
        df = pd.DataFrame()
        for c in range(1, self.n_columns+1):
            values = [random.randint(self.min_number, self.max_number) for l in range(self.n_rows)]
            df[f'column_{c}'] = values
        return df
    
    