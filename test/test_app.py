from myApp import check_name, check_name_len, check_sid_len

def test_check_type():
    assert check_name("abc") == True
    assert check_name("ab ") == False
    assert check_name("ªª") == True
    assert check_name("ª ª") == True
    assert check_name("ª ª") == True
    assert check_name("ª ú ") == False
    assert check_name("中文_is_printable") == True
    assert check_name_len("abc") == True
    assert check_name_len("abc abc") == True
    assert check_name_len("ªª") == True
    assert check_name_len("ª ª") == True
    assert check_name_len("abc abc abc abc abc a") == False
    assert check_name_len("ªªªªªªªªªª") == True
    assert check_name_len("ªªªªª ªªªªª") == False
    assert check_sid_len("1155") == False
    assert check_sid_len("1155111111") == True
    assert check_sid_len("115511111 ") == False
    assert check_sid_len(115511111) == False
    assert check_sid_len(1155111111) == True
    assert check_sid_len("1155 11111") == False