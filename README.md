# Microblog
Microblog is a web application that allows users to create profiles, write posts, send messages, follow each other, and many other social interactions. The platform supports English, Arabic, French, Spanish, and German. The website is implemented in [flask](https://flask.palletsprojects.com/en/3.0.x/) (a python framework) and following [Flask Mega-Tutorial](https://blog.miguelgrinberg.com/post/the-flask-mega-tutorial-part-i-hello-world).

## Installation instructions:
- Clone the remote repositery
- Go to the directory of the local repositery to create and activate a python environment 
  ```
  python -m venv venv
  source venv/bin/activate #in Ubuntu, WSL, or even Bash Terminal
  ```
-  After activating the environment install the required dependencies
  ```
  pip install -r requirments.txt
  ```
- Create _'.env'_ file in the directory and add these variables in it:
  ```
  SECRET_KEY=an-example-of-a-strong-password   # create a strong password and drop it here to be used later in resseting the user password
  MAIL_SERVER=localhost
  MAIL_PORT=25
  MS_TRANSLATOR_KEY= ***********************  #Your microsoft azure translation key 
  CAFILE=http_ca.crt                          #this certificate is optained from ElasticSearch and copied to the directory of microblog  
  ELASTICSEARCH_URL=https://localhost:9200
  ELASTIC_NAME=elastic
  ELASTIC_PASSWORD=*******************    #your ElasticSearch password optained from running ElasticSearch server for the first time
  ```
  - *Notes*:
  - Azure translation key could be optained for free, follow this [Microsoft tutorial](https://learn.microsoft.com/en-us/azure/ai-services/translator/create-translator-resource)
  - ElasticSearch service should be installed and running to be able to index and search the website posts, follow this [installation guide](https://www.elastic.co/guide/en/elasticsearch/reference/current/install-elasticsearch.html) and   I highly recommend downloading and running it in docker following [Elastic docker installation](https://www.elastic.co/guide/en/elasticsearch/reference/current/docker.html)

## Entity Relationship Diagram (ERD):
<p align="center">
  <img width="800"  src="https://github-production-user-asset-6210df.s3.amazonaws.com/65557776/285468941-0014317c-fb1e-46bc-85a1-c62455482b36.png">
</p> 

## Main functionalities and Features: 
### Home page:
Feed that only shows posts of people you are following and your own posts
<p align="center">
  <img width="800" src="https://github-production-user-asset-6210df.s3.amazonaws.com/65557776/285478977-ee86b85f-1c71-4643-8baf-94df0ec2705c.png">
</p>

### Explore:
Feed that shows posts from all people whether you follow them or not
<p align="center">
  <img width="800" src="https://github-production-user-asset-6210df.s3.amazonaws.com/65557776/285483631-fa1dd79c-3c29-4b4e-b8fd-512ef110a502.png">
</p>

### Indexing and Searching posts using Elasticsearch:
<p align="center">
  <img width="800" src="https://github-production-user-asset-6210df.s3.amazonaws.com/65557776/285498769-11a7fe97-b0c1-4021-aa3a-02618369a1ad.png">
</p>

### Dynamic Translation (using Microsoft Azure translation api):
<p align="center">
  <img width="800" src="https://github-production-user-asset-6210df.s3.amazonaws.com/65557776/285484006-15f4e6d7-3c98-457d-9c9a-3c4b175bcf1b.png">
  <img width="800" src="https://github-production-user-asset-6210df.s3.amazonaws.com/65557776/285484015-3e53b00a-49a8-4dd0-8fd2-24fd8627f826.png">
</p>

### Website Languages:
The website supports 5 Languages ['en', 'ar', 'es', 'fr', 'de'], Microblog chooses the language based on the browser default language which could be changed:
<br>
*ONLY DO ONE OF THESE TWO*
- Open '_edge://settings/languages_' or whats equivalent in your choosen browser, add a language, then move it up in priority.
- Force certain language by commenting '_return request.accept_languages.best_match(current_app.config['LANGUAGES'])_'  in _get_locale()_ [microblog/app/__init__.py line 15](https://github.com/AhmedElshobaky/microblog/blob/d028e84cfa52c1573d7476b4ac02013d8ec2ab82/app/__init__.py#L15)

#### German LeftToRight Bootstrap Vs Arabic RTL Bootstrap::
<p align="center">
  <img width="500" height="330" src="https://github-production-user-asset-6210df.s3.amazonaws.com/65557776/285485668-09b7d028-e300-475f-9440-258b35a50c65.png">
  <img width="500" height="330" src="https://github-production-user-asset-6210df.s3.amazonaws.com/65557776/285485127-8f0c6aa9-f411-4778-bb8e-937049f05040.png">
</p>

### Profile:
Profile avatars are auto generated using [Gravatar](https://gravatar.com/), the avatars are '_identicon avatar_' generated uniquely for each user using the user's mail 
<p align="center">
  <img width="800" src="https://github-production-user-asset-6210df.s3.amazonaws.com/65557776/285487003-83aeaee4-d515-4666-8e37-59213265a4ba.png">
</p>

### Messages:
Users can send private messages to each others
- Ahmed Sends TheCoolestUser a message
<p align="center">
  <img width="800" src="https://github-production-user-asset-6210df.s3.amazonaws.com/65557776/285490013-057dcff2-34e5-4c46-8822-aeab562a6f15.png">
</p>

- TheCoolestUser Gets notified in the upper right corner that he has received a new message
<p align="center">
  <img width="800" src="https://github-production-user-asset-6210df.s3.amazonaws.com/65557776/285490473-d36eb903-604e-4d50-9117-cc50dd06af43.png">
</p>

- TheCoolestUser opens his inbox to check the message
<p align="center">
  <img width="800" src="https://github-production-user-asset-6210df.s3.amazonaws.com/65557776/285490465-4693bf62-7bec-47b5-883e-a2b50efc9082.png">
</p>
