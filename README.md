# Video Service
## Requirements
* Python 3.10+
* PostgreSQL15
## База данных
Я впервые использовал PostgreSQL для проекта. Известные мне ранее методы настройки БД не подошли по какой-то неведомой мне причине. Но на всякий случай я оставлю инструкцию для запуска двумя методами. 

Для работы сайта потребуется установленный в системе PostgreSQL. 

Эти команды для Linux Ubuntu:
``` bash 
sudo -iu postgres psql -c "alter user postgres with password 'postgres';"
sudo -iu postgres psql -c "create database red;"
```
Первая обновит пароль для пользователя postgres, вторая создаст базу данных с именем red.

Аналогично для Mac OS: 
``` bash 
psql -U postgres -c "alter user postgres with password 'postgres';"
psql -U postgres -c "create database red;"
```

В случае чего можно, можно войти в консоль PGSQL и вручную сделать тоже самое, хоят технически эти команды должны отрабатывать корректно.