def most_frequent(string):
    # Create an empty dictionary to store the frequency of each character
    frequency = {}
    
    # Iterate over each character in the string
    for char in string:
        if char in frequency:
            frequency[char] += 1
        else:
            frequency[char] = 1
    
    # Sort the dictionary by value in descending order
    sorted_frequency = sorted(frequency.items(), key=lambda x: x[1], reverse=True)
    
    # Print the characters in decreasing order of frequency
    for char, count in sorted_frequency:
        print(char, count)
    
most_frequent(input("Enter the string:- "))
