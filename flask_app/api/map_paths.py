from flask import render_template
def correct_action(current_state):
   next_actions = []
   if current_state == "split_data":
      next_actions = ['actions/select_training_ratio_value.html']
   elif current_state == "upload":
      next_actions = ['actions/describe_data.html',
                     'actions/clean_data.html']
   return render_template('actions/actions.html', next_actions)
