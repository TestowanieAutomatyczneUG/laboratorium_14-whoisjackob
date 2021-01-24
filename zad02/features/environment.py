from behave import *
from Roman import Roman

def before_scenario(context, scenario):
    print("before")

def after_scenario(context, scenario):
    print("after")