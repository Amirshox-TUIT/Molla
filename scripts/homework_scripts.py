from django.db.models import Count, Avg, F, Q
from django.utils.timezone import now
from apps.blogs.models import Course, Student, Instructor, Section, Enrollment, ExamResult


def homework1_get_courses_without_enrollments():
    """Hech bir sectionida yozilish bo‘lmagan fanlarni qaytaradi"""
    return Course.objects.annotate(
        enroll_count=Count("sections__enrollments")
    ).filter(enroll_count=0)


def homework2_get_students_not_enrolled_in_term(term_id):
    """Berilgan termda umuman yozilmagan talabalarni qaytaradi"""
    return Student.objects.exclude(
        enrollments__section__term_id=term_id
    )


def homework3_get_instructors_with_full_sections(term_id):
    """Berilgan termda to‘liq to‘lgan sectionlari bor o‘qituvchilarni qaytaradi"""
    return Instructor.objects.filter(
        sections__term_id=term_id
    ).annotate(
        enrolled_count=Count("sections__enrollments")
    ).filter(enrolled_count=F("sections__capacity")).distinct()


def homework4_get_overbooked_sections(term_id):
    """Capacity dan ortiq yozilgan sectionlarni topadi"""
    return Section.objects.filter(term_id=term_id).annotate(
        enrolled_count=Count("enrollments")
    ).filter(enrolled_count__gt=F("capacity"))


def homework5_get_top_students_in_course(course_code, term_id, limit=5):
    """Kurs bo‘yicha eng yuqori o‘rtacha imtihon balliga ega talabalarni qaytaradi"""
    return Student.objects.filter(
        exam_results__exam__section__course__code=course_code,
        exam_results__exam__section__term_id=term_id
    ).annotate(
        avg_score=Avg("exam_results__score")
    ).order_by("-avg_score")[:limit]


def homework6_get_all_active_students():
    """Faol (is_active=True) talabalarni qaytaradi"""
    return Student.objects.filter(is_active=True)


def homework7_get_courses_in_department(department_id):
    """Berilgan kafedradagi fanlarni qaytaradi"""
    return Course.objects.filter(department_id=department_id)


def homework8_get_instructors_in_department(department_name):
    """Berilgan kafedradagi o‘qituvchilarni qaytaradi"""
    return Instructor.objects.filter(department__name=department_name)


def homework9_get_students_by_year(year):
    """Berilgan kurs (year_of_study) dagi talabalarni qaytaradi"""
    return Student.objects.filter(year_of_study=year)


def homework10_get_sections_for_course(course_code):
    """Berilgan kursga tegishli barcha sectionlarni qaytaradi"""
    return Section.objects.filter(course__code=course_code)


def homework11_get_students_born_this_year():
    """Hozirgi yilda tug‘ilgan talabalarni qaytaradi"""
    return Student.objects.filter(birth_date__year=now().year)


def homework12_get_courses_taught_by_instructor(instructor_id):
    """Berilgan instructor tomonidan o‘tiladigan fanlarni qaytaradi"""
    return Course.objects.filter(
        sections__instructor_id=instructor_id
    ).distinct()


def homework13_get_courses_without_prerequisites():
    """Hech qanday prerequisite talab qilmaydigan fanlarni qaytaradi"""
    return Course.objects.exclude(prereqs_for__isnull=False)


def homework14_get_enrollments_of_student(student_id):
    """Berilgan talabaning barcha yozilishlarini qaytaradi"""
    return Enrollment.objects.filter(student_id=student_id)


def homework15_get_exam_results_of_student(student_id):
    """Berilgan talabaning barcha imtihon natijalarini qaytaradi"""
    return ExamResult.objects.filter(student_id=student_id)
