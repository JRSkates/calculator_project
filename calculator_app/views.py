from django.shortcuts import render
from django.http import JsonResponse
from .calculator import Calculator

def home(request):
  return render(request, 'calculator.app/home.html')

def calculator(request):
  expression = request.GET.get('expression', '')
  calc = Calculator()

  try:
    result = eval(expression, {}, {'calc': calc})
    calc.result = result
  except Exception as e:
    result = f"Error: {str(e)}"

  return JsonResponse({'result': result})

# Create your views here.
