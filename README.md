
# Amazon Eventbridge demonstration using Cloud Development Kit (CDK python)

This project demonstrates creating a custom eventbus, API destination, Lambda and rules using
cdk. This stack shows how you can automate the deployment of an service oriented architecture 
in Amazon Web Services using Amazon Event Bridge.

If you deploy this example unaltered messages will be posted to webhook.site. 
https://webhook.site/#!/d2062f94-8283-4327-ba52-355d943bc20e/ 
Be careful not to send anything private here. You may also see messages posted from other 
users if they have not deleted their tests. 

The first rule is named TestRule001 and is fired when Event Bridge messages are received with a
source of com.testing.test.001. When this rule fires it POSTS to webhook.site and renames
the incoming parameter named id to be test-id. This shows how you using api destinations
you can call a simple webservice and rename field names to suit the destination endpoint.

The second rule is named TestRule002 and is fired when Event Bridge messages are received with a
source of com.testing.test.002. When this rule fires it calls a Lambda fucntion. This Lambda function
then transforms the message by renaming the field and adding a new field with the current time 
and calls back to Event Bridge with a new message with source com.testing.test.003. This shows how Lambda can be used to completely
manipulate / reroute messages coming through Event Bridge.

The first rule is named TestRule003 and is fired when Event Bridge messages are received with a
source of com.testing.test.003. When this rule fires it POSTS to webhook.site and passes the payload
as was sent from the lambda function to the api destination.



```
$ python -m venv .venv
```

After the init process completes and the virtualenv is created, you can use the following
step to activate your virtualenv.

```
$ source .venv/bin/activate
```

If you are a Windows platform, you would activate the virtualenv like this:

```
% .venv\Scripts\activate.bat
```

Once the virtualenv is activated, you can install the required dependencies.

```
$ pip install -r requirements.txt
```

At this point you can now synthesize the CloudFormation template for this code.

```
$ cdk synth
```

To deply this example as is
```
$ cdk deploy --all
```

Then you can repeat the tests performed documented in the Medium blog post located here

