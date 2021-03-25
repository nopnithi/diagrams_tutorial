from diagrams import Diagram, Cluster
from diagrams.aws.general import Users
from diagrams.aws.network import ALB, Route53
from diagrams.aws.compute import EC2Instance
from diagrams.aws.database import RDS


def generate(name, num_of_instances):
    with Diagram(name, direction='TB', show=True):
        with Cluster('Auto Scaling Group'):
            app_group = [EC2Instance('App') for _ in range(num_of_instances)]
        rds_master = RDS('DB (Master)')
        rds_standby = RDS('DB (Standby)')
        Users('Users') >> Route53('Route 53') >> ALB('ALB') >> app_group >> rds_master
        rds_master - rds_standby


if __name__ == '__main__':
    name = input('Diagram name: ')
    num_of_instances = input('Number of instances: ')
    generate(name, int(num_of_instances))
