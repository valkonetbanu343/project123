import os

for filename in os.listdir("."):
    if filename.endswith(".py"):
        print(f"Processing {filename}")
        # Add your code here
