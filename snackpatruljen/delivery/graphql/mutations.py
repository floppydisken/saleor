import graphene


class CreateDelivery(graphene.Mutation):
    class Arguments:
        pass

    @classmethod
    def mutate(root, info, name):
        pass
