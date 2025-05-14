from django.shortcuts import render, redirect
from .models import Question, Choice
from django.contrib import messages

# Create your views here.
def edgenosquiz_view(request):
  questions = Question.objects.all()
  if request.method == 'POST':
        score = 0
        total = questions.count()
        for question in questions:
            selected_choice_id = request.POST.get(f'question_{question.id}')
            if selected_choice_id:
                choice = Choice.objects.get(id=selected_choice_id)
                if choice.is_correct:
                    score += 1
        percentage = (score / total) * 100
        if percentage >= 80:
            feedback = "Excellent! You have a strong understanding of the Layeredge ecosystem."
        elif percentage >= 50:
            feedback = "Good job! You know the Layeredge ecosystem fairly well, but there's room to learn more."
        else:
            feedback = "You might want to explore the Layeredge documents further to deepen your knowledge."
        return render(request, 'quiz/result.html', {
            'score': score,
            'total': total,
            'percentage': percentage,
            'feedback': feedback
        })
  return render(request, 'quiz/quiz.html', {'questions': questions})
