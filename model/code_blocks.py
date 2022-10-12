from collections import deque

class CodeBlock:
   def __init__(self, comment, statements):
      self.comment = comment
      self.statements = statements

   def to_text(self):
      text_value = "#"+self.comment+"\n"
      for statement in self.statements:
         text_value += statement+"\n"
      return text_value

   def from_text(self, text):
      pass

class AllBlocks:
   def __init__(self):
      self.blocks = deque()
   
   #clear previously insetred blocks of code
   def resetAll(self):
      self.blocks = deque()
       
   def from_file(self, file_name):
      pass

   def to_text(self):
      code = ""
      for block in self.blocks:
         code+=block.to_text()
      return code

   def to_file(self, file_name):
      pass

   def add_next_block(self, next_block):
      self.blocks.append(next_block)
