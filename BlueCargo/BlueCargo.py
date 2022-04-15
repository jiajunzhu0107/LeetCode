#Questions:
# Balanced paranthesis
# "{}" -> Balanced
# "}{" -> not balanced
# input a single string

# "asd{fds}sfsd#$" -> Balanced


# "{{[[()]]}}" -> Balanced
# ”{[}]” -> Not Balanced


def is_balanced_paranthesis(input_str):
    stack = []
    paranthesis_left = {
        "{": "}",
        "[": "]",
        "(": ")"
    }
    paranthesis_right = {"}", "]", ")"}
    for c in input_str:
        if c in paranthesis_left:
            stack.append(paranthesis_left[c])
        elif c in paranthesis_right:
            if len(stack) < 1:
                return False
            val = stack.pop()
            if val != c:
                return False
            else:
                continue
        else:
            continue
    if len(stack) == 0:
        return True
    else:
        return False



# input_str = "asd{fds}sfsd#$"
# input_str = "{{[[()]]}}"
# input_str = "{[}]"
# input_str = "{((12)[ab])}"
input_str = "{((12)[ab]}"
print(is_balanced_paranthesis(input_str))

