import TransformUtil as util

product = {}

data = util.read_saved_json('ncaaf_fans_zip.json')

def getFavorite(teams):
    max = 0
    fav = ''
    for team in teams:
        for name in team:
            if(team[name]['likes'] > int(max)):
                max = team[name]['likes']
                fav = name
    return fav

def getTeamKey(teams, target):
    key = ''
    for team in teams:
        for name in team:
            if (name == target):
                key = team[name]['team_key']
    return key

#for each key in ncaaf_fans_zip
for teamZipCode in data.keys():
    #get absolute favorite team
    teamName = getFavorite(data[teamZipCode]['teams'])

    try:
        product[teamName]['zips'].append(teamZipCode)
    except:
        product[teamName] = {}
        product[teamName]['zips'] = [teamZipCode]
        team_key = getTeamKey(data[teamZipCode]['teams'], teamName)
        product[teamName]['team_key'] = team_key

print len(product.keys())

util.save_json(product, 'ncaaf_team_zip.json')