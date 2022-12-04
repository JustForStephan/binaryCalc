import sys

class dataPreperation:

    def binaryToDecimal(self,value):
        decimal = 0
        sortedList = []
        for x in range(len(value)-1,-1,-1):
            sortedList.append(value[x])
        for x in range(len(value)):
            if(value[x]==1):
                decimal = decimal + 2**x
        return decimal

    def obtainValues(self):
        values = []
        operants = []
        counter = 0
        print("Enter the operants in the following. Notice to take the operator before the operant!")
        while (True):
            element = input("operant " + str((counter + 1)) + ":")
            if (element == "exit"):
                break
            if (element[0] == "+" or element[0] == "-" or element[0] == "*" or element[0] == "/"):
                operants.append(element[0])
                element = element.replace("+","")
                element = element.replace("-","")
                element = element.replace("*","")
                element = element.replace("/","")
            print(element)
            if (element == "exit"):
                break
            else:
                values.append(self.convertToByte(element))
                counter = counter + 1

        for x in values:
            x = self.extendZero(x)

        return values, operants

    def extendZero(self,list):
        return list.insert(0,0)

    def convertToByte(self,string):
        resultList = []
        for i in range(len(string)):
            try:
                resultList.append(int(string[i]))
            except BaseException:
                print("Error occoured: The input \""+string[i]+ "\" is no suitable value!")
                sys.exit()
        return  resultList

class calculation:
    prepare = dataPreperation
    operant1 = 0
    operant2 = 0

    def search(self, operant1, operant2, operation):
        print(operation)
        if(operation == "+"):
            print("took +")
            return self.addition(operant1, operant2)
        elif(operation == "-"):
            return self.substraction(operant1, operant2)
        elif(operation == "*"):
            print("took *")
            return self.multiplicationate(operant1, operant2)
        elif(operation == "/"):
            print("took /")
            return self.division(operant1, operant2)
        else:
            print("Unhandable operant used. Restart algorithm!")
            sys.exit()

    def addition(self,operant1, operant2):
        result = [0]*len(operant1)
        transfer = 0
        for x in range(len(operant1)-1,-1,-1):
            if(operant1[x] == 1 and operant2[x] == 1):
                result[x] = 0+ transfer
                if(transfer == 0):
                    transfer = 1
            else:
                result[x] = operant1[x]+operant2[x]+transfer
                if(transfer + operant2[x] + operant1[x] == 2):
                    result[x] == 0
                else:
                    transfer = 0

        return result

    def substraction(self, operant1, operant2):
        if(self.prepare.binaryToDecimal(self.prepare, operant1) < self.prepare.binaryToDecimal(self.prepare,operant2)):
            #build second complement
            for x in range(len(operant2)):
                if(operant2[x] == 1):
                    operant2[x] = 0
                else: operant2[x] = 1
                plusOne = [0]*len(operant1)
                plusOne[len(operant1)] = 1
                operant2 = calculation.addition(operant1, plusOne)
                return calculation.addition(operant1, operant2)
        else:
            transfer2 = 0
            result = [0]*len(operant1)
            for x in range(len(operant1)-1,-1,-1):
                result[x],transfer1 = calculation.substractionCalcSystem(self,operant1[x], operant2[x])
                result[x],z = calculation.substractionCalcSystem(self, result[x],transfer2)
                transfer2 = transfer1
            return result

    def substractionCalcSystem(self, operant1, operant2):
        if(operant1 == 1 and operant2 == 1):
            return 0,0
        elif(operant1 == 1 and operant2 == 0):
            return 1,0
        elif(operant1 == 0 and operant2 == 1):
            return 1,1
        elif(operant1 == 0 and operant2 == 0):
            return 0,0

    def multiplication(self):
        pass
    def division(self):
        pass

class Main:

    prepare = dataPreperation()
    calc = calculation()
    global values #extends all operants
    global operants # extends all operations for calculating

    # structure
    values, operants = prepare.obtainValues()

    # adds to the first positive value a 0, so that the + can stay
    if (operants[0] == "+"):
        toInsert = [0]*len(values[0])
        values.insert(0,toInsert)

    print(calc.substraction([0,1,1,0,0,1,1],[0,1,0,1,1,0,1]))