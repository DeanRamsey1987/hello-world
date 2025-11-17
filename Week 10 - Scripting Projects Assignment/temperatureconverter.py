from breezypythongui import EasyFrame

class TemperatureConverter(EasyFrame):
    def __init__(self):
        EasyFrame.__init__(self, title="Temperature Converter")

        self.addLabel(text="Fahrenheit", row=0, column=0)
        self.addLabel(text="Celsius", row=0, column=1)

        self.fField = self.addFloatField(value=32.0,
                                         row=1,
                                         column=0,
                                         width=10)

        self.cField = self.addFloatField(value=0.0,
                                         row=1,
                                         column=1,
                                         width=10)

        self.addButton(text=">>>>",
                       row=2, column=0,
                       command=self.fToC)

        self.addButton(text="<<<<",
                       row=2, column=1,
                       command=self.cToF)

    def fToC(self):
        f = self.fField.getNumber()
        c = (f - 32) * 5.0 / 9.0
        self.cField.setNumber(c)

    def cToF(self):
        c = self.cField.getNumber()
        f = (c * 9.0 / 5.0) + 32
        self.fField.setNumber(f)

def main():
    TemperatureConverter().mainloop()

if __name__ == "__main__":
    main()
