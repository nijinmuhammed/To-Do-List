import time

print('''
    ================
    --TASK MANAGER--
    ================
''')

timeNow = time.localtime()
hour = timeNow.tm_hour
if hour >= 5 and hour < 12:
    print("Good morning!")
elif hour >= 12 and hour < 16:
    print("Good afternoon!")
elif hour >= 16 and hour <= 19:
    print("Good evening!")
else:
    print("")

todolist = []
i = 1
while True:
    question = int(input('''
    ACTIONS:
    1. Add a task
    2. Delete a task
    3. Mark as done
    4. Task list
    5. Exit
    
    Enter your option: '''))
    if question == 5:
        print("\n    Okay Bie....\n    Have a nice day!")
        break
    elif question == 1:
        add = input("    Add a task to do: ")
        todolist.append(add)
    elif question == 2:
        for item in todolist:
            print(item)
        item = int(input("    Enter the index of task you want to delete: ")) - 1
        todolist.pop(item)
        print(f"Task {item+1} is deleted")
    elif question == 4:
        print('''
            TO DO LIST
            ----------''')
        i = 1
        for item in todolist:
            print(i, "         ", item)
            i += 1
    elif question == 3:
        for item in todolist:
            print("   ", item)
        ask = int(input("    Which task you have completed: "))-1
        print(f"\n    Yeah... you have completed task {ask+1}")
        todolist[ask] += " ✓"
    else:
        print("\nSelect a valid option...!")
