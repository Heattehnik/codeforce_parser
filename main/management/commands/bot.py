from django.core.management import BaseCommand
from telebot import TeleBot
from dotenv import load_dotenv
from main.models import Theme, Problem
import os

load_dotenv()

bot = TeleBot(os.getenv('BOT_TOKEN'))


class Command(BaseCommand):
    help = 'Telegram бот'

    def handle(self, *args, **kwargs):

        @bot.message_handler(commands=['welcome', 'go'])
        def main(message):
            theme_list = Theme.objects.all()
            bot.send_message(message.chat.id, 'Добрый день! Выберите тему. И напишите её мне.')
            for theme in theme_list:
                bot.send_message(message.chat.id, theme)
            bot.register_next_step_handler(message, get_difficulty)

        def get_difficulty(message):
            problems_set = Problem.objects.filter(theme__theme=message.text)
            bot.send_message(message.chat.id, 'Выберите сложность!')
            bot.register_next_step_handler(message, get_problems, problems_set)

        def get_problems(message, problems_set):
            filtered_problems = problems_set.filter(difficulty=message.text)[:10]
            for problem in filtered_problems:
                bot.send_message(message.chat.id,
                                 f'{problem.title}\n '
                                 f'https://codeforces.com/problemset/problem/{problem.contest_id}/{problem.index}')

        bot.polling()
