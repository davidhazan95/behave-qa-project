from behave import *
from features.steps.mocks_json import *
from features.steps.mocks_dataset import *
from features.steps.utils import *

@given(u'I have a Dataset')
def step_impl(context):
    context.cisco_valid_dataset= mock_generate_dataset()

@when(u'I validate the Dataset with a base json')
def step_impl(context):
    context.cisco_910_json = generate_cisco_910_mock_json()


@then(u'I see that the two are compatible')
def step_impl(context):
    assert context.cisco_910_json == context.cisco_valid_dataset

@given(u'I have a Dataset with {invalid_path}')
def step_impl(context,invalid_path):
    context.cisco_invalid_path_dataset= mock_generate_invalid_path_dataset(invalid_path)

@when(u'I validate the Dataset with wrong path')
def step_impl(context):
    context.message_invalid_path = validate_path_regex(context.cisco_invalid_path_dataset["path"])

@then(u'I see message of invalid path')
def step_impl(context):
    assert context.message_invalid_path == "Path Syntax in Dataset is not valid!"

@given(u'I have a Dataset generated by the WebScraper with "{vendor}","{url}","{series}","{category}","{model}","{path}","{release}"')
def step_impl(context,vendor,url,series,category,model,path,release):
    context.empty_field_dataset = generate_custom_dataset(vendor,url,series,category,model,path,release)

@when(u'I validate the Dataset with wrong field')
def step_impl(context):
    context.message_empty_field = validate_dataset_empty_field(context.empty_field_dataset)


@then(u'I see message with invalid {field}')
def step_impl(context,field):
    print(context.message_empty_field)
    print("The following field is empty: "+field) 
    assert context.message_empty_field == "The following field is empty: "+field