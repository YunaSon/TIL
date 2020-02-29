from math import sqrt

def getnumbers():
    nums = []
    xStr = input("Enter a number (<Enter> to quit) >>")
    while xStr != "":
        x = float(xStr)
        nums.append(x)
        xStr = input("Enter a number (<Enter> to quit) >>")
    return nums


def mean(nums):
    total = 0.0
    for num in nums:
        total = total + num
    return total / len(nums)


def stdDev(nums, xbar):
    sumdevSq = 0.0
    for num in nums:
        dev = xbar - num
        sumdevSq = sumdevSq + (dev*dev)
    return sqrt(sumdevSq/len(nums)-1)


def median(nums):
    nums.sort()
    if len(nums) % 2 != 0:
        idx = float(len(nums)/2)
        idx = int(round(idx, 0))-1
        median = nums[idx]
    else:
        idxl = int(len(nums)/2 -1)
        idxr = int(len(nums)/2)
        median = (nums[idxl] + nums[idxr]) / 2
    return median

def main():
    data = getnumbers()
    xbar = mean(data)
    std = stdDev(data, xbar)
    med = median(data)
    print("numbers= {}, average= {}, standard deviation= {}, median= {}".format(data,xbar,std,med))

if __name__ == '__main__':
    main()