class CodeBlock:
   def __init__(self, comment, statements):
      self.comment = comment
      self.statements = statements
      self.next_block = None

   def to_text(self):
      text_value = self.comment+"\n"
      for statement in self.statements:
         text_value += statement+"\n"
      return text_value

   def set_next_block(self, next_block):
      self.next_block = next_block

   def get_next_block(self):
      return self.next_block
