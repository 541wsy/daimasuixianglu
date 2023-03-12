class Solution(object):
    def evalRPN(self, tokens):
        """
        :type tokens: List[str]
        :rtype: int
        """
        stack = []
        signs = ['+', '-', '*', '/']
        for ch in tokens:
            if ch not in signs:
                stack.append(ch)
            else:
                num1 = stack.pop()
                num2 = stack.pop()
                result = eval(''.join([num2, ch, num1]))  # 计算结果
                stack.append(str(int(result)))  # 将计算结果放入栈内
        return int(stack[0])

tokens = ["10","6","9","3","+","-11","*","/","*","17","+","5","+"]
solution = Solution()
solution.evalRPN(tokens)
