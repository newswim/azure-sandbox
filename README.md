### Resources

https://learn.microsoft.com/en-us/azure/azure-functions/functions-bindings-http-webhook-trigger?tabs=in-process%2Cfunctionsv2&pivots=programming-language-python#example

https://learn.microsoft.com/en-us/azure/storage/blobs/storage-quickstart-blobs-python?tabs=environment-variable-windows

## Using an SDK

1. Need a "connection string" -- the secret associated with some role

- provision the resources and actions that you need
- typically, there will be a role assigned to some set of credential that you're using
- The role will have a set of permissions associated; these grant or deny access to ceratin actions taken on certain objects
- E.g. READ, WRITE, EXECUTE, NONE .. but all the API actions in the SDK
- Contains additional user info

## Pyenv

- Doesn't set a global version by default

## Blob storage

- Service Acct (fs)
  - Container (folder)
    - Blob (file)

This request is not authorized to perform this operation. RequestId:52936712-001e-0075-4337-dc40f3000000 Time:2022-10-09T23:31:47.6040659Z

This storage account's 'Firewalls and virtual networks' settings may be blocking access to storage services. Try adding your client IP address ('XXX.XXX.X.XXX') to the firewall exceptions, or by allowing access from 'all networks' instead of 'selected networks'. Learn more

## Benefits

- We use more Microsoft services and that will make them happy.

## Basic Architecture

- Scrapers (python scripts) -> HTML -> Parser -> JSON -> Aggregated / Normalized -> CSV (or Parquet)
