for i in range(101):

    sum_res = i + i
    print(f"{i} + {i} = {sum_res}")

    sub_res = i - i
    print(f"{i} - {i} = {sub_res}")
    
    mul_res = i * i
    print(f"{i} * {i} = {mul_res}")
    
    if i != 0:
        div_res = i / i
        print(f"{i} / {i} = {div_res}")
    else:
        print(f"{i} / {i} = დაუშვებელია (0-ზე გაყოფა)")
