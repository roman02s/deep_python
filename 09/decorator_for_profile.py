import sys
import cProfile
import pstats
from plans import PlansCommon
from memory_profiler import profile


def profile_deco(in_f):
    pr = cProfile.Profile()

    def wrapper(*args, **kwargs):
        def _print_stats():
            pstats.Stats(pr, stream=sys.stdout).sort_stats().print_stats()
        pr.enable()
        result = in_f(*args, **kwargs)
        pr.disable()
        wrapper.__dict__["print_stats"] = _print_stats
        return result
    return wrapper


@profile_deco
def create_list_plans_common(n: int):
    return [PlansCommon("first", "second", "third") for _ in range(n)]


if __name__ == "__main__":
    create_list_plans_common(1000000)
    create_list_plans_common(1000000)
    create_list_plans_common(1000000)
    create_list_plans_common(1000000)
    create_list_plans_common.print_stats()
