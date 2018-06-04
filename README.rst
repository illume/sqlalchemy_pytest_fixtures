sqlalchemy pytest fixtures

The benefits for these are they can::

    * makes writing sql tests easy, fast, and robust.
    * Run in parallel, in separate schemas per connection.
    * Only create the tables once for each pytest session.

Example::

    >>> def test_bla(session):
            from bla.models import Bla
            bla = Bla(name="hell")
            assert bla.name == 'hell'
            session.add(bla)
            session.commit()


Here you can see the nesting of transactions and db code as it happens.

    Creates an engine per pytest.session.
    Creates a connection per pytest.session.
        transaction
            create unique schema for these tests
            create tables
                nested transaction
                    sqlalchemy.session
                        user test code.

