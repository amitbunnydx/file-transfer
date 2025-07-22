import os

# Accessing all environment variables
env_vars = os.environ

# Printing environment variables
for key, value in env_vars.items():
    print("-------------------")
    print(f"{key}: {value}")