#!/home/valentyna-sinichenko/miniconda3/envs/checkio/bin/checkio --domain=py run currency-style

# "Well, it's that time of the month again. Payroll checks for our employees,      which require your signatures. And no forgetting to sign the big ones!"
# -- Trading Places
# 
# Many countries use different conventions for the thousands separator and decimal mark.  For example in the Netherlands    one million one thousand two hundred and eighty one-hundredths is written as 1.001.200,80, but in the US this is written    as 1,001,200.80.  Use your coding skills to convert dollars in the first style (Netherlands, Germany, Turkey,    Brazil, and others) to the second style (US, UK, Canada, China, Japan, Mexico, and others).
# 
# Only currency amounts in dollars should be converted: $1.234,50 to $1,234.50, $1.000 to $1,000, and $4,57 to $4.57.    Don't accidentally convert your router's IP address 192.168.1.1.  You should leave currency noted in the US style unchanged.
# 
# Input:A string(str).
# 
# Output:A string(str).
# 
# Preconditions:0 < len(text) ≤ 1000;len(fractional_part_of_currency) in {0,2};all(s[-1].isdigit() for s in currency_substrings);all(s[0] == '$' for s in currency_substrings)
# 
# 
# END_DESC

def checkio(line: str) -> str:
    # your code here
    return ""


print("Example:")
print(checkio("$5.34"))

assert checkio("$5.34") == "$5.34"
assert checkio("$5,34") == "$5.34"
assert checkio("$222,100,455.34") == "$222,100,455.34"
assert checkio("Is $1.050,25 bigger than $1,050?") == "Is $1,050.25 bigger than $1,050?"
assert checkio("$222.100.455,34") == "$222,100,455.34"
assert checkio("$222,100,455") == "$222,100,455"
assert checkio("222.100.455") == "222.100.455"
assert (
    checkio("This is an IP address 192.168.1.1") == "This is an IP address 192.168.1.1"
)
assert checkio("The price of bread is $1,50") == "The price of bread is $1.50"
assert (
    checkio("The price of bread is 1,50 in some currency.")
    == "The price of bread is 1,50 in some currency."
)

print("The mission is done! Click 'Check Solution' to earn rewards!")