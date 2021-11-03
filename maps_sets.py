#summary to maps, sets and their functions etc.
androidVersions = {
    '4.0' : 'Ice Cream Sandwitch',
    '4.1' : 'Jelly Bean',
    '4.4' : 'KitKat',
    '5.0' : 'Lollipop',
    '6.0' : 'Marshmallow',
    '7.0' : 'Nougat',
    '8.0' : 'Oreo',
    '9.0' : 'Pie',
    '10.0' : 'Android Q',
    '11.0' : 'Android R',
    '12.0' : 'Snow Cone',
}
remedy_games = {'Max Payne', 'Max Payne 2', 'Alan Wake', 'Quantum Break', 'Control'}


#------map manipulations------
print(androidVersions['4.0'])
print(androidVersions.get('4.0'))
print(androidVersions.get('123', 'Upcoming version is being tested'))

#------set manipulations------ 
remedy_games.add('Alan Wake\'s American Nightmare')
new_game = {'Alan Wake Remastered'}
remedy_games.update(new_game)
print(remedy_games)