import re
def parse_template(template_name, args):
   template = 'pandas_code/code_templates/'+template_name+".py"
   generated_comments = []
   generated_code = []
   with open(template, encoding='ascii') as source_code:
       lines = source_code.readlines()
       for line in lines:
           trimmed_line = line.strip()
           if trimmed_line.startswith("def get_code"):
               continue
           if trimmed_line.startswith("return"):
               continue
           if trimmed_line.startswith("#"):
               generated_comments.append(trimmed_line)
           else:
               trimmed_line = replace_args_with_values(trimmed_line, args)
               generated_code.append(trimmed_line)

   return (generated_comments, generated_code)


def replace_args_with_values(line, args):
   match = re.search(r"args\[[0-9]\]", line)
   while match:
       args_span = match.span()
       args_string = line[args_span[0]:args_span[1]]
       args_index = get_args_index(args_string)

       line = line[0:args_span[0]]+args[args_index]+line[args_span[1]:]
       match = re.search(r"args\[[0-9]\]", line)

   return line


def get_args_index(args_string):
   index_match = re.search('[0-9]+', args_string)
   index_span = index_match.span()
   index_string = args_string[index_span[0]:index_span[1]]
   index_value = int(index_string)
   return index_value
