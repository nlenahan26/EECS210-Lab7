# Name: Nathan Lenahan
# KUID: 31789
# LAB Session (Day/Time): Wednesday 11AM
# LAB Assignment: Lab 07
# Description: The program produces the next permutation in lexicographic order,
#              It implements and follows the methodolgy of Algorithm 1 of Section 6.6
# Collaborators/Sources: None

#Function converts a valid user input into a list of ints
#Does not allow the user to input repeated digits or anything that is not a number
def get_input():
    while True:
        num_str = input("Enter a number with no repeated digits: ")

        #Check that all characters are digits
        if not num_str.isdigit():
            print("Input must be a number.")
            continue

        #Check for repeated digits
        if len(set(num_str)) != len(num_str):
            print("Number must not have repeated digits.")
            continue

        #Convert to list of integers
        digits = [int(ch) for ch in num_str]
        '''
        #Check if it's the last permutation
        if all(digits[i] >= digits[i+1] for i in range(len(digits)-1)):
            print("Input is the last permutation, no next permutation exists.")
            continue
        '''
        return digits  # only returns once input is valid

#Next permuatation algorithm of Section 6.6
def next_permutation(num):

    #Sets n equal to the last index and j to the second to last index
    n = len(num) - 1 
    j = n -1 

    #While the digit at index j is greater than the last digit, decrement j
    while num[j] > num[j+1]:
        j = j-1

    #Finds the largest index k where the digit at k is greater than the digit at j
    k = n 
    while num[j] > num[k]:
        k = k-1 

    #Interchange digits at positiions j and k
    num[j], num[k] = num[k], num[j]

    #Sets r and s to the ends of the digits left
    r = n
    s = j+1

    #Reverse digits after position j
    while r > s:
        num[r], num[s] = num[s], num[r]
        r = r-1 
        s = s+1

    #Prints the digits
    for digit in num:
        print(digit, end="")
    print()



def main():
    num_list = get_input()
    next_permutation(num_list)

if __name__ == "__main__":
    main()