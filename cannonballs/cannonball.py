'''
2.3
The year: 1777. The setting: General Washington's camp somewhere in
the colonies. The British have been shelling the Revolutionary forces with
a large cannon within their camp. You have been assigned a dangerous
reconnaissance mission-to infiltrate the enemy camp and determine the
amount of ammunition available for that cannon.
Fortunately for you, the British (being relatively neat and orderly)
have stacked the cannonballs into a single pyramid-shaped stack. At the
top is a single cannonball resting on a square of four cannonballs, which
is itself resting on a square of nine cannonballs, and so forth. Given the
danger in your situation, you only have a chance to count the number of
layers before you escape back to your own encampment.
Using mathematical induction, prove that, if N is the number of layers,
the total number of cannonballs is given by N(N + l)(2N + l)/6


the given formula is not correct. it doesn't apply even for the first test case. if n == 2 => total = 5.
in the test it is said that the row has 4 cannonballs not 5


3.2
Without using the explicit formula. write a recursive function which computes
the answer to the "cannonball" problem from Exercise 2-3.
'''

def func(rowNum):
    if rowNum == 1:
        print("randul", rowNum, "are 1 bila")
        return 1
    else:
        print("randul", rowNum, "nr bile", (rowNum*(2*rowNum))//2)
        return (rowNum*(2*rowNum))//2 + func(rowNum-1)
        
#tried the same problem with memoization
def memo(num, dic):
    if num == 1:
        return dic[num]
    else:
        formula = (num*(2*num))//2
        ans = formula + memo(num-1, dic)
        dic[num] = ans
        return ans

dic = {1:1}
n = 990
memo(n,dic)

print("recursive",func(n))
print("memo with dic", dic[n])