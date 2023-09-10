environment = {
    'A': 'Dirty',
    'B': 'Dirty'
}

# Define the possible actions
actions = ['Left', 'Right', 'Clean']

# Define the vacuum cleaner agent
def vacuum_cleaner_agent(env):
    # Check if the environment is clean
    if all(value == 'Clean' for value in env.values()):
        return
    
    # Check the current state of the environment
    if env['A'] == 'Dirty':
        print("Vacuum cleaner is cleaning room A.")
        env['A'] = 'Clean'
    elif env['B'] == 'Dirty':
        print("Vacuum cleaner is cleaning room B.")
        env['B'] = 'Clean'
    elif env['A'] == 'Clean' and env['B'] == 'Clean':
        if env['Location'] == 'A':
            print("Vacuum cleaner is moving from room A to room B.")
            env['Location'] = 'B'
        else:
            print("Vacuum cleaner is moving from room B to room A.")
            env['Location'] = 'A'
    
    # Recursively call the vacuum cleaner agent
    vacuum_cleaner_agent(env)

# Set the initial location of the vacuum cleaner
environment['Location'] = 'A'

# Run the vacuum cleaner agent
vacuum_cleaner_agent(environment)
