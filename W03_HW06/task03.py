# Task 3: Создать класс IT компании, который будет хранить в себе
#         сотрудников-разработчиков из задания 1.
#
#         У класса должны быть методы чтобы добавлять новых сотрудников
#         и просматривать их список.
#
#         Список разработчиков должен выводиться в читабельной форме, и
#         отсортирован по возрастанию опыта сотрудника в виде
#         '{name} - {years_experience} years, {language}'
#
#         3.1* Добавить возможность увольнять разработчика из компании,
#         после увольнения он не должен отображаться в списке (Пусть ключем
#         для увольнения будет имя сотрудника, если ключей несколько - удаляйте
#         одного из, если ключа нет, то вывести текст, что сотрудник с
#         таким именем не найден)
#
#         3.2*. Добавить ограничение по опыту для сотрудников, если опыт работы
#         сотрудника меньше 3 лет, то при добавлении его в компанию выводить сообщение
#         о том, что его опыта не достаточно.

import task01 as dev


class ITCompany:

    employees = []

    def list_employees(self):
        return sorted(self.employees, key=lambda developer: developer.years_experience)

    def add_employee(self, new_employee: dev.Developer):
        if new_employee.years_experience < 3:
            print('Not enough experience')
        else:
            self.employees.append(new_employee)

    def fire_employee(self, name: str):
        for emp in self.employees:
            if emp.name == name:
                self.employees.remove(emp)
                return "Employee {name} is fired".format(name=name)
        return "Employee {name} not found".format(name=name)
