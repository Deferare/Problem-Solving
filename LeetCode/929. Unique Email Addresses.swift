extension String {
    func get(_ n:Int) -> Character{
        return self[self.index(self.startIndex, offsetBy: n)]
    }
}
class Solution {
    func numUniqueEmails(_ emails: [String]) -> Int {
        var uniqEmail:Set<String> = Set()
        for email in emails {
            var turn = 0
            var nextEmail = ""
            var i = 0
            while i < email.count{
                if turn == 0{
                    if email.get(i) == "+"{
                        var j = i+1
                        while true{
                            if email.get(j) == "@"{
                                i = j-1
                                turn = 1
                                break
                            }
                            j += 1
                        }
                    }
                    else if email.get(i) != "."{
                        nextEmail += String(email.get(i))
                        if email.get(i) == "@"{
                            turn = 1
                        }
                    }
                }
                else{
                    nextEmail += String(email.get(i))
                }
                i += 1
            }
            uniqEmail.insert(nextEmail)
        }
        return uniqEmail.count
    }
}
