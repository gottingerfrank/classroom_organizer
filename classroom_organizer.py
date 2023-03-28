from roster import student_roster
import itertools


# Import modules above this line
class ClassroomOrganizer:
    def __init__(self):
        self.sorted_names = self._sort_alphabetically(student_roster)
        self.number_of_students = len(self.sorted_names)
        self.index = 0

    def _sort_alphabetically(self, students):
        names = []
        for student_info in students:
            name = student_info['name']
            names.append(name)
        return sorted(names)

    def get_students_with_subject(self, subject):
        selected_students = []
        for student in student_roster:
            if student['favorite_subject'] == subject:
                selected_students.append((student['name'], subject))
        return selected_students

    def __iter__(self):
        return self

    def __next__(self):
        if self.index < self.number_of_students:
            current_name = self.sorted_names[self.index]
            self.index += 1
            return current_name
        else:
            raise StopIteration

    def get_combinations(self):
        combinations = itertools.combinations(self.sorted_names, 2)
        return combinations
