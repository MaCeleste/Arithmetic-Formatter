def arithmetic_arranger(problems):
  problemsAsInt = []
  problemsAsStr = []
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
      operands[0] = int(operands[0])
      operands[2] = int(operands[2])
    except:
      return('Error: Numbers must only contain digits.')
      break
    #creating a list that stores the problems with the operands converted to integers
    problemsAsInt.append(operands)
    #splitting the user input into strings
    operandsAsStr = problem.split()
    problemsAsStr.append(operandsAsStr)

  #in this variable I will store the problems with the correct number of spaces
  problemsWithSpaces = []
  #iterating through each problem to find the longest of the two operands and
  #apply the correct number of spaces
  for sproblem in problemsAsStr:
    problemWithSpaces = []
    longest = max(sproblem, key=len)
    #print(longest)
    if longest == sproblem[2]:
      smallest = sproblem[0].rjust(len(longest)+2, ' ')
      problemWithSpaces.append(smallest)
      problemWithSpaces.append(sproblem[1]+" "+longest)
    if longest == sproblem[0]:
      smallest = sproblem[2].rjust(len(longest), ' ')
      problemWithSpaces.append('  '+longest)
      problemWithSpaces.append(sproblem[1]+" "+smallest)

    problemsWithSpaces.append(problemWithSpaces)


  #to put each the first operand of each problem in the first line,
  #the second operand of each problem in the second line
  #and add a third line with the correct number of '-'
  firstLine = ''
  secondLine = ''
  thirdLine = ''
  count = 1
  for fproblem in problemsWithSpaces:
    if count == len(problemsWithSpaces):
      firstLine = firstLine + fproblem[0]
      secondLine = secondLine + fproblem[1]
      thirdLine = thirdLine + '-'*len(fproblem[0])
    else:
      firstLine = firstLine + fproblem[0] + '    '
      secondLine = secondLine + fproblem[1] + '    '
      thirdLine = thirdLine + '-'*len(fproblem[0]) + '    '
    count += 1

  #concatenate the three lines
  arranged_problems = firstLine + '\n' + secondLine + '\n' + thirdLine

  return arranged_problems



print(arithmetic_arranger(["32 + 698", "3801 - 2", "45 + 43", "123 + 49"]))
