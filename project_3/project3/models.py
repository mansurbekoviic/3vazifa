from django.db import models

class Course(models.Model):
    title = models.CharField(max_length=100, verbose_name = "Kurs nomi")
    description = models.TextField(verbose_name = "Kurs tavsiyasi")
    created_at = models.DateTimeField(auto_now_add = True, verbose_name = "Yaratilgan vaqti")
    updated_at = models.DateTimeField(auto_now = True, verbose_name = "Yangilangan vaqti")

    def __str__(self):
        return self.title
    
class Student(models.Model):
    name = models.CharField(max_length=100, verbose_name = "Ism")
    email = models.EmailField(verbose_name = "Email: ")
    enrolled_at = models.DateTimeField(auto_now_add = True)
    course = models.ForeignKey(Course, on_delete=models.CASCADE, verbose_name = "Kurs")
    
    def __str__(self):
        return self.name


class Comment(models.Model):
    course = models.ForeignKey(Course, on_delete=models.CASCADE, related_name = "comments", verbose_name = "Kurs")
    student = models.ForeignKey(Student, on_delete=models.CASCADE, related_name = "comments", verbose_name = "Talaba")
    comment_text = models.TextField(verbose_name = "Izoh matni")
    created_at = models.DateTimeField(auto_now_add = True, verbose_name = "Izox qoldirilgan vaqt")
    
    def __str__(self):
        return f"{self.student.name} - {self.course.title}"