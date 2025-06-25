# 計算一個列表所有數字的平均值
def average(nums: list[float]) -> float:
    if not nums:
        return 0.0
    return sum(nums) / len(nums)