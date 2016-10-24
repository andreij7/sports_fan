import TransformUtil as util

def qualityCheck(team_name):
    if(team_name == 'Ucla Bruins'): return 'UCLA Bruins'
    if(team_name == 'Usc Trojans'): return 'Southern California Trojans'
    if(team_name == 'Texas A And M Aggies'): return 'Texas A&M Aggies'
    if(team_name == 'Ole Miss Rebels'): return 'Mississippi Rebels'
    if(team_name == 'Lsu Tigers'): return 'Louisiana State Tigers'
    return team_name

#load ncaaf_fan
data = util.read_saved_json('ncaaf_fan_zip.json')

url = 'http://aimepublish.gmti.gbahn.net/SportsData/Metadata.svc/DES/teampicker/ncaaf/2016'
ncaaf_teams = util.fetch_data(url)

team_key = util.buildTeamKeyConf(ncaaf_teams)

team_key['Byu Cougars'] = "/sport/football/team:33"
team_key['Tcu Horned Frogs'] = "/sport/football/team:110"
team_key['Southern Miss Golden Eagles'] = '/sport/football/team:58'
team_key['Florida International Panthers'] = '/sport/football/team:230'
team_key['Miami Redhawks'] = '/sport/football/team:121'
team_key['Umass Minutemen'] = '/sport/football/team:207'
team_key['Louisiana Monroe Warhawks'] = '/sport/football/team:137'
team_key['Smu Mustangs'] = '/sport/football/team:73'
team_key['Utep Miners'] = '/sport/football/team:41'
team_key['Unlv Rebels'] = '/sport/football/team:108'
team_key['Louisiana Lafayette Ragin Cajuns'] = '/sport/football/team:38'
team_key['Ucf Knights'] = '/sport/football/team:142'
#team_key['Uab Blazers'] = '/sport/football/team:142' //same id as ucf knights from 2014

notInlist = set();

#for each team match key with team_long and add the team_key
for zipCode in data.keys():
    for team in data[zipCode]['teams']:
        for team_long in team.keys():
            try:
                dict_key = qualityCheck(team_long)
                team[team_long]['team_key'] = team_key[dict_key]
            except:
                notInlist.add(team_long)

util.save_json(data, 'ncaaf_fans_zip.json')