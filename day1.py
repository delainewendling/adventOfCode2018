# Given a frequency input that operates as such:

# +1, +1, +1 results in  3
# +1, +1, -2 results in  0
# -1, -2, -3 results in -6
# Starting with a frequency of zero, what is the resulting frequency after all of the changes in frequency have been applied?

frequency_input = open('day1.txt')
ADD = '+'
SUBTRACT = '-'
frequency = 0

with frequency_input as f:
    for line in f:
        operation = line[0]
        value = int(line[1:])
        if operation == ADD:
            frequency += value
        else:
            frequency -= value

print(frequency)