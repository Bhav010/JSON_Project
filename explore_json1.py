import json

infile = open('eq_data_1_day_m1.json','r')      #reading from file
outfile = open('readable_eq_data.json','w')     #creating new output file

eq_data = json.load(infile)                 #formats the object 'eq_data' as the type of 'infile' contents, dictionary here 

json.dump(eq_data, outfile, indent=5)