class Solution:
    def maximumUnits(self, boxTypes: List[List[int]], truckSize: int) -> int:
        boxTypes.sort(key=lambda x:x[1], reverse=True)
        truck_puted = 0
        result = 0
        index = 0
        while index < len(boxTypes):
            if boxTypes[index][0] <= truckSize-truck_puted:
                result += boxTypes[index][0] * boxTypes[index][1]
                truck_puted += boxTypes[index][0]
            else:
                put_ex = (truckSize-truck_puted)
                result += boxTypes[index][1] * put_ex
                truck_puted += put_ex
            if truck_puted == truckSize:
                break
            index += 1
        return result
