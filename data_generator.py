#!/usr/bin/python3

from faker import Faker

class RandomDataGenerator:
    def __init__(self):
        """
        Initial paramethers of the data random generator class
        """
        pass

    def __iter__(self):
        """
        Sets up the class as an iterator class, returning itself
        :return:
        """
        pass

    def __next__(self):
        """
        Defines the logic to create new random data of corresponding type
        :return:
        """
        pass

    def _gen_random(self):
        """
        Generates a line of fake data, using this model
        - personal_data: name, sex, address, number, passport, email
        - profesional_data: name,company, company address, company number, job, company email
        - driving_data: name, car license
        - bank_data :passport, Bank, IBAN, Salary
        """
        pass


