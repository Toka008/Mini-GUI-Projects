from distutils import command
from tkinter import *

class LoanCalculator():
    def __init__(self):
        window = Tk()
        window.title("Loan Calculator")
        window.config(bg ="light green")
        
        Label(window,font = "Helvetica 12 bold",text = "Annual Interest Rate",bg ="light green").grid(row = 1,column = 1,sticky =W)
        Label(window,font = "Helvetica 12 bold",text = "Number Of Years",bg = "light green").grid(row = 2,column = 1,sticky =W)
        Label(window,font = "Helvetica 12 bold",text = "Loan Amount",bg = "light green").grid(row = 3,column = 1,sticky =W)
        Label(window,font = "Helvetica 12 bold",text = "Monthly Payment",bg = "light green").grid(row = 4,column = 1,sticky =W)
        Label(window,font = "Helvetica 12 bold",text = "Total Payment",bg = "light green").grid(row = 5,column = 1,sticky =W)

        self.annualInterestRateVar = StringVar()
        Entry(window,textvariable=self.annualInterestRateVar,bg ="light grey",justify=RIGHT).grid(row = 1,column = 2)

        self.numberofYearsVar = StringVar()
        Entry(window,textvariable=self.numberofYearsVar,bg = "light grey",justify = RIGHT).grid(row = 2,column = 2)

        self.loanAmountVar = StringVar()
        Entry(window,textvariable=self.loanAmountVar,bg = "light grey",justify=RIGHT).grid(row = 3,column = 2)

        self.monthlyPaymentVar = StringVar()
        lblMonthlyPaymnet = Label(window,textvariable=self.monthlyPaymentVar,bg = "light blue",justify=RIGHT).grid(row = 4,column = 2,sticky=E)

        self.totalPaymentVar= StringVar()
        lblTotalPayment = Label(window,textvariable=self.totalPaymentVar,bg = "light blue",justify=RIGHT).grid(row = 5,column = 2,sticky = E)

        btComputePayment = Button(window,font = "Helvetica 12 bold",text = "Compute Payment",bg = "cyan",fg = "black",command = self.computePayment).grid(row = 6,column=2,sticky = E)

        btClear = Button(window,font = "Helvetica 12 bold",text = "Clear",bg = "cyan",fg = "black",command = self.clear).grid(row =6,column=8,padx = 20,pady = 20,sticky = E)

        window.mainloop()
        
    def computePayment(self):
        monthlyPayment = self.getMonthlyPayment(
            float(self.loanAmountVar.get()),
            float(self.annualInterestRateVar.get()) / 1200,
            int(self.numberofYearsVar.get()))

        self.monthlyPaymentVar.set(format(monthlyPayment, "10.2f"))
        
        totalPayment = float(self.monthlyPaymentVar.get()) * 12 \
            * int (self.numberofYearsVar.get())
        
        
        self.totalPaymentVar.set(format(totalPayment, "10.2f"))


    def getMonthlyPayment(self,loanAmount,monthlyInterestRate,numberofYears):
        monthlyPayment = loanAmount * monthlyInterestRate / (1 - 1 / (1 + monthlyInterestRate) ** (numberofYears * 12))
        return monthlyPayment

    def clear(self):
        self.annualInterestRateVar.set("")
        self.numberofYearsVar.set("")
        self.loanAmountVar.set("")
        self.monthlyPaymentVar.set("")
        self.totalPaymentVar.set("")



LoanCalculator()




    


