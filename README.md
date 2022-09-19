
Eksisozluk

This is an api project that simply copy of the Eksisozluk which is an kind of social media platform very popular in Turkey.

In this project there are users they can create topics if they are allowed and other users can arguing or write their thoughts about that topic.

Also in this project includes very simply blog api original Eksisozluk also has it.

In general purposes of this project is learning the some crud operations with django rest framework and deep diving in django.








## Api Urls

**localhost::api/titles/**


That api request shows the all titles with their details page by page.

- id
- Tag list (Nested Serializer)
- First Entry (Nested Serializer)
- Title Name
- Created Date
- Creator By
- Total Click

**localhost::api/titles/entry_pk**

This url returns the entries given title id.

**localhost::api/create-title/**

To create an title there are two necessary things. Firstly, user must be logged in and it must have super user or ‘PR’ status. Otherwise system will not allow user to create a new title.  

Post method should consist the same paremeters like in the ss

 


**localhost::api/entries/entry-id**

This get method show us the detail of that entry.

If user owner of that entry or user is admin, they can change the content or delete the entry.

Ex: localhost::/api/enties/50


**localhost::api/create-entry/title-id**

With this allowed users can post their ideas about the title. There is two parameter in this url. Post content and image url.


**localhost::api/blog/create**

Allowed users can create blog, with title, its content and one optional image.



**localhost::api/blog/blog-id**

It allows user to see details of an blog, if the user is provider or admin they can olsa delete or update their blog details.

## Users

**localhost::api/user/login**

Users can login by using thier username and password.

**localhost::api/user/registration**

Users can complete the registration part by posting necessary parts.


**localhost::api/login/fb**

Also users can login via Facebook by using their access token, Code and id token.


## Installation

Install my-project with npm

```bash
  python3 -m venv yourenv
```

```bash
  source yourenv/bin/activate
```


```bash
  git clone https://github.com/axmetmercan/eksisozluk.git
  cd ./eksisozluk
  pip3 install -r requirements.txt
  cd ./eksisozluk
  python3 manage.py migrate
  python3 manage.py makemigrations
  python3 manage.py runserver
```
 Tada you are good to go!

    

