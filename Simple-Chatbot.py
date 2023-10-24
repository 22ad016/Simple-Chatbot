import random
import webbrowser
import wikipedia
from datetime import datetime


def greet_user(user_input):
    user_greetings = ["hi", "hello", "hey"]
    responses = ["Hello, how can I assist you today?", "Hi there, what can I do for you?"]
    if user_input.lower() in user_greetings:
        return random.choice(responses)


def get_weather_response():
    responses = ["The weather is great today.", "It's rainy outside.", "It's sunny outside"]
    return random.choice(responses)


def open_google():
    webbrowser.open("https://www.google.com")
    return

def open_youtube():
    webbrowser.open("https://www.youtube.com")
    return


def get_time_and_date_response():
    current_time = datetime.now().strftime("%H:%M:%S")
    current_date = datetime.now().strftime("%Y-%m-%d")
    return f"Chatbot: Today's date is {current_date} and the time is {current_time}"


def respond_to_user(user_input):
    query = user_input.lower()
    if "who are you" in query or "name" in query:
        print("Chatbot: I am 'The Simple CHATBOT'. I am here to assist you.")
        return
    elif "weather" in query:
        print(get_weather_response() + " I am not sure.")
        return
    elif "google" in query:
        print("Chatbot: Opening Google search engine...")
        return open_google()
    elif "youtube" in query:
        print("Chatbot: Opening Youtube...")
        return open_youtube()
    elif "time" in query or "date" in query:
        print(get_time_and_date_response())
        return
    else:
        return None

def main():
    while True:
        user_input = input("User: ").lower()
        exit_keywords = ["bye", "exit", "finish"]

        if user_input in exit_keywords:
            print("Chatbot: Goodbye")
            break
        elif user_input in ["hi", "hello", "hey"]:
            print("Chatbot:", greet_user(user_input))
        elif user_input.startswith("tell me about") or user_input.startswith("what is"):
            query = user_input[len("tell me about "):].strip()
            try:
                summary = wikipedia.summary(query, sentences=2)
                print(summary)
            except wikipedia.exceptions.DisambiguationError:
                print("I found multiple results. Please be more specific.")
            except (wikipedia.exceptions.PageError, wikipedia.exceptions.WikipediaException):
                print("I couldn't find any information on that topic.")
        else:
            response = respond_to_user(user_input)

if __name__ == "__main__":
    main()
