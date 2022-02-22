from model import code_blocks
import pandas as pd

class CodeGenerator:
   def __init__(self):
      self.blocks = code_blocks.AllBlocks();

   def load_data(self, csv_file):
      self.dataframe = pd.read_csv(csv_file)
      block = code_blocks.CodeBlock("Create a dataframe", 
         ["import pandas as pd", "dataframe = pd.read_csv(\'"+csv_file+"\')"])
      self.blocks.add_next_block(block)
      return self.dataframe.shape

   def describe_data(self):
      output = self.dataframe.describe()
      block = code_blocks.CodeBlock("Describe data",
         ["data_description = dataframe.describe()", "print(data_description)"])
      self.blocks.add_next_block(block)
      return output

   def clean_data(self):
      self.dataframe.dropna(axis=0,inplace=True)
      block = code_blocks.CodeBlock("Drop null rows",
         ["dataframe.dropna(axis=0,inplace=True)"])
      self.blocks.add_next_block(block)
      return self.dataframe.shape

   def get_labels(self):
      block = code_blocks.CodeBlock("Get feature names",
         ["keys = dataframe.keys()", "print(keys)"])
      keys = self.dataframe.keys()
      self.blocks.add_next_block(block)
      return keys
     
   def download_code(self):
      return self.blocks.to_text()
