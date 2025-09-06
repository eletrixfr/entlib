# ENTLib (v3 soon with support for educonnect)

ENTLib is a API wrapper for OpenNG (NEO) written in Python.
I have reverse-engineered the API and created this library for fun.

## Installation

To install ENTLib, simply run the following command:

```bash
pip install git+https://github.com/eletrixfr/entlib.git
```

## Examples

To use ENTLib, you first need to create an instance of the `ENT` class. This class requires three arguments:

- `username`: The username of the user you want to authenticate with.
- `password`: The password of the user you want to authenticate with.
- `ent_url`: The URL of the ENT instance you want to connect to.

Once you have created an instance of the `ENT` class, you can use the various methods provided by the class to interact with the ENT instance.

For example, to get the youself, you can use the `get_myself_data` method:

```python
from entlib import ENT

ent = ENT("username", "password", "https://your-ent.example.com") 
user_data = ent.get_myself_data()
print(user_data)
```


## License

ENTLib is licensed under the GPL 2.0 License. See the LICENSE file for more information.

**Made with 💖 by [eletrix.fr](https://eletrix.fr)**

## NOTE: This librarie does not support **EduConnect** (but somes ENT you can still use /auth/login) i'm working on a V3 with support for EduConnect.