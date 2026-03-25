student = int(input("How many students on the course?"))
group = int(input("Desired group size?"))
form = student // group
if student % group !=0:
    form += 1
print(f"Number of groups formed: {form}")
