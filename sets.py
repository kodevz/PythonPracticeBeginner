
heights = "161 182 161 154 176 170 167 171 170 174"
heights =  set(input().split(" "))
print(sum([int(h) for h in heights]) / len(heights))