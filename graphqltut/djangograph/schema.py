import graphene
from graphene import ObjectType, Node, Schema
from graphene_django.fields import DjangoConnectionField
from graphene_django.types import DjangoObjectType
from .models import Employee

class EmployeeNode(DjangoObjectType):
    class Meta:
        model = Employee
        interfaces = (Node, )

class Query(ObjectType):
    employee = Node.Field(EmployeeNode)
    all_employees = DjangoConnectionField(EmployeeNode)


schema = Schema(query=Query)



