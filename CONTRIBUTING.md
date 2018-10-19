# Contributing

First off, thank you for considering contributing to Wapyce.

## Table of contents

* [Code of conduct](#code-of-conduct)
* [Reporting bugs and request new feature](#reporting-bugs-and-request-new-feature)
* [Code contribution](#code-contribution)
  * [Pull request](#pull-request)
  * [Styleguides](#styleguides)
    * [Git commit messages](#git-commit-messages)
    * [Python styleguide](#python-styleguide)
* [Donate](#donate)

## Code of conduct

This project and everyone participating in it is governed by the [Wapyce code of conduct](CODE_OF_CONDUCT.md). By participating, you are expected to uphold this code. Please report unacceptable behavior to [wapyce@protonmail.com](wapyce@protonmail.com).

## Reporting bugs and request new feature

This section guides you through submitting a bug report or request new feature for Wapyce.

Before submitting a bug report or request feature check if you're using the latest version of Wapyce and [ensure the bug or feature was not already reported](https://github.com/wapyce/wapyce/issues).

If you're unable to find an open issue addressing the problem or requesting this feature, [open a new one issue](https://github.com/wapyce/wapyce/issues/new).

## Code contribution

If you want submit your code to Wapyce you need follow the code conventions, the styleguides and pull request process.

### Pull request

1. [Install Python](http://www.diveintopython3.net/installing-python.html);
2. [Fork the repository](https://help.github.com/articles/fork-a-repo/);
3. [Install, create and activate a virtualenv](https://packaging.python.org/guides/installing-using-pip-and-virtualenv/);
4. [Install dependencies](https://packaging.python.org/guides/installing-using-pip-and-virtualenv/#using-requirements-files);
5. [Install PostgreSQL](https://wiki.postgresql.org/wiki/Detailed_installation_guides);
6. Configure enviroment variables;
    ```bash
    export DATABASE_LOCAL_NAME=wapyce_local
    export DATABASE_LOCAL_USER=postgres
    export DATABASE_LOCAL_PASSWORD=postgres
    export DATABASE_LOCAL_HOST=localhost
    export DATABASE_LOCAL_PORT=5432
    ```
7. [Create the database schema of Wapyce](https://docs.djangoproject.com/en/2.1/ref/django-admin/#django-admin-migrate);
8. [Start a web server to run Wapyce](http://goodcode.io/articles/django-nginx-gunicorn/);
9. Start coding :smile:;
10. [Commit and push your changes](https://help.github.com/articles/adding-a-file-to-a-repository-using-the-command-line/);
11. [Do a pull-request](https://help.github.com/articles/creating-a-pull-request/) with a short description explaining briefly what you've done.

### Styleguides

#### Git commit messages

* Limit to one line
* Limit the line to 72 characters or less
* Reference issues after comma
* Start the commit message with an applicable emoji:
  * :tada: `:tada:` Initial commit
  * :art: `:art:` Cosmetic
  * :racehorse: `:racehorse:` Performance
  * :memo: `:memo:` Documentation
  * :bug: `:bug:` Bugfix
  * :fire: `:fire:` Remove code
  * :white_check_mark: `:white_check_mark:` Tests
  * :sparkles: `:sparkles:` New Feature
  * :recycle: `:recycle:` Refactoring
  * :globe_with_meridians: `:globe_with_meridians:` Internationalization
  * :octocat: `:octocat:` GitHub especific resource
  * :bookmark: `:bookmark:` Version Tag
  * :wrench: `:wrench:` Tooling
  * :lock: `:lock:` Security
  * :heavy_check_mark: `:heavy_check_mark:` Tests

#### Python styleguide

The Wapyce follow the [PEP 8 -- Style Guide for Python Code](https://www.python.org/dev/peps/pep-0008/?) and the most of [Pylint rules](http://pylint.pycqa.org/en/latest/intro.html).
  
## Donate
  
If you'd like to monetarily support Wapyce development, you can:

* Donate Bitcoin to **36QNXpPzUDLdt611E2t3wdr9zBhWePBJga** wallet address;
* Donate Ethereum to **0xd7446224eb2da4f41f5f68f82be01e1f5fa1940e** wallet address;
* Donate Litecoin to **LVgF8LE8n6jFrKKfYZoyh9eckx2oBxcaGP** wallet address;
* Donate Waves to **3P7Hapj4Kvbn1k9GN2reb8aUsyDjNPy6pbS** wallet address;
* Donate Zcash to **t1dpafSCveZqa4mwk5Lrf55uKzPLVWCQLf6** wallet address;
* Donate Bitcoin Cash to **qp5sz7q3yxhrca7cvq54wktrk8392pgd9ucetl3w6n** wallet address.
