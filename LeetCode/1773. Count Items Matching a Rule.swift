class Solution {
func countMatches(_ items: [[String]], _ ruleKey: String, _ ruleValue: String) -> Int {
    var keyIndex = 0
    if ruleKey == "color" {
        keyIndex = 1
    }
    else if ruleKey == "name" {
        keyIndex = 2
    }
    var result = 0
    for i in 0...items.count-1 {
        if items[i][keyIndex] == ruleValue {
            result += 1
        }
    }
    return result
}
}
