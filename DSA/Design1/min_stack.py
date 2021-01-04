# Time Complexity is O(1) for push, pop, top, getMin
# Space Complexity is O(1) - self.min stores the minimum value


class MinStack:
    def __init__(self):
        """
        Initializing a list as a stack
        and initializing min to infinity
        """

        self.stack = []
        self.min = inf

    def push(self, x: int) -> None:
        """
        Append the value at the top of the stack
        and check the appended value with min,
        if its less than the min update the min

        """
        self.stack.append(x)
        if x < self.min:
            self.min = x

    def pop(self) -> None:
        """
        Pop the value at the top of the stack,
        if the popped value is equal to min, get a
        new min value.
        """
        popped = self.stack.pop()
        if popped == self.min:
            # if the stack is not empty
            if len(self.stack) > 0:
                self.min = min(self.min)
            else:
                # assign min to inf
                self.min = inf

    def top(self) -> int:
        # return the top of the stack
        return self.stack[-1]

    def getMin(self) -> int:
        # return the min value
        return self.min


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(x)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()