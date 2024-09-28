from django.shortcuts import render
from django.http import HttpResponse
import os
from google.cloud import dialogflow
from django.conf import settings

os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = os.path.join(
    settings.BASE_DIR, r"E:\exam\faq-cvba-c8c20ac74326.json"
)


def index(request):
    return render(request, "bot/index.html")


def detect_intent_texts(project_id, session_id, text, language_code):
    session_client = dialogflow.SessionsClient()
    session = session_client.session_path(project_id, session_id)
    text_input = dialogflow.TextInput(text=text, language_code=language_code)
    query_input = dialogflow.QueryInput(text=text_input)
    response = session_client.detect_intent(session=session, query_input=query_input)
    return response.query_result.fulfillment_text


def get_response(request):
    userMessage = request.GET.get("usertext")
    project_id = "faq-cvba"
    session_id = "unique"
    language_code = "en"
    bot_response = detect_intent_texts(
        project_id, session_id, userMessage, language_code
    )
    return HttpResponse(bot_response)
