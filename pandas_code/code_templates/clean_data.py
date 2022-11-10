# removes rows with null entries
def get_code(args):
   args[0].dropna(axis=0,inplace=True)
   return args[0]


# need to clean xs and ys seperate 