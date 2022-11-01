from flask import render_template
def correct_action():
   possible_actions = []
   #next_actions = {'upload' : [('describe', 'actions/describe_data.html'), 
   #                           ('clean', 'actions/clean_data.html')]}
   next_actions = ['actions/describe_data.html', 'actions/clean_data.html']
   #value = next_actions.get(key)
   #for page in value:                           
   #   possible_actions.append(page[1])
   return render_template('actions/actions.html', next_actions)
