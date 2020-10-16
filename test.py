file name: test.py

my_list = [[['apple', 'banana'],['fig','melon']], [['grapes', 'pear'],['cherry','mandarine']]]
for (c, value) in enumerate(my_list):
  for (d, val) in enumerate(value):
    for (m, vall) in enumerate(val):
       print((c, d, m), vall)
