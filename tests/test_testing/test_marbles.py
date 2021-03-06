import rx
from rx.testing import marbles


def test_alias():
    assert rx.Observable.from_string == rx.Observable.from_marbles


def test_from_to_marbles():
    for marbles in '0-1-(10)-|', '0|', '(10)-(20)|', '(abc)|':
        #from nose.tools import set_trace; set_trace()
        stream = rx.Observable.from_string(marbles)
        result = stream.to_blocking().to_marbles()
        assert result == marbles
