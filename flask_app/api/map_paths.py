from flask import render_template

def correct_action(current_state):   
   actions = []
   
   if current_state == 'start':
      actions = ['actions/upload_data.html']
   elif current_state == 'upload':
      actions = ['actions/describe.html']

   return render_template('actions/actions.html', next_actions = actions)
