#file name: Explanation of why it does not make sense to convert every list to set for every membership query.py
l = [5,2,6,1,8,2,4,6]

2 in l # cost: 2
4 in l # cost: 7

# average cost: len(l)/2 -> O(n)
ls = [1,2,2,4,5,6,6,8] # sorted.
#searching in a sorted collection has an average cost of log2(len(ls)). -> O(log(n))

#Let's say we want to convert l into ls.
#Insertion Sort: Worst Case: O(n^2)
#Merge Sort: Worst Case: O(n*log(n))

[5],[2],[6],[1],[8],[2],[4],[6]
[2,5],[1,6],[2,8],[4,6]
[1,2,5,6],[2,4,6,8]
[1,2,2,4,5,6,6,8]
#Total: O(n*log(n))