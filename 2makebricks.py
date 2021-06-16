# =============================================================================
# We want to make a row of bricks that is goal inches long. We have a number of
# small bricks (1 inch each) and big bricks (5 inches each). Return true if it
# is possible to make the goal by choosing from the given bricks. This is a
# little harder than it looks and can be done without any loops in a single line!
# 
# makeBricks(3, 1, 8) → true
# makeBricks(3, 1, 9) → false
# makeBricks(3, 2, 10) → true
# makeBricks(6, 0, 11) → false
# makeBricks(1, 4, 12) → false
# =============================================================================
def makeBricks(small, big, goal):
    return (goal%5 - small <= 0) and (small + 5*big >= goal)

print(makeBricks(3,1,8))


