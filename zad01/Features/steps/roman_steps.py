from behave import *
from Roman import Roman
from assertpy import *


use_step_matcher("re")

@given(u'I am in the zad01 directory')
def step_impl(context):
    context.roman = Roman()


@when(u'the input is (?P<strand1>.+)')
def step_impl(context, strand1):
    context.wynik = context.roman.roman(int(strand1))


@then(u'the output should be (?P<result>.+)')
def step_impl(context, result):
    assert_that(context.wynik).is_equal_to(str(result))


