report = {'Komal':99, 'Priyanka':76, 'Antara':95, 'Renuka':70}
name = input("Enter Student Name: ")

if name in report:
    print(report[name])
else:
    print("Student Not Found")