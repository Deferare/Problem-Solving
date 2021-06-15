class Solution {
func merge(_ nums1: inout [Int], _ m: Int, _ nums2: [Int], _ n: Int) {
    var pbotFirst = m-1
    var pbotScond = nums2.count-1
    var inputDex = nums1.count-1
    if pbotFirst < 0 {
        pbotFirst = 0
        nums1[pbotFirst] = -1000000000
    }
    while pbotScond >= 0 {

        if nums1[pbotFirst] > nums2[pbotScond] {
            nums1[inputDex] = nums1[pbotFirst]
            nums1[pbotFirst] = -1000000000
            if pbotFirst > 0 {
                pbotFirst -= 1
            }
        }
        else if nums1[pbotFirst] <= nums2[pbotScond] {
            nums1[inputDex] = nums2[pbotScond]
            if pbotScond >= 0 {
                pbotScond -= 1
            }
        }
        inputDex -= 1
    }
}
}
