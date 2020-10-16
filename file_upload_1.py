#file name: file_upload_1.py
from google.colab import files
uploaded = files.upload()
#You will see a "Browse"-button to select the file that you want to upload.
import pandas as pd
import io
df = pd.read_csv(io.StringIO(uploaded['Tunnel_1_4Linear8Sensors9ClassesCappedRange8Fast_10.txt'].decode('utf-8')), sep='\t')
#You need to specify which file you want to read in your code.
df
#You see the content of the file as a table.
"""
Distance_to_wall-180 	Distance_to_copter-180 	Distance_to_wall-135 	Distance_to_copter-135 	Distance_to_wall-90 	Distance_to_copter-90 	Distance_to_wall-45 	Distance_to_copter-45 	Distance_to_wall0 	Distance_to_copter0 	Distance_to_wall45 	Distance_to_copter45 	Distance_to_wall90 	Distance_to_copter90 	Distance_to_wall135 	Distance_to_copter135 	Class
0 	6.249167 	1.270782 	8.00000 	5.068242 	5.457317 	3.014043 	8.000000 	8.000000 	1.350833 	8.000000 	8.000000 	8.000000 	4.142683 	1.775731 	6.017233 	3.629062 	4
1 	0.162360 	8.000000 	8.00000 	8.000000 	6.079319 	3.376747 	8.000000 	3.991678 	7.437640 	0.177941 	6.554736 	3.738134 	3.520681 	8.000000 	8.000000 	8.000000 	4
"""