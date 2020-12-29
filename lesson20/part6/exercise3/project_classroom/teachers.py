import json

from teacher import Teacher


class Teachers:
    def __init__(self):
        try:
            with open("teachers.json") as f:
                teachers_list = json.load(f)
            self.teachers = []
            for teacher_dict in teachers_list:
                t = Teacher()
                t.from_dict(teacher_dict)
                self.teachers += [t]
        except FileNotFoundError:
            self.teachers = []

    def save_teachers_data(self):
        list_to_write = []
        for teacher in self.teachers:
            list_to_write += [teacher.to_dict()]

        with open("teachers.json", "w") as f:
            json.dump(list_to_write, f)

    def next_id(self):
        if not self.teachers:
            return 1001
        else:
            ids = []
            for t in self.teachers:
                ids.append(t.teacher_id)
            return max(ids) + 1

    def create_teacher(self, first_name, surname):
        for teacher in self.teachers:
            if teacher.first_name == first_name and teacher.surname == surname:
                print("Error, this teacher already exists")
                return None
        t = Teacher(first_name, surname, self.next_id())
        self.teachers.append(t)
        return t

    def read_teacher(self, teacher_id):
        for teacher in self.teachers:
            if teacher_id == teacher.teacher_id:
                return teacher
        else:
            return None

    def update_teacher(self, teacher_id):
        for teacher in self.teachers:
            if teacher_id == teacher.teacher_id:
                teacher.print_teacher()
                choice = int(input("Update 1-name: , 2-surname: "))
                if choice == 1:
                    teacher.first_name = input("Type new name: ")
                elif choice == 2:
                    teacher.surname = input("Type new surname: ")
                return

    def delete_teacher(self, teacher_id, lessons):
        for i in range(len(self.teachers)):
            if teacher_id == self.teachers[i].teacher_id:
                self.teachers.pop(i)
                for lesson in lessons.lessons:
                    if teacher_id == lesson.teacher_ids:
                        lesson.teacher_ids.remove(teacher_id)
            else:
                print("no teacher with this id")
