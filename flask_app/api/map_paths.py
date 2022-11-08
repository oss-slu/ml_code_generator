from flask import render_template

def correct_action(current_state):   
   next_actions = []
   
   if current_state == 'start'
      next_actions = ['actions/describe.html']

   return render_template('actions/actions.html', next_actions)
