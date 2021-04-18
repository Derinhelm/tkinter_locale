**Инсталировать**

sudo apt install gettext

pip install babel

**Начало:**

Каждый фрагмент текста, который будет переводиться, поместить внутрь такой конструкции _("Text"), см. пример

pybabel extract -o po/app.pot app.py

pybabel init -D app -i po/app.pot -d po -l eng

vim po/eng/LC_MESSAGES/app.po
 
pybabel compile -D app -i po/eng/LC_MESSAGES/app.po -o po/eng/LC_MESSAGES/app.mo

Запуск в английской версии LC_ALL=eng python3 app.py
В русской версии python3 app.py

**После изменений**

pybabel extract -o po/app.pot app.py

vim po/eng/LC_MESSAGES/app.po - прописать переводы, удалить строки с fuzzy

pybabel compile -D app -i po/eng/LC_MESSAGES/app.po -o po/eng/LC_MESSAGES/app.mo


