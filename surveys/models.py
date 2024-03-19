from django.db import models


class Survey(models.Model):
    title = models.CharField(max_length=255)

    def __str__(self):
        return self.title


class Question(models.Model):
    text = models.TextField()
    survey = models.ForeignKey(Survey, on_delete=models.CASCADE)

    def __str__(self):
        return self.text


class Answer(models.Model):
    text = models.CharField(max_length=255)
    question = models.ForeignKey(Question, on_delete=models.CASCADE)

    def __str__(self):
        return self.text


class Link(models.Model):
    from_question = models.ForeignKey(Question, related_name='from_question', on_delete=models.CASCADE)
    to_question = models.ForeignKey(Question, related_name='to_question', on_delete=models.CASCADE)
    answer = models.ForeignKey(Answer, related_name='answer', blank=True, null=True, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.from_question} -> {self.to_question} -> {self.answer}'
