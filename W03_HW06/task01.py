# Task 1: Создать базовый класс Developer и 3 класса наследника:
#         PythonDeveloper, JavaDeveloper, RubyDeveloper.
#
#         1.1 В базовый класс Developer поместить свойство числового
#         типа years_experience, строкового типа name и language, а так
#         же методы about, write_code
#
#         Конструктор базового типа обязательно должен принимать name и
#         years_experience сохраняя значения в соответствующие атрибуты
#         класса Developer, значение language для базового класса оставить
#         пустой строкой.
#
#         Метод about должен выполнять проверку опыта работы разработчика,
#         если years_experience <= 3 , выводим текст
#         "My name is {name} and I am a Junior Developer."
#         если years_experience <= 5 , выводим текст
#         "My name is {name} and I am a Middle Developer."
#         а в других случаях выводим
#         "My name is {name} and I am a Senior Developer."
#         {name} - имя разработчика из свойства name
#         метод write_code должен вывести текст "I am a developer and I write code"
#
#         1.2 В классах наследниках переопределить метод write_code, а атрибуту
#         language присвоить название языка Python, Java, Ruby в зависимости от
#         класса. Метод write_code должен выводить текст:
#         "I use {language} to write code".
#
#         1.3 Создать как минимум один экземпляр каждого класса наследника.
#         Вызвать на каждом из них методы about и write_code.
#
#         1.4 Дополнить класс Developer магическим методом, чтобы команда print()
#         выводила их в виде: '{name} - {years_experience} years, {language} '
#
#         1.5 Дополнить класс Developer магическим методом, который бы позволил
#         вызывать объекты как функции и выводил результат функции write_code:
#         developer = PythonDeveloper()
#         developer() выводит на экран то же самое что и write_code, например
#         "I use Python to write code"
#
#         Magic Methods: https://docs.python.org/3/reference/datamodel.html#special-method-names


class Developer:

    language = ''

    def __init__(self, name: str, years_experience: int):
        self.name = name
        self.years_experience = years_experience

    def about(self):
        level = 'Senior'
        if self.years_experience <= 3:
            level = 'Junior'
        elif self.years_experience <= 5:
            level = 'Middle'
        print("My name is {name} and I am a {level} Developer.".format(name=self.name, level=level))

    def write_code(self):
        print("I am a developer and I write code")

    def __str__(self):
        '''1.4. add special method for print()'''
        return "{name} - {years_experience} years, {language}"\
            .format(name=self.name, years_experience=self.years_experience, language=self.language)

    def __call__(self):
        '''1.5. call instance as a function'''
        return self.write_code()


class PythonDeveloper(Developer):

    language = 'Python'

    def write_code(self):
        print("I use {language} to write code".format(language=self.language))


class JavaDeveloper(Developer):

    language = 'Java'

    def write_code(self):
        print("I use {language} to write code".format(language=self.language))


class RubyDeveloper(Developer):

    language = 'Ruby'

    def write_code(self):
        print("I use {language} to write code".format(language=self.language))


# 1.3: create instance of each class and call methods about and write_code for each instance
dev1 = PythonDeveloper('Stive', 15)
dev2 = JavaDeveloper('Alex', 3)
dev3 = RubyDeveloper('Hellen', 6)

dev1.about()
dev1.write_code()

dev2.about()
dev2.write_code()

dev3.about()
dev3.write_code()

# 1.5. call instance as a function
developer = PythonDeveloper('Andy', 6)
developer()