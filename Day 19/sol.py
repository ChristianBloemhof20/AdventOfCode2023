from operator import attrgetter

class Part:
    def __init__(self, x, m, a, s):
        self.x = x
        self.m = m
        self.a = a
        self.s = s

    def __repr__(self) -> str:
        return f"Part(m={self.x},m={self.m},a={self.a},s={self.s})"
    
    def rating(self):
        return self.x + self.m + self.a + self.s

    @classmethod
    def parse(cls, string):
        return cls(*(int(attr.split("=")[1]) for attr in string[1:-1].split(",")))

with open("input.txt") as file:
    workflows, parts = file.read().strip().split("\n\n")
    workflows = {wf[:wf.index("{")]: wf[wf.index("{") + 1:-1].split(",") for wf in workflows.split("\n")}
    parts = [Part.parse(part) for part in parts.split("\n")]

total = 0
for part in parts:
    workflow = "in"
    while True:
        for rule in workflows[workflow]:
            if "<" in rule:
                attr, rest = rule.split("<")
                value, next = rest.split(":")
                if attrgetter(attr)(part) < int(value):
                    workflow = next
                    break
            elif ">" in rule:
                attr, rest = rule.split(">")
                value, next = rest.split(":")
                if attrgetter(attr)(part) > int(value):
                    workflow = next
                    break
            else:
                workflow = rule
                break
        if workflow == "A":
            total += part.rating()
            break
        elif workflow == "R":
            break
print(total)