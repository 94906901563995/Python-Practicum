children = int(input())
candies = int(input())
print(candies // children)
remainder = candies - (candies // children) * children
print(remainder)