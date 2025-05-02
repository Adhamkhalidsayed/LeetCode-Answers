class Solution:
    def pushDominoes(self, dominoes: str) -> str:
        dom = list(dominoes)
        dq = deque()

        for i, d in enumerate(dom):
            if d != ".": dq.append((i,d))


        while dq:
            i, d = dq.popleft()
            if d == "L":
                if i > 0 and dom[i-1] == ".":
                    dq.append((i-1, "L"))
                    dom[i-1] = "L"

            if d == "R":
                if i < len(dom) - 1 and dom[i+1] == ".":
                    if i < len(dom) - 2 and dom[i+2] == "L":
                        dq.popleft()
                    else:
                        dq.append((i+1,"R"))
                        dom[i+1] = "R"

        string = "".join(dom)
        return string