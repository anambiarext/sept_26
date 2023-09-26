with open("1.txt","r") as f1:
  content = f1.readlines()

with open("2.txt","w") as f2:
  for line in content:
    f2.write(line)
