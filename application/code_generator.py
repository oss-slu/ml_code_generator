import pandas as pd

class CodeGenerator:
   def load_data(self, csv_file):
      self.dataframe = pd.read_csv(csv_file)
      self.code_block = CodeBlock("Create a dataframe", ["import pandas as pd", "pd.read_csv("+csv_file+")"])

   def download_code(self):
      block = self.code_block
      while block != None:
         code+=block.to_text()
         block = block.get_next_block()
      return code
