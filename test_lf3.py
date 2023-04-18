from LFTracer import LFTracer
import py7zr

def test_lf_py7zr():
    testarg = "StarWars60.wav"
    with LFTracer(target_func = ["search_function", "build_header", "prepare_coderinfo"]) as traced:
        with py7zr.SevenZipFile("archive.7z", 'w') as archive:
            archive.writeall(testarg)

    answer = {'build_header': {1029: 1, 1031: 1, 1032: 1, 1033: 1, 1034: 2}, 'prepare_coderinfo': {383: 2, 384: 2, 385: 2, 386: 2, 387: 2, 388: 2, 389: 2, 390: 2, 392: 4}, 'search_function': {71: 1, 74: 1, 75: 1, 85: 1, 86: 1, 88: 1, 89: 2, 90: 1, 93: 1, 94: 1, 96: 1, 99: 2, 100: 1, 106: 1, 110: 1, 111: 1, 116: 1, 122: 1, 123: 1, 139: 1, 143: 1, 144: 2, 145: 1, 146: 1, 153: 2}}
    assert traced.getLFMap() == answer
