from diagrams import Diagram
from diagrams.aws.network import ALB
from diagrams.aws.compute import EC2
from diagrams.aws.database import RDS

with Diagram('MyDiagram1', show=True):
    ALB('MyALB') >> EC2('MyEC2') >> RDS('MyRDS')
