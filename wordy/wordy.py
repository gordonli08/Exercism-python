import operator
operate = {
    'plus': operator.add,
    'minus': operator.sub,
    'multiplied': operator.mul,
    'divided':operator.truediv
}
def answer(question):
    query = question[:-1].split()
    if not (query[0] == 'What' and query[1] == 'is'):
        raise ValueError('Non-math question')
    try:
        ret = int(query[2])
    except IndexError:
        raise ValueError('No operand')
    except TypeError:
        raise ValueError('Syntax Error')
    index = 3
    while index < len(query):
        ope = query[index]
        if ope not in operate:
            raise ValueError('Invalid operator')
        if ope == 'multiplied' or ope == 'divided':
            index += 2
        else:
            index += 1
        try:
            num = int(query[index])
        except IndexError:
            raise ValueError('Operand not provided')
        except TypeError:
            raise ValueError('Syntax error')
        index += 1
        ret = operate[ope](ret, num)
    
    return ret

