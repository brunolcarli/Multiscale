import graphene
import battle_log.schema


class Query(battle_log.schema.Query, graphene.ObjectType):
    pass


class Mutation(battle_log.schema.Mutation, graphene.ObjectType):
    pass


schema = graphene.Schema(query=Query, mutation=Mutation)
