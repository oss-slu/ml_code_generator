from model import code_blocks
class CodeParser:
   def __init__(self, template_mapping, parse_template):
      self.blocks = code_blocks.AllBlocks()
      self.function_mapping = template_mapping
      self.parse_template = parse_template
      self.data = {}

   def download_code(self):
      return self.blocks.to_text()

   def _create_new_block(self, comment, statements):
      block = code_blocks.CodeBlock(comment, statements)
      self.blocks.add_next_block(block)

   def _parse_and_execute(self, template, args):
      print("Args is ", args)
      replaced_args = []
      string_args = []
      for arg in args:
         print("Each Argument::", arg)
         if isinstance(arg, str) and arg in self.data:
            replaced_args.append(self.data[arg])
            string_args.append(arg)
         else:
            replaced_args.append(arg)
            if isinstance(arg, str):
               string_args.append('\"'+arg+'\"')
            else:
               string_args.append(str(arg))
         print("replaced arg", replaced_args)
         print("string arg", string_args)

      (comments, code) = self.parse_template(template, string_args)
      self._create_new_block(comments[0], code)
      output = self.function_mapping[template](replaced_args)
      return output

   def _save(self, key, value):
      self.data[key] = value
