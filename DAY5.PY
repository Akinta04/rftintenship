data=[]
# open csv file
with open ("RECORD.csv","r") as file:
    #Read all lines
    lines = file.readlines()
    # FIRST LINE = HEADERS
    headers = lines[0].strip().split(",")
    # Read remaining lines
    for line in lines[1:]:
        # Remove extra spaces/newline and split data
        values =line.strip().split(",")
        # Handle missing values
        if len(values)!=len(headers):
            continue
        #  create dictionary
        student = {headers[0]:values[0],headers[1]:int(values[1]),headers[2]:int(values[2])}
        # add dictionary to list
        data.append(student)
print(data)

# Calculate Average marks
total = 0
for item in data:
    total += item["MARKS"]
    average = total/len(data)
print("AVERAGE MARKS =",average)

