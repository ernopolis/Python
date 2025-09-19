def get_answer(message):
    answer = input(message)
    answer = answer.lower()
    while answer not in ["yes", "no"]:
        print("Invalid answer [yes/no]")
        answer = input(message)
        answer = answer.lower()
    return answer


answer = get_answer("Want cookies? ")
print(f"You said {answer}")
