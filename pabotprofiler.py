import cProfile
import pstats
from pabot.pabot import main
import os
import sys
import tempfile

with tempfile.NamedTemporaryFile(suffix=".out", prefix="pybot-profile", dir=".", delete=False) as tf:
    profile_results = tf.name
cProfile.run("main(sys.argv[1:])", profile_results)
stats = pstats.Stats(profile_results)
stats.sort_stats("cumulative").print_stats(50)
os.remove(profile_results)
