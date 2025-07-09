#!/home/valentyna-sinichenko/miniconda3/envs/checkio/bin/checkio --domain=py run autopilot

# A large electric car factory is making improvements to its autopilot system and needs your help to implement a program that decides whether car B, which is driving in the middle of two cars A and C, needs to accelerate, decelerate or maintain its current speed. The cars are the same and the autopilot sensors will provide the current position of the rear of the three cars on an imaginable axis. See an example in the figure.
# 
# 
# 
# Car B needs to be accelerated if the distance from its rear to the rear of car A is less than the distance from its rear to the rear of car C. If it is greater, it needs to be decelerated. If it's the same, it needs to maintain its current speed.
# 
# Input:Three integers(int), which represent the current positions of the backs of cars A, B and C, respectively.
# 
# Output:An integer 1 if car B needs to accelerate; -1 if it needs to decelerate; or 0 if it needs to maintain its current speed.
# 
# Preconditions:A < B < C
# 
# 
# END_DESC

def speed_adjust(A: int, B: int, C: int) -> int:
    # your code here
    return 0


print("Example:")
print(speed_adjust(2, 4, 6))

# These "asserts" are used for self-checking
assert speed_adjust(0, 2, 6) == 1
assert speed_adjust(0, 4, 6) == -1
assert speed_adjust(0, 3, 6) == 0

print("The mission is done! Click 'Check Solution' to earn rewards!")