# profile-analyzer
search profiles on github and save them in a list django based web app.

# build & run
In order to run this application you have to fullfill these requirements:
You have to have a postgres database(you can get a docker container for this one):
Markdown | Less 
--- | --- 
DATABASE_NAME | postgres
USER| postgres
PASSWORD| postgrespw
HOST| localhost
PORT| 49153

And a python interpreter whis has Django version 4.1.1 and then run these commands.

```bash
python.exe .\manage.py makemigrations
python.exe .\manage.py migrate
python.exe .\manage.py runserver
```

![Screenshot 2022-09-26 211705](https://user-images.githubusercontent.com/55808189/192351559-adc3280d-bdb2-428d-bbc0-c565603076bb.png)
![Screenshot 2022-09-26 211604](https://user-images.githubusercontent.com/55808189/192351569-1ae5ffab-40b8-41fe-b62e-8735ab896225.png)
