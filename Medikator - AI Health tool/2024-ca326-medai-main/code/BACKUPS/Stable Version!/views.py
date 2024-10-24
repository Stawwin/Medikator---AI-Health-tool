from django.shortcuts import render
from django.http import JsonResponse, HttpResponse
from django.views.decorators.csrf import csrf_exempt
from .medbot.medbot import *  # Import functions

# Create your views here.
# views.py

def chat_view(request):
    if request.method == 'POST':
        user_input = request.POST.get('user_input')  # Assuming your user input is sent as a POST parameter
        # Call the modified tree_to_code function with user input
        bot_response = tree_to_code(your_decision_tree_model, your_feature_names, user_input)
        return JsonResponse({'bot_response': bot_response})
    else:
        return render(request, 'chat.html')

def process_user_input(request):
    if request.method == 'POST':
        input_data = request.POST.get('input_data')

        # Save the user input to a list stored in the session
        user_inputs = request.session.get('user_inputs', [])
        user_inputs.append(input_data)
        request.session['user_inputs'] = user_inputs
        bot_response = main1(user_inputs)

        return render(request, 'result_template.html', {'input_data': input_data, 'bot_response': bot_response})
    else:
        return render(request, 'input_form_template.html')
    
# views.py
def display_user_inputs(request):
    user_inputs = request.session.get('user_inputs', [])
    return render(request, 'user_inputs_template.html', {'user_inputs': user_inputs})
