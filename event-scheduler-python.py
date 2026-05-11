#Program to manage event scheduling and detect overlapping time conflicts betwen events.
schedule = []

while True:
    event = input("Event name: ")
    start = float(input("Start time: "))
    end = float(input("End time: "))

    conflict_found = False

    for s_event, s_start, s_end in schedule:
        if start < s_end and end > s_start:   
            print("Conflict with:", s_event)
            conflict_found = True
            break

    if not conflict_found:
        schedule.append([event, start, end])
        print("Event added")

    if input("Add more? (yes/no): ") != "yes":
        break

print("\nFinal events:", schedule)
