# 🌟 MOIZA
* Everyone can suggest their opinion super freely!!!
* Each decision steps will be preserved until the end of the development.
---

## 🖥 DEMO VIDEO
### <a href="https://youtu.be/3K2CKHKzg3g">CHECK HERE</a>

## 🔮 View
<img width="250" alt="스크린샷 2021-06-26 오후 5 14 44" src="https://user-images.githubusercontent.com/39653584/123506982-03b26100-d6a2-11eb-9680-24260ee5f93c.png">

---


## 💫 Contributors
[![All Contributors](https://img.shields.io/badge/all_contributors-6-orange.svg?style=flat-square)](#contributors-)
<table>
  <tr>
    <td align="center"><a href="https://github.com/minji9611"><img src="https://avatars.githubusercontent.com/u/81851584?v=4?s=200" width="200px;" alt=""/><br /><sub><b>Minji Kim</b></sub></a><br />Designer<br/><a href="https://github.com/LikeLion-CAU-9th/MOIZA/commits?author=minji9611" title="Documentation">🔥</a></td>
    <td align="center"><a href="https://github.com/youngkwon02"><img src="https://avatars.githubusercontent.com/u/39653584?v=4?s=200" width="200px;" alt=""/><br /><sub><b>Youngkwon Kim</b></sub></a><br />Developer<br /><a href="https://github.com/LikeLion-CAU-9th/MOIZA/commits?author=youngkwon02" title="Documentation">🔥</a></td>
    <td align="center"><a href="https://github.com/rineeee"><img src="https://avatars.githubusercontent.com/u/62981406?v=4?s=200" width="200px;" alt=""/><br /><sub><b>Harin Kim</b></sub></a><br />Developer<br /><a href="https://github.com/LikeLion-CAU-9th/MOIZA/commits?author=rineeee" title="Documentation">🔥</a></td>
    <td align="center"><a href="https://github.com/Seojisoo20191941"><img src="https://avatars.githubusercontent.com/u/76681519?v=4?s=200" width="200px;" alt=""/><br /><sub><b>Jisoo Seo</b></sub></a><br />Developer<br /><a href="https://github.com/LikeLion-CAU-9th/MOIZA/commits?author=Seojisoo20191941" title="Documentation">🔥</a></td>
    <td align="center"><a href="https://github.com/yunseonyeong"><img src="https://avatars.githubusercontent.com/u/64634970?v=4?s=200" width="200px;" alt=""/><br /><sub><b>Seonyeong Yun</b></sub></a><br />Developer<br /><a href="https://github.com/LikeLion-CAU-9th/MOIZA/commits?author=yunseonyeong" title="Documentation">🔥</a></td>
    <td align="center"><a href="https://github.com/jjanggyu"><img src="https://avatars.githubusercontent.com/u/59885351?v=4?s=200" width="200px;" alt=""/><br /><sub><b>Changyu Lee</b></sub></a><br />Professor<br /><a href="https://github.com/LikeLion-CAU-9th/MOIZA/commits?author=jjanggyu" title="Documentation">🔥</a></td>
  </tr>
</table>


---


## 📚 Tech Stack
![](https://img.shields.io/badge/django-3.2.2-green)&nbsp;&nbsp;
![](https://img.shields.io/badge/HTML-5.3-orange)&nbsp;&nbsp;
![](https://img.shields.io/badge/CSS-blue)&nbsp;&nbsp;
![](https://img.shields.io/badge/JS-ES6-yellow)&nbsp;&nbsp;




## 🌈 Communication

|<img width= 50 src="https://i.imgur.com/Ap8neHw.png">| <img width= 50 src="https://i.imgur.com/jrN40gS.jpg">    |
| :---------------------------------------------------: | :---------------------------------------------------: |
|                        GitHub                     |                        Notion                         |


---

## License
[![License: MIT](https://img.shields.io/badge/License-MIT-skyblue.svg)](https://opensource.org/licenses/MIT)

---

## 🪄 Installation
#### - Pre-Set(! You need to install MySQL for using this)
```sh
pip install pymysql
pip install mysqlclient
```

(If you use Windows OS)
: Just run MySQL-client

(If you use Unix Family OS such as Linux or Mac)
```sh
sudo mysql -u root -p
```

---

- Create Database and use it
```sh
CREATE DATABASE MOIZA_DB;
USE MOIZA_DB;
```

- Create Tables
```sh
CREATE TABLE account_user_info
(
user_seq int auto_increment primary key,
user_name longtext not null,
user_pw longtext not null,
user_email varchar(254) not null,
register_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);
```

```sh
CREATE TABLE opinion_group_info
(
group_seq int auto_increment primary key,
name longtext not null,
create_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
owner int not null,
index(owner)
);
```

```sh
CREATE TABLE opinion_group_info
(
group_seq int auto_increment primary key,
name longtext not null,
create_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
owner int not null,
index(owner)
);
```

```sh
CREATE TABLE opinion_group_url
(
group_seq int not null,
url longtext not null
);
```

```sh
CREATE TABLE opinion_membership
(
id bigint auto_increment primary key,
join_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
auth varchar(3),
group_seq int not null,
user_seq int not null,
index(group_seq),
index(user_seq)
);
```

```sh
CREATE TABLE opinion_response
(
response_seq int auto_increment primary key,
content longtext not null,
selection_seq_id bigint not null,
suggestion_id bigint not null,
writer_id int not null,
index(selection_seq_id),
index(suggestion_id),
index(writer_id),
);
```

```sh
CREATE TABLE opinion_selection
(
id bigint auto_increment primary key,
selection_content varchar(100) not null,
suggestion_id bigint not null,
index(suggestion_id)
);
```

```sh
CREATE TABLE opinion_suggestion
(
id bigint auto_increment primary key,
topic varchar(80),
other_selection tinyint(1) not null,
no_selection tinyint(1) not null,
group_sequence_id int not null,
owner_seq int,
index(group_sequence_id)
);
```

#### - Download & Run
```sh
git clone https://github.com/youngkwon02/MOIZA.git
cd MOIZA/moiza
python manage.py runserver
```
