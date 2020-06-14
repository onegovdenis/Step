from exceptions import *


class Atm(object):
    __atm_balance = 10000
    __attempts = 2
    __client_can_get_money = False

    def rise_money(self, rise_money):
        """Method to add some money to the ATM"""
        return self.__atm_balance + rise_money

    def enter_pin(self, pin):
        """Method to check pin"""
        correct_pin = 777

        if self.__attempts == 0:
            raise AttemptsOver("Attempts are over!!!")

        if pin != correct_pin:
            self.__attempts = self.__attempts - 1
            raise IncorrectPin("Incorrect Pin!!!")

        if correct_pin == pin:
            self.__client_can_get_money = True
            return True

    def get_money(self, money):
        """Method to get some money for sweets from the ATM"""
        if self.__client_can_get_money:
            if money <= self.__atm_balance:
                self.__atm_balance = self.__atm_balance - money
                return money
            else:
                raise AtmBalance("Atm balance is no enough!!!")
        raise EnterPin("Enter pin first!!!")

    def check_balance(self):
        """Method to check ATM balance"""
        if self.__client_can_get_money:
            return self.__atm_balance

        raise EnterPin("Enter pin first!!!")
