# schedule-tweet
Django based scheduler of tweets

## How to install and set it up for yourself

### Clone the repo

The first step is to clone the repo.

[https://github.com/singh1114/schedule-tweet](https://github.com/singh1114/schedule-tweet)

```shell
git clone git@github.com:singh1114/schedule-tweet.git
```

### Install the requirements

```shell
cd schedule-tweet
```

Turn on the virtualenv and install the requirements

```shell
pip install -r requirements.txt
```

### Run migrations to set up the database

```shell
cd scheduletweet
python manage.py migrate
```

### Create a super user

```shell
python manage.py createsuperuser
```

### Export the creds


Read [this post](https://pythonprogramming.org/how-to-create-a-webscraping-twitter-bot-in-python/) to get your creds.

```shell
export CONSUMER_KEY="#"
export CONSUMER_SECRET="#"
export ACCESS_TOKEN="#"
export TOKEN_SECRET="#"
```

You have to keep exporting them whenever you open a new shell window or you can [use direnv](https://ranvir.xyz/blog/dir-env-to-create-environment-variables-in-ubuntu/) to make your life easier.

### Run the server

```shell
python manage.py runserver
```

### Open the admin window and schedule a tweet after sometime

Visit [http://127.0.0.1:8000/admin](http://127.0.0.1:8000/admin) to login with `superuuser` creds and [twitterschedulermodel](http://127.0.0.1:8000/admin/twitter/twitterschedulermodel/) to create a new scheduled tweet.
