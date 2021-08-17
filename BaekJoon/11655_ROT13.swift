let strs = readLine()
var result = ""
for crnt in strs! {
    let crnt_asci = crnt.asciiValue!
    if ((crnt_asci >= 65) && (crnt_asci <= 122)){
        if crnt_asci >= 65 && crnt_asci < 78 || crnt_asci >= 97 && crnt_asci < 110{
            result = result + String(UnicodeScalar(crnt_asci+13))
        }
        else {
            result = result + String(UnicodeScalar(crnt_asci-13))
        }
    }
    else if crnt_asci >= 48 && crnt_asci <= 57{
        result += String(crnt)
    }
    else{
        result += " "
    }
}
print(result)
