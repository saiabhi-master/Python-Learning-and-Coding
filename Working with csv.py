import csv

#with open("filename.csv", 'r'/'w'/'a') as csv_file:
#to read: csv_reader = csv.reader(csv_file) ( also mention delimiter if exists)

# to loop through line to a print out each row
# for line in csv_reader:
#    print(line) --> each line is a list
# eg output: ['john', 'smith', 'johns@gmail.com']

#to ignore first line which is usually labels:
# next(csv_reader)

#usually commas are used as the "delimiter",
# but sometimes otherthings can also be used like dashes

#to write csv file:
# with open('newfilename.csv', 'w') as new_file:
# csv_writer = csv.writer(new_file, delimiter='-') (if dash is used)
# for line in csv_reader:
#   csv_writer.writerow(line)

#to work with CSV using dictionary reader and writer
# csv_reader = csv.DictReader(csv_file)
# for line in csv_reader:
#   print(line) --> each line will be dictionary with key(name) and value(john) etc..

# to use dictionary writer - we have to provide field names of our file
# fieldnames = ['first_name', 'last_name', 'email']
# csv_writer = csv.DictWriter(new_file, fieldnames=fieldnames)
# csv_writer.writeheader() -- > writes fieldnames as first row
# for line in csv_reader:
#   del line['email']   --> to delete email value for each line
#   csv_writer.writerow(line)





