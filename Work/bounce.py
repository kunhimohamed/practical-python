# bounce.py
#
# Exercise 1.5

height_of_ball_drop = int(input())

for index, value in enumerate(range(10)):
    the_required_result = height_of_ball_drop*(3/5)
    print(index+1, round(the_required_result, 4))
    height_of_ball_drop = the_required_result