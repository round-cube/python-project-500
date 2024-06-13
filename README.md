### Hexlet tests and linter status:

[![Maintainability](https://api.codeclimate.com/v1/badges/6eb28c78122007ed6431/maintainability)](https://codeclimate.com/github/round-cube/python-project-500/maintainability)


# Проект Вычислитель отличий

**Вычислитель отличий** – программа, определяющая разницу между двумя структурами данных.
Это задача, для решения которой существуют в т.ч. онлайн-сервисы.
Подобный механизм используется при выводе тестов или при автоматическом отслеживании изменении в конфигурационных файлах.

**Возможности утилиты:**
+ Поддержка разных входных форматов: yaml и json
+ Генерация отчета в виде stylish, plain и json


_Шаг 3_
**Сравнение плоских файлов**

[![asciicast](https://asciinema.org/a/6xBWfg1A2rkpCiAbZlE25obe8.svg)](https://asciinema.org/a/6xBWfg1A2rkpCiAbZlE25obe8)


_Шаг 5_
**Сравнение плоских файлов (YAML)**

[![asciicast](https://asciinema.org/a/uU51qzr8ekHip6QPfprbj3Yxw.svg)](https://asciinema.org/a/uU51qzr8ekHip6QPfprbj3Yxw)


_Шаг 6_
**Рекурсивное сравнение**

[![asciicast](https://asciinema.org/a/aNBaJjPR2MDK31zitVYRXT1YN.svg)](https://asciinema.org/a/aNBaJjPR2MDK31zitVYRXT1YN)


_Шаг 7_
**Плоский формат**

[![asciicast](https://asciinema.org/a/O7zdKZJuhpu29kfMklPHxWnqW.svg)](https://asciinema.org/a/O7zdKZJuhpu29kfMklPHxWnqW)


_Шаг 8_
**Вывод в JSON**

[![asciicast](https://asciinema.org/a/snV9puiOyRPkTkJXNz4zKCBiP.svg)](https://asciinema.org/a/snV9puiOyRPkTkJXNz4zKCBiP)


## Требования к установке
```
* Python 3.10.
* Poetry 1.8
```

## Установка
Для запуска игр необходимо предварительно установить данный проект.

1. Склонировать репозиторий:
```
https://github.com/EvgenyAleksov/python-project-50.git
```

2. Прейти в директорию проекта:
```
cd python-project-50
```

3. Установить проект:
```
make package-install
````


## Проверка кода проекта линтером _flake8_
```
poetry run flake8 gendiff
```
