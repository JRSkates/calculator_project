from django.shortcuts import render, HttpResponse
from django.http import JsonResponse, HttpResponseBadRequest
from .calculator import Calculator
import json

def home(request):
  return render(request, 'calculator_app/home.html')

def calculate(request):
    if request.method == 'POST':
        expression = request.POST.get('expression', '')
        func = request.POST.get('func', '')

        calculator = Calculator()
        print(f"Received request: expression={expression}, func={func}")

        try:
            if func in ['add', 'subtract', 'multiply', 'divide', 'calculate_expression',
                        'raise_to_power_of', 'remainder', 'ln', 'log']:
                result = getattr(calculator, func)(*map(float, expression.split()))
            elif func in ['pi', 'e']:
                result = getattr(calculator, func)()
            else:
                return JsonResponse({'error': 'Invalid function provided.'}, status=400)

            print(f"Calculation result: {result}")
            return JsonResponse({'result': result})

        except ValueError as ve:
            return JsonResponse({'error': str(ve)}, status=400)
        except ZeroDivisionError:
            return JsonResponse({'error': 'Division by zero is not allowed.'}, status=400)
        except Exception as e:
            return JsonResponse({'error': str(e)}, status=400)

    else:
        return JsonResponse({'error': 'Invalid request method.'}, status=405)
