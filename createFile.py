import os
import time

startTime = time.time()

for i in range(1000):
  f = open("createFile.txt", "w")
  f.close()

  os.remove("createFile.txt")

print("----%s seconds ---" % (time.time() - startTime))