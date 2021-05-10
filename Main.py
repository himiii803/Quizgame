import tkinter
from tkinter import *
from tkinter import messagebox as mb

root = tkinter.Tk()
root.title("PyQuiz")
root.geometry("800x450")
root.resizable(0, 0)
#You can change the color theme of this quiz app as per your requirement
root.config(background='black')
name_var = StringVar()


def submit():
    global nn
    name = name_var.get()
    nn = name
    print("The name is :" + name)
    name_var.set("")
    return name


l1 = Label(root, text="QUIZ GAME IN PYTHON", width=35, bg="blue", fg="white",
           font="Castellar 24 bold")
l1.pack()
l2 = Label(root, text="NAME", font='ariel 18 bold', bg='black', fg='white')
l2.place(x=180, y=105)
e = Entry(root, textvariable=name_var, width=25, font='ariel 16 bold')
e.place(x=300, y=110)

#You can add any number of questions or change the questions as per your need!
q = [
    "Q1. ∫x dx from x=0 to x=2 will be?",
    "Q2. Formula for mass energy equivalence is?",
    "Q3. Which one of the following is the correct extension of\nthe Python file?",
    "Q4. Which of the following is the slope intercept form of a line?",
    "Q5. The Lens maker's formula is:",
    "Q6. Which of the following operators is the correct option for\npower(ab)?",
    "Q7. Torque on a dipole placed in the electric field:",
    "Q8. Probability of getting a 6 on throwing a fair die is?",
    "Q9. Which character is used in Python to make a single\nline comment?",
    "Q10. nCr = ?"
]

#If you are changing the questions, do not forget to make changes in the options and the answer list too :)
options = [
    ["0", "1", "2", "4"],
    ["R = Ro e^-λt", "Δm = M – m = [Zmp + (A – Z)mn – mn]", "E=mc^2 ", "dN/dt = - λN"],
    [".python", ".py", ".p", "None of these"],
    ["y-y1=m(x-x1)", "y=mx+c", "Ax+By=C", "x/a + y/b = 1"],
    ["1/v – 1/u = 1/f", "m= -v/u", "1/f = (n−1)(1/R1 – 1/R2)", "1/v + 1/u = 2/R"],
    ["a ^ b", "a ^ ^ b", "a ^ * b", "a**b"], ["τ=p×E", "p=qd", "U=−p.E", "τ=p.E"], ["1/6", "0", "1/2", "1"],
    ["/", "//", "#", "!"], ["n!/(n-r)!", "(n-r)!/r!", "r!/(n-r)!", "n!/r!(n-r)!"]
]

a = [3, 3, 2, 2, 3, 4, 1, 1, 3, 4]


def start():
    l1.destroy()
    l2.destroy()
    e.destroy()
    b1.destroy()
    sub_btn.destroy()
    Quiz()


class Quiz:
    def __init__(self):
        self.qn = 0
        self.opt_selected = IntVar()
        self.ques = self.question(self.qn)
        self.opts = self.radio_buttons()
        self.display_options(self.qn)
        self.buttons()
        self.correct = 0

    def question(self, qn):
        l3 = Label(root, text="2 marks", font='ariel 14 bold', bg='black', fg='white')
        l3.place(x=700, y=50)
        t = Label(root, text="QUIZ GAME IN PYTHON", width=35, bg="blue", fg="white",
                  font="Castellar 24 bold")
        t.place(x=0, y=2)
        qn = Label(root, text=q[qn], bg='black', fg='white', width=50, font="ariel 16 bold", anchor='w')
        qn.place(x=70, y=100)
        return qn

    def radio_buttons(self):
        val = 0
        b = []
        yp = 150
        while val < 4:
            btn = Radiobutton(root, text="", variable=self.opt_selected, bg='black', fg='white',
                              value=val + 1, font="ariel 14")
            b.append(btn)
            btn.place(x=100, y=yp)
            val += 1
            yp += 40
        return b

    def display_options(self, qn):
        val = 0
        self.opt_selected.set(0)
        self.ques['text'] = q[qn]
        for op in options[qn]:
            self.opts[val]['text'] = op
            val += 1

    def buttons(self):
        nb = Button(root, text="NEXT", command=self.next_btn, width=10, bg='green', fg='white',
                    font='ariel 16 bold')
        nb.place(x=200, y=380)
        qb = Button(root, text="QUIT", command=quit, width=10,
                    bg='red', fg='white', font='ariel 16 bold')
        qb.place(x=380, y=380)

    def check_ans(self, qn):
        if self.opt_selected.get() == a[qn]:
            return True

    def next_btn(self):
        if self.check_ans(self.qn):
            self.correct += 1
        self.qn += 1
        if self.qn == len(q):
            self.display_result()
        else:
            self.display_options(self.qn)

    def display_result(self):
        score = int(self.correct * 100 / len(q))
        result = "Percentage = " + str(score) + "%"
        wc = len(q) - self.correct

        correct = "No. of correct answers: " + str(self.correct)
        wrong = "No. of wrong answers: " + str(wc)

        string = "Candidate Name: " + str(nn)
        mb.showinfo("RESULT", "\n".join([string, correct, wrong, result]))


sub_btn = Button(root, text='Submit', command=submit, font='ariel 14 bold', bg='orange')
sub_btn.pack(pady=150)
b1 = Button(root, text="START", font='ariel 20 bold', relief='raised', bg='green', cursor='hand2', command=start)
b1.pack(pady=5)
root.mainloop()
