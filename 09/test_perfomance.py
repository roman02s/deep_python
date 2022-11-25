import sys
import cProfile
import pstats
import time
import gc
from memory_profiler import profile
from plans import PlansCommon, PlansSlots, PlansRef


@profile
def test_perfomance(n: int):
    gc.disable()
    start_ts = time.time()
    plans = [PlansCommon("first", "second", "third") for _ in range(n)]
    end_ts = time.time()
    print(f"Time of create plans: {end_ts - start_ts} seconds")
    start_ts = time.time()
    slot_plans = [PlansSlots("first", "second", "third") for _ in range(n)]
    end_ts = time.time()
    print(f"Time of create slot_plans: {end_ts - start_ts} seconds")
    start_ts = time.time()
    weakref_plans = [PlansRef() for _ in range(n)]
    end_ts = time.time()
    print(f"Time of create weakref_plans: {end_ts - start_ts} seconds")

    start_ts = time.time()
    del plans
    end_ts = time.time()
    print(f"Time of del plans: {end_ts - start_ts} seconds")
    start_ts = time.time()
    del slot_plans
    end_ts = time.time()
    print(f"Time of del slot_plans: {end_ts - start_ts} seconds")
    start_ts = time.time()
    del weakref_plans
    end_ts = time.time()
    print(f"Time of del weakref_plans: {end_ts - start_ts} seconds")


    gc.enable()

    return None


if __name__ == "__main__":
    pr = cProfile.Profile()
    pr.enable()

    test_perfomance(1_00_000)
    pr.disable()

    ps = pstats.Stats(pr, stream=sys.stdout).sort_stats().print_stats()
