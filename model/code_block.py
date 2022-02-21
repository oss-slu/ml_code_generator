class CodeBlock:
   def __init__(self, comment, statements):
      self.comment = comment
      self.statements = statements

   def to_text(self):
      text_value = comment+"\n"
      for s in statements:
         text_value += s+"\n"
      return text_value
