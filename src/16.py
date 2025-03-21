import os

def main():
    # Example of reading and writing data to a file
    with open("data.txt", "w") as f:
        f.write("This is some text.\n")
    
    # Example of using Python's built-in function for converting hexadecimal to binary
    hex_value = "1A3F"  # Replace this with your desired hexadecimal value
    bin_value = bin(int(hex_value, 16))[2:]  # Convert and format the number as a binary string
    
    print(bin_value)

if __name__ == "__main__":
    main()
