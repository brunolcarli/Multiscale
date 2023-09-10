<table align="center"><tr><td align="center" width="9999">


# Multiscale

*Pokémon Showdown Battle Log parser*
</td></tr>

</table>    

<div align="center">

> ![Version badge](https://img.shields.io/badge/version-0.0.1-silver.svg)
> ![GraphQl Badge](https://badgen.net/badge/icon/graphql/pink?icon=graphql&label)

This API aims to parse and convert a Pokémon Shwdown battle replay log into a csv file to expand the possibilities of battle data analysis.


</div>

<hr />


# API request

The service implements a GraphQL API, the request must contain a mutation query payload with a single text input which is the battle log.

The response returns a data structure in array format in the field `data`, a unique `tile`  that is the key to redirect to the csv format throught the serve URL at the endpoint `/donwload/?` followed by the title generated.

The `url` field returns a link to the raw csv parsed data.

### Mutation payload:

```js
mutation{
  parseBattleLog(input: {
    logText: ""
  }){
    battleLog{
      title
      data
      columns
      csvUrl
    }
  }
}
```

## Example using Python to make the request


Consider this battle log example:

```py
log = "|join|kdarewolf\n|join|Onox\n|player|p1|kdarewolf|37\n|player|p2|Onox|159\n|gametype|singles\n|gen|6\n|tier|OU Monotype\n|rated\n|rule|Same Type Clause: Pokemon in a team must share a type\n|rule|Sleep Clause Mod: Limit one foe put to sleep\n|rule|Species Clause: Limit one of each Pokemon\n|rule|OHKO Clause: OHKO moves are banned\n|rule|Moody Clause: Moody is banned\n|rule|Evasion Moves Clause: Evasion moves are banned\n|rule|Endless Battle Clause: Forcing endless battles is banned.\n|rule|HP Percentage Mod: HP is reported as percentages\n|clearpoke\n|poke|p1|Kecleon, F, shiny\n|poke|p1|Diggersby, M\n|poke|p1|Girafarig, M, shiny\n|poke|p1|Heliolisk, F\n|poke|p1|Chansey, F, shiny\n|poke|p1|Staraptor, F, shiny\n|poke|p2|Espeon, M, shiny\n|poke|p2|Metagross, shiny\n|poke|p2|Reuniclus, M, shiny\n|poke|p2|Alakazam, M, shiny\n|poke|p2|Delphox, M, shiny\n|poke|p2|Gardevoir, M, shiny\n|teampreview\n|callback|decision\n|\n|start\n|switch|p1a: May Day Parade|Kecleon, F, shiny|324/324\n|switch|p2a: AMagicalFox|Delphox, M, shiny|292/292\n|turn|1\n|callback|decision\n|\n|move|p1a: May Day Parade|Fake Out|p2a: AMagicalFox\n|-damage|p2a: AMagicalFox|213/292\n|cant|p2a: AMagicalFox|flinch\n|\n|turn|2\n|callback|decision\n|\n|-start|p1a: May Day Parade|typechange|Dark|[from] Protean\n|move|p1a: May Day Parade|Sucker Punch|p2a: AMagicalFox\n|-crit|p2a: AMagicalFox\n|-supereffective|p2a: AMagicalFox\n|-damage|p2a: AMagicalFox|0 fnt\n|faint|p2a: AMagicalFox\n|\n|callback|decision\n|\n|switch|p2a: Moustachio|Alakazam, M, shiny|252/252\n|turn|3\n|callback|decision\n|\n|-formechange|p2a: Moustachio|Alakazam-Mega\n|message|Alakazam has Mega Evolved into Mega Alakazam!\n|-ability|p2a: Moustachio|Protean|[from] ability: Trace|[of] p1a: May Day Parade\n|-start|p1a: May Day Parade|typechange|Ghost|[from] Protean\n|move|p1a: May Day Parade|Shadow Sneak|p2a: Moustachio\n|-supereffective|p2a: Moustachio\n|-damage|p2a: Moustachio|84/252\n|-start|p2a: Moustachio|typechange|Normal|[from] Protean\n|move|p2a: Moustachio|Substitute|p2a: Moustachio\n|-start|p2a: Moustachio|Substitute\n|-damage|p2a: Moustachio|21/252\n|\n|turn|4\n|callback|decision\n|\n|-start|p1a: May Day Parade|typechange|Normal|[from] Protean\n|move|p1a: May Day Parade|Fake Out|p2a: Moustachio\n|-message|(Fake Out only works your first turn out.)\n|-fail|p2a: Moustachio\n|-start|p2a: Moustachio|typechange|Ghost|[from] Protean\n|move|p2a: Moustachio|Shadow Ball|p1a: May Day Parade\n|-immune|p1a: May Day Parade|[msg]\n|\n|turn|5\n|callback|decision\n|\n|-start|p1a: May Day Parade|typechange|Ghost|[from] Protean\n|move|p1a: May Day Parade|Shadow Sneak|p2a: Moustachio\n|-crit|p2a: Moustachio\n|-supereffective|p2a: Moustachio\n|-end|p2a: Moustachio|Substitute\n|-start|p2a: Moustachio|typechange|Fighting|[from] Protean\n|move|p2a: Moustachio|Focus Blast|p1a: May Day Parade\n|-immune|p1a: May Day Parade|[msg]\n|\n|turn|6\n|callback|decision\n|\n|switch|p2a: BrainCell|Reuniclus, M, shiny|424/424\n|move|p1a: May Day Parade|Shadow Sneak|p2a: BrainCell\n|-supereffective|p2a: BrainCell\n|-damage|p2a: BrainCell|320/424\n|\n|-heal|p2a: BrainCell|346/424|[from] item: Leftovers\n|turn|7\n|callback|decision\n|\n|switch|p1a: Of Mice & Men|Diggersby, M|362/362\n|move|p2a: BrainCell|Calm Mind|p2a: BrainCell\n|-boost|p2a: BrainCell|spa|1\n|-boost|p2a: BrainCell|spd|1\n|\n|-heal|p2a: BrainCell|372/424|[from] item: Leftovers\n|turn|8\n|callback|decision\n|\n|move|p1a: Of Mice & Men|U-turn|p2a: BrainCell\n|-supereffective|p2a: BrainCell\n|-damage|p2a: BrainCell|180/424\n|callback|decision\n|\n|switch|p1a: Paramedic|Chansey, F, shiny|704/704\n|move|p2a: BrainCell|Focus Blast|p1a: Paramedic\n|-supereffective|p1a: Paramedic\n|-damage|p1a: Paramedic|466/704\n|\n|-heal|p2a: BrainCell|206/424|[from] item: Leftovers\n|turn|9\n|callback|decision\n|\n|switch|p1a: May Day Parade|Kecleon, F, shiny|324/324\n|move|p2a: BrainCell|Recover|p2a: BrainCell\n|-heal|p2a: BrainCell|418/424\n|\n|-heal|p2a: BrainCell|424/424|[from] item: Leftovers\n|turn|10\n|callback|decision\n|\n|-start|p1a: May Day Parade|typechange|Fighting|[from] Protean\n|move|p1a: May Day Parade|Power-Up Punch|p2a: BrainCell\n|-resisted|p2a: BrainCell\n|-damage|p2a: BrainCell|397/424\n|-boost|p1a: May Day Parade|atk|1\n|move|p2a: BrainCell|Calm Mind|p2a: BrainCell\n|-boost|p2a: BrainCell|spa|1\n|-boost|p2a: BrainCell|spd|1\n|\n|-heal|p2a: BrainCell|423/424|[from] item: Leftovers\n|turn|11\n|callback|decision\n|\n|-start|p1a: May Day Parade|typechange|Dark|[from] Protean\n|move|p1a: May Day Parade|Sucker Punch|p2a: BrainCell\n|-supereffective|p2a: BrainCell\n|-damage|p2a: BrainCell|127/424\n|move|p2a: BrainCell|Psyshock|p1a: May Day Parade\n|-immune|p1a: May Day Parade|[msg]\n|\n|-heal|p2a: BrainCell|153/424|[from] item: Leftovers\n|turn|12\n|callback|decision\n|\n|-start|p1a: May Day Parade|typechange|Ghost|[from] Protean\n|move|p1a: May Day Parade|Shadow Sneak|p2a: BrainCell\n|-supereffective|p2a: BrainCell\n|-damage|p2a: BrainCell|0 fnt\n|faint|p2a: BrainCell\n|\n|callback|decision\n|-message|Onox forfeited.\n|\n|win|kdarewolf\n|raw|Ladder updating...\n|leave|Onox\n|player|p2\n|raw|kdarewolf's rating: 1049 &rarr; <strong>1076</strong><br />(+27 for winning)\n|raw|Onox's rating: 1087 &rarr; <strong>1059</strong><br />(-28 for losing)"
```


```python
import requests

url = 'https://multiscale.brunolcarli.repl.co/graphql/'
def get_payload(log):
    log = log.replace('\n', '\\n')
    return f'''
    mutation {{
      parseBattleLog(input: {{
        logText: "{log}"
      }}){{
        battleLog{{
          data
          columns
          csvUrl
          title
        }}
      }}
    }}
    '''


request = requests.post(url, json={'query': get_payload(log)})

print(request.status_code)
print(request.json()
```

```js
{'data': {'parseBattleLog': {'battleLog': {'data': [[1,
      'move',
      None,
      'Fake Out',
      None,
      'Kecleon, F, shiny',
      'Delphox, M, shiny',
      False,
      False,
      False,
      False,
      'singles',
      'OU Monotype',
      'p1',
      'kdarewolf VS Onox'],
      ...  # ommited
     [12,
      'move',
      None,
      'Shadow Sneak',
      None,
      'Kecleon, F, shiny',
      'Reuniclus, M, shiny',
      False,
      False,
      False,
      True,
      'singles',
      'OU Monotype',
      'p1',
      'kdarewolf VS Onox']],
    'columns': ['TURN',
     'P1_ACTION',
     'P2_ACTION',
     'P1_MOVE_USED',
     'P2_MOVE_USED',
     'P1_POKEMON',
     'P2_POKEMON',
     'P1_SWITCHED',
     'P2_SWITCHED',
     'P1_WAS_KO',
     'P2_WAS_KO',
     'GAMETYPE',
     'TIER',
     'WINNER',
     'BATTLE'],
    'csvUrl': 'https://multiscale.brunolcarli.repl.co/download/?a08867a9-9fc0-416d-88c9-e1724213f5c8',
    'title': 'a08867a9-9fc0-416d-88c9-e1724213f5c8'}}}}
```

By acessing the response `csvUrl` we get access to the raw csv:

```csv
TURN,P1_ACTION,P2_ACTION,P1_MOVE_USED,P2_MOVE_USED,P1_POKEMON,P2_POKEMON,P1_SWITCHED,P2_SWITCHED,P1_WAS_KO,P2_WAS_KO,GAMETYPE,TIER,WINNER,BATTLE
1,move,,Fake Out,,"Kecleon, F, shiny","Delphox, M, shiny",False,False,False,False,singles,OU Monotype,p1,kdarewolf VS Onox
2,move,,Sucker Punch,,"Kecleon, F, shiny","Delphox, M, shiny",False,True,False,True,singles,OU Monotype,p1,kdarewolf VS Onox
3,move,move,Shadow Sneak,Substitute,"Kecleon, F, shiny","Alakazam, M, shiny",False,False,False,False,singles,OU Monotype,p1,kdarewolf VS Onox
4,move,move,Fake Out,Shadow Ball,"Kecleon, F, shiny","Alakazam, M, shiny",False,False,False,False,singles,OU Monotype,p1,kdarewolf VS Onox
5,move,move,Shadow Sneak,Focus Blast,"Kecleon, F, shiny","Alakazam, M, shiny",False,False,False,False,singles,OU Monotype,p1,kdarewolf VS Onox
6,move,switch,Shadow Sneak,,"Kecleon, F, shiny","Alakazam, M, shiny",False,True,False,False,singles,OU Monotype,p1,kdarewolf VS Onox
7,switch,move,,Calm Mind,"Kecleon, F, shiny","Reuniclus, M, shiny",True,False,False,False,singles,OU Monotype,p1,kdarewolf VS Onox
8,switch,move,U-turn,Focus Blast,"Diggersby, M","Reuniclus, M, shiny",True,False,False,False,singles,OU Monotype,p1,kdarewolf VS Onox
9,switch,move,,Recover,"Chansey, F, shiny","Reuniclus, M, shiny",True,False,False,False,singles,OU Monotype,p1,kdarewolf VS Onox
10,move,move,Power-Up Punch,Calm Mind,"Kecleon, F, shiny","Reuniclus, M, shiny",False,False,False,False,singles,OU Monotype,p1,kdarewolf VS Onox
11,move,move,Sucker Punch,Psyshock,"Kecleon, F, shiny","Reuniclus, M, shiny",False,False,False,False,singles,OU Monotype,p1,kdarewolf VS Onox
12,move,,Shadow Sneak,,"Kecleon, F, shiny","Reuniclus, M, shiny",False,False,False,True,singles,OU Monotype,p1,kdarewolf VS Onox
```


### Contributions are welcome