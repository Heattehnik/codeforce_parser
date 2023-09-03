import requests

from main.models import Problem, Theme


def get_problems():
    url = 'https://codeforces.com/api/problemset.problems'
    response = requests.get(url)
    problems = response.json()
    list_of_problems = []

    for i in range(len(problems['result']['problems'])):
        result_dict = {
            'contest_id': problems['result']['problems'][i]['contestId'],
            'index': problems['result']['problems'][i]['index'],
            'title': problems['result']['problems'][i]['name'],
            'type': problems['result']['problems'][i]['type'],
            'rating': problems['result']['problems'][i].get('rating'),
            'tags': problems['result']['problems'][i]['tags'],
            'solvedCount': problems['result']['problemStatistics'][i]['solvedCount']
        }
        list_of_problems.append(result_dict)

    return list_of_problems


def problems_to_db(args):
    for problem in args:
        new_tags = Theme.objects.filter(theme__in=problem.get('tags')) # Новые значения тегов
        if not Problem.objects.filter(
                contest_id=problem.get('contest_id'),
                index=problem.get('index')
                ).exists():
            create_ = Problem.objects.create(
                        contest_id=problem.get('contest_id'),
                        index=problem.get('index'),
                        title=problem.get('title'),
                        difficulty=problem.get('rating'),
                        solve_count=problem.get('solvedCount')
                        )

            create_.theme.set(new_tags)  # Используйте метод set() для установки новых значений
            create_.save()


def get_themes():
    url = 'https://codeforces.com/api/problemset.problems'
    response = requests.get(url)
    problems = response.json()
    list_of_themes = []
    for i in range(len(problems['result']['problems'])):
        list_of_themes.extend(problems['result']['problems'][i]['tags'])
    set_of_themes = set(list_of_themes)
    return list(set_of_themes)


def themes_to_db(args):
    for theme in args:
        create_ = Theme.objects.create(theme=theme)
        create_.save()


if __name__ == '__main__':
    print(get_themes())

