# traceroute
# task on internet protocols

Катяева Дарья КН202

###### Описание:
Трассировка автономных систем. Пользователь вводит доменное имя
или IP адрес. Осуществляется трассировка до указанного узла.
- поиск ip адресов осуществляется с помощью утилиты tracert
- поиск номеров автономных систем осуществляется с помощью утилиты curl и api.whois.vu

###### Пример запуска:
- python traceroute.py -d=ip or domain for tracing 
- python traceroute.py -d vk.com
- python traceroute.py -d 88.88.88.88
