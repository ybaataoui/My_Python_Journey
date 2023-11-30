import sys

sys.path.insert(1, r'C:\Users\ybaataoui\Desktop\Python\workplace') #You need to include the path of the module to import.

import trial # import a not built in module.

print(trial.names)

# best practices is to import only functions we need inside a project.
from math import sqrt

root = sqrt(9)
print(root)

#Use aliases in import
import math as m

cosine = m.cos(0)
print(cosine)