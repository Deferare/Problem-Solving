func Solution() {
    while let word = readLine(){
        var lowwer = 0; var upper = 0; var number = 0; var blank = 0
        for crnt in word{
            let crnt_asci = crnt.asciiValue!
            if crnt_asci >= 65 && crnt_asci <= 90{
                upper += 1
            }
            else if crnt_asci >= 97 && crnt_asci <= 122{
                lowwer += 1
            }
            else if crnt_asci >= 48 && crnt_asci <= 57{
                number += 1
            }
            else {
                blank += 1
            }
        }
        print("\(lowwer) \(upper) \(number) \(blank)")
    }
}

Solution()
