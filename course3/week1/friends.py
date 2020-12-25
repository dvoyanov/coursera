import requests
import datetime

def calc_age(uid):
    year_now = datetime.datetime.now().year
    vk_friends = get_vk_user_friends(get_vk_user_id(uid))
    friends_years_old = []
    for friend in vk_friends:
        year_of_birth = get_year_of_birth_for_vk_friend(friend)
        if year_of_birth != 0:
            friends_years_old.append(year_now - year_of_birth)
    set_years = set(friends_years_old)
    couple_age_number_of_friends = []
    for year in set_years:
        couple_age_number_of_friends.append((year, friends_years_old.count(year)))
    return sorted(couple_age_number_of_friends, key=lambda pair: (-pair[1], pair[0]))

def get_year_of_birth_for_vk_friend(friend):
    if 'bdate' in friend:
        if friend['bdate'].count(".") == 2:
            return int(friend['bdate'].split(".")[-1])
    return 0


def get_vk_user_id(name):
    payload = {'v': '5.71', 'access_token': '17da724517da724517da72458517b8abce117da17da72454d235c274f1a2be5f45ee711',
               'user_ids': '{}'.format(name)}
    r = requests.get('https://api.vk.com/method/users.get', params=payload)
    return r.json()['response'][0]['id']

def get_vk_user_friends(uid):
    payload = {'v': '5.71', 'access_token': '17da724517da724517da72458517b8abce117da17da72454d235c274f1a2be5f45ee711',
               'user_id': '{}'.format(uid), 'fields': 'bdate'}
    r = requests.get('https://api.vk.com/method/friends.get', params=payload)
    return r.json()['response']['items']

#if __name__ == '__main__':
#    res = calc_age('reigning')
#    print(res)