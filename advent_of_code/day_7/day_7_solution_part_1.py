from pprint import pprint  as pp
# with open('/Users/aabitokh/Desktop/repo/Assir-Bitokhov/advent_of_code/day_7/input_test.txt', 'r') as f:
#     input_file = f.read()

#!/usr/bin/env python

# Read the input file
with open('/Users/aabitokh/Desktop/repo/Assir-Bitokhov/advent_of_code/day_7/input_test.txt', 'r')as f:
    input_lines = f.readlines()
# Parse the input data
directories = {'/': {'size': 0, 'children': []}}
current_dir = '/'
data = input_lines
for line in data:
  # If the line starts with '$', it is a command
  if line[0] == '$':
    # Split the line into command and arguments
    tokens = line.strip().split(' ')
    command = tokens[0][1:]
    args = tokens[1:]
    # Handle the different commands
    if command == 'cd':
      if args[0] == '/':
        current_dir = '/'
      elif args[0] == '..':
        current_dir = directories[current_dir]['parent']
      else:
        current_dir = args[0]
    elif command == 'ls':
      # Process the files and directories in the current directory
      for entry in args:
        # Split the entry into name and size
        tokens = entry.split(' ')
        name = tokens[1]
        size = int(tokens[0])
        if name[-1] == '.':
          # This is a file, so add its size to the current directory
          directories[current_dir]['size'] += size
        else:
          # This is a directory, so add it as a child of the current directory
          directories[name] = {'parent': current_dir, 'size': 0, 'children': []}
          directories[current_dir]['children'].append(name)

# Recursively calculate the total size of each directory
def calc_total_size(dir_name):
  total_size = directories[dir_name]['size']
  for child_name in directories[dir_name]['children']:
    total_size += calc_total_size(child_name)
  return total_size

# Find all directories with a total size of at most 100000
sum_of_sizes = 0
for dir_name in directories:
  total_size = calc_total_size(dir_name)
  if total_size <= 100000:
    sum_of_sizes += total_size

# Print the result
print(sum_of_sizes)
