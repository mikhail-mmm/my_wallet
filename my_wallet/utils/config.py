from typing import Any, Mapping


def get_connection_dsn(config: Mapping[str, Any]) -> str:
    return (
        f"postgresql://{config['POSTGRES_USER']}:{config['POSTGRES_PASSWORD']}@"
        f"{config['POSTGRES_HOST']}:{config['POSTGRES_PORT']}/{config['POSTGRES_DBNAME']}"
    )


def test_get_connection_dsn():
    config = {
        'POSTGRES_USER': 'user',
        'POSTGRES_PASSWORD': 'password',
        'POSTGRES_HOST': 'localhost',
        'POSTGRES_PORT': '123',
        'POSTGRES_DBNAME': 'test'
    }
    result_dsn = get_connection_dsn(config)
    assert result_dsn == 'postgresql://user:password@localhost:123/test'
