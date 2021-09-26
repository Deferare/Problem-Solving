class Solution {
    func subtractProductAndSum(_ n: Int) -> Int {
        var digitList = [Int]()
        let n = String(n)
        for crnt in n{
            digitList.append(Int(String(crnt))!)
        }
        var multN = digitList[0]; var sumN = digitList[0];
        for i in 1..<digitList.count{
            multN *= digitList[i]
            sumN += digitList[i]
        }
        return multN-sumN
    }
}
