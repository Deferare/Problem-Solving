class Solution:
    def defangIPaddr(self, address: str) -> str:
        result_str = ""
        for crnt in address:
            if crnt != ".":
                result_str += crnt
            else:
                result_str += "["
                result_str += crnt
                result_str += "]"
        return result_str
