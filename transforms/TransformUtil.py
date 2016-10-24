import json, urllib

def read_saved_json(fileName):
    with open('../sports/%s' % fileName, 'r') as f:
        return json.load(f)


def fetch_json(league):
    url = 'http://aimepublish.gmti.gbahn.net/SportsData/Mobile.svc/team/%s'%league

    response = urllib.urlopen(url)

    return json.loads(response.read())

def fetch_data(url):
    response = urllib.urlopen(url)

    return json.loads(response.read())

def buildTeamKey(teams):
    team_key = {}

    for group in teams['groups']:
        for team in group['teams']:
            team_key[team['team_long']] = team['team_key']

    return team_key

def buildTeamKeyConf(teams):
    team_key = {}

    for group in teams['conference']:
        for team in group['team']:
            fullName = team['first_name'] + ' ' + team['last_name']
            team_key[fullName] = team['team_key']

    return team_key

def save_json(json_data, fileName):
    with open('../sports/%s' % fileName, 'w') as outfile:
        json.dump(json_data, outfile)