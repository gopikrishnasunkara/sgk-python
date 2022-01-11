import csv
# with open(r"C:\Users\nemma\Desktop\studetails.csv", "r", newline="") as fobj:
#     r = csv.reader(fobj)
#     print(dir(r))
#     for line in r:
#         print(line)


data = [['roll_no', 'stu_name', 'course', 'fee'], [1, 'syam','python', 3000], [2, 'RAMA','Maths', 35000], [3, 'Hari','Arthematics', 55000], [4, 'siva','java', 15000]
, [5, 'anj','bigdata', 14500], [6, 'geetha','python', 3000], [7, 'surya','hadoop', 45000]]


with open(r"C:\Users\nemma\Desktop\studetails.csv", "a", newline="") as fobj:
    w = csv.writer(fobj)
    w.writerows(data)