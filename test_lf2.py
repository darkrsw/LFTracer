import yaml
from LFTracer import LFTracer

def test_lf_pyyaml():
    document = """
                  a: 1
                  b:
                    c: 3
                    d: 4
                """
    with LFTracer(target_func = ["write_plain", "construct_yaml_map", "parse_node"]) as traced:
        yaml.dump(yaml.load(document, Loader=yaml.FullLoader))

    answer = {'parse_node': {273: 9, 274: 9, 279: 9, 280: 9, 281: 9, 282: 9, 292: 9, 301: 9, 315: 9, 316: 9, 317: 9, 318: 9, 319: 9, 325: 9, 337: 2, 342: 2, 347: 2, 352: 2, 353: 2, 354: 4, 355: 2, 356: 2, 372: 18, 326: 7, 327: 7, 328: 7, 329: 7, 334: 14, 335: 7, 336: 7}, 'construct_yaml_map': {410: 2, 411: 2, 412: 6, 413: 2, 414: 4}, 'write_plain': {1080: 7, 1081: 7, 1083: 7, 1085: 7, 1091: 7, 1092: 7, 1093: 7, 1094: 7, 1095: 7, 1096: 28, 1097: 14, 1098: 14, 1099: 7, 1100: 14, 1113: 14, 1127: 14, 1134: 14, 1135: 7, 1136: 7, 1137: 14, 1128: 7, 1129: 7, 1130: 7, 1132: 7, 1133: 7, 1086: 3, 1087: 3, 1088: 3, 1090: 3}}
    assert traced.getLFMap() == answer
