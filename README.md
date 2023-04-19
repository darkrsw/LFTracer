# LFTracer
Midterm exam problem for KNU SE Spring 2023 (Line visit counter).

## Requirements

* R1. Count the number of visiting for each statement in the target functions.
* R2. Write your `LFTracer.py` in the repository.
* R3. Test your `LFTracer.py` by using `pytest`.
* R4. You need to let your TA know your repository URL and your student ID together.
* R5. `LFTracer` class should be defined in the `LFTracer.py`
* R6. The above class is tested as:

```
def test_lf_sha256():
    with LFTracer(target_func = ["generate_hash", "_sigma0"]) as traced:
        encoded = "mysalt".encode()
        generate_hash(encoded).hex()

    answer = ...
    assert traced.getLFMap() == answer
```

* R7. LFTracer should count the number of visiting for each statement in each target functions.
      - The target functions should be specified by `target_func = ["func1", "func2"]`.
* R8. There is a member function called “getLFMap()” in LFTracer, which returns a dictionary of {“func1”: {1: x1, 2: y1, ...}, “func2”: {1: x2, 2: y2, ...}, …}.
* R9. "target_function" can be called multiple times.

