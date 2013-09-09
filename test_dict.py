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
    def dictdict(self):
        ddict = BigDict()
        ddict['banana'] = {}
        ddict['banana']['apple'] = 12


    def test_simpled(self, simpled):
        assert simpled['a'] == 9
        assert simpled[12] == 'b'
        simpled['a'] = 6
        assert simpled['a'] == 6
        with raises(KeyError):
            b =  simpled['h']

    def test_ddict(self, ddict):
        assert ddict['banana']['apple'] == 12
        with raises(KeyError):
            whatever = ddict['apple']['potato']

        
    
