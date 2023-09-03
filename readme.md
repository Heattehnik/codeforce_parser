# Парсер задач с Codeforce

При создании приложения использовались следующие технологии.

![](https://img.shields.io/badge/Code-Python-informational?style=flat&logo=python&logoColor=white&color=green) 
![](https://img.shields.io/badge/framework-Django-informational?style=flat&logo=django&logoColor=white&color=green)
![](https://img.shields.io/badge/database-Postgresql-informational?style=flat&logo=postgresql&logoColor=white&color=green)
![](https://img.shields.io/badge/Cache-Redis-informational?style=flat&logo=redis&logoColor=white&color=green)
![](https://img.shields.io/badge/Tasks-Celery-informational?style=flat&logo=celery&logoColor=white&color=green)
![](https://img.shields.io/badge/Bot-PyTelegramBotAPI-informational?style=flat&logo=telegram&logoColor=white&color=green)



## Описание

Приложение через API Codeforce c помощью библиотеки requests забирает и сохраняет в базу данных задачи.

## Начало работы

Перед началом работы убедитесь что у вас установлен Python и Redis

```
Пример:
- Python 3.6+
- Redis
```

### Установка

```Bash
Пример:
1. Склонируйте репозиторий: `git clone https://github.com/Heattehnik/codeforce_parser.git`
2. Перейдите в директорию проекта.
3. Установите зависимости: `pip install -r requirements.txt`
4. Создайте файл `.env` и заполните его данными из `.env_sample`.
```
### Запуск

```Bash
Пример:
1. Запустите сервер: `python manage.py runserver`
2. Откройте веб-браузер и перейдите по адресу: http://localhost:8000/
3. Для запуска бота используйте команду python manage.py bot
```

## Использование

Перед использованием необходимо добавить в базу данных расписание для работы celery-beat

```Bash
Для запуска используйте команду:
python manage.py loaddata celery_fixture.json
```

Для того чтобы периодические задачи срабатывали не забудьте запустить worker и celery beat

```Bash
celery -A config worker
```

```Bash
celery -A config beat -l INFO --scheduler django_celery_beat.schedulers:DatabaseScheduler
```

## Взаимодействие с ботом

Перед началом работы необходимо отправить боту команду /start.

Затем для получения списка задач нужно использовать команду /go или /welcome и следовать инструкциям бота.
