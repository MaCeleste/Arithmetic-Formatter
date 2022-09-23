verifiedProblems = []

def arithmetic_arranger(problems):
  for problem in problems:

    #checking if up to 5 problems were entered
    if len(problems) > 5:
      return('Error: Too many problems.')
      break
    #checking if input has either + or - symbol
    if '+' not in problem and '-' not in problem:
      return("Error: Operator must be '+' or '-'.")
      break
    #splitting problem
    operands = problem.split()
    #checking if operands have up to 4 digits digits
    if len(operands[0]) > 4 or len(operands[2]) > 4:
      return('Error: Numbers cannot be more than four digits.')
      break
    #checking if operands contain only digits
    try:
      int(operands[0])
      int(operands[2])
    except:
      return('Numbers must only contain digits.')
      break
    verifiedProblems.append(operands)
  print(verifiedProblems)



print(arithmetic_arranger(["32 + 698", "3801 - 2", "45 + 43", "123 + 49"]))
