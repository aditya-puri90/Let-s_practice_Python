questions = [["Who is Sharukh Khan?","WWE wrestler","Actor","astronaut","Plumber",2],
["What is the capital of france?","Paris","London","Berlin","mumbai",1],
["Who is the largest mammal?","Elephant","blue Whale","Giraffe","shark",2],
["What planet is known as red planet?","Earth","Mars","venus","jupiter",2],
["Who wrote 'romeo and juiet'?","william shakesphere","Jane Auten","charles Dickens""Homer",1],
["What is the smallest country in the world?","San fransisco","vatican city","monaco","Liechtenstein",2]
]

prizes =[10000,320000,400000,500000,600000,700000]
i= 0

for question in questions:
    print(question[0])
    print(f"a.{question[1]}")
    print(f"b.{question[2]}")
    print(f"c.{question[3]}")
    print(f"d.{question[4]}")

    # chaeck wherter the answer is correct or not

    a = int(input("ENter your answer.1 for a, 2 for b, 3 for c, 4 for d \n"))

    if (question[5]== a):
        print("Correct Answer")
    else:
        print(f"Incorrect , the answer is {question[5]}")
        print("Better Luck next time!")
        break
    print(f"You Won {prizes[i]}")
    i+=1




