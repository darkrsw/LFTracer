from LFTracer import LFTracer
import nayajson
from divide import divide
from merge_insertion_sort import merge_insertion_sort
from red_black_tree import RBTree, RBNode


def test_lvv_json1():
    testjson = """
        [
            {
                "id": 1,
                "type": "message",
                "content": "Hello!"
            },
            {
                "id": 2,
                "type": "query",
                "user_name": "tarzan",
                "password": "not_jane"
            },
            {
                "id": 3,
                "type": "command",
                "action": "swing"
            }
        ]
    """
    with LFTracer(target_func = ["parse_string", "tokenize"]) as traced:
        obj = nayajson.parse_string(testjson)

    answer = {'parse_string': {334: 1, 335: 2}, 'tokenize': {40: 1, 41: 1, 44: 1, 45: 1, 46: 1, 47: 1, 49: 1, 314: 1, 315: 1, 316: 1, 317: 458, 318: 457, 319: 457, 322: 457, 326: 457, 327: 437, 328: 437, 323: 47, 324: 47, 325: 141, 329: 1, 330: 2}}
    assert traced.getLFMap() == answer


def test_lvv_json2():
    testjson = """
        {
            "id": 3,
            "type": "command",
            "action": "swing"
        }
    """
    with LFTracer(target_func = ["process_char", "parse"]) as traced:
        obj = nayajson.parse_string(testjson)

    answer = {'parse': {337: 1, 338: 1, 339: 1, 340: 1, 342: 1, 343: 2, 344: 1, 345: 2}, 'process_char': {49: 114, 51: 114, 52: 114, 53: 114, 54: 114, 55: 79, 58: 78, 61: 77, 64: 77, 67: 77, 70: 75, 73: 72, 75: 67, 78: 66, 81: 66, 84: 66, 86: 66, 88: 66, 90: 66, 310: 114, 313: 228, 56: 1, 57: 1, 74: 5, 92: 35, 108: 34, 122: 34, 131: 34, 137: 34, 147: 34, 160: 34, 166: 34, 171: 34, 176: 34, 181: 34, 188: 34, 193: 34, 198: 34, 205: 34, 210: 34, 215: 34, 222: 34, 223: 29, 227: 24, 230: 24, 311: 25, 224: 5, 225: 5, 226: 5, 231: 5, 232: 5, 233: 5, 234: 5, 71: 3, 72: 3, 76: 1, 77: 1, 93: 1, 95: 1, 98: 1, 101: 1, 102: 1, 103: 1, 104: 1, 105: 1, 68: 2, 69: 2, 59: 1, 60: 1}}
    assert traced.getLFMap() == answer
#
def test_lvv_json3():
    testjson = """
        {
    "glossary": {
        "title": "example glossary",
		"GlossDiv": {
            "title": "S",
			"GlossList": {
                "GlossEntry": {
                    "ID": "SGML",
					"SortAs": "SGML",
					"GlossTerm": "Standard Generalized Markup Language",
					"Acronym": "SGML",
					"Abbrev": "ISO 8879:1986",
					"GlossDef": {
                        "para": "A meta-markup language, used to create markup languages such as DocBook.",
						"GlossSeeAlso": ["GML", "XML"]
                    },
					"GlossSee": "markup"
                }
            }
        }
    }
}

    """
    with LFTracer(target_func = ["process_char", "parse"]) as traced:
        obj = nayajson.parse_string(testjson)

    answer = {'parse': {337: 1, 338: 1, 339: 1, 340: 1, 342: 1, 343: 2, 344: 1, 345: 2}, 'process_char': {49: 624, 51: 624, 52: 624, 53: 624, 54: 624, 55: 303, 58: 297, 61: 291, 64: 290, 67: 289, 70: 279, 73: 264, 75: 238, 78: 238, 81: 238, 84: 238, 86: 238, 88: 238, 90: 238, 310: 624, 313: 1248, 56: 6, 57: 6, 74: 26, 92: 321, 108: 321, 122: 321, 131: 321, 137: 321, 147: 321, 160: 321, 166: 321, 171: 321, 176: 321, 181: 321, 188: 321, 193: 321, 198: 321, 205: 321, 210: 321, 215: 321, 222: 321, 223: 295, 227: 269, 230: 269, 311: 269, 224: 26, 225: 26, 226: 26, 231: 26, 232: 26, 233: 26, 234: 26, 71: 15, 72: 15, 68: 10, 69: 10, 62: 1, 63: 1, 65: 1, 66: 1, 59: 6, 60: 6}}
    assert traced.getLFMap() == answer


def test_divide():
    with LFTracer(target_func = ["divide"]) as traced:
        divide(5, 2)

    answer = {'divide': {6: 1, 9: 1, 12: 1, 14: 1, 15: 1, 16: 1, 18: 1, 21: 1, 28: 1, 30: 2, 32: 1, 33: 1, 34: 1, 39: 1, 41: 1, 42: 1, 43: 1, 44: 1, 45: 1, 48: 1, 50: 2}}
    assert traced.getLFMap() == answer


def test_red_black_tree():
    with LFTracer(target_func=["left_rotate", "right_rotate",  "insert"]) as traced:
        rb = RBTree()
        children = [11, 2, 14, 1, 7, 15, 5, 8, 4]
        for child in children:
            node = RBNode(child, 1)
            rb.insert(node)

    answer = {'insert': {62: 9, 64: 9, 65: 9, 67: 27, 74: 9, 75: 9, 77: 1, 83: 9, 84: 9, 85: 9, 87: 18, 68: 18, 69: 18, 72: 10, 78: 8, 80: 4, 70: 8, 82: 4}, 'left_rotate': {20: 1, 22: 1, 23: 1, 27: 1, 28: 1, 29: 1, 30: 1, 32: 1, 34: 1, 35: 1, 38: 1, 39: 2}, 'right_rotate': {41: 1, 43: 1, 44: 1, 48: 1, 49: 1, 50: 1, 51: 1, 53: 1, 54: 1, 59: 1, 60: 2}}
    assert traced.getLFMap() == answer

def test_merge_insertion_sort():
    with LFTracer(target_func=["binary_search_insertion", "merge", "sortlist_2d", "merge_insertion_sort"]) as traced:
        merge_insertion_sort([0, 5, 3, 2, 2])

    answer = {'merge_insertion_sort': {65: 1, 89: 1, 92: 1, 98: 1, 99: 1, 100: 4, 101: 3, 104: 2, 110: 2, 111: 1, 113: 1, 102: 1, 115: 1, 121: 1, 123: 1, 136: 1, 138: 1, 151: 1, 153: 1, 165: 1, 166: 1, 167: 1, 169: 1, 183: 1, 184: 2, 185: 1, 187: 1, 190: 1, 193: 1, 195: 2}, 'sortlist_2d': {53: 3, 58: 3, 59: 3, 61: 1, 62: 2, 60: 4}, 'merge': {39: 1, 44: 1, 45: 2, 46: 1, 47: 1, 50: 2}, 'binary_search_insertion': {18: 2, 23: 2, 24: 2, 25: 4, 26: 4, 27: 4, 31: 2, 34: 1, 28: 2, 29: 2, 30: 2, 35: 2, 36: 4, 32: 1}}
    assert traced.getLFMap() == answer

if __name__ == '__main__':
    test_lvv_json1()
    test_lvv_json2()
    test_lvv_json3()
    test_divide()
    test_red_black_tree()
    test_merge_insertion_sort()
