def calculator():
    print("this is my calculator app")
    while True:
        user_input = input("plz enter number(s), and if u want to quit type 'exit': ")
        if user_input.lower() == 'exit':
            print("brah wtf...")
            break
        try:
            result = eval(user_input)
            print("answer: ", result)
        except Exception as e:
            print("u did a fuck up ", str(e))

if __name__ == "__main__":
    calculator()