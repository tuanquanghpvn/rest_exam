# RESTful with Django

## Technology
* [Django](https://www.djangoproject.com/)
* [Django Rest Framework](http://www.django-rest-framework.org/)
* [Marshmallow](http://marshmallow.rtfd.org) ( is an ORM/ODM/framework-agnostic library for converting complex datatypes, such as objects, to and from native Python datatypes)
* [SQlAlchemy](http://www.sqlalchemy.org/) (query sql)
* [Aldjemy](https://github.com/Deepwalker/aldjemy/) (query sql for sqlalchemy in like django orm)
* [Pytest](http://pytest.org/latest/) (write test in django)
* [Pytest-django](https://pytest-django.readthedocs.org/en/latest/) (write test in django)

## Installation

1. Clone it!
2. Create new virtual (you can use pyenv-virtual).
3. Run project: python manage.py runserver [port].
4. Create request and check data or status return.

## Model

Category
+ id: int (identity)
+ name: string (required)
+ slug: string (required)

Story
+ id: int (identity)
+ name: string (required)
+ slug: string (required)
+ description: string (optional)
+ content: string (required)
+ category_id: int (required)

## Usage

You can send request with get, put, post, delete with url and receive data, status from server

Category
+ Get list: http://[domain:port]/category/
+ Post: http://[domain:port]/category/
+ Put: http://[domain:port]/category/
+ Get detail: http://[domain:port]/category/[id]/
+ Delete: http://[domain:port]/category/[id]/

Story
+ Get list: http://[domain:port]/story/
+ Post: http://[domain:port]/story/
+ Put: http://[domain:port]/story/
+ Get detail: http://[domain:port]/story/[id]/
+ Delete: http://[domain:port]/story/[id]/

## Contributing

1. Fork it!
2. Create your feature branch: `git checkout -b my-new-feature`
3. Commit your changes: `git commit -am 'Add some feature'`
4. Push to the branch: `git push origin my-new-feature`
5. Submit a pull request :D

## License

MIT
