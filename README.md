<table align="center"><tr><td align="center" width="9999">


# Multiscale

*Pokémon Showdown Battle Log parser*
</td></tr>

</table>    

<div align="center">

> ![Version badge](https://img.shields.io/badge/version-0.0.3-silver.svg)
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
log = "|join|kdarewolf\n|join|Onox\n|player|p1|kdarewolf|37\n|player|p2|Onox|159\n|gametype|singles\n|gen|6\n|tier|OU Monotype\n|rated\n|rule|Same Type Clause: Pokemon in a team must share a type\n|rule|Sleep Clause Mod: Limit one foe put to sleep\n|rule|Species Clause: Limit one of each Pokemon\n|rule|OHKO Clause: OHKO moves are banned\n|rule|Moody Clause: Moody is banned\n|rule|Evasion Moves Clause: Evasion moves are banned\n|rule|
 ...  #ommited
"
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