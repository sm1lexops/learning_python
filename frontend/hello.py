import sys

print("First create file `hello.py`")

print(f"First we need install python {sys.version}.{sys.version_info}")
print("What is your name dude?")
name = input().strip().upper()
first_name, last_name = name.split()

print(f"Hello, {first_name} {last_name}")

