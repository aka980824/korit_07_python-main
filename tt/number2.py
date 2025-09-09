class Student:
    def __init__(self, name, student_id):
        self.name = name
        self.student_id = student_id
        self.grades = {}
    def add_grade(self, subject, score):
        self.grades[subject] = score
    def get_average_grade(self):
        if not self.grades:
            return 0.0
        total = sum(self.grades.values())
        average = total / len(self.grades)
        return average

student1 = Student("테스트", "20250909")

student1.add_grade("수학", 100)
student1.add_grade("영어", 87)
student1.add_grade("과학", 90)

average_score = student1.get_average_grade()

print(f"학생 이름: {student1.name}")
print(f"평균 성적: {average_score:.1f}점")

print(f"{student1.name} 학생의 성적:")
for subject, score in student1.grades.items():
    print(f"- {subject}: {score}점")