import os

os.makedirs("src", exist_ok=True)

with open("src/example.py", "w+") as f:
    f.write("""print("I am the change 2")\n""")

print("Complete!!")