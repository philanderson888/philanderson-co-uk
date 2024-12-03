'''
You are given a dictionary/hash/object containing some languages and your test results in the given languages. Return the list of languages where your test score is at least 60, in descending order of the scores.

Note: the scores will always be unique (so no duplicate values)

Examples
{"Java": 10, "Ruby": 80, "Python": 65}    -->  ["Ruby", "Python"]
{"Hindi": 60, "Dutch" : 93, "Greek": 71}  -->  ["Dutch", "Greek", "Hindi"]
{"C++": 50, "ASM": 10, "Haskell": 20}     -->  []
'''
results = {"Java": 10, "Ruby": 80, "Python": 65}
def my_languages(results):
    
    keysResults = results.keys()
    valuesResults = results.values()
    
    filtered_results = []
    
    for each_key in valuesResults: 
        if each_key >= 60:
            filtered_results.append(each_key)
            filtered_results.sort()
            # Turn values to keys
    print(results[10])
    print(filtered_results)
    return filtered_results




# Make two separate dictionaries - one with just the keys and one with just values
# Append to filtered_results all keys that are 60 or above.
# Sort the dictionary
# Turn the values in the dictionary to their assigned keys.




    filtered_results = []
    for each_value in results:
       if results[each_value] >= 60:
           filtered_results.append(results.keys())   
       return filtered_results.sort()

print(my_languages(results))