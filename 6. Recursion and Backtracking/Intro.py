
# Power Function: Implement a function to calculate x^n. Both x and n can be positive/negative and overflow doesn't happen. Try doing it in O(log(n)) time.


# recursion, divide and conquer

def power_func(base, power):
    if power == 0:
        return 1
    if power == 1:
        return base
    if power == -1:
        return 1/base
    if base == 0 and power <= 0:
        raise Exception('error!')

    remainder = base if power%2==1 else 1
    half = power_func(base, power//2)
    return half * half * remainder



print(power_func(2,2)) #should equal 4
print(power_func(2,-2)) #should equal 0.25 
print(power_func(-2,3)) #should equal -8
print(power_func(-3,2)) #should equal 9
print(power_func(-3,3)) #should equal -27
print(power_func(-1,10)) #should equal 1 
print(power_func(-3,4)) #should equal 81




