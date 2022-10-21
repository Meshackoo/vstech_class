from sqlite3 import Time


fee=100,000
name="Jett"
fee_paid=170,000
attended_classes=False
if fee_paid>=fee and attended_classes:
    print(f"{name},you can sit for exam")
else:
    print("you can not sit for exams")
