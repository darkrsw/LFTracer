class LFTracer():
    def __init__(self, target_func: str = [], list_func: bool = False, file: TextIO = sys.stdout) -> None:

    def __enter__(self) -> Any:
        return self

    def __exit__(self, exc_tp: Type, exc_value: BaseException, exc_traceback: TracebackType) -> Optional[bool]:
        return None

    def getLFMap(self):
        return None
