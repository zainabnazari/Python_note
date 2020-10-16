#file name: file_upload_2.py
from google.colab import drive
drive.mount("/gdrive")
#You will see a link that will guide you through the authorization of file access on Google Drive. It will end up showing you a code that you have to copy and paste into a text box that opens when you run this line of code.
import pandas as pd

df = pd.read_csv('../gdrive/My Drive/Tunnel_1_4Linear8Sensors9ClassesCappedRange8Fast_10.txt', sep='\t')
#You need to specify which file you want to read in your code.
df
#You see the content of the file as a table, the same as in file_upload_1.py.