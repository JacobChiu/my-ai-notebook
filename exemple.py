# 計算一個列表所有數字的平均值
def average(nums: list[float]) -> float:
    if not nums:
        return 0.0
    return sum(nums) / len(nums)    
print(f"平均值為: {average([1, 2, 3, 4, 5])}")
print(f"平均值為: {average([10.5, 20.5, 30.5])}")
print(f"平均值為: {average([])}")
print(f"平均值為: {average([100, 200, 300, 400])}")
#建立一個隨機數字列表
import random
random_nums = [random.uniform(1, 100) for _ in range(10)]   
print(f"隨機數字列表: {random_nums}")
print(f"隨機數字的平均值為: {average(random_nums)}")   
