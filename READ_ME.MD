1. install python
2. install pip
3. pip install django
4. django-admin --version (check)

5. django-admin startproject projectname
6. py manage.py startapp appname
7. add app to setting.py : 'sampleappname.apps.MembersConfig'
8. py manage.py shell -> add database by member = Member(firstname='a', lastname='b') member.save()
9. py manage.py makemigration sampleappname
