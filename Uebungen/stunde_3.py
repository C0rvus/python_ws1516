roboDatei = open("demoData.csv")
roboDaten = roboDatei.readlines()
print roboDaten
for line in roboDaten[1:]:
    line = [float(i) for i in line.split(",")]
print line