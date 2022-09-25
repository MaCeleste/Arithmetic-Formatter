def arithmetic_arranger(problems, show_result = False ):
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

    #splitting problem into operands
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
      return('Error: Numbers must only contain digits.')
      break

    #adding the splitted problem into a new list that will store each problem as a list
    problemsAsStr.append(operands)

  #calculating the solution to each problem and storing the results in a new list
  results = []
  for sproblem in problemsAsStr:
    if sproblem[1] == '+':
      result = int(sproblem[0])+int(sproblem[2])
    else:
      result = int(sproblem[0])-int(sproblem[2])
    results.append(str(result))

  #in this variable I will store a list of the formatted problems
  #with the correct number of spaces and their corresponding result
  formattedProblems = []
  #iterating through each problem to find the longest of the two operands and
  #applying the correct number of spaces
  count = 0
  for sproblem in problemsAsStr:
    #this variable will store each problem once the spaces have been added
    problemWithSpaces = []
    longest = max(sproblem, key=len)
    #if the second operand is the longest operand, we need to apply to the smallest
    #operand a number of spaces that will be equal to the lenght of the longest
    #operand + 2, to account for the operator symbol and the space next to it
    #then we concatenate the symbol, one space and the longest operand and
    #add both to the list that stores the problem with spaces added
    if longest == sproblem[2]:
      smallest = sproblem[0].rjust(len(longest)+2, ' ')
      problemWithSpaces.append(smallest)
      problemWithSpaces.append(sproblem[1]+" "+longest)
    #if the first operand is the longest operand, we need to apply to the smallest
    #operand a number of spaces that will be equal to the lenght of the longest
    #operand. The longest operand needs two spaces before it to account for the operator
    #symbol and the space next to it.
    if longest == sproblem[0]:
      smallest = sproblem[2].rjust(len(longest), ' ')
      problemWithSpaces.append('  '+longest)
      problemWithSpaces.append(sproblem[1]+" "+smallest)
    #finally we append to the list the result of the problem from the results variable
    #with a number of spaces equal to the lenght of the longest operator + 2
    problemWithSpaces.append(results[count].rjust(len(longest)+2, ' '))
    count += 1
    #each problemWithSpaces now is a list that contains 3 items: the first operand,
    # the symbol concatenated with the second operand and lastly the result. Correct
    #number of spaces has been applied.
    formattedProblems.append(problemWithSpaces)

  #to put the first operand of each problem in the first line,
  #the second operand of each problem in the second line
  #add a third line with the correct number of '-'
  #and the results on the fourth line
  firstLine = ''
  secondLine = ''
  thirdLine = ''
  fourthLine = ''
  count = 1
  for fproblem in formattedProblems:
    #if we have reached the last item of the list, we should not add spaces
    #to the end of the string.
    if count == len(formattedProblems):
      firstLine = firstLine + fproblem[0]
      secondLine = secondLine + fproblem[1]
      thirdLine = thirdLine + '-'*len(fproblem[0])
      fourthLine = fourthLine + fproblem[2]

    else:
      firstLine = firstLine + fproblem[0] + '    '
      secondLine = secondLine + fproblem[1] + '    '
      thirdLine = thirdLine + '-'*len(fproblem[0]) + '    '
      fourthLine = fourthLine + fproblem[2] + '    '
    count = count + 1


  #concatenate either three or four lines depending on the second parameter passed to the function
  if show_result == False:
    arranged_problems = firstLine + '\n' + secondLine + '\n' + thirdLine
  else:
    arranged_problems = firstLine + '\n' + secondLine + '\n' + thirdLine+ '\n' + fourthLine

  return arranged_problems

print(arithmetic_arranger(["32 + 698", "3801 - 2", "45 + 43", "123 + 49"]))
print(arithmetic_arranger(["32 + 698", "3801 - 2", "45 + 43", "123 + 49"], True))
print(arithmetic_arranger(['1 + 2', '1 - 9380']))
print(arithmetic_arranger(['1 + 2', '1 - 9380'], True))
print(arithmetic_arranger(["11 + 4", "3801 - 2999", "1 + 2", "123 + 49", "1 - 9380"]))
print(arithmetic_arranger(['3 / 855', '3801 - 2', '45 + 43', '123 + 49']))
print(arithmetic_arranger(['24 + 85215', '3801 - 2', '45 + 43', '123 + 49']))
print(arithmetic_arranger(['98 + 3g5', '3801 - 2', '45 + 43', '123 + 49']))
print(arithmetic_arranger(['44 + 815', '909 - 2', '45 + 43', '123 + 49', '888 + 40', '653 + 87']))
