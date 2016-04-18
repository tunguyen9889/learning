def checkio(data):
    if len(data) > 9:
        if any(i.isupper() for i in data) \
                and any(i.islower() for i in data) \
                and any(i.isdigit() for i in data):
            return True
        else:
            return False
    else:
        return False


if __name__ == '__main__':
    assert checkio(u'A1213pokl') == False, "1st example"
    assert checkio(u'bAse730onE4') == True, "2nd example"
    assert checkio(u'asasasasasasasaas') == False, "3rd example"
    assert checkio(u'QWERTYqwerty') == False, "4th example"
    assert checkio(u'123456123456') == False, "5th example"
    assert checkio(u'QwErTy911poqqqq') == True, "6th example"
