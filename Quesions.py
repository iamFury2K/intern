# The below  Questions have been attempted in code-chef on Monday 04 july 2022
# Question code: ENSPACE
# Link: https://www.codechef.com/submit/ENSPACE
# Code:
t = int(input())
for salu in range(0,t,1):
        n,x,y = map(int, input().split(" "))
            y *= 2
                if n >= (x + y):
                            print("YES")
                                else:
                                            print("NO")

# Question code: ACCURACY
# Link: https://www.codechef.com/submit/ACCURACY
# Code:
import math as m
t = int(input())
for salu in range(0, t):
        x = int(input())
            marks = m.ceil(x/3) * 3
                print(marks - x)
# Quesiom code: CHANGEPOS
# Link: https://www.codechef.com/submit/CHANGEPOS
# Code:
t = int(input())
for i in range(0, t):
        sx, sy, ex, ey = map(int, input().split(' '))
            if (sx != ex) and (sy != ey):
                        print(1)
                            elif(sx == ey and sy == ex):
                                        print(1)
                                            elif sx == ex and sy != ey:
                                                        print(2)
                                                            elif sx != ex and sy == ey:
                                                                        print(2)
                                                                            else:
                                                                                        print(abs(ex - ey))
# Question code: CHEFAPPS
# Link: https://www.codechef.com/submit/CHEFAPPS
# Code:
t = int(input())
for ii in range(0, t):
        s,x,y,z = map(int, input().split(' '))
            free_space = s - (x+y)
                if free_space >= z:
                            print(0)
                                elif free_space + x >= z or free_space + y >= z:
                                            print(1)
                                               else:
                                                            print(2)


