"what I have not done:"
i am unable to complete the notification popup task as i dont have much time explore.
I have tried to complete the that task using Celery but i don't have much time to do that.
I have hosted the backend in docker. i have attached screenshot along with readme file please do check it.


# Meetify API Documentation

Meetify is a sophisticated Meeting Scheduling App designed to streamline the scheduling process, allowing users to effortlessly book, manage, and track meetings.

## Setup

#### clone the project

```bash
git clone <repository_url>
```

#### Install Dependencies

```bash
cd slot/

python3 -m venv env
source env/bin/activate

pip install -r requirements.txt
```

#### Run Migrations

```bash
python manage.py makemigrations
python manage.py migrate
```

## Usage

### User Endpoints

#### Create User

```bash
curl --location 'http://localhost:8000/api/users/' \
--header 'Content-Type: application/json' \
--data-raw '{
    "name": "vishal",
    "email": "vishal@gmail.com",
    "dnd_start_time": "2024-06-20T08:00:00+05:30",
    "dnd_end_time": "2024-06-20T11:00:00+05:30",
    "preferred_timezone": "IST"
}'
```

#### Update User

```bash
curl --location --request PATCH 'http://localhost:8000/api/users/1/' \
--header 'Content-Type: application/json' \
--data-raw '{
    "dnd_start_time": "2024-06-20T10:00:00+05:30",
    "dnd_end_time": "2024-06-20T12:00:00+05:30",
    "preferred_timezone": "IST"
}'
```

#### List Users

```bash
curl --location 'http://localhost:8000/api/users/list/'
```

#### Create Meeting

```bash
curl --location 'http://localhost:8000/api/meeting/' \
--header 'Content-Type: application/json' \
--data '{
    "user": 1,
    "meeting_type": "ONLINE",
    "start_time": "2024-06-20T12:00:00+05:30",
    "end_time": "2024-06-20T12:20:00+05:30",
    "notification_interval": "10"
}'
```

#### Booked Meetings

```bash
curl --location 'http://localhost:8000/api/users/booked-meetings/?user=1&start_time=2024-06-19%2015%3A00%3A00&end_time=2024-06-21%2015%3A00%3A00'
```
![image](https://github.com/Vishal7780/meetify_oneassure/assets/90459452/fe908ec8-a59c-4b31-bdd9-7e84991b219c)


