import requests
import json
from pprint import pprint

def discriminant(a, b, c):
    
    D = b**2 - 4*a*c
    return D
    

def solution(a, b , c ):
    disk = discriminant(a,b,c)
    if disk > 0:
        x1 = (-b + disk**0.5)/2*a
        x2 = (-b-disk**0.5)/2*a
        return(f"{x1} {x2}")
    elif disk == 0:
        x1 = -b/(2*a)
        return(f"{x1}")
    else:
        return("корней нет")
    
courses = ["Python-разработчик с нуля", "Java-разработчик с нуля", "Fullstack-разработчик на Python", "Frontend-разработчик с нуля"]

mentors = [
	["Евгений Шмаргунов", "Олег Булыгин", "Дмитрий Демидов", "Кирилл Табельский", "Александр Ульянцев", "Александр Бардин", "Александр Иванов", "Антон Солонилин", "Максим Филипенко", "Елена Никитина", "Азамат Искаков", "Роман Гордиенко"],
	["Филипп Воронов", "Анна Юшина", "Иван Бочаров", "Анатолий Корсаков", "Юрий Пеньков", "Илья Сухачев", "Иван Маркитан", "Ринат Бибиков", "Вадим Ерошевичев", "Тимур Сейсембаев", "Максим Батырев", "Никита Шумский", "Алексей Степанов", "Денис Коротков", "Антон Глушков", "Сергей Индюков", "Максим Воронцов", "Евгений Грязнов", "Константин Виролайнен", "Сергей Сердюк", "Павел Дерендяев"],
	["Евгений Шмаргунов", "Олег Булыгин", "Александр Бардин", "Александр Иванов", "Кирилл Табельский", "Александр Ульянцев", "Роман Гордиенко", "Адилет Асканжоев", "Александр Шлейко", "Алена Батицкая", "Денис Ежков", "Владимир Чебукин", "Эдгар Нуруллин", "Евгений Шек", "Максим Филипенко", "Елена Никитина"],
	["Владимир Чебукин", "Эдгар Нуруллин", "Евгений Шек", "Валерий Хаслер", "Татьяна Тен", "Александр Фитискин", "Александр Шлейко", "Алена Батицкая", "Александр Беспоясов", "Денис Ежков", "Николай Лопин", "Михаил Ларченко"]
]

def get_mentors(mentors):
    all_list = []
    for m in mentors:
        all_list+=m

    all_names_list = []
    for mentor in all_list:
        name = mentor.split()[0]
        all_names_list.append(name)
        

    unique_names = set(all_names_list)


    all_names_sorted = sorted(unique_names)

    all_names_s= ", ".join(all_names_sorted)

    return f'Уникальные имена преподавателей: {all_names_s}'




courses = ["Java-разработчик с нуля", "Fullstack-разработчик на Python", "Python-разработчик с нуля", "Frontend-разработчик с нуля"]
mentors = [
	["Филипп Воронов", "Анна Юшина", "Иван Бочаров", "Анатолий Корсаков", "Юрий Пеньков", "Илья Сухачев", "Иван Маркитан", "Ринат Бибиков", "Вадим Ерошевичев", "Тимур Сейсембаев", "Максим Батырев", "Никита Шумский", "Алексей Степанов", "Денис Коротков", "Антон Глушков", "Сергей Индюков", "Максим Воронцов", "Евгений Грязнов", "Константин Виролайнен", "Сергей Сердюк", "Павел Дерендяев"],
	["Евгений Шмаргунов", "Олег Булыгин", "Александр Бардин", "Александр Иванов", "Кирилл Табельский", "Александр Ульянцев", "Роман Гордиенко", "Адилет Асканжоев", "Александр Шлейко", "Алена Батицкая", "Денис Ежков", "Владимир Чебукин", "Эдгар Нуруллин", "Евгений Шек", "Максим Филипенко", "Елена Никитина"],
	["Евгений Шмаргунов", "Олег Булыгин", "Дмитрий Демидов", "Кирилл Табельский", "Александр Ульянцев", "Александр Бардин", "Александр Иванов", "Антон Солонилин", "Максим Филипенко", "Елена Никитина", "Азамат Искаков", "Роман Гордиенко"],
	["Владимир Чебукин", "Эдгар Нуруллин", "Евгений Шек", "Валерий Хаслер", "Татьяна Тен", "Александр Фитискин", "Александр Шлейко", "Алена Батицкая", "Александр Беспоясов", "Денис Ежков", "Николай Лопин", "Михаил Ларченко"]
]
durations = [14, 20, 12, 20]
def get_time_mentors(courses, mentors, durations):
    courses_list = []
    for course, mentor, duration in zip(courses, mentors, durations):
        course_dict = {"title":course, "mentors":mentor, "duration":duration}
        courses_list.append(course_dict)


    durations_dict = {}

    for id, _ in enumerate(courses_list):
        key = courses_list[id]["duration"]
        if key not in durations_dict:
            durations_dict[key] = [id]
        if id not in durations_dict[key]:
            durations_dict[key].append(id)


    durations_dict = dict(sorted(durations_dict.items()))


    for keys, indec in durations_dict.items():
        for ind in indec:
            return f'{courses_list[ind]["title"]} - {keys} месяцев'
        
with open("private/token.txt", "r") as f: 
    token_yan = f.read()
        
class YaUploader:

    url = "https://cloud-api.yandex.net/v1/disk/"

    def __init__(self, token: str):
        self.token = token
        
    def common_headers(self):
        return {
            "Authorization": "OAuth "+ self.token
        }
    def _build_url(self,api_method):
        return f"{self.url}{api_method}"
    def create_folder(self):
        params = {"path":f"/1"}
        response = requests.put(self._build_url("resources"), headers=self.common_headers(), params=params)
    def get_spisok_files(self):
        response = requests.get(self._build_url("resources"), headers = self.common_headers(), params = {"path":f"/"})
        return response.json()





       