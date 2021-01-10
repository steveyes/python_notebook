class TestClassOne(object):
    def test_one(self):
        x = "this"
        assert 'h' in x

    def test_two(self):
        x = "hello"
        assert hasattr(x, 'check')


class TestClassTwo(object):
    def test_one(self):
        x = "iphone"
        assert 'p'in x

    def test_two(self):
        x = "apple"
        assert hasattr(x, 'check')