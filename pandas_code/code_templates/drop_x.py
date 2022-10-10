# drop dataset features passed to args param
def get_code(args):
   x_values = args[0].drop(args[1], axis=1)
   return x_values
