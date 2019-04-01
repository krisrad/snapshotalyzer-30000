# snapshotalyzer-30000
Demo project to manage AWS EC2 instance snapshots

## About

This project is a demo, and  uses boto3 to manage AWS EC2 instance snapshots.

## Configuring

snapshotalyzer uses the configuration file created by the AWS cli.

`aws configure --profile snapshotalyzer`

## Running

`pipenv run python shotty\ec2test.py <command> <subcommand> <--project=PROJECT>`

*command* is instances, volumes or snapshots
*subcommand* depends on command
*project* is optional
