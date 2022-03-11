
from tkinter import *
from functools import partial
from tkinter import scrolledtext

wd = Tk()
wd.title("calculate_helper")
#wd.geometry("640x400+100+100")

Label(wd, text="이전타임 계산").grid(row=0, column=0, pady=10)

label_List1 = [None] * 8
entry_list1 = [0] * 8
label2_List1 = [None] * 8
message_List1 = ["바깥 동전", "카드 영수증", "계좌이체", "만원권(장수)", "오천원권", "천원권", "오백원", "백원"]
btn_List1 = [None] * 3
eval_List1 = [0] * 8
multply_List1 = [10000, 5000, 1000, 500, 100]

# 함수 내에서 바로 반영시켜줘야한다.
def cal(i):
    if i == "total":
        e1['text'] = "총 금액 : " + str(sum(eval_List1))
    elif i != 3 :
        eval_List1[i] = eval(entry_list1[i].get())
        label2_List1[i]['text'] = "금액 : " + str(eval_List1[i])
    else :
        for j in range(3, 8):
            eval_List1[j] = multply_List1[j-3] * eval(entry_list1[j].get())
            label2_List1[j]['text'] = "금액 : " + str(eval_List1[j])

def init1():
    for i in range(len(eval_List1)):
        eval_List1[i] = 0
        label2_List1[i]['text'] = "금액 : "
        entry_list1[i].delete(0,"end")
        entry_list1[i].insert(0, 0)
    e1['text'] = "총 금액 : " + "0"
    

for i in range(8):
    label_List1[i] = Label(wd, text=message_List1[i]).grid(row=1+i, column=0)
    entry_list1[i] = Entry(wd)
    entry_list1[i].insert(0, 0)
    if i == 0 or i == 1 or i == 2:
        btn_List1[i] = Button(wd, text="계산", command=partial(cal, i)).grid(row=1+i, column=2)
        label2_List1[i] = Label(wd, text="금액 : ")
    else:
        label2_List1[i] = Label(wd, text="금액 : ")

for i in range(8):
    label2_List1[i].grid(row=1+i, column=3)
    entry_list1[i].grid(row=1+i, column=1)

a1 = Button(wd, text="초기화", command=init1).grid(row=9, column=0)
b1 = Button(wd, text="현금 합산 계산", command=partial(cal,3)).grid(row=9, column=1)
e1 = Label(wd, text="총 금액 : ")
b1_2 = Button(wd, text="총액 계산", command=partial(cal,"total")).grid(row=9, column=2)
e1.grid(row=9, column=3)


Label(wd, text="근무중 추가된 금액").grid(row=10, column=0, pady=10)
label_List2 = [None] * 3
entry_list2 = [0] * 3
label2_List2 = [None] * 3
message_List2 = ["카드 영수증", "계좌이체", "현금"]
eval_List2 = [0] * 3

def cal2():
    for i in range(3):
        eval_List2[i] = eval(entry_list2[i].get("1.0", END))
        label2_List2[i]['text'] = "금액 : " + str(eval_List2[i])
    e2['text'] = "총 금액 : " + str(sum(eval_List2))
    
for i in range(3):
    label_List2[i] = Label(wd, text=message_List2[i]).grid(row=11+i, column=0)
    entry_list2[i] = scrolledtext.ScrolledText(wd, width=20, height=3)
    entry_list2[i].insert('1.0', 0)
    label2_List2[i] = Label(wd, text="금액 : ")

e2 = Label(wd, text="총 금액 : ")
b2 = Button(wd, text="총액 계산", command=cal2).grid(row=18, column=1)
e2.grid(row=18, column=3)

for i in range(3):
    entry_list2[i].grid(row=11+i, column=1)
    label2_List2[i].grid(row=11+i, column=3)


Label(wd, text="마감시 계산").grid(row=19, column=0, pady=10)

label_List3 = [None] * 8
entry_list3 = [None] * 8
label2_List3 = [None] * 8
message_List3 = ["바깥 동전", "카드 영수증", "계좌이체", "만원권(장수)", "오천원권", "천원권", "오백원", "백원"]
btn_List3 = [None] * 3
eval_List3 = [0] * 8
multply_List3 = [10000, 5000, 1000, 500, 100]

# for i in range(8):
#     label_List3[i] = Label(wd, text=message_List1[i]).grid(row=20+i, column=0)
#     entry_list3[i] = Entry(wd).grid(row=20+i, column=1)
#     if i == 0 or i == 1 or i == 2:
#         btn_List3[i] = Button(wd, text="계산").grid(row=20+i, column=2)
#     label2_List3[i] = Label(wd, text="금액 : ").grid(row=20+i, column=3)

# b4 = Button(wd, text="현금 합산 계산").grid(row=28, column=1)
# e3 = Label(wd, text="총 금액 : ").grid(row=28, column=3)

# 수정 시작
def cal3(i):
    if i == "total":
        e3['text'] = "총 금액 : " + str(sum(eval_List3))
    elif i != 3 :
        eval_List3[i] = eval(entry_list3[i].get())
        label2_List3[i]['text'] = "금액 : " + str(eval_List3[i])
    else :
        for j in range(3, 8):
            eval_List3[j] = multply_List3[j-3] * eval(entry_list3[j].get())
            label2_List3[j]['text'] = "금액 : " + str(eval_List3[j])

def init3():
    for i in range(len(eval_List1)):
        eval_List3[i] = 0
        label2_List3[i]['text'] = "금액 : "
        entry_list3[i].delete(0,"end")
        entry_list3[i].insert(0, 0)
    e3['text'] = "총 금액 : " + "0"

for i in range(8):
    label_List3[i] = Label(wd, text=message_List3[i]).grid(row=20+i, column=0)
    entry_list3[i] = Entry(wd)
    entry_list3[i].insert(0, 0)
    if i == 0 or i == 1 or i == 2:
        btn_List3[i] = Button(wd, text="계산", command=partial(cal3, i)).grid(row=20+i, column=2)
        label2_List3[i] = Label(wd, text="금액 : ")
    else:
        label2_List3[i] = Label(wd, text="금액 : ")

for i in range(8):
    label2_List3[i].grid(row=20+i, column=3)
    entry_list3[i].grid(row=20+i, column=1)

a3 = Button(wd, text="초기화", command=init3).grid(row=28, column=0)
b3 = Button(wd, text="현금 합산 계산", command=partial(cal3,3)).grid(row=28, column=1)
e3 = Label(wd, text="총 금액 : ")
b3_2 = Button(wd, text="총액 계산", command=partial(cal3,"total")).grid(row=28, column=2)
e3.grid(row=28, column=3)
#수정 끝

wd.mainloop()