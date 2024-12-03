def find_uniq(arr):
    import statistics
    mode = statistics.mode(arr)
    for num in arr:
        if num != mode:
            return num

# finds the odd number out of an integer array of same numbers