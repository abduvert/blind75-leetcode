# initial solution
def maxProfit(prices):
    profit=0
    mini = float('inf')


    for i in prices:
        if(mini > i):
            mini = i
        if(profit < i - mini):
            profit = i - mini
            
        
    return profit




profit = maxProfit([7,6,4,3,1])
print(profit)
        



    
