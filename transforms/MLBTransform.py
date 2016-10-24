import TransformUtil as util
# Completed
'''
#load mlb fan
data = util.read_saved_json('mlb_fan_zip.json')

#load
mlb_teams = util.fetch_json('mlb')

team_key = util.buildTeamKey(mlb_teams)

def qualityCheck(team_abbr):
    if (team_abbr == 'SFG'): team_abbr = 'SF'
    if (team_abbr == 'TBR'): team_abbr = 'TB'
    if (team_abbr == 'WSN'): team_abbr = 'WSH'
    if (team_abbr == 'KCR'): team_abbr = 'KC'
    if (team_abbr == 'CHW'): team_abbr = 'CWS'
    if (team_abbr == 'SDP'): team_abbr = 'SD'

    return team_abbr

#for each team match key with team_abbr and add the team_key
for zipCode in data.keys():
    for team in data[zipCode]['teams']:
        for team_abbr in team.keys():
            dict_team_abbr = qualityCheck(team_abbr)
            team[team_abbr]['team_key'] = team_key[dict_team_abbr]


util.save_json(data, 'mlb_fans_zip.json')
'''



