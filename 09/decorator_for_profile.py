import sys
import cProfile
import pstats
from plans import PlansCommon


def profile_deco(in_f):
    pr = cProfile.Profile()
    pr.enable()

    def wrapper(*args, **kwargs):
        def _print_stats():
            pr.disable()
            pstats.Stats(pr, stream=sys.stdout).sort_stats().print_stats()
            pr.enable()
        wrapper.__dict__["print_stats"] = _print_stats
        return in_f(*args, **kwargs)
    return wrapper


@profile_deco
def create_list_plans_common(n: int):
    return [PlansCommon("first", "second", "third") for _ in range(n)]


if __name__ == "__main__":
    create_list_plans_common(100000)
    create_list_plans_common.print_stats()
