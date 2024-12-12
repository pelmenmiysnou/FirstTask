#1
def read_last(lines, file = open('c:/py/prticle.txt')):    
  file = file.readlines()
    for i in range(lines, 0, -1):        
      print(file[-(i)])
lines = int(input())
read_last(lines) 

#4 
filename = input("name")

if not filename.endswith(".txt"):
    filename = filename + ".txt"

with open(filename, "w") as f:

    while True:
      for i in range(999):
        line = input(f"line {i}:")

        if line == "":
            print("saved")
            break

        f.write(line + "\n")
