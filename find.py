print('import from find.py')

def find_index(to_search, target):
  """ Find the index of a value in a sequence """
  for index, value in enumerate(to_search):
    if value == target:
      # Found
      return f'Index of {target} is {index}'
  # Not Found
  return 'No element in the sequence'