__author__ = 'markusguder'
import numpy as np
personen = np.array([[3.0,5.0],[4.0,1.0],[5.0,1.0]])
print personen[:,0]
median = np.median(personen[:,0])
print median
schlechtorientierten = personen[:,0] < median
print schlechtorientierten
personen[schlechtorientierten,1]