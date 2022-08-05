# Check file is empty or not

import os
a= os.stat("test.txt").st_size
if a==0:
    print("File is empty")
else:
    print("file is not empty"
          )
