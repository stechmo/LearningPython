# List
# find max and min of a list
# remove duplicates

def minmax(inputlist):
    return min(inputlist),max(inputlist)

def removeduplicates(inputlist):
    return list(dict.fromkeys(inputlist))