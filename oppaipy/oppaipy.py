import os
from contextlib import AbstractContextManager
from enum import IntEnum

import oppai

# Custom errors
class OppaiError(Exception):
    pass

class MissingBeatmapException(Exception):
    pass

class Calculator(AbstractContextManager):
    def __init__(self, beatmap_path=None, mods=None, combo=None, accuracy=None, count_100=0, count_50=0, misses=0, score_version=None):
        # New oppai context
        self._ez = oppai.ezpp_new()
        
        self._beatmap_data = None
        if beatmap_path:
            self.set_beatmap(beatmap_path)

        # Set 
        if mods:
            self.set_mods(mods)
        if combo:
            self.set_combo(combo)
        if accuracy:
            self.set_accuracy_percent(accuracy)
        if count_100 or count_50:
            self.set_accuracy(count_100, count_50)
        if misses:
            self.set_misses(misses)
        if score_version:
            self.set_score_version(score_version)
    
    def __exit__(self, exc_type, exc_value, traceback):
        self.close()

    def close(self):
        oppai.ezpp_free(self._ez)

    # Config setters
    def set_beatmap(self, beatmap_path):
        # Validate beatmap path
        if not os.path.isfile(beatmap_path):
            raise MissingBeatmapException("Beatmap file is missing")

        if self._beatmap_data:
            reset = True
        else:
            reset = False

        # Read into
        with open(beatmap_path, "r", encoding="utf-8") as fp:
            self._beatmap_data = fp.read()
        if reset:
            self.reset()

    def set_mods(self, mods):
        oppai.ezpp_set_mods(self._ez, mods)

    def set_combo(self, combo):
        oppai.ezpp_set_combo(self._ez, combo)

    def set_accuracy_percent(self, accuracy):
        oppai.ezpp_set_accuracy_percent(self._ez, accuracy)

    def set_accuracy(self, count_100=0, count_50=0):
        oppai.ezpp_set_accuracy(self._ez, count_100, count_50)

    def set_misses(self, misses):
        oppai.ezpp_set_nmiss(self._ez, misses)

    def set_score_version(self, score_version):
        oppai.ezpp_set_score_version(self._ez, score_version)
    
    def set_base_ar(self, ar):
        oppai.ezpp_set_base_ar(self._ez, ar)
    
    def set_base_od(self, od):
        oppai.ezpp_set_base_od(self._ez, od)
    
    def set_base_cs(self, cs):
        oppai.ezpp_set_base_cs(self._ez, cs)
    
    def set_base_hp(self, hp):
        oppai.ezpp_set_base_hp(self._ez, hp)

    def reset(self):
        oppai.ezpp_set_mode(self._ez, oppai.MODE_STD)
        oppai.ezpp_set_mods(self._ez, oppai.MODS_NOMOD)
        oppai.ezpp_set_nmiss(self._ez, 0)
        oppai.ezpp_set_combo(self._ez, -1)
        oppai.ezpp_set_score_version(self._ez, 1)
        oppai.ezpp_set_accuracy_percent(self._ez, -1)
        oppai.ezpp_set_accuracy(self._ez, 0, 0)
        oppai.ezpp_set_base_ar(self._ez, -1)
        oppai.ezpp_set_base_od(self._ez, -1)
        oppai.ezpp_set_base_cs(self._ez, -1)
        oppai.ezpp_set_base_hp(self._ez, -1)

    # Result properties
    @property
    def pp(self):
        return oppai.ezpp_pp(self._ez)

    @property
    def aim_pp(self):
        return oppai.ezpp_aim_pp(self._ez)

    @property
    def speed_pp(self):
        return oppai.ezpp_speed_pp(self._ez)

    @property
    def acc_pp(self):
        return oppai.ezpp_acc_pp(self._ez)

    @property
    def stars(self):
        return oppai.ezpp_stars(self._ez)

    @property
    def aim_stars(self):
        return oppai.ezpp_aim_stars(self._ez)

    @property
    def speed_stars(self):
        return oppai.ezpp_speed_stars(self._ez)

    def calculate(self):
        # Throw exception if beatmap not set, or file doesn't exist at path
        if not self._beatmap_data:
            raise MissingBeatmapException("Beatmap not set")

        # Calculate and error check
        result = oppai.ezpp_data_dup(self._ez, self._beatmap_data, len(self._beatmap_data.encode("utf-8")))
        if result < 0:
            raise OppaiError(oppai.errstr(result))
        
        # Return diff and pp for convenience
        return self.stars, self.pp
