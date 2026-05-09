a = 5.08
b = 5.33
c = 5.55
d = b - a
e = c - b
if d > e:
     print ("The population growth in Scotland is decelerating")
elif d < e:
     print ("The population growth in Scotland is accelerating")   
else:
     print("The population growth in Scotland do not change")
# The results of comparing is d > e, so the population growth of Scotland is decelerating.
X=True
Y=False
W=X or Y
print(W)
# X is True, Y is True, then W is True
# X is True, Y is False, then W is True
# X is False, Y is True, then W is True
# X is False, Y is False, then W is False
