from flask import render_template

#function should check for the current_state that it is given
#then should show the appropriate action pages
def mapp(current_state):
   if current_state == "upload_data":
      return render_template('actions/actions.html', next_actions=['actions/decribe_data.html'])
   return 0