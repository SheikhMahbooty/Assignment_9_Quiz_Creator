#Assignment 9: Create a program that ask user for a question, it will also ask for 4 possible answer (a,b,c,d) and the correct answer. Write the collected data to a text file. Ask another question until the user chose to exit.

#Create loop so the user can input a question
while True:
    input_question = input("Enter a question or type 'exit' to exit: ") #Created question loop to exit or add a question
    if input_question.lower() == "exit":
        break
#Changed variables to "answer_a... answer_d"
    answer_a = input("Enter answer a: ")
    answer_b = input("Enter answer b: ")
    answer_c = input("Enter answer c: ")
    answer_d = input("Enter answer d: ")
#Make choices to make new questions or quit
#Would you like to make a new question? or quit
    print(answer_a, answer_b, answer_c, answer_d)
    print(input_question)
#Export to txt file (I DO NOT KNOW HOW!!!!!)
