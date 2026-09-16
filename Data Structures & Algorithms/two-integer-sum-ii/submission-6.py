class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        start = 0
        end = len(numbers) - 1
        #print("initial values:" +str(start)+" "+str(end))
        #i = 0
        while start != end:
            
            summ = numbers[start] + numbers[end]
            #print("summation is "+str(summ)+"target is "+str(target))
            if summ == target:
                #print("numbers returned ", numbers[start], " ", numbers[end])
                return [start+1, end+1]

            if summ < target:
                start +=1
            else:
                end -=1
            #i+=1
            #print("current iteration"+str(i)+": " +str(start)+" "+str(end))
        return [0,0]