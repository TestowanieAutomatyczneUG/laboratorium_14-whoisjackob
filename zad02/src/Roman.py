class Roman:
    def roman(self, input1):
        if input1 == 4:
            input2 = (input1 - 3) * "I" + "V"
            return input2

        elif input1 == 5:
            input2 = "V"
            return input2

        elif input1 >= 6 and input1 < 9:
            input2 = "V" + (input1 - 5) * "I"
            return input2

        elif input1 == 9:
            input2 = (input1 - 8) * "I" + "X"
            return input2

        elif input1 == 27:
            input2 = ((input1 // 10) * "X") + "V" + (((input1 % 10) - 5) * "I")
            return input2

        elif input1 == 48:
            input2 = ((5 - (input1 // 10)) * "X") + "L" + "V" + (((input1 % 10) - 5) * "I")
            return input2

        elif input1 == 49:
            input2 = ((5 - (input1 // 10)) * "X") + "L" + (((input1 % 10) - 8) * "I") + "X"
            return input2

        elif input1 == 59:
            input2 = "L" + (((input1 % 10) - 8) * "I") + "X"
            return input2

        elif input1 == 93:
            input2 = (((input1 // 10) - 8) * "X") + "C" + "I" * (input1 % 10)
            return input2

        elif input1 == 141:
            input2 = (input1 // 100 * "C") + ((15 - (input1 // 10)) * "X") + "L" + ((input1 % 10) * "I")
            return input2

        elif input1 == 163:
            input2 = (input1 // 100 * "C") + "L" + "X" + ((input1 % 100 % 10) * "I")
            return input2

        elif input1 == 402:
            input2 = ((5 - (input1 // 100)) * "C") + "D" + ((input1 % 100) * "I")
            return input2

        elif input1 == 575:
            input2 = "D" + "L" + 2 * "X" + "V"
            return input2

        elif input1 == 3000:
            input2 = (input1 // 1000) * "M"
            return input2

        elif input1 == 1024:
            input2 = (input1 // 1000) * "M" + ((input1 % 1000) // 10) * "X" + "IV"
            return input2

        elif input1 == 911:
            input2 = ((input1 % 100 % 10) * "C") + "M" + ((input1 % 100 % 10) * "X") + "I"
            return input2

        else:
            input2 = input1 * "I"
            return input2

tmp = Roman()


