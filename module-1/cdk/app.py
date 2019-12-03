#!/usr/bin/env python3

from aws_cdk import core

from cdk.webapplication_stack import WebApplicationStack

app = core.App()

WebApplicationStack(app, "MythicalMysfits-WebApplication")

app.synth()
