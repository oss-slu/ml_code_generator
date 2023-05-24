import re
import os
def parse_template(template_name, args):
   # hashmap for access of PATH
   root_map = {'clean_data' : 'pandas/', 'describe_data' : 'pandas/',
               'drop_x' : 'pandas/', 'one_hot_encode_x_data' : 'pandas/',
               'one_hot_encode_y_data' : 'pandas/', 'read_csv' : 'pandas/', 
               'select_y' : 'pandas/', 'eval_decision_tree' : 'sklearn/', 
               'eval_lin_reg' : 'sklearn/','split' : 'sklearn/',
               'train_decision_tree' : 'sklearn/', 'train_lin_reg' : 'sklearn/',
               'get_keys' : '','predict_decision_tree' : 'tensorflow/', 
               'predict_lin_reg' : 'tensorflow/' }
   root_dir = os.environ.get("PYTHONPATH", None)
   template = root_dir+'/code_templates/'+root_map[template_name]+template_name+".py"
   generated_comments = []
   generated_code = []
   indent_size = 0
   is_space = False
   with open(template, encoding='ascii') as source_code:
      lines = source_code.readlines()
      if (not is_space) and re.match(r'\s', lines[0]):
         is_space = True
      for line in lines:
         trimmed_line = line.rstrip()
         if trimmed_line.startswith("def get_code"):
            continue
         if trimmed_line.strip().startswith("return"):
            continue
         if trimmed_line.startswith("#"):
            generated_comments.append(trimmed_line)
         else:
            trimmed_line = replace_args_with_values(trimmed_line, args)
            if not (trimmed_line.startswith("from") or trimmed_line.startswith("import")):
               if indent_size == 0:
                  indent_size = len(trimmed_line) - len(trimmed_line.lstrip())
               if not is_space:
                  trimmed_line = trimmed_line.expandtabs(3)
                  indent_size = 3
               trimmed_line = trimmed_line[indent_size:]
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
