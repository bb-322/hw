import random

class CoachError(Exception):
    def __str__(self):
        return 'No such coach'

class Gym:
    def __init__(self, **kwargs):
        for key, value in kwargs.items():
            setattr(self, key, value)
    
    def show_sports(self):
        return f"\nSports:\n" + "\n".join(self.Sports)
    
    def show_coaches(self):
        result = ['\nCoaches:']
        for coach, sport in coaches_dict.items():
            result.append(f"\t{coach}: {sport}")
        return '\n'.join(result)
    
    def show_schedule(self):
        result = ["\nSchedule:"]
        for day, sports in self.Week.items():
            result.append(f"\t{day}:")
            for sport, time in sports.items():
                result.append(f"\t\t{sport}: {time}")
        return "\n".join(result)


sports_list = [
    'Basketball', 
    'Volleyball', 
    'Table Tennis', 
    'Badminton', 
    'Boxing', 
    'Wrestling', 
    'MMA', 
    'Powerlifting', 
    'Bodybuilding', 
    'CrossFit'
    ]

coaches_list = [
    'Alexander Reid',
    'Benjamin Clarke',
    'Nathan Scott',
    'Samuel Turner',
    'Jonathan Hayes',
    'Lucas Morgan',
    'Christopher Allen',
    'Daniel Brooks',
    'James Foster',
    'Michael Quinn',
    'William Hart',
    'Andrew Blake',
    'Ryan Cooper',
    'Emily Vaughn',
    'Olivia Grant',
]

schedule_dict = {
    'Week': {
        'Monday': {
            'Volleyball': '8:30 AM',
            'MMA': '11:00 AM',
            'Crossfit': '5 PM'
            },
        'Tuesday': {
            'Basketball': '9:00 AM',
            'Boxing': '3:00 PM',
            'Powerlifting': '6:30 PM'
            },
        'Wednesday': {
            'Table Tennis': '7:30 AM',
            'Wrestling': '12:00 PM',
            'Badminton': '4:00 PM'
            },
        'Thursday': {
            'Bodybuilding': '10:00 AM',
            'Boxing': '1:30 PM',
            'Volleyball': '7:00 PM'
            },
        'Friday': {
            'Powerlifting': '8:00 AM',
            'Basketball': '2:00 PM',
            'MMA': '6:00 PM'
            },
        'Saturday': {
            'Table Tennis': '9:00 AM',
            'CrossFit': '11:00 AM',
            'Badminton': '3:00 PM'
            }
    }
}
schedule = Gym(**schedule_dict)

sports_dict = {
    'Sports': sports_list
    }
sports = Gym(**sports_dict)

coaches_dict = {}
for coach in coaches_list:
    coaches_dict[coach] = random.choice(sports_list)


coaches = Gym(**coaches_dict)

while True:
    menu = int(input("\nMenu:\n1 - sports list\n2 - coaches\n3 - workouts schedule\n4 - price per 1 workout\n5 - find coach\n"))
    match menu:
        case 1:
            print(sports.show_sports())
        
        case 2:
            print(coaches.show_coaches())

        case 3:
            print(schedule.show_schedule())
        
        case 4:
            print('\n')
            for item in coaches_list:
                print(f'{item}: {random.randint(20, 50)}$')
        
        case 5:
            user_coach = input('Which coach are you looking for: ')
            if user_coach in coaches_list:
                print(f"{user_coach}'s sport(s):\n{coaches_dict[user_coach]}")
            else:
                raise CoachError