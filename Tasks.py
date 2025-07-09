import sys
from datetime import datetime, time, timedelta

def main():
    original_stdin = sys.stdin
    sys.stdin = open("tasks.in")
    TASKS, end, task_list = inputs()
    minutes = time_get(end)
    x = sum([int(i[1])for i in task_list])
    if minutes < x:
        task_list = remove_items(task_list, original_stdin, minutes)
    
def remove_items(task_list: list, original_in, minutes) -> list:
    sys.stdin = original_in
    print("Remove Format: Task, Operation, Number (Put Null if not applicable), say /h for more")
    [print(f"{x[0]}: {x[1]}") for x in task_list]
    x = input("Remove an Item: ").split(" ")
    if minutes < x:
        task_list = remove_items(task_list, original_in, minutes)
    return task_list

#Returns how many minutes are left
def time_get(end: list) -> int:
    ct = datetime.now()
    end_timer = datetime(ct.year, ct.month, ct.day, end[0], end[1], end[2])
    time_left = end_timer-ct
    if end_timer.hour < ct.hour:
        raise ValueError(f"Negative Time Left from {str(ct.hour)}:{str(ct.minute).zfill(2)} to {str(end_timer.hour).zfill(2)}:00")
    return round(int(time_left.total_seconds())/60, 2)

#Gets all the inputs
def inputs() -> list:
    TASKS = int(input())
    end = [int(x) for x in input("").split(" ")]
    task_list = [input("").split(" ") for x in range(TASKS)]
    #Task_Name, Time Percentage, Is_Completed
    return TASKS, end, task_list

if __name__ == "__main__":
    main()
