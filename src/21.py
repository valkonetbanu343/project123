import os
import subprocess
import sys

def main():
    # Add your main function logic here
    print("Hello, World!")

if __name__ == "__main__":
    try:
        # Call the main function if it's called as a script (not imported)
        main()
    except Exception as e:
        # Print any exceptions that occur
        print(f"An error occurred: {e}")

# Uncomment to run as a separate script
if __name__ == "__main__":
    try:
        subprocess.run(["python", "project123.py"])
    except Exception as e:
        print(f"An error occurred: {e}")
