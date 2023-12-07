# To-Do-List
This is a web application that implements the basic concept of a task list, allows you to conveniently create, modify and manage them. Implemented sorting and additional tags for convenience to mark tasks with them.
****
**To start the project you need**
**set up the environment:**

```
python -m venv venv
```

for Windows:
```
source venv\Scripts\activate
```
for Mac OS
```
source venv/bin/activate
```

Using Python 3.11

Make sure requirements are installed, if not, type in terminal

```pip install -r requirements.txt```

To populate the database, use the json file by executing the command:

```python manage.py loaddata data.json```

(If you have problems, you can try migrations)

Next, you may need access to the admin panel to work. For this, you can use a ready-made user:

```
username: admin
password: 1qazcde3
```

And for start server working:

```
python manage.py runserver
```


Implementation of a list of tasks that can be manipulated and marked as completed. Also, if the deadline is late, it will highlight this in the right column.
![img1.png](img_for_readme%2Fimg1.png)
The tag column displays all the tags associated with the task by the Many-to-Many relationship

![img2.png](img_for_readme%2Fimg2.png)

Implementation of forms for creating and updating data for tasks and tags
![img3.png](img_for_readme%2Fimg3.png)
![img4.png](img_for_readme%2Fimg4.png)
But a warning before deleting
![img5.png](img_for_readme%2Fimg5.png)