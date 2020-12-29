import json
from pupil import Pupil


class Pupils:
    def __init__(self):
        try:
            with open("pupils.json") as f:
                pupils_list = json.load(f)
            self.pupils = []
            for pupils_dict in pupils_list:
                p = Pupil()
                p.from_dict(pupils_dict)
                self.pupils += [p]
        except FileNotFoundError:
            self.pupils = []

    def __str__(self):
        st = ""
        for pupil in self.pupils:
            st += "\n" + "=" * 20
            st += str(pupil)
        return st

    def save_pupils_data(self):
        list_to_write = []
        for pupil in self.pupils:
            list_to_write += [pupil.to_dict()]
        with open("pupils.json", "w") as f:
            json.dump(list_to_write, f)

    def next_id(self):
        if not self.pupils:
            return 1001
        else:
            ids = []
            for p in self.pupils:
                ids.append(p.pupil_id)
            return max(ids) + 1

    def create_pupil(self):
        first_name = input("Type Pupil's Name: ")
        last_name = input("Type Pupil's Lastname: ")
        fathers_name = input("Type Pupil's Father's Name: ")
        for pupil in self.pupils:
            if first_name == pupil.first_name and last_name == pupil.last_name and fathers_name == pupil.last_name:
                print("this pupil already exists")
                ch = input("Do you want to continue? (y-yes, n-no): ")
                if ch == "n":
                    return None
        age = int(input("Type the pupils age: "))
        class_name = input("Type the class name: ")
        id_card = input("does the pupil have an id card? (y-yes, n-no): ")
        if id_card == "y":
            id_number = input("Type pupil's id number: ")
        else:
            id_number = None
        pupil = Pupil(first_name, last_name, first_name, age, class_name, id_number, self.next_id())

        self.pupils.append(pupil)
        return pupil

    def search_pupil_by_id(self, pupil_id):
        for pupil in self.pupils:
            if pupil_id == pupil.pupil_id:
                return pupil
        return None

    def search_pupil_by_surname(self, last_name):
        match_pupils = []
        for pupil in self.pupils:
            if last_name == pupil.last_name:
                match_pupils.append(pupil)
        return match_pupils

    def pupil_update(self, pupil):
        print(pupil)
        print("=" * 15)
        print("1-name")
        print("2-surname")
        print("3-father's name")
        print("4-age")
        print("5-class")
        print("6-id number")
        print("=" * 15)
        update_choice = int(input("Pick something to update: "))
        if update_choice == 1:
            pupil.first_name = input("Give new name: ")
        elif update_choice == 2:
            pupil.last_name = input("Give new surname: ")
        elif update_choice == 3:
            pupil.fathers_name = input("Give new father's name: ")
        elif update_choice == 4:
            pupil.age = input("Give new age: ")
        elif update_choice == 5:
            pupil.class_name = input("Give new class: ")
        elif update_choice == 6:
            pupil.id_number = input("Give new id number: ")

        print("=" * 15)
        print(pupil)
        print("Pupil updated! ")

    def delete_pupil_by_id(self, pupil_id, lessons):
        for i in range(len(self.pupils)):
            if pupil_id == self.pupils[i].pupil_id:
                self.pupils.pop(i)
                for lesson in lessons.lessons:
                    if pupil_id == lesson.pupil_ids:
                        lesson.pupil_ids.remove(pupil_id)

                print("Pupil deleted!")
                return
        else:
            print("No pupil with this id!")

    def print_pupils_names(self):
        for pupil in self.pupils:
            print(f"{pupil.first_name} {pupil.fathers_name[0]}. {pupil.last_name}")
