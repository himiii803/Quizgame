import tkinter
from tkinter import *
from tkinter import messagebox as mb

root = tkinter.Tk()
root.title("PyQuiz")
root.geometry("800x450")
root.resizable(0, 0)

q = [
    "Q1. ∫x dx from x=0 to x=2 will be?",
    "Q2. Formula for mass energy equivalence is?",
    "Q3. Which one of the following is the correct extension of the Python file?",
    "Q4. Which of the following is the slope intercept form of a line?", "Q5. The Lens maker's formula is:",
    "Q6. Which of the following operators is the correct option for power(ab)?",
    "Q7. Torque on a dipole placed in the electric field:", "Q8. Probability of getting a 6 on throwing a fair die is?",
    "Q9. Which character is used in Python to make a single line comment?", "Q10. nCr = ?"
]

options = [
    ["0", "1", "2", "4"], ["R = Ro e^-λt", "Δm = M – m = [Zmp + (A – Z)mn – mn]", "E=mc^2 ", "dN/dt = - λN"],
    [".python", ".py", ".p", "None of these"], ["y-y1=m(x-x1)", "y=mx+c", "Ax+By=C", "x/a + y/b = 1"],
    ["1/v – 1/u = 1/f", "m= -v/u", "1/f = (n−1)(1/R1 – 1/R2)", "1/v + 1/u = 2/R"],
    ["a ^ b", "a ^ ^ b", "a ^ * b", "a**b"], ["τ=p×E", "p=qd", "U=−p.E", "τ=p.E"], ["1/6", "0", "1/2", "1"],
    ["/", "//", "#", "!"], ["n!/(n-r)!", "(n-r)!/r!", "r!/(n-r)!", "n!/r!(n-r)!"]
]

a = [3, 3, 2, 2, 3, 4, 1, 1, 3, 4]


class Quiz:
    def __init__(self):
        self.qn = 0
        self.opt_selected = IntVar()
        self.ques = self.question(self.qn)
        self.opts = self.radiobuttons()
        self.display_options(self.qn)
        self.buttons()
        self.correct = 0

    def question(self, qn):
        t = Label(root, text="QUIZ GAME IN PYTHON", width=35, bg="blue", fg="white",
                  font="Castellar 24 bold")
        t.place(x=0, y=2)
        qn = Label(root, text=q[qn], width=60, font="ariel 16 bold", anchor='w')
        qn.place(x=70, y=100)
        return qn

    def radiobuttons(self):
        val = 0
        b = []
        yp = 150
        while val < 4:
            btn = Radiobutton(root, text="", variable=self.opt_selected,
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
        nbutton = Button(root, text="NEXT", command=self.next_btn, width=10, bg='green', fg='white',
                         font='ariel 16 bold')
        nbutton.place(x=200, y=380)
        qbutton = Button(root, text="QUIT", command=quit, width=10,
                         bg='black', fg='white', font='ariel 16 bold')
        qbutton.place(x=380, y=380)

    def checkans(self, qn):
        if self.opt_selected.get() == a[qn]:
            return True

    def next_btn(self):
        if self.checkans(self.qn):
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
        string = "Name"
        mb.showinfo("RESULT", "\n".join([string, correct, wrong, result]))


quiz = Quiz()
root.mainloop()
