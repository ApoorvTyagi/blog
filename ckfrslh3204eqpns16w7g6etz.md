## Different ways to authenticate your APIs

![API-security.png](https://cdn.hashnode.com/res/hashnode/image/upload/v1601194999161/9O7PVey6u.png)

Whenever we are designing secure systems that needs authentication for API access, you must consider how your applications and users should authenticate themselves.

In this article, we’ll be discussing three different ways to achieve this: 

1. [HTTP Basic Authentication](#basic)
2. [API Keys](#api-key)
3. [OAuth](#oauth) 

We’ll also look into the advantages & disadvantages of all these methods.

<a id="basic"></a>
# HTTP Basic Auth 🔒

Basic Auth is one of the most simple method of authenticating using a pre defined username and password. This technique uses a header called Authorization, with a base64 encoded representation of the username and password.

A simple request using basic authentication with the username & password looks like this:

```
GET / HTTP/1.1
Host: api.xyz.com
Authorization: Basic XGFuaAVsOnbHc3M3b32Jl
```

Using basic authentication for authenticating users is usually not recommended since sending the user credentials for every request is a bad practice.

### Benefits:
HTTP Basic Auth is easy to use and implement & can act as a decent authentication for applications in server-to-server environments.

## Drawbacks:
When a user is authenticated, the application is required to collect the password. From the user perspective, it’s not possible to know what the app does with the password. The application will gain full access to the account, and there’s no other way for the user to revoke the access than to change the password.

<a id="api-key"></a>
# API Key 🔑

API keys are a way to authenticate an application accessing any API without referencing an actual user. The app adds the key to each API request, and the API can use the key to identify the application and authorize the request. Using the key you can also perform the actions like rate limiting.

Some APIs use query parameters for sending/receiving the API key, some use the header, some use the body parameters. 

For instance, API key with a query parameter will be like this:

```
curl -X POST https://language.googleapis.com/v1/blablabla?key=API_KEY
```

While generally i prefer API key to be sent in a custom header like this:
```
curl https://api.xyz.com/v1/blablabla \
     -H "Content-Type:application/json" \
     -H "X-Auth-Key:1234567893feefc5f0q5000bfo0c38d90bbeb" 
```
(Here -H depicts the field is going inside the header)

To learn more about curl read here 👉 [What is cURL?](https://curl.haxx.se/docs/manpage.html)

### Benefits:
It’s relatively easy for clients & developer to use API keys. Adding a key to the API request is quite simple too.

### Drawbacks:
The API key only identifies the application, not the user of the application. It is difficult to keep the key a secret. For server-to-server communication, it’s possible to hide the key & restrict the access to only be used in backend scenarios. However, in cases of client to server requests , the keys might leak if application is not properly secured.

<a id="oauth"></a>
# OAuth token based authentication 🔐

A token-based API is based on the fact that all services which needs to access the API will receive a token as proof that the app is allowed to call the service. The token is issued by a third party that can be trusted by both the application and service. 

The most popular protocol for obtaining these tokens is OAuth 2.0, specified in RFC 6749.

OAuth specifies mechanisms where an application can ask a user for access to services on behalf of the user, and receive a token as proof that the user agreed. 

This approach allows better authentication, the application must publish an Authorization Server (AS) beforehand which is in-charge of issuing the tokens. This AS also allows third party applications to register, and receive credentials for their application to be able to request access on behalf of users.

These are the processes involved in OAuth authentication process :

1. The user visits your application, enters information

2. Application redirects the user to the 3rd party token generating service.

3. The third party service returns an authorization code, contained in a redirect URL. This redirects the user back to the application.

5. Your application calls the service again and passes the authorization token that can be used for authenticating transactions with API.

Now, the third party application can call the API using the received token. The token is sent along with the request by adding it to the Authorization header with the Bearer keyword as follows:
```
GET /XYZ HTTP/1.1
Host api.xyz.com
Authorization: Bearer  <your-received-token>
```

### Token Validation
The issued token can be returned in two ways, either by returning a reference to the token data or returning the value of the token directly. For the reference token, the service will have to send a request to the AS to validate the token and return the data associated with it. This process is called introspection, and a sample response looks like this:

```
{
"active": true,
"sub": “username”,
"client_id": "app_id",
"scope": "read"
…
}
```

Based on this information, the service can decide if it should allow or deny the request. The client_id can also be used for statistics and rate-limiting of the application.

For returning the value, a token format like JSON Web Token (JWT) is usually used. This token can be signed or encrypted so that the service can verify the token by simply using the public key of the trusted AS.

### Benefits:
Time saving - It’s an incredibly time saving method in the long run. Whether it’s finding a new site online or returning to a previously visited one, if the sites you frequent support OAuth then you only need to create one account for the majority of your online activities for eg you might have seen websites that say login with google/twitter/facebook, all of these are using OAuth internally. 

Security - OAuth is now the standard model all OAuth data transfers must take place on SSL (Secure Sockets Layer) to ensure the most trusted cryptography industry protocols are being used to keep data as safe as possible.


### Drawbacks:
Phishing - When performed correctly, OAuth should be safe, but the act of asking users to login to a different site really quick can train us to be careless into thinking this practice is always safe. But there are many cases happened so far where users will fall victim to a convincing looking popup ad and have their data phished.

# Conclusion ⛳

![API meme.jpg](https://cdn.hashnode.com/res/hashnode/image/upload/v1601197522720/ydn6uR8hB.jpeg)

In this article we have discussed three main methods of securing your APIs. All of these 3 have their own pros & cons but the best that comes out to be is OAuth which many industries & businesses prefer when dealing with client-server scenarios.

However, for the cases where your multiple applications need to communicate with one another i.e server-server scenarios, you can still prefer to use Basic Auth & API keys for their simplicity.

# Other articles you may like 😊

- [Understanding Linear Regression](https://apoorvtyagi.tech/understanding-linear-regression) - One of the most popular algorithm in machine learning that every data scientist should know.
- [GIT INIT (Part-1)](https://apoorvtyagi.tech/git-init-part-1) - A series on GIT for beginners.
- [Bitcoin Mining](https://apoorvtyagi.tech/let-us-mine) -  Learn about what exactly happens in bitcoin mining.
- [Improving Time Complexity](https://apoorvtyagi.tech/improving-time-complexity) - Understanding how to improve the time complexity of your code.
- [GPT-3](https://apoorvtyagi.tech/gpt3) - A large open source state-of- 
   the-art language model with more than 175 billion parameters by 
   OpenAI.