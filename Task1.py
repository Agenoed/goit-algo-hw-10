from pulp import *

prob = LpProblem("Виробництво напоїв", LpMaximize)

lemonade = LpVariable("Лимонад", lowBound=0, cat='Integer')
fruit_juice = LpVariable("Фруктовий сік", lowBound=0, cat='Integer')

prob += lemonade + fruit_juice, "Загальна кількість напоїв"

prob += 2 * lemonade + fruit_juice <= 100, "Обмеження води"
prob += lemonade <= 50, "Обмеження цукру"
prob += lemonade <= 30, "Обмеження лимонного соку"
prob += 2 * fruit_juice <= 40, "Обмеження фруктового пюре"


prob.solve()

print("Статус:", LpStatus[prob.status])
print("Оптимальне рішення:")
print("  Лимонад:", value(lemonade))
print("  Фруктовий сік:", value(fruit_juice))
print("Загальна кількість напоїв:", value(lemonade + fruit_juice))