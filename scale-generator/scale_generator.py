SHARP_SCALE = [ 'A', 'A#', 'B', 'C', 'C#', 'D', 'D#', 'E', 'F', 'F#', 'G', 'G#']
FLAT_SCALE = [ 'A', 'Bb', 'B', 'C', 'Db', 'D', 'Eb', 'E', 'F', 'Gb', 'G', 'Ab' ]

SHARP_TONICS = [ 'C', 'a', 'G', 'D', 'A', 'E', 'B', 'F#', 'e', 'b', 'f#', 'c#', 'g#', 'd#' ]

OFFSET_DICT = { 'm' : 1, 'M' : 2, 'A': 3 }

class Scale:
    def __init__(self, tonic):
        self.tonic = tonic
        if self.tonic in SHARP_TONICS:
            self.scale = SHARP_SCALE
        else:
            self.scale = FLAT_SCALE

    def chromatic(self):
        tonic_index = self.scale.index(self.tonic.capitalize())
        return self.scale[tonic_index:] + self.scale[:tonic_index]

    def interval(self, intervals):
        c_scale = self.chromatic()
        ret = []
        pos = 0
        for offset in intervals:
            ret.append(c_scale[pos])
            pos = (pos + int(OFFSET_DICT[offset])) % len(self.scale)
        return ret
