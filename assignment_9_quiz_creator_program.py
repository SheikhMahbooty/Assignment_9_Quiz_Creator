#Assignment 9: Create a program that ask user for a question, it will also ask for 4 possible answer (a,b,c,d) and the correct answer. Write the collected data to a text file. Ask another question until the user chose to exit.

#Make python create a txt file and if user adds more questions, update the file every time a new question gets added
file = open("quiz_questions.txt", "a")

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
    
#Input for the correct answer
    while True:
        correct = str(input("\nCorrect answer (a/b/c/d): "))
        if correct == "a":
            correct = answer_a
            break
        elif correct == "b":
            correct = answer_b
            break
        elif correct == "c":
            correct = answer_c
            break
        elif correct == "d":
            correct = answer_d
            break
        else:
            correct = print("\nInvalid input, enter a,b,c,d")


    file.write(f"Question: {input_question}")
    file.write(f"a) {answer_a}")
    file.write(f"b) {answer_b}")
    file.write(f"c) {answer_c}")
    file.write(f"d) {answer_d}")
    file.write(f"Correct Answer: {correct}")
#check if the variables are correct

    print(input_question)
    print(answer_a, answer_b, answer_c, answer_d)
    print(correct)
    
file.close()
