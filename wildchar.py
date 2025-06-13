#Write code to check if two strings match where one string contains wildcard characters
import fnmatch

def is_match(string, pattern):
    return fnmatch.fnmatch(string, pattern)

# Example usage
string = input("Enter the string: ")
pattern = input("Enter the pattern (use * and ? as wildcards): ")

if is_match(string, pattern):
    print("The string matches the pattern.")
else:
    print("The string does not match the pattern.")
