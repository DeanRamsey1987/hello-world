from breezypythongui import EasyFrame

class TaxCalculator(EasyFrame):
    def __init__(self):
        EasyFrame.__init__(self, title="Tax Calculator")
        self.addLabel(text="Gross Income", row=0, column=0)
        self.incomeField = self.addFloatField(value=0.0,
                                              row=0,
                                              column=1,
                                              width=12)
        self.addLabel(text="Dependents", row=1, column=0)
        self.depField = self.addIntegerField(value=0,
                                             row=1,
                                             column=1,
                                             width=5)
        self.addLabel(text="Total Tax", row=2, column=0)
        self.taxField = self.addFloatField(value=0.0,
                                           row=2,
                                           column=1,
                                           width=12,
                                           precision=2,
                                           state="readonly")
        self.addButton(text="Compute",
                       row=3, column=0,
                       columnspan=2,
                       command=self.computeTax)

    def computeTax(self):
        try:
            income = self.incomeField.getNumber()
            dependents = self.depField.getNumber()
            taxable = income - (dependents * 3500)
            if taxable < 0:
                taxable = 0
            tax = taxable * 0.10
            self.taxField.setNumber(tax)
        except ValueError:
            self.messageBox(title="Error",
                            message="Enter valid numeric values.")

def main():
    TaxCalculator().mainloop()

if __name__ == "__main__":
    main()
