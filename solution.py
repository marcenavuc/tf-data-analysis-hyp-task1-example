import pandas as pd
import numpy as np


chat_id = 351730666 # Ваш chat ID, не меняйте название переменной


def solution(x_success: int,
             x_cnt: int, 
             y_success: int, 
             y_cnt: int) -> bool:
    """
    x_success - кол-во продаж в контрольной выборке
    x_cnt - кол-во заявок в контрольной выборке
    y_success - кол-во продаж на тестовой выборке
    y_cnt - кол-во заявок на тестовой выборке 
    """
    # Измените код этой функции
    # Это будет вашим решением
    # Не меняйте название функции и её аргументы
    return proportions_ztest([y_success, x_success], [y_cnt, x_cnt], alternative="larger")[1] < 0.06
