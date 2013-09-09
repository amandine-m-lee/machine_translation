import pytest
from special_dict import BigDict


#Need to do something with the pytest fixture

class TestBigDict():
    @pytest.fixture
    def simpled(self):
        simpled = BigDict()
        simpled['a'] = 9
        simpled[12] = 'a'
        return simpled

    @pytest.fixture
    def ddict(self):
        ddict = BigDict()
        ddict['banana'] = {}
        ddict['banana']['apple'] = 12
        return ddict

    def test_simpled(self, simpled):
        assert simpled['a'] == 9
        assert simpled[12] == 'a'
        simpled['a'] = 6
        assert simpled['a'] == 6
        with pytest.raises(KeyError):
            b =  simpled['h']

    def test_ddict(self, ddict):
        assert ddict['banana']['apple'] == 12
        with pytest.raises(KeyError):
            ddict['apple']['potato']
    
    def test_len(self, simpled):
        assert len(BigDict()) == 0
        assert len(simpled) == 2
        simpled['c'] = 13
        assert len(simpled) == 3

    def test_keys(self, simpled):
        assert BigDict().keys() == []
        assert simpled.keys().sort() == ['a',12].sort()
        simpled[('thing', 'thang')] = -5
        assert simpled.keys().sort() == [12, 'a', ('thing', 'thang')].sort()
    
    def test_values(self, simpled):
        assert BigDict().values() == []
        assert simpled.values().sort() == [9, 'a'].sort()
        simpled['e'] = "hello"
        assert simpled.values().sort() == [9, 'a', "hello"].sort()

    def test_get(self, simpled):
        assert simpled.get('a') == 9

