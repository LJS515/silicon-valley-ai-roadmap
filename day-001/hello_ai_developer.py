def print_header():
    print("Silicon Valley AI Developer Roadmap")
    print("Day 1 - Developer Environment and Core Workflow")
    print("_" * 60)


def print_core_principle():
    print("Core Principle:")
    print("I use AI to write code faster and solve problems more boldly.")
    print("I do not use AI because I cannot code without it.")
    print("I must understand, verify, debug, and improve the code.")

def print_day_1_tasks():
    tasks = {
        "Set up the development environment",
        "Create the first roadmap repository",
        "Write the first Python script",
        "Write the project README",
        "Make the first Git commit",
        "Push the repository to GitHub",
        "Write the Day 1 reflection",
    }

    print("Day 1 Tasks:")

    for index, task in enumerate(tasks, start=1):
        print(f"{index}, {task}")

def main():
    print_header()
    print_core_principle()
    print()
    print_day_1_tasks()

if __name__ == "__main__":
    main()