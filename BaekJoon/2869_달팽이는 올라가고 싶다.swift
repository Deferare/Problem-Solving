var put = readLine()!.split(separator: Character(" "))
var a = Int(put[0])!; var b = Int(put[1])!; var c = Int(put[2])!
var cb = c-b
var ab = a-b
if (cb%ab == 0) {
    print(cb/ab)
}
else {
    print((cb/ab)+1)
}
