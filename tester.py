# The actual analyzer class/code
import audfprint_analyze
# Access to match functions, used in command line interface
import audfprint_match
# My hash_table implementation
from hash_table import HashTable
import tempfile
import librosa


def create_frames(filename, frame_size, hop_length):
    """
    :param filename (str) - Filename of the query track
    :param frame_size (int) - frame size in seconds
    :param hop_length (int) - hop length in seconds

    Returns: np.ndarray<int, int>, samples of the frame size
    """

    sample_rate = 11025
    filenames = []
    y, sr = librosa.load(filename, sample_rate)
    # create the frames
    frames = librosa.util.frame(y, frame_length=frame_size * sample_rate, hop_length=hop_length * sample_rate)
    frames = frames.transpose()
    # for each frame save into a tempfile
    return frames


def localtest():
    """Function to provide quick test"""
    filename = "../data/songs/query/T008.wav"
    database_filename = './fpdes.pklz'

    chunked_queries = create_frames(filename, 12, 6)
    matcher = audfprint_match.Matcher()
    analyzer = audfprint_analyze.Analyzer(density=20)
    analyzer.usePeaks = False
    hash_tab = HashTable(database_filename)

    for qry in chunked_queries:
        try:
            matcher.illustrate_match(analyzer, hash_tab,'',d=qry)
        except:
            print("no match")



if __name__ == "__main__":
    localtest()
