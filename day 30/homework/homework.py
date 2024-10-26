names = ["გიორგი", "gfsdlkfg;sudnf;ol", "ეკატერინე", "fbslkjhfl;wehglf", "გაბრიელა", "ანასტასია", "ივანიშვილი", "კონსტანტინე", "თეოდორა", "დემეტრე"]

filtered_names = []

for name in names:
    if len(name) <= 10:
        filtered_names.append(name)

print(filtered_names)