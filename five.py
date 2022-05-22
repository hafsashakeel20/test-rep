#5
def comm_list():
    print("")
    participants_list = [
        ['Sam', 'Emma', 'Joan', 'Krish', 'John', 'Desmond', 'Tom', 'Nicole' ],
        ['Brad', 'Walter', 'Sam', 'Krish','Desmond', 'Jennifer'],
        ['Tom', 'Krish', 'Emma', 'Mia', 'Nicole', 'Sam', 'Desmond'],
        ['Desmond', 'Sam', 'Krish', 'Mia', 'Harry'],
        ['Ron', 'Ginny', 'Ted', 'Krish', 'Mia', 'Sam', 'Sachin', 'Desmond', 'Kapil'],
        ['Krish', 'Brad', 'Walter', 'Jennifer','Desmond', 'Harry', 'Nicole', 'Sam']
        ]
    
    all_participants=participants_list[0]+participants_list[1]+participants_list[2]+participants_list[3]+participants_list[4]+participants_list[5]
    
    daily_participants = [i for i in all_participants if all_participants.count(i)==len(participants_list)]
    print("Daily participants: " ,list(set(daily_participants)))

    one_time_participants = [i for i in all_participants if all_participants.count(i)<2]
    print("One time participants: " ,one_time_participants)

    first_day_participants = [i for i in all_participants if all_participants.count(i)<2 and i in participants_list[0]]
    print("first day participants: " ,first_day_participants)
comm_list()
