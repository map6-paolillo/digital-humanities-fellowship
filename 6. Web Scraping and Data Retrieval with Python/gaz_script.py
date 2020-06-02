import csv

# in Python, we sometimes need to import additional functionality from a "library"
# Libraries are either already bundled with Python, but not included in the basic
# Python functions (like csv) or need to be downloaded before being imported
# in this case, we can add csv functionality with the above line

counties = []

# we've assigned the counties variable an empty list, indicated by []
# this list will eventaully fill up with county names, each represented as a string
# the end result will look like ["countyA", "countyB", "countyC"...]

with open("gazetteer.txt", 'r') as gaz:

# here, we open up the gazetteer file and assign it a "handle" variable called gaz
# note that in Python, we still need to go through another step to extract the data
# but now we can do so by referencing the handle

    for line in gaz:

# this is an iterator pattern. we are going to loop through every line in gaz
# and do something with that data. for every iteration or "cycle," the variable line
# contains just our current line as a string. think of this as "working memory"

        county = line.rstrip()

        # .rstrip() is a method we can call on a string variable. in this case
        # it will remove trailing whitespace and newline characters that are hard to see
        # but will affect our program if we don't handle them here!

        counties.append(county)

        # the .append() method adds whatever parameter we put into the parentheses
        # (in this case, the current name of county) to our big list of counties

print(counties)

# instead of printing as we go, we can print at the end to make sure our list looks OK

students = []

# similarly, we will assign an empty list to students that will fill up with information
# about students. however! this will be a little more complicated than a list of strings.
# in this case, we'll actually make a list of *dictionaries*. 
# 
# A dictionary is a collection
# like a list, but instead of it being an ordered collection, it is a grab-bag of pairings
# between "keys" (or labels) and "values" (or whatever data we want to associate with it)
#
# The benefit of using a dictionary is that later on, we can say "hey, give me the value
# associated with the 'Name' key" and our dictionary will return that value, without knowing
# anything about order.
#
# Our list will look something lke this in the end:
# [{Student A Dictionary}, {Student B Dictionary}, {Student C Dictionary}]
# (We'll go into more detail about dictionaries later on)

with open('students.csv', 'r') as student_file:

    # again, we are creating a file handle for our file data

    student_data = csv.DictReader(student_file)
    # working with a CSV requires this additional step. the csv library helps
    # Python understand how to work with csv's. in particular, it instructs Python
    # that headers for a column are an appropriate label (or "key") for the data
    # in that column, which is useful for us later

    for student in student_data:

        # like before, we iterate over each row in our data (although this time it's a table)

        students.append(student)

        # we append the entire row (each row is a student's data) to our students variable

    
print(students[0])

# printing all 6.5K students is burdensome here. instead, we can pluck just one specific
# item from our list using a *list index* with a bracket and a number after the list variable name
# students[0] returns the 0th element of our students list -- remember Python begins
# counting at zero, so this is the first item!


## NEXT STEPS



# Step 0: Create a new list variable, called students_cleaned, and assign it an empty list
## Your code here


# Step 1: Again, use the iterator pattern. This time, iterate over each our the students, and isolate just the words in the Details column.
## Here's some code to start:

for student in students:
    name = student['Name']
    year = student['Matriculation Year']
    details = student['Details']

    ## Your code here: split up student details into separate words
    ## You'll need to use a few methods:
    ## .replace() can switch out a punctuation with something else, including nothing ("")
    #  .replace("," , "") for instance, replaces commas with nothing (or deletes them) 
    ## .split() separates out words based on a delimiter (by default, a blank space)
    
    ## d_words = YOUR CODE


    # Step 2: Create a new variable, called county_name. By default, assign it to a blank string.
    ## Your code here

    # Step 3: Iterate over each word in d_words. Are any of these words contained in our gazetteer list?
    # If so, overwrite "county_name" with that word.

    # Step 4: Add this newly-expanded student data to the running students_cleaned list you created earlier.
    # Hint: Start by making a new dictionary with key-value pairs for 'Name', 'Matriculation Year', 'Details', and 'County'
    ## Your code here


# print(students_cleaned[0])
# When you've added your code above, this should print the relevant data for the first student in the students list.
# Uncomment the line to test it out.



# Step 5: Export our list of dictionaries as a .csv file. This step is like the inverse of our earlier file read steps
# (Python even uses the same open() function, but with the 'wb' parameter instead)

keys = ['Name', 'Matriculation Year', 'Details', 'County']

## Write code here.