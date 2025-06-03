def arithmetic_arranger(problems, show_answers=False):

    fn_list = []
    sn_list = []
    op_list = []

    for item in problems:
        item = item.strip().split(" ")
        fn_list.append(int(item[0]))
        sn_list.append(int(item[2]))
        op_list.append(item[1])
    
    return None

arithmetic_arranger(["3 + 855", "3801 - 2", "45 + 43", "123 + 49"])