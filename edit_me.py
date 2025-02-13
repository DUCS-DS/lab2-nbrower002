
def monotonic(first):
    """Return True if lst is monotonic; return False, otherwise."""
    if not first: 
        return True
    
    increasing = decreasing = True

    for i in range(1, len(first)):
        if first[i] > first[i -1]:
            decreasing = False
        if first[i] < first[i - 1]:
            increasing = False

    return increasing or decreasing

print(monotonic([1,2,3,4]))
# 
#
