import graphene
from django.conf import settings



class BattleLogTable(graphene.ObjectType):
    data = graphene.List(graphene.String)



class Query:
    version = graphene.String()
    def resolve_version(self, info, **kwargs):
        return settings.VERSION



class ParseBattleLog(graphene.relay.ClientIDMutation):
    battle_log = graphene.Field(BattleLogTable)

    class Input:
        log_text = graphene.String(required=True)

    def mutate_and_get_payload(self, info, **kwargs):
        return ParseBattleLog(['foo'])


class Mutation:
    parse_battle_log = ParseBattleLog.Field()
