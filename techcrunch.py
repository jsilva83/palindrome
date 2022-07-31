# Read a large file.
file_name = "techcrunch.csv"

# Crete a generator that will hold the lines of the file.
lines = (line for line in open(file_name))

# Create a second generator based in the first that splits the lines into a list.
list_line = (s.rstrip().split(",") for s in lines)

# Extract the columns of the file.
cols = next(list_line)

# Now create a dictionary based in the columns and the remaining data of the list_line generator.
company_dicts = (dict(zip(cols, data)) for data in list_line)

# Create a new generator to filter those dictionary elements that match the condition "round" == "a".
funding = (
    int(company_dict["raisedAmt"])
    for company_dict in company_dicts
    if company_dict["round"] == "a"
)

# Until now there was no iteration. Sum takes an iterator/generator as argument.
total_series_a = sum(funding)
print(f"Total series A fundraising: ${total_series_a}")
