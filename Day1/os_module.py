import os

print(os.getcwd())  # Get the current working directory
print(os.listdir())  # List all files and directories in the current working directory
os.mkdir("sample")  # Create a new directory named "sample"
os.chdir("sample")  # Change the current working directory to "sample"
os.chdir("..")  # Change the current working directory back to the parent directory
os.rmdir("sample")  # Remove the directory named "sample"

print(os.cpu_count())  # Get the number of CPUs in the system