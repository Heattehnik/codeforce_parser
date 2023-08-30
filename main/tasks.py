from celery import shared_task
from main.models import Problem
from main.services import get_problems, problems_to_db, get_themes, themes_to_db
from dotenv import load_dotenv
import os
import telebot

load_dotenv()


# @shared_task
# def habits_notification(object_pk):
#     print('start notification')
#     habit = Habit.objects.get(pk=object_pk)
#     bot = telebot.TeleBot(os.getenv('BOT_TOKEN'))
#     place = Place.objects.get(pk=habit.place_id)
#     message = (f'Трекер привычек напоминает: требуется совершить '
#                f'{habit.action} в {habit.time} в {place}')
#     bot.send_message(habit.user.chat_id, message)
#     print('Success')

@shared_task
def create_problems():
    problems = get_problems()
    problems_to_db(problems)


@shared_task
def create_themes():
    themes = get_themes()
    themes_to_db(themes)
