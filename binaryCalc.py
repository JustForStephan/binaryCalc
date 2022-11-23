#!/usr/bin/env python3
#/bin/bash
import sys
summands = []
operation = "+"

def introduction():
    print("Dieser Algorithmus addiert, subtrahiert, multipliziert und dividiert alle moeglichen binearen Werte miteinander")
    print("Dabei gelten folgende Regeln:")
    print("-----------------------------------------------------")
    print("1. Leerzeichen, Sonderzeichen oder Buchstaben sind nicht erlaubt")
    print("2. Die binearen Werte sind ohne Komma, Punkt oder Semikolon einzugeben. Zum Beispiel: 1010")
    print("3. Die Operatoren sind in Form von \"+\", \"-\", \"*\", \"/\" einzugeben")
    print("4. Alle Werte müssen die gleiche Länge besitzen")
    print("-----------------------------------------------------\n")
    

def addition(summand1, summand2):
    result = []
    summand = summand.remove("p")
    for i in range(len(summand1)):
        if(summand1[i] == 1 and summand2[i] == 1):
               rusult[i] = 1
        else:
            result[i] = 0
    return result

def substraction(summand1, summand2):
    result[]
    for i in range(summand2):
        if(summand2(i) == 1):
            summand2(i) == 0)
        if(summand2(i) == 0):
            summand2(i) == 1
    for i in range(len(summand1)):
        if(summand1[i] == 1 and summand2[i] == 1):
               rusult[i] = 1
        else:
            result[i] = 0

    return result

def multiplicate(factor1, factor2):
    factor1.add(0)
    factor2 = [0,factor2]
    result = []
    for i in range(len(factor1)):
        if(factor1[i] == 1 and factor2[i] == 1):
            result[i] = 0
            result[i+1] = 1
        if(factor1[i] == 0 and factor2[i] == 0):
            result[i] = 0
        if(factor1[i] == 1 Xor factor2[i] == 1):
            result[i] = 1
    return result

def division(divisor1, divisor2):
    

def prepareInput(answer):
    result = []
    answer = answer.replace("+","p|") # give signal to add
    answer = answer.replace("-","m|") # give signal to   subtract
    answer = answer.replace("*","t|") # give signal to multiplicate
    answer = answer.replace("/","d|") # give signal to divide
    numbers = numbers.split("|")
    
    for i in numbers:
        number = i.split("")
        
        try:
            result[i] = int(number[i]) #must consider, that the operant-extension is not int
        except NameError:
            if(number[i] == "p" or number[i] == "m" or number[i] == "m" or number[i] == "d"):
                result[i] = number[i]
            else:
                print("Du Idiot hast Buchstaben, Leerzeichen oder Sonderzeichen verwendet! Nochmal...")
                Sys.exit()
    return 
            
        
introduction()

while(True):
    summands = prepareInput(input("Gib den vollsteandigen Term ein:"))
    
