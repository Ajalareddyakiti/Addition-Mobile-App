from rest_framework.decorators import api_view
from rest_framework.response import Response

@api_view(['GET', 'POST'])  # Accepts both GET and POST requests
def add_numbers(request):
    if request.method == 'GET':
        return Response({"message": "Send a POST request with num1 and num2."}, status=200)

    if request.method == 'POST':
        num1 = request.data.get('num1')
        num2 = request.data.get('num2')

        if num1 is None or num2 is None:
            return Response({"error": "Both numbers are required"}, status=400)

        try:
            sum_result = float(num1) + float(num2)
            return Response({"sum": sum_result})
        except ValueError:
            return Response({"error": "Invalid number format"}, status=400)
