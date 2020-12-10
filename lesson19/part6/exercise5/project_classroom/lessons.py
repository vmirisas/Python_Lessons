import json
from lesson import Lesson


class Lessons:
    def __init__(self):
        try:
            with open("lessons.json") as f:
                lessons_list = json.load(f)

            self.lessons = []
            for lesson_dict in lessons_list:
                l = Lesson()
                l.from_dict(lesson_dict)
                self.lessons += [l]
        except FileNotFoundError:
            self.lessons = []

    def save_lessons_data(self):
        list_to_write = []
        for lesson in self.lessons:
            list_to_write += [lesson.to_dict()]

        with open("lessons.json", "w") as f:
            json.dump(list_to_write, f)

    def next_id(self):
        if not self.lessons:
            return 1001
        else:
            ids = []
            for l in self.lessons:
                ids.append(l.teacher_id)
            return max(ids) + 1

    def create_lesson(self, lesson_name):
        for lesson in self.lessons:
            if lesson.lesson_name == lesson_name:
                print("Error, this lesson already exists")
                return None
        l = Lesson(lesson_name, self.next_id())
        self.lessons.append(l)
        return l

    def read_lesson(self, lesson_id):
        for lesson in self.lessons:
            if lesson_id == lesson.lesson_id:
                return lesson
        else:
            return None

    def update_lesson(self, lesson_id, teachers, pupils):
        for lesson in self.lessons:
            if lesson_id == lesson.lesson_id:
                lesson.print_lesson_details(teachers, pupils)
                choice = int(input("Update 1-name: , 2-teachers: , 3-pupils: "))
                if choice == 1:
                    lesson.lesson_name = input("Type new name: ")
                elif choice == 2:
                    update_teacher_choice = int(input("updating lesson teachers: 1-add, 2-remove: "))
                    if update_teacher_choice == 1:
                        print("Teachers (not in lesson): ")
                        for teacher in teachers.teachers:
                            if teacher.teacher_id not in lesson.teacher_ids:
                                print(f"{teacher.teacher_id}-{teacher.first_name} {teacher.surname}")
                        update_teacher_id = int(input("Type the id you want to add: "))
                        lesson.teacher_ids.append(update_teacher_id)
                    elif update_teacher_choice == 2:
                        print("Lesson Teachers: ")
                        for teacher_id in lesson.teacher_ids:
                            teacher = teachers.read_teacher(teacher_id)
                            print(f"{teacher.teacher_id}-{teacher.first_name} {teacher.surname}")
                        update_teacher_id = int(input("Type the id you want to delete: "))
                        lesson.teacher_ids.remove(update_teacher_id)
                elif choice == 3:
                    update_pupil_choice = int(input("updating lesson pupils: 1-add, 2-remove: "))
                    if update_pupil_choice == 1:
                        print("Pupils not in lesson: ")
                        for pupil in pupils.pupils:
                            if pupil.pupil_id not in lesson.pupil_ids:
                                print(f"{pupil.pupil_id}-{pupil.first_name} {pupil.last_name}")
                        update_pupil_id = int(input("Type the id you want to add: "))
                        lesson.pupil_ids.append(update_pupil_id)
                    elif update_pupil_choice == 2:
                        print("Lesson Pupils: ")
                        for pupil_id in lesson.pupil_ids:
                            pupil = pupils.search_pupil_by_id(pupil_id)
                            print(f"{pupil.pupil_id}-{pupil.first_name} {pupil.last_name}")
                        update_pupil_id = int(input("Type the id you want to delete: "))
                        lesson.pupil_ids.remove(update_pupil_id)
                # return
                break

    def delete_lesson(self, lesson_id):
        for i in range(len(self.lessons)):
            if lesson_id == self.lessons[i].lesson_id:
                self.lessons.pop(i)
                return
        else:
            print("no lesson with this id")
