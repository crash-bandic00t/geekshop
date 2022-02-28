import requests
from social_core.exceptions import AuthForbidden
from django.db import transaction


@transaction.atomic
def get_user_info(backend, user, response, *args, **kwargs):
    userinfo = requests.get(
        f"https://people.googleapis.com/v1/people/me?personFields=genders,birthdays",
        headers={"Authorization": "Bearer %s" % response["access_token"]}
    ).json()
    if userinfo['genders']:
        if userinfo['genders'][0]['value'] == 'male':
            user.profile.gender = 'M'
        else:
            user.profile.gender = 'F'
    print(user.profile.gender)
    user.profile.save()