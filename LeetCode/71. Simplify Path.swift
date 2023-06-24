class Solution {
    func simplifyPath(_ path: String) -> String {
        let pathComponents = path.split(separator: "/")
        var stack = Array<String>()
        for component in pathComponents {
            if component == ".." {
                let _ = stack.popLast()
            } else if component != "." {
                stack.append(String(component))
            }
        }
        return "/" + stack.joined(separator: "/")
    }
}
