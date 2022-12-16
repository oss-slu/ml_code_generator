from flask import render_template

def correct_action(current_state):
   actions = []
   if current_state == 'start':
      return render_template('actions/upload_data.html')
   if current_state == 'upload':
      actions = ['actions/describe_data.html']
   elif current_state == 'describe':
      actions = ['actions/prepare_model.html']
   elif current_state == 'prepare':
      actions = ['actions/split_data.html']
   elif current_state == 'split':
      actions = ['actions/train_lin_reg.html']
   elif current_state == 'train':
      actions = ['actions/download_code.html']

   return render_template('actions/actions.html', next_actions = actions)
