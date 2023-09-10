import graphene
from django.conf import settings
from battle_log.resolvers import parse_log_to_table
from battle_log.types import DynamicScalar


class BattleLogTable(graphene.ObjectType):
    data = DynamicScalar()
    columns = graphene.List(graphene.String)


class Query:
    version = graphene.String()
    def resolve_version(self, info, **kwargs):
        return settings.VERSION



class ParseBattleLog(graphene.relay.ClientIDMutation):
    battle_log = graphene.Field(BattleLogTable)

    class Input:
        log_text = graphene.String(required=True)

    def mutate_and_get_payload(self, info, **kwargs):
        data, columns = parse_log_to_table(kwargs['log_text'])
        return ParseBattleLog(BattleLogTable(data=data, columns=columns))


class Mutation:
    parse_battle_log = ParseBattleLog.Field()
