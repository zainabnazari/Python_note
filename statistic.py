#file name: statistic.py
# here is a list of 15 student's height in cm which includes mistakenly some wrong values, let's see how we can deal with that.
student_h=[1.40, 1.42,1.50, 1.67, 1.44, 16.5, 1.38,1.77, 1.44,166, 1.54, 1.30, 1.83, 1.47, 1.44]
# let's see the mean of their hights:
import numpy as np
np_student_h=np.array(student_h)
print("mean: ", np.mean(np_student_h))
# the output is: 13.473333333333334, it seems something went wrong! but not with the mean, maybe a value inserted wrongly.
# let's see the median
print("median: ", np.median(np_student_h))
# output is:  1.47  which makes sense

# let's see the maximum, and minimum height of this list:

print("maximum: ", np.max(np_student_h)) # output: maximum:  166.0
print("minimum: ", np.min(np_student_h)) # output: minimum:  1.3

# As you see it seems that the maximum height of the students has been inserted wrongly in cm instead of meter, which affected the mean but not the median.
