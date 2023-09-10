import uuid
import graphene
import pandas as pd
from django.conf import settings
from battle_log.resolvers import parse_log_to_table
from battle_log.types import DynamicScalar
from battle_log.models import BattleLogCSV

class BattleLogTable(graphene.ObjectType):
    title = graphene.String()
    data = DynamicScalar()
    columns = graphene.List(graphene.String)
    csv_url = graphene.String()


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
        df = pd.DataFrame(data, columns=columns)
        title = str(uuid.uuid4())
        csv_url = f'{info.context.META["wsgi.url_scheme"]}://{info.context.META["HTTP_HOST"]}/download/?{title}'
        csv_log = BattleLogCSV.objects.create(title=title, data=df.to_csv(index=False))
        csv_log.save()
        
        
        return ParseBattleLog(BattleLogTable(data=data, columns=columns, csv_url=csv_url, title=title))


class Mutation:
    parse_battle_log = ParseBattleLog.Field()
