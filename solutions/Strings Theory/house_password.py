#!/home/valentyna-sinichenko/miniconda3/envs/checkio/bin/checkio --domain=py run house-password

# Stephan and Sophia forget about security and use simple passwords for everything.    Help Nikola develop a password security check module. The password will be considered strong enough if its length is greater than or equal to 10 symbols, it has at least one digit, as well as containing one uppercase letter and one lowercase letter in it. The password contains only ASCII latin letters or digits.
# 
# Input:A password as a string(str).
# 
# Output:Is the password safe or not as a logic value(bool).
# 
# 
# Preconditions:re.match("[a-zA-Z0-9]+", password);0 < len(password) ≤ 64.
# 
# 
# END_DESC

def checkio(data: str) -> bool:
    # your code here
    return False


print("Example:")
print(checkio("A1213pokl"))

# These "asserts" are used for self-checking
assert checkio("ULFFunH8ni") == True
assert checkio("aaaaaaaaaaaaaaaaaaaaa") == False
assert checkio("aA1") == False
assert checkio("awzbdzkfz") == False
assert checkio("RCAGOSHTTS") == False
assert checkio("6691219721") == False
assert checkio("PVlppfwrT") == False
assert checkio("45ae5lkgz") == False
assert checkio("1cmuPF1Ycz") == True
assert checkio("Pv4HdnUNb") == False
assert checkio("jRNfXg6CdM15SLChALq") == True
assert checkio("HZeLrcRR3NU5KprAybp") == True
assert checkio("aaaaaaaaaa1A") == True
assert checkio("aaaaaaaaa1Za") == True
assert checkio("aaaaaaaaa9Aa") == True
assert checkio("AAAAAAAAA1zA") == True

print("The mission is done! Click 'Check Solution' to earn rewards!")