resource "aws_ecs_task_definition" "app" {
  family                   = "microservices-task"
  network_mode             = "awsvpc"
  requires_compatibilities = ["FARGATE"]
  cpu                      = "256"
  memory                   = "512"

  execution_role_arn = aws_iam_role.ecsTaskExecutionRole.arn

  container_definitions = jsonencode([{
    name  = "app"
    image = "amazon/amazon-ecs-sample"
    cpu   = 256
    memory = 512
    essential = true
    portMappings = [{
      containerPort = 80
      hostPort      = 80
    }]
  }])
}

resource "aws_ecs_service" "app" {
  name            = "microservices-service"
  cluster         = aws_ecs_cluster.main.id
  task_definition = aws_ecs_task_definition.app.arn
  desired_count   = 1

  network_configuration {
    subnets         = [aws_subnet.public[0].id]
    security_groups = [aws_security_group.ecs.id]
  }
}
