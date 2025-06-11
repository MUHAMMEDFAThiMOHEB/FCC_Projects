def arithmetic_arranger(problems, show_answers=False):
    
    fn_list = []
    sn_list = []
    op_list = []
    noop = 0
    bspace = "    "
    n_dashs = 0
    space = " "
    separator = "-"

    top_line = []
    bottom_line = []
    dash_line = []
    result_line = []

    for item in problems:
        noop += 1
        item = item.strip().split(" ")
        fn_list.append(item[0])
        sn_list.append(item[2])
        op_list.append(item[1])
    
    for x in range(noop):
        first = fn_list[x]
        second = sn_list[x]
        op = op_list[x]

        # Determine the width for formatting
        width = max(len(first), len(second)) + 2
        align_top = first.rjust(width)
        align_bot = op + second.rjust(width - 1)
        dashes = separator * width

        top_line.append(align_top)
        bottom_line.append(align_bot)
        dash_line.append(dashes)

        if show_answers:
            result = str(eval(first + op + second)).rjust(width)
            result_line.append(result)

    # Print each line side by side
    arranged = (
        bspace.join(top_line) + "\n" +
        bspace.join(bottom_line) + "\n" +
        bspace.join(dash_line)
    )

    if show_answers:
        arranged += "\n" + bspace.join(result_line)

    print(arranged)
    return ""

    return ""

print(arithmetic_arranger(["3 + 855", "3801 - 2", "45 + 43", "123 + 49"]))