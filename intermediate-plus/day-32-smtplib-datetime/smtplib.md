# Email

## Simple Mail Transfer Protocol (SMTP)

- Contains all of the rules for sending email
 
## Python's `smtplib` Module

 This module defines an SMTP client session object that can be used to send mail to any internet machine with an SMTP or ESMTP listener daemon.

### Steps to Send an Email

Note: Some providers may require you to enable "less secure apps" in your email settings, or app specific passwords.

```python
import smtplib
```

#### 1) create a connection object

```python
connection = smtplib.SMTP("smtp.gmail.com")
```

#### 2) Start Transport Layer Security (TLS) to apply encryption

```python
connection.starttls()
```

#### 3) Login to your email account

```python
connection.login(user="", password="")
```

#### 4) Send an email

```python
connection.sendmail(
        from_addr="",
        to_addrs="",
        msg="Subject:Hello\n\nThis is a test email."
        )
```

#### Finally, close the connection

```python
connection.close()
```

## Automatic closing of the connection using `with`

```python
import smtplib

my_email = "example@example.com"
to_email = "example2@example.com"
password = "password"
subject = "Hello"
message = "This is a test email."

with smtplib.SMTP("smtp.gmail.com") as connection:
    connection.starttls()
    connection.login(user=my_email, password=password)
    connection.sendmail(
        from_addr=my_email,
        to_addrs=to_email,
        msg=f"Subject:{subject}\n\n{message}"
    )
```
