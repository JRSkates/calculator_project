from django.shortcuts import render, HttpResponse
from django.http import JsonResponse, HttpResponseBadRequest
from .calculator import Calculator
import json

def home(request):
  return render(request, 'calculator_app/home.html')

def calculate(request):
    if request.method == 'POST':
        try:
            raw_data = request.body.decode('utf-8')
            data = json.loads(raw_data)

            expression = data.get('display', '')
            func = data['func']
            numeric_inputs = data.get('numeric_inputs', [])

            calculator = Calculator()
            print(f"Received request: func={func}, numeric_inputs={numeric_inputs}")

            # Ensure that 'numeric_inputs' is passed to the Calculator functions
            if func in ['add', 'subtract', 'multiply', 'divide', 'calculate_expression',
                        'raise_to_power_of', 'remainder', 'ln', 'log']:
                result = getattr(calculator, func)(*map(float, numeric_inputs))
            elif func in ['pi', 'e']:
                # For functions that don't take multiple numeric inputs
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

# def calculate(request):
#     if request.method == 'POST':
#         expression = request.POST.get('display', '')
#         func = request.POST.get('func', '')
#         numeric_inputs = request.POST.getlist('numeric_inputs[]', [])
        
#         # Handle non-numeric inputs
#         # try:
#         #     numeric_inputs = [float(num) for num in expression.split()]
#         # except ValueError:
#         #     return JsonResponse({'error': 'Invalid input. Please enter numeric values.'}, status=400)

#         calculator = Calculator()

#         try:
#             # Perform calculations based on the function provided
#             if func == 'calculate_expression':
#                 result = calculator.calculate_expression(expression)
#             elif func == 'square_root':
#                 result = calculator.square_root(*numeric_inputs)
#             elif func == 'sin':
#                 result = calculator.sin(*numeric_inputs)
#             elif func == 'cos':
#                 result = calculator.cos(*numeric_inputs)
#             elif func == 'tan':
#                 result = calculator.tan(*numeric_inputs)
#             elif func == 'raise_to_power_of':
#                 result = calculator.raise_to_power_of(*numeric_inputs)
#             elif func == 'remainder':
#                 result = calculator.remainder(*numeric_inputs)
#             elif func == 'factorial':
#                 result = calculator.factorial(*numeric_inputs)
#             elif func == 'ln':
#                 result = calculator.ln(*numeric_inputs)
#             elif func == 'log':
#                 result = calculator.log(*numeric_inputs)
#             elif func == 'pi':
#                 result = calculator.pi()
#             elif func == 'e':
#                 result = calculator.e()
#             else:
#                 return JsonResponse({'error': 'Invalid function provided.'}, status=400)

#         except ValueError as ve:
#           return JsonResponse({'error': str(ve)}, status=400)
#         except ZeroDivisionError:
#           return JsonResponse({'error': 'Division by zero is not allowed.'}, status=400)
#         except Exception as e:
#             return JsonResponse({'error': str(e)}, status=400)

#         return JsonResponse({'result': result})
#     else:
#         return JsonResponse({'error': 'Invalid request method.'}, status=405)
#     #return HttpResponseBadRequest("Invalid request method")

# Create your views here.
