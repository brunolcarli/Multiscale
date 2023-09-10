

def parse_log_to_table(log):
    columns = [
        'TURN', 'P1_ACTION', 'P2_ACTION', 'P1_MOVE_USED', 'P2_MOVE_USED', 'P1_POKEMON', 'P2_POKEMON',
        'P1_SWITCHED', 'P2_SWITCHED', 'P1_WAS_KO', 'P2_WAS_KO', 'GAMETYPE', 'TIER', 'WINNER', 'BATTLE'
    ]

    data = []
    turns = log.split('|turn|')

    p1 = turns[0].split('|player|p1|')[1].split('\n')[0].split('|')[0]
    p2 = turns[0].split('|player|p2|')[1].split('\n')[0].split('|')[0]
    try:
        winner = turns[-1].split('|win|')[1].split('\n')[0]
        if winner in p1:
            winner = 'p1'
        elif winner in p2:
            winner = 'p2'
        else:
            winner = None
    except:
        winner = None

    gametype = turns[0].split('|gametype|')[1].split('\n')[0]
    tier = turns[0].split('|tier|')[1].split('\n')[0]    
    p1_poke = turns[0].split('|start\n')[1].split('|switch|')[1].removeprefix('p1a: ').split('|')[1]
    p2_poke = turns[0].split('|start\n')[1].split('|switch|')[2].removeprefix('p2a: ').split('|')[1]

    row = [None, None, None, None, None, p1_poke, p2_poke, None, None, None, None, gametype, tier, winner, f'{p1} VS {p2}']

    for i in turns[1:]:
        round = int(i.split('\n')[0])
        p1_action = None
        # player 1 used a move?
        if '|move|p1a:' in i:
            p1_action = 'move'
            p1_move_used = i.split('|move|p1a: ')[1].split('p2a')[0].split('|')[1]
        else:
            p1_move_used = None

        # player 1 was ko?
        if '|faint|p1a' in i:
            p1_was_ko = True
        else:
            p1_was_ko = False

        # player 1 has switched?
        if '|switch|p1a:' in i:
            p1_action = 'switch' if not p1_was_ko else p1_action
            p1_switched = True
            p1_poke = i.split('|switch|p1a: ')[1].split('\n')[0].split('|')[1]
        else:
            p1_switched = False

        ########

        p2_action = None
        # player 2 used a move?
        if '|move|p2a:' in i:
            p2_action = 'move'
            p2_move_used = i.split('|move|p2a: ')[1].split('p1a')[0].split('|')[1]
        else:
            p2_move_used = None

        # player 2 was ko?
        if '|faint|p2a' in i:
            p2_was_ko = True
        else:
            p2_was_ko = False

        # player 2 has switched?
        if '|switch|p2a:' in i:
            p2_action = 'switch' if not p2_was_ko else p2_action
            p2_switched = True
            p2_poke = i.split('|switch|p2a: ')[1].split('\n')[0].split('|')[1]
        else:
            p2_switched = False

        row[0] = round
        row[1] = p1_action
        row[2] = p2_action
        row[3] = p1_move_used
        row[4] = p2_move_used
        row[7] = p1_switched
        row[8] = p2_switched
        row[9] = p1_was_ko
        row[10] = p2_was_ko
        data.append(row)
        row = [None, None, None, None, None, p1_poke, p2_poke, None, None, None, None, gametype, tier, winner, f'{p1} VS {p2}']
    return data, columns
