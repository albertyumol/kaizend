def lowercase(x):
    return x.lower()


def test_lowercase():
    """
    - Given: parameters
    - When: params under certain conditions
    - Expectation: what am i expecting the results to be
    """
    assert lowercase('TEAM KAIZEND') == 'team kaizend'


def test_lowercase2():
    assert lowercase('Team Kaizend') == 'team kaizend'
