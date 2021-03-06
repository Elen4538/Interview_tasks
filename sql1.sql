"""
[Дана структура таблицы)
CREATE TABLE payments (
FIO VARCHAR2( 50 ) NOT NULL
PAYMENT INT( 10) NOT NULL,
DT DATE NOT NULL
);
[Пример заполнения]
Иванов | 100 | 1/1/2019
Иванов | 100 | 1/2/2019
Петров | 150 | 1/2/2019
Петров | 150 | 1/4/2019
....
Нужно написать SQL запрос, выводящий список сотрудников и сумма всех выплат по сотруднику, но только по тем сотрудникам, у которых было более 5 выплат.

[Пример вывода результата]
Иванов | 5000
Петров | 7000
"""


SELECT FIO, 
SUM(PAYMENT)
FROM payments
GROUP BY FIO
HAVING COUNT(FIO) >5;
