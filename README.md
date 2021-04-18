В репозитории хранится файл программы, и файлы .pot, .po. То есть репозиторий находится в состоянии, при котором сделаны действия 1-4 из пункта "Начало"

Для запуска программы из репозитория необходимо 
1. инсталировать gettext и babel, 
2. сгенерировать .mo файл (действие 5 из пункта "Начало"): pybabel compile -D app -i po/eng/LC_MESSAGES/app.po -o po/eng/LC_MESSAGES/app.mo

--------------------------------------------

**Инсталяция**

sudo apt install gettext

pip install babel

**Запуск**

В английской версии LC_ALL=eng python3 app.py
В русской версии python3 app.py

--------------------------------------------

**Начало:**

1. Каждый фрагмент текста, который будет переводиться, поместить внутрь такой конструкции _("Text"), см. пример

2. pybabel extract -o app.pot app.py; mkdir po; mv app.pot po/app.pot

3. pybabel init -D app -i po/app.pot -d po -l eng

4. В файле po/eng/LC_MESSAGES/app.po написать соответствующие переводы
 
5. pybabel compile -D app -i po/eng/LC_MESSAGES/app.po -o po/eng/LC_MESSAGES/app.mo

**После изменений**

1. pybabel extract -o po/app.pot app.py

2. msgmerge -Uv po/eng/LC_MESSAGES/app.po po/app.pot

3. В файле po/eng/LC_MESSAGES/app.po прописать переводы, удалить строки с fuzzy

4. pybabel compile -D app -i po/eng/LC_MESSAGES/app.po -o po/eng/LC_MESSAGES/app.mo


